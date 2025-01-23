

# This frontend branch is for frontend developement using react js tailwind 
# GenAI Content Generator

A LLM-driven content generator leveraging GPT-2 (Transformer library) with a Streamlit user interface and REST API backend. The project uses Docker for containerization, ensuring consistent deployment across environments.

## Table of Contents
- [Architecture Overview](#architecture-overview)
- [Key Features](#key-features)
- [Project Setup](#project-setup)
- [Development Guide](#development-guide)
- [Prompt Engineering](#prompt-engineering)
- [Documentation](#documentation)
- [Future Roadmap](#future-roadmap)

## Architecture Overview

### REST API Integration
The project implements a REST API to:
- Expose model functionality in a scalable manner
- Enable cross-platform accessibility
- Handle requests efficiently
- Manage authentication and rate limiting

### Docker Implementation
Docker containerization provides:
- Consistent development and production environments
- Easy deployment across different systems
- Simplified dependency management
- Isolated runtime environment

##  Project Setup

### Prerequisites
- Python 3.8+
- Docker (optional)
- Git
- Streamlit
### 1. Clone the Repository
```bash
git clone https://github.com/baranidharan27/GenAI
cd GenAI
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Setup
Create a `.env` file in the root directory:
```env
MODEL_PATH=./models
API_KEY=your_api_key
PORT=8501
```

##  Development Guide

### Running the Application

#### Local Development
```bash
# Start the Streamlit application
streamlit run app/main.py

# Host on all network interfaces
streamlit run app/main.py --server.address 0.0.0.0
```


#### Using Docker
```bash
# Build the Docker image
docker build -t genai .

# Run the container
docker run -p 8501:8501 genai

# Access at http://localhost:8501
```

### Documentation Server
```bash
# Start the documentation server
mkdocs serve

# Access at http://127.0.0.1:8000
```

##  Prompt Engineering

### Optimization Process

1. **Initial Assessment**
   - Baseline prompt testing
   - Performance metrics collection
   - Identification of improvement areas

2. **Iterative Refinement**
   - Context enhancement
   - Token optimization
   - Task-specific customization

3. **Results**
   - Improved response coherence
   - Better domain adaptation
   - Reduced token wastage

### Key Improvements

```plaintext
Before: Generic, unfocused outputs
```
![UI of chatbot](<image/First_attempt.png>)
#### Response Quality
```plaintext
After:  Contextual, precise responses
```
![UI of chatbot](<image/image.png>)
![UI of chatbot](<image/After_prompting.png>)

#### Token Efficiency
- Optimized prompt structure
- Reduced redundancy
- Reduced hallucination
- Improved response accuracy

##  Documentation

### API Documentation
Access the API documentation at `/docs` endpoint when running locally.

### Component Structure
```
GenAI/
├── app/
│   ├── main.py
│   ├── api/
│   └── utils/
├── models/
├── docs/
└── docker/
```

## Future Roadmap

### Planned Features
1. Domain-specific fine-tuning
2. Extended model support
3. Advanced analytics dashboard
4. Performance optimization

### Upcoming Improvements
- Enhanced error handling
- Additional API endpoints
- Improved documentation
- Extended test coverage

##  Contributing

1. Fork the repository
2. Create your feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

For more information, please refer to the [official documentation](https://github.com/baranidharan27/GenAI).
