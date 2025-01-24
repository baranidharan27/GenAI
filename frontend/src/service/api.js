// frontend/src/service/api.js
import axios from 'axios';

const API_URL = "http://127.0.0.1:8000";  // Backend URL

export const sendMessage = async (message) => {
    try {
        const response = await axios.post(`${API_URL}/api/chat`, { text: message });
        return response.data.response;
    } catch (error) {
        console.error("Error sending message:", error);
        throw error;
    }
};
