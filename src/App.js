import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [FILE_TYPES, setFileTypes] = useState([
    '.txt',
    '.py',
    '.js',
    '.sql',
    '.env',
    '.json',
    '.html',
    '.css',
    '.md',
    '.ts',
    '.java',
    '.cpp',
    '.c',
    '.cs',
    '.php',
    '.rb',
    '.xml',
    '.yml',
    '.md',
    '.sh',
    '.swift',
    '.h',
    '.pyw',
    '.asm',
    '.bat',
    '.cmd',
    '.cls',
    '.coffee',
    '.erb',
    '.go',
    '.groovy',
    '.htaccess',
    '.java',
    '.jsp',
    '.lua',
    '.make',
    '.matlab',
    '.pas',
    '.perl',
    '.pl',
    '.ps1',
    '.r',
    '.scala',
    '.scm',
    '.sln',
    '.svg',
    '.vb',
    '.vbs',
    '.xhtml',
    '.xsl',
  ]);
  const [repoUrl, setRepoUrl] = useState('');
  const [docUrl, setDocUrl] = useState('');
  const [response, setResponse] = useState('');
  const [selectedFileTypes, setSelectedFileTypes] = useState([]);
  const [fileSelection, setFileSelection] = useState('all');
  const [customFileType, setCustomFileType] = useState('');
  const [isDarkMode, setIsDarkMode] = useState(false);

  const handleRepoChange = (e) => {
    setRepoUrl(e.target.value);
  };

  const handleDocChange = (e) => {
    setDocUrl(e.target.value);
  };

  const handleFileTypeChange = (e) => {
    if (e.target.checked) {
      setSelectedFileTypes([...selectedFileTypes, e.target.value]);
    } else {
      setSelectedFileTypes(
        selectedFileTypes.filter((fileType) => fileType !== e.target.value)
      );
    }
  };

  const handleFileSelectionChange = (e) => {
    setFileSelection(e.target.value);
  };

  const handleAddFileType = () => {
    if (customFileType && !FILE_TYPES.includes(customFileType)) {
      setFileTypes([...FILE_TYPES, customFileType]);
    }
    setCustomFileType('');
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    let fileTypesToSend = selectedFileTypes;
    if (fileSelection === 'all') {
      fileTypesToSend = FILE_TYPES;
    }

    try {
      const result = await axios.post('http://localhost:5000/scrape', {
        repoUrl,
        docUrl,
        selectedFileTypes: fileTypesToSend,
      });
      setResponse(result.data.response);
    } catch (error) {
      console.error(error);
    }
  };

  const handleCopyText = () => {
    const outputArea = document.querySelector('.outputArea');
    outputArea.select();
    document.execCommand('copy');
  };

  const toggleTheme = () => {
    setIsDarkMode(!isDarkMode);
  };

  return (
    <div className={`container ${isDarkMode ? 'dark-mode' : ''}`}>
      <div className="inputContainer">
        <input
          value={repoUrl}
          onChange={handleRepoChange}
          placeholder="Enter Github repo URL"
          className="inputArea"
        />
        <input
          value={docUrl}
          onChange={handleDocChange}
          placeholder="Enter documentation URL (optional)"
          className="inputArea"
        />
        <div className="fileSelectionContainer">
          <div>
            <input
              type="radio"
              value="all"
              checked={fileSelection === 'all'}
              onChange={handleFileSelectionChange}
            />
            <label>All Files</label>
          </div>
          <div>
            <input
              type="radio"
              value="select"
              checked={fileSelection === 'select'}
              onChange={handleFileSelectionChange}
            />
            <label>Select File Types</label>
          </div>
        </div>
        {fileSelection === 'select' && (
          <div className="fileTypesContainer">
            {FILE_TYPES.map((fileType, index) => (
              <div key={index}>
                <input
                  type="checkbox"
                  value={fileType}
                  onChange={handleFileTypeChange}
                />
                <label>{fileType}</label>
              </div>
            ))}
            <div>
              <input
                value={customFileType}
                onChange={(e) => setCustomFileType(e.target.value)}
                placeholder="Enter new file type"
                className="smallInputArea"
              />
              <button onClick={handleAddFileType} className="addButton">
                Add
              </button>
            </div>
          </div>
        )}
      </div>
      <div className="buttonContainer">
        <button onClick={handleSubmit} className="transformButton">
          Submit
        </button>
        <button onClick={handleCopyText} className="copyButton">
          Copy Text
        </button>
        <button onClick={toggleTheme} className="toggleThemeButton">
          {isDarkMode ? 'Light Mode' : 'Dark Mode'}
        </button>
      </div>
      <div className="outputContainer">
        <textarea value={response} readOnly className="outputArea" />
      </div>
    </div>
  );
}

export default App;
