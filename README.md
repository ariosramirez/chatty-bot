# ChattyBot


**Build the Docker image** <br>
docker build -t chattybot .

**Run the Docker container** <br>
docker run -p 5000:5000 chattybot

Sure! Here is the description formatted in Markdown:

---

# ChattyBot: A Conversational AI Chatbot using Flask and Rasa

## Overview

**ChattyBot** is a conversational AI chatbot built with Flask and Rasa, designed to provide a simple yet powerful interface for interacting with users. This project demonstrates how to integrate a Flask web application with the Rasa conversational AI framework, allowing for robust natural language understanding and responses.

## Features

- **Natural Language Understanding**: Leveraging Rasa's advanced NLU capabilities for accurate intent recognition and response generation.
- **Simple Web Interface**: A clean and user-friendly web interface built with HTML and JavaScript.
- **Dockerized Deployment**: Easy to set up and run with Docker Compose, ensuring consistent environments and smooth deployments.
- **Live File Updates**: Automatically reflects changes in the source code, thanks to Docker volumes.
- **Cross-Origin Resource Sharing (CORS)**: Configured to handle requests from different origins, facilitating integration with various frontend applications.

## Project Structure

```plaintext
project/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── app.py
├── static/
│   └── index.html
└── rasa/
    ├── actions/
    ├── data/
    ├── models/
    ├── config.yml
    ├── credentials.yml
    ├── domain.yml
    └── endpoints.yml
```

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/chattybot.git
    cd chattybot
    ```

2. **Build and run the Docker containers**:

    ```bash
    docker-compose up --build
    ```

3. **Access the application**:

    Open your web browser and navigate to `http://localhost:5000`.

## Usage

- **Chat Interface**: Type messages into the input box and interact with ChattyBot through the web interface.
- **Custom Training Data**: Update the Rasa training data in the `rasa/data` directory to customize the bot's responses.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements, bug fixes, or features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please open an issue in the repository or contact **ariosramirez.data@gmail.com**.

