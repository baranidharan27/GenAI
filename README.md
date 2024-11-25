# Content Generator

A LLM -driven content generator built using GPT-2(Transformer lib). This project uses Streamlit for the user interface and integrates a REST API for backend functionality. Additionally, Docker is used for containerization to ensure the application can run seamlessly across different environments.

## Why REST API?

The REST API is implemented to expose the model’s functionality in a way that is accessible and scalable. With the API in place, users can interact with the AI content generator from various platforms.

## Why Docker?

Docker is used to containerize the application, making it portable and easy to deploy. By using Docker, you can run the application on any system that supports Docker, without worrying about compatibility issues. The containerization ensures that all dependencies are included and managed, providing a consistent development and production environment.

## Project Setup

To get the application running, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/baranidharan27/GenAI
```
```sh
cd GenAI
```
2. **Install Dependencies**
You can install the required dependencies by running the following command in your project directory:
```sh
pip install -r requirements.txt
```
This will install all the necessary libraries for the project, including Streamlit, Transformers, and others.

3. **Accessing the Documentation**
You can find the documentation for this project in the docs directory. The documentation is built using MkDocs and can be accessed through the following steps:
To build and view the documentation locally, run:

```bash
mkdocs serve
```
This will start a local server, and you can access the documentation in your browser at http://127.0.0.1:8000.

4. **Running with Streamlit**

To run the application locally with Streamlit, execute the following command:
```sh
streamlit run app/main.py
```
This will start the application and open a browser window where you can interact with the AI content generator.
or 
```sh
streamlit run app/main.py --server.address 0.0.0.0
```
5. **Running with Docker**
If you prefer to run the application using Docker, follow these steps:

### Build the Docker image:
```sh
docker build -t .
Run the Docker container:
```
```bash
docker run -p 8501:8501 GenAI
```
This will start the application inside the Docker container and map it to port 8501 on your machine.

5. **Accessing the Documentation**
You can find the documentation for this project in the docs directory. The documentation is built using MkDocs and can be accessed through the following steps:
To build and view the documentation locally, run:




Working pictures :
![UI of chatbot](<image/Screenshot (32).png>)
2.**Response**
![UI of chatbot](<image/Screenshot (33).png>)

# Prompt engineering

1.  ![First prompting](<image/prompt_result.png>)

2. ![Secondprompting](<image/prompt_2.png>)


# Conclusion
This project is a work-in-progress, and while the current functionality is working well, there are many additional features and improvements planned for the future. I look forward to expanding this project with more capabilities once I have the resources and time to do so.
