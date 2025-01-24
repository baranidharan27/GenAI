import React, { useState } from 'react';
import axios from 'axios';
import { sendMessage } from './service/api'; // Adjusted path


const Chat = () => {
    const [userInput, setUserInput] = useState('');
    const [messages, setMessages] = useState([]);

    const sendMessage = async () => {
        if (userInput.trim()) {
            setMessages([...messages, { user: true, text: userInput }]);

            try {
                const response = await axios.post('http://127.0.0.1:8000/api/chat', { text: userInput });
                setMessages([
                    ...messages,
                    { user: true, text: userInput },
                    { user: false, text: response.data.response },
                ]);
            } catch (error) {
                console.error('Error sending message:', error);
            }

            setUserInput('');  // Clear input field
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
                <button onClick={sendMessage}>Send</button>
            </div>
        </div>
    );
};

export default Chat;
