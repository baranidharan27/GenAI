import React, { useState } from "react";
import axios from "axios";

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return; // Prevent empty messages
    const userMessage = { user: true, text: input };
    setMessages([...messages, userMessage]);

    try {
      const response = await axios.post("/api/chat", { text: input });
      const botMessage = { user: false, text: response.data.response };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      const errorMessage = { user: false, text: "Error connecting to backend." };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    }

    setInput("");
  };

  return (
    <div className="flex flex-col items-center bg-gray-100 h-screen p-4">
      <div className="w-full max-w-md bg-white shadow-lg rounded-lg flex flex-col overflow-hidden">
        <div className="flex-1 overflow-y-auto p-4 space-y-2">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`p-3 rounded-lg max-w-xs ${
                msg.user ? "bg-blue-500 text-white ml-auto" : "bg-gray-200 text-black"
              }`}
            >
              {msg.text}
            </div>
          ))}
        </div>
        <div className="flex items-center p-4 border-t">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            className="flex-1 p-2 border rounded-lg mr-2"
            placeholder="Type a message..."
          />
          <button
            onClick={sendMessage}
            className="bg-blue-500 text-white px-4 py-2 rounded-lg"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
};

export default Chat;
