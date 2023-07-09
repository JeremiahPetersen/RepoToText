# RepoToText

RepoToText is a web app that scrapes a GitHub repository and converts its files into a single organized .txt. It allows you to enter the URL of a GitHub repository and an optional documentation URL (the doc info will append to the top of the .txt). The app retrieves the contents of the repository, including all files and directories and also fetches the documentation from the provided URL and includes it in a single organized text file.  The .txt file will be saved in the root project directory with user/repo/timestamp info.  This file can then be uploaded to Code Interpreter and you can use the chatbot to interact with the entire GitHub repo. 

## Technologies Used

- Frontend: React.js
- Backend: Python Flask
- GitHub API: PyGithub library
- Additional Python libraries: beautifulsoup4, requests, flask_cors, retry

## Frontend

The frontend of the app is implemented using React.js. The main component is `App.js`, which handles user input and interacts with the backend API.

### App.js

This file defines the main React component of the application. It uses React hooks to manage the state of input fields and the response received from the backend.

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

5. Click the "Submit" button to initiate the scraping process. The converted text will be displayed in the output area.

6. Optionally, click the "Copy Text" button to copy the generated text to the clipboard.

