import React, { useState, useRef, useEffect } from 'react';
import { Send, Bot, Copy, Check, Terminal } from 'lucide-react';

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

  const formatMessage = (text, messageIndex) => {
    if (text.includes('``') || text.includes('def ') || text.includes('class ') || text.includes(' ')) {
      const lines = text.split('\n');
      let formattedContent = [];
      let isInCodeBlock = false;
      let currentCode = [];
      let codeBlockCount = 0;

      lines.forEach((line, idx) => {
        if (line.includes('```') || (!isInCodeBlock && (line.trim().startsWith('def ') || line.trim().startsWith('class ')| line.trim().startsWith('#')| line.trim().startsWith('a')))) { 
          if (isInCodeBlock) {
            // End code block
            const codeId = `${messageIndex}-${codeBlockCount}`;
            formattedContent.push(
              <div key={`code-${idx}`} className="terminal-container">
                <div className="terminal-header">
                  <div className="terminal-title">
                    <Terminal size={14} />
                    <span>Python</span>
                  </div>
                  <button 
                    className="copy-button"
                    onClick={() => handleCopy(currentCode.join('\n'), codeId)}
                  >
                    {copiedStates[codeId] ? (
                      <Check size={14} className="copied-icon" />
                    ) : (
                      <Copy size={14} />
                    )}
                  </button>
                </div>
                <pre className="terminal-code">
                  <code>{currentCode.join('\n')}</code>
                </pre>
              </div>
            );
            currentCode = [];
            codeBlockCount++;
            isInCodeBlock = false;
          } else {
            isInCodeBlock = true;
          }
        } else if (isInCodeBlock) {
          currentCode.push(line);
        } else if (line.trim().startsWith('# ') || line.trim().startsWith('## ')) {
          formattedContent.push(
            <div key={`comment-${idx}`} className="code-comment">{line}</div>
          );
        } else if (line.trim()) {
          formattedContent.push(<p key={`text-${idx}`}>{line}</p>);
        }
      });

      // Handle any remaining code block
      if (currentCode.length > 0) {
        const codeId = `${messageIndex}-${codeBlockCount}`;
        formattedContent.push(
          <div key="final-code" className="terminal-container">
            <div className="terminal-header">
              <div className="terminal-title">
                <Terminal size={14} />
                <span>Python</span>
              </div>
              <button 
                className="copy-button"
                onClick={() => handleCopy(currentCode.join('\n'), codeId)}
              >
                {copiedStates[codeId] ? (
                  <Check size={14} className="copied-icon" />
                ) : (
                  <Copy size={14} />
                )}
              </button>
            </div>
            <pre className="terminal-code">
              <code>{currentCode.join('\n')}</code>
            </pre>
          </div>
        );
      }

      return formattedContent;
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
        setMessages(prev => [...prev, { 
          user: false, 
          text: data.response 
        }]);
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
        <h1>Test for ui .</h1>
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