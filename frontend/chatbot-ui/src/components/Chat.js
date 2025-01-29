import React, { useState, useRef, useEffect } from 'react';
import { Send, Bot, Copy, Check } from 'lucide-react';

const Chat = () => {
  const [userInput, setUserInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [isTyping, setIsTyping] = useState(false);
  const [copiedStates, setCopiedStates] = useState({});
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleCopy = (text, id) => {
    navigator.clipboard.writeText(text);
    setCopiedStates({ ...copiedStates, [id]: true });
    setTimeout(() => {
      setCopiedStates({ ...copiedStates, [id]: false });
    }, 2000);
  };

  const detectLanguage = (code) => {
    if (code.includes('python') || code.includes('def ') || code.includes('import ')) {
      return 'python';
    } else if (code.includes('npm') || code.includes('bash') || code.includes('$')) {
      return 'bash';
    }
    return 'plaintext';
  };

  const formatMessage = (text, messageIndex) => {
    if (text.includes('```') || text.includes('python') || text.includes('def ') || text.includes('npm')) {
      const lines = text.split('\n');
      let inCodeBlock = false;
      let codeBlockCount = 0;
      let currentCode = '';
      const formattedLines = [];

      lines.forEach((line, idx) => {
        if (line.includes('```')) {
          if (inCodeBlock) {
            // End of code block
            const codeId = `${messageIndex}-${codeBlockCount}`;
            formattedLines.push(
              <div key={`code-${idx}`} className="code-block-container">
                <div className="code-block-header">
                  <span className="code-language">{detectLanguage(currentCode)}</span>
                  <button 
                    className="copy-button"
                    onClick={() => handleCopy(currentCode, codeId)}
                  >
                    {copiedStates[codeId] ? (
                      <Check size={16} className="copied-icon" />
                    ) : (
                      <Copy size={16} />
                    )}
                  </button>
                </div>
                <pre className="code-block">
                  <code>{currentCode.trim()}</code>
                </pre>
              </div>
            );
            currentCode = '';
            codeBlockCount++;
          }
          inCodeBlock = !inCodeBlock;
        } else if (inCodeBlock) {
          currentCode += line + '\n';
        } else if (line.trim().startsWith('python') || line.includes('def ') || line.includes('npm')) {
          // Inline code block
          const codeId = `${messageIndex}-${codeBlockCount}`;
          formattedLines.push(
            <div key={`code-${idx}`} className="code-block-container">
              <div className="code-block-header">
                <span className="code-language">{detectLanguage(line)}</span>
                <button 
                  className="copy-button"
                  onClick={() => handleCopy(line, codeId)}
                >
                  {copiedStates[codeId] ? (
                    <Check size={16} className="copied-icon" />
                  ) : (
                    <Copy size={16} />
                  )}
                </button>
              </div>
              <pre className="code-block">
                <code>{line}</code>
              </pre>
            </div>
          );
          codeBlockCount++;
        } else {
          formattedLines.push(<p key={idx}>{line}</p>);
        }
      });

      return formattedLines;
    }
    return text;
  };

  const sendMessage = async () => {
    if (userInput.trim()) {
      const newMessage = { user: true, text: userInput };
      setMessages(prev => [...prev, newMessage]);
      setUserInput("");
      setIsTyping(true);

      try {
        const response = await fetch("http://127.0.0.1:8000/api/chat", {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ text: userInput }),
        });
        
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        
        const data = await response.json();
        setMessages(prev => [...prev, { user: false, text: data.response }]);
      } catch (error) {
        console.error("Error sending message:", error);
        setMessages(prev => [...prev, { 
          user: false, 
          text: "Sorry, I encountered an error. Please try again." 
        }]);
      }
      setIsTyping(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <Bot size={24} className="bot-icon" />
        <h1>Testing for UI</h1>
      </div>

      <div className="chat-messages">
        {messages.map((msg, index) => (
          <div key={index} 
               className={`message ${msg.user ? 'user-message' : 'bot-message'}`}>
            {formatMessage(msg.text, index)}
          </div>
        ))}
        {isTyping && (
          <div className="typing-indicator">
            <div className="typing-dots">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className="input-container">
        <input
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Type a message..."
          className="chat-input"
        />
        <button
          onClick={sendMessage}
          disabled={!userInput.trim()}
          className="send-button"
          aria-label="Send message"
        >
          <Send size={20} />
        </button>
      </div>
    </div>
  );
};

export default Chat;