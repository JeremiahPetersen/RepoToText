import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [repoUrl, setRepoUrl] = useState("");
  const [docUrl, setDocUrl] = useState("");
  const [response, setResponse] = useState("");

  const handleRepoChange = (e) => {
    setRepoUrl(e.target.value);
  };

  const handleDocChange = (e) => {
    setDocUrl(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const result = await axios.post("http://localhost:5000/scrape", {
        repoUrl,
        docUrl,
      });
      setResponse(result.data.response);
    } catch (error) {
      console.error(error);
    }
  };

  const handleCopyText = () => {
    const outputArea = document.querySelector(".outputArea");
    outputArea.select();
    document.execCommand("copy");
  };

  return (
    <div className="container">
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
      </div>
      <div className="buttonContainer">
        <button onClick={handleSubmit} className="transformButton">
          Submit
        </button>
        <button onClick={handleCopyText} className="copyButton">
          Copy Text
        </button>
      </div>
      <div className="outputContainer">
        <textarea value={response} readOnly className="outputArea" />
      </div>
    </div>
  );
}

export default App;
