"""
This module handles the back end Flask server for RepoToText
"""

# pylint: disable=line-too-long
# pylint: disable=C0103

import os
from datetime import datetime
import re
from github import Github, RateLimitExceededException, GithubException
from bs4 import BeautifulSoup
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from requests.exceptions import RequestException
from retry import retry

app = Flask(__name__)
CORS(app)

class GithubRepoScraper:
    """Scrape GitHub repositories."""
    def __init__(self, repo_name, doc_link=None, selected_file_types=None):
        if selected_file_types is None:
            selected_file_types = []
        self.github_api_key = os.getenv("GITHUB_API_KEY")
        if not self.github_api_key:
            raise ValueError("GitHub API key not set in environment variables")
        self.repo_name = repo_name
        self.doc_link = doc_link
        self.selected_file_types = selected_file_types

    @retry(RateLimitExceededException, tries=5, delay=2, backoff=2)
    def fetch_all_files(self):
        """Fetch all files from the GitHub repository."""
        def recursive_fetch_files(repo, contents):
            files_data = []
            for content_file in contents:
                if content_file.type == "dir":
                    try:
                        new_contents = repo.get_contents(content_file.path)
                    except GithubException as e:
                        print(f"Error accessing directory {content_file.path}: {e}")
                        continue
                    files_data += recursive_fetch_files(repo, new_contents)
                else:
                    if any(content_file.name.endswith(file_type) for file_type in self.selected_file_types):
                        file_content = f"\n'''--- {content_file.path} ---\n"
                        try:
                            if content_file.encoding == "base64":
                                file_content += content_file.decoded_content.decode("utf-8")
                            else:
                                print(f"Warning: Skipping {content_file.path} due to unexpected encoding '{content_file.encoding}'.")
                                continue
                        except Exception as e:
                            file_content += f"[Content not decodable: {e}]"
                        file_content += "\n'''"
                        files_data.append(file_content)
            return files_data

        github_instance = Github(self.github_api_key)
        try:
            repo = github_instance.get_repo(self.repo_name)
        except GithubException as e:
            raise ValueError(f"Error accessing GitHub repository {self.repo_name}: {e}")
        
        try:
            contents = repo.get_contents("")
        except GithubException as e:
            raise ValueError(f"Error fetching repository contents: {e}")

        files_data = recursive_fetch_files(repo, contents)
        return files_data

    def scrape_doc(self):
        """Scrape webpage."""
        if not self.doc_link:
            return ""
        try:
            page = requests.get(self.doc_link, timeout=10)
            soup = BeautifulSoup(page.content, 'html.parser')
            return soup.get_text(separator="\n")
        except RequestException as e:
            print(f"Error fetching documentation: {e}")
            return ""

    def write_to_file(self, files_data):
        """Build a .txt file with all of the repo's files"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"/app/data/{self.repo_name.replace('/', '_')}_{timestamp}.txt"
        with open(filename, "w", encoding='utf-8') as f:
            doc_text = self.scrape_doc()
            if doc_text:
                f.write(f"Documentation Link: {self.doc_link}\n\n")
                f.write(f"{doc_text}\n\n")
            f.write(f"*GitHub Repository \"{self.repo_name}\"*\n")
            for file_data in files_data:
                f.write(file_data)
        return filename

    def clean_up_text(self, filename):
        """Remove excessive line breaks."""
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
        cleaned_text = re.sub('\n{3,}', '\n\n', text)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)

    def run(self):
        """Run the scraping process."""
        print("Fetching all files...")
        files_data = self.fetch_all_files()

        print("Writing to file...")
        filename = self.write_to_file(files_data)

        print("Cleaning up file...")
        self.clean_up_text(filename)

        print("Done.")
        return filename

@app.route('/scrape', methods=['POST'])
def scrape():
    """Endpoint to initiate scraping of GitHub repositories."""
    data = request.get_json()
    repo_url = data.get('repoUrl')
    doc_url = data.get('docUrl')
    selected_file_types = data.get('selectedFileTypes', [])

    if not repo_url:
        return jsonify({"error": "Repo URL not provided."}), 400

    repo_name = repo_url.split('github.com/')[-1]
    scraper = GithubRepoScraper(repo_name, doc_url, selected_file_types)
    try:
        filename = scraper.run()
    except ValueError as e:
        return jsonify({"error": str(e)}), 500

    with open(filename, 'r', encoding='utf-8') as file:
        file_content = file.read()

    return jsonify({"response": file_content})

if __name__ == "__main__": # -- UNCOMMENT TO RUN WITH DOCKER
    app.run(host='0.0.0.0')

# if __name__ == "__main__": -- UNCOMMENT TO RUN LOCALLY WITHOUT DOCKER
#     app.run(port=5000)
