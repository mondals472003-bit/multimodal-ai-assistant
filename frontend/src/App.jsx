import { useState } from "react";
import axios from "axios";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const askQuestion = async () => {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/ask",
        {
          question: question,
        }
      );

      setAnswer(response.data.answer);
    } catch (error) {
      console.error(error);
      setAnswer("Error connecting to backend");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>AI PDF Assistant</h1>

      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask a question..."
        style={{ width: "400px", padding: "10px" }}
      />

      <button
        onClick={askQuestion}
        style={{ marginLeft: "10px", padding: "10px" }}
      >
        Ask
      </button>

      <h2>Answer:</h2>
      <p>{answer}</p>
    </div>
  );
}

export default App;