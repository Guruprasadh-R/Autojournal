import { useState } from "react";
import axios from "axios";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!text.trim()) return;
    setLoading(true);
    setResult(null);
    try {
      const res = await axios.post("http://127.0.0.1:5000/analyze", { text });
      setResult(res.data);
    } catch (err) {
      console.error(err);
      setResult({ error: "Server error. Try again later." });
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-100 via-white to-blue-50 flex flex-col items-center justify-center px-4 py-10">
      <div className="text-center mb-8">
        <h1 className="text-4xl font-extrabold text-blue-700 mb-2 tracking-tight">
          Emotion Analyzer
        </h1>
        <p className="text-gray-600">
          Understand your emotions and get personalized advice powered by AI.
        </p>
      </div>

      <div className="bg-white shadow-xl rounded-2xl p-6 w-full max-w-xl border border-gray-100">
        <textarea
          className="w-full p-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-400 focus:outline-none resize-none"
          rows="5"
          placeholder="Type your thoughts here..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        ></textarea>

        <button
          onClick={handleAnalyze}
          disabled={loading}
          className={`mt-5 w-full py-3 rounded-lg font-medium text-white text-lg shadow-md transition-all ${
            loading
              ? "bg-blue-400 cursor-not-allowed"
              : "bg-blue-600 hover:bg-blue-700"
          }`}
        >
          {loading ? "Analyzing..." : "Analyze Emotion"}
        </button>

        {result && (
          <div className="mt-6 p-5 bg-gray-50 border border-gray-200 rounded-xl text-gray-700">
            {result.error ? (
              <p className="text-red-600">{result.error}</p>
            ) : (
              <>
                <p className="text-lg">
                  <strong className="text-blue-700">Emotion:</strong>{" "}
                  {result.emotion}
                </p>
                <p className="mt-3 text-gray-800 leading-relaxed">
                  <strong className="text-blue-700">Advice:</strong>{" "}
                  {result.tip}
                </p>
              </>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
