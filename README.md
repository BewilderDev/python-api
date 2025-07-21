# ChatBot API

A Python REST API for managing chatbot interactions with MongoDB backend.

## Features

- RESTful API endpoints for question-answer management
- MongoDB integration for data persistence
- Chuck Norris jokes integration
- Docker support for easy deployment
- Environment-based configuration

## Prerequisites
- Docker
- Docker Compose

## Quick Start

1. Clone the repository
   ```bash
   git clone https://github.com/BewilderDev/python-api.git
   cd python-api
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configurations
   ```

3. **Build the container**
   ```bash
   docker-compose up --build
   ```
   
4. **Access the container**
   ```bash
   docker exec -it python-api-python-api-1 sh
   ```
   
5. **Install Dependencies**
    ```bash
   poetry install
    ```

6. **Run the application**
   ```bash
   python app/main.py
    ```

   The API will be available at `http://localhost:8000`

## API Endpoints

### Questions

- `POST /api/questions` - Create a new question-answer pair
- `GET /api/questions` - Get all questions (paginated)
- `GET /api/questions/?q={question}` - Get answer for specific question

## Environment Variables (FOR TESTING PURPOSES)

| Variable | Description                | Default      |
|----------|----------------------------|--------------|
| MONGO_HOST | MongoDB host               | db           |
| MONGO_PORT | MongoDB port               | 27017        |
| MONGODB_ROOT_USERNAME | MongoDB username           | chatbot_user |
| MONGODB_ROOT_PASSWORD | MongoDB password           | root         |
| API_KEY | API Key for authentication | sk-2fY9pLwqT7vXz5KeRjMn0bQdG6SaEhUv         |


