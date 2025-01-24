// src/App.js or where you use api.js
import React, { useState } from 'react';
import { sendMessage } from './service/api'; // Correct path


const Chat = () => {
    const [userInput, setUserInput] = useState('');
    const [messages, setMessages] = useState([]);

    const handleSendMessage = async () => {
        if (userInput.trim()) {
            setMessages([...messages, { user: true, text: userInput }]);
            try {
                const response = await sendMessage(userInput);
                setMessages([
                    ...messages,
                    { user: true, text: userInput },
                    { user: false, text: response },
                ]);
            } catch (error) {
                console.error("Error sending message:", error);
            }
            setUserInput('');
        }
    };

    return (
        <div className="chat-container">
            <div className="messages">
                {messages.map((msg, index) => (
                    <div key={index} className={msg.user ? 'user-message' : 'bot-message'}>
                        {msg.text}
                    </div>
                ))}
            </div>
            <div className="input-area">
                <input
                    type="text"
                    value={userInput}
                    onChange={(e) => setUserInput(e.target.value)}
                    placeholder="Type a message..."
                />
                <button onClick={handleSendMessage}>Send</button>
            </div>
        </div>
    );
};

export default Chat;
