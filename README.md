![example workflow](https://github.com/JeremiahPetersen/RepoToText/actions/workflows/pylint.yml/badge.svg)
![example workflow](https://github.com/JeremiahPetersen/RepoToText/actions/workflows/es-lint.yml/badge.svg)

![repo to text 5](https://github.com/JeremiahPetersen/RepoToText/assets/118206017/0d65016d-6388-48e0-b833-4ea1a169acfe)

![repo to text 7](https://github.com/JeremiahPetersen/RepoToText/assets/118206017/7d28fa8f-8bb1-4ddd-99f3-b33ddb26f0e9)

## RepoToText

RepoToText is a web app that scrapes a GitHub repository and converts its files into a single organized .txt. It allows you to enter the URL of a GitHub repository and an optional documentation URL (the doc info will append to the top of the .txt). The app retrieves the contents of the repository, including all files and directories and also fetches the documentation from the provided URL and includes it in a single organized text file.  The .txt file will be saved in the root project directory with user/repo/timestamp info.  This file can then be uploaded to Code Interpreter and you can use the chatbot to interact with the entire GitHub repo.  Add your GitHub API Key in the .env file 

GITHUB_API_KEY='YOUR GITHUB API KEY HERE'

## Prompt Example

This is a .txt file that represents an entire GitHub repository. The repository's individual files are separated by the sequence '''--- , followed by the file path, ending with ---. Each file's content begins immediately after its file path and extends until the next sequence of '''--- *Add your idea here (Example)*: Please create a react front end that will work with the back end 

## FolderToText

FolderToText.py is a script that allows you to turn a local folder, or local files, into a .txt in the same way RepoToText.py does.  Choose your files with browse (you can continue adding by clicking "Browse".  Once you have all of your files selected and uploaded with browse, type in the file type endings you want to copy with a ',' in between.  Example: .py , .js , .md , .ts ---> You can also turn this off and it will add every file you uploaded to the .txt ---> Last, enter in the file name you want to appear and the output path.  The file will be written with your file name choice and a timestamp.

## Info

- creates a.txt with ('''---) seperating each file from the repo.
- each file from the repo has a header after ('''---) with the file path as the title
- the .txt file is saved in the root directory
- you can add a url to a doc page and the doc page will append to the top of the .txt file (great to use for tech that came out after Sep 2021)

## Tech Used

- Frontend: React.js
- Backend: Python Flask
- GitHub API: PyGithub library
- Additional Python libraries: beautifulsoup4, requests, flask_cors, retry

## Frontend

The frontend of the app is implemented using React.js. The main component is `App.js`, which handles user input and interacts with the backend API.

### App.js

This file defines the main React component of the app. It uses React hooks to manage the state of input fields and the response received from the backend.

- `useState` hooks are used to define the state variables `repoUrl`, `docUrl`, and `response`, which hold the values of the repository URL, documentation URL, and the response from the backend API, respectively.

- The component defines event handlers (`handleRepoChange`, `handleDocChange`, `handleSubmit`, and `handleCopyText`) to update the state variables based on user interactions.

- When the user clicks the "Submit" button, the `handleSubmit` function is called. It sends a POST request to the backend API using the Axios library, passing the `repoUrl` and `docUrl` values in the request body. The response from the API is then stored in the `response` state variable.

- The component renders the input fields, buttons, and the output area using JSX.

## Backend

The backend of the application is implemented using Python and the Flask web framework. The main script is `RepoToText.py`, which defines the Flask application and handles the scraping and conversion logic.

### RepoToText.py

This file contains the Flask application and the `GithubRepoScraper` class responsible for scraping the GitHub repository and generating the text file.

- The `GithubRepoScraper` class initializes with a GitHub API key and the repository URL. It provides methods to fetch all files from the repository, scrape documentation from a provided URL, write the files and documentation to a text file, and clean up the text file by removing unnecessary line breaks.

- The Flask application is created using the `Flask` class and enables Cross-Origin Resource Sharing (CORS) using the `CORS` extension. It defines a single route `/scrape` that accepts POST requests.

- When a POST request is received at the `/scrape` endpoint, the request data is extracted and the repository URL and documentation URL are retrieved.

- An instance of `GithubRepoScraper` is created with the repository URL and documentation URL.

- The `run` method of `GithubRepoScraper` is called, which fetches all files from the repository, writes them to a text file along with the documentation, and performs cleanup on the text file.

- The generated text file is read and returned as the response of the API.

## Running the Application

To run the application, follow these steps:

1. Install the required dependencies mentioned in the frontend and backend sections.

2. Start the backend server by running the `RepoToText.py` script. The Flask application will listen on port 5000.

3. Start the frontend development server by running the React application.

4. Access the application in a web browser and enter the GitHub repository URL and documentation URL (if available).

5. Choose All files or choose specific file types.

6. Click the "Submit" button to initiate the scraping process. The converted text will be displayed in the output area, and it will also be saved to the project root directory.

7. You can also click the "Copy Text" button to copy the generated text to the clipboard.

## TODO

- [ ] FIX: Broken file types: .ipynb |
- [ ] FIX: FolderToText - fix so a user can pick one folder (currently only working when user selects individual files
- [ ] add in the ability to work with private repositories
- [ ] create a small desktop app via PyQT or an executable file
- [ ] add ability to store change history and update .txt to reflect working changes
- [ ] add checker function to make sure .txt is current repo version
- [ ] adjust UI for flow, including change textarea output width, adding file management and history UI
- [ ] explore prompt ideas including breaking the prompts into discrete steps that nudge the model along
