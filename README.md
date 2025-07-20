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

3. **Run with Docker**
   ```bash
   docker-compose up -d
   ```

   The API will be available at `http://localhost:8000`

4. **Run locally (without Docker)**
   ```bash
   # Create and activate virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Run the application
   python main.py
   ```

## API Endpoints

### Questions

- `POST /api/v1/questions` - Create a new question-answer pair
- `GET /api/v1/questions` - Get all questions (paginated)
- `GET /api/v1/questions/?q={question}` - Get answer for specific question

## Environment Variables (FOR TESTING PURPOSES)

| Variable | Description | Default      |
|----------|-------------|--------------|
| MONGO_HOST | MongoDB host | db           |
| MONGO_PORT | MongoDB port | 27017        |
| MONGODB_ROOT_USERNAME | MongoDB username | chatbot_user |
| MONGODB_ROOT_PASSWORD | MongoDB password | root         |


