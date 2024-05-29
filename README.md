
![example workflow](https://github.com/JeremiahPetersen/RepoToText/actions/workflows/pylint.yml/badge.svg)
![example workflow](https://github.com/JeremiahPetersen/RepoToText/actions/workflows/es-lint.yml/badge.svg)

![repo to text 5](https://github.com/JeremiahPetersen/RepoToText/assets/118206017/0d65016d-6388-48e0-b833-4ea1a169acfe)

![repo to text 7](https://github.com/JeremiahPetersen/RepoToText/assets/118206017/7d28fa8f-8bb1-4ddd-99f3-b33ddb26f0e9)

## RepoToText

RepoToText is a web app that scrapes a GitHub repository and converts its files into a single organized .txt. It allows you to enter the URL of a GitHub repository and an optional documentation URL (the doc info will append to the top of the .txt). The app retrieves the contents of the repository, including all files and directories, and also fetches the documentation from the provided URL and includes it in a single organized text file. The .txt file will be saved in the /data folder with user + repo + timestamp info. This file can then be uploaded to (GPT-4, Claude Opus, etc) and you can use the chatbot to interact with the entire GitHub repo. 

## Demo

Creating a React front end for a GitHub repo containing a functioning back end:

https://chat.openai.com/share/0670c1ec-a8a8-4568-ad09-bb9b152e1f0b

Working front-end project: https://github.com/JeremiahPetersen/CaseConnect/tree/front-end

## Running the Application with Docker

To run the application using Docker, follow these steps:

1. Clone the repository.  Create a .env file in the root folder.
2. Set up the environment variable `GITHUB_API_KEY` in the `.env` file.
3. Build the Docker images with `docker compose build`.
4. Start the containers with `docker compose up`.
5. Access the application (http://localhost:3000) in a web browser and enter the GitHub repository URL and documentation URL (if available).
6. Choose All files or choose specific file types.
7. Click the "Submit" button to initiate the scraping process. The converted text will be displayed in the output area, and it will also be saved in the /data folder. 
8. You can also click the "Copy Text" button to copy the generated text to the clipboard.

## Prompt Example

This is a .txt file that represents an entire GitHub repository. The repository's individual files are separated by the sequence '''--- , followed by the file path, ending with ---. Each file's content begins immediately after its file path and extends until the next sequence of '''--- *Add your idea here (Example)*: Please create a react front end that will work with the back end 

## Environment Configuration
Add your GitHub API Key in the .env file 

```
GITHUB_API_KEY='YOUR GITHUB API KEY HERE'
```

## FolderToText

FolderToText.py is a script that allows you to turn a local folder, or local files, into a .txt in the same way RepoToText.py does.  Choose your files with browse (you can continue adding by clicking "Browse".  Once you have all of your files selected and uploaded with browse, type in the file type endings you want to copy with a ',' in between.  Example: .py , .js , .md , .ts ---> You can also turn this off and it will add every file you uploaded to the .txt ---> Last, enter in the file name you want to appear and the output path.  The file will be written with your file name choice and a timestamp.

## Info

- Creates a .txt with ('''---) separating each file from the repo.
- Each file from the repo has a header after ('''---) with the file path as the title.
- The .txt file is saved in the /data folder 
- You can add a URL to a documentation page and the documentation page will append to the top of the .txt file (great to use for tech that came out after Sep 2021).

## Tech Used

- Frontend: React.js
- Backend: Python Flask
- Containerization: Docker
- GitHub API: PyGithub library
- Additional Python libraries: beautifulsoup4, requests, flask_cors, retry


## TODO

- [x] Add Docker to project
- [x] Add Dark Mode
- [ ] Build web app for (https://repototext.com/)
- [ ] FIX: Broken file types: .ipynb
- [ ] FIX: FolderToText - fix so a user can pick one folder (currently only working when user selects individual files)
- [ ] Add in the ability to work with private repositories
- [ ] Add ability to store change history and update .txt to reflect working changes
- [ ] Add function to make sure .txt is current repo version
- [ ] Adjust UI for flow, including change textarea output width, adding file management and history UI

---
