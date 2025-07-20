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
- `GET /api/v1/questions/{question}` - Get answer for specific question
- 

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| MONGO_HOST | MongoDB host | db |
| MONGO_PORT | MongoDB port | 27017 |
| MONGODB_ROOT_USERNAME | MongoDB username | admin |
| MONGODB_ROOT_PASSWORD | MongoDB password | password |

## Project Structure
```
python-api/ ├── app/ │ ├── api/ │ │ └── v1/ # API version 1 routes │ ├── core/ # Core functionality │ ├── models/ # Data models │ └── services/ # Business logic ├── tests/ # Test cases ├── docker/ # Docker configuration └── requirements/ # Dependencies
``` 

## Testing

Run the test suite:
```
bash pytest
``` 

## Development

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```

2. Make your changes and test
3. Push your branch and create a PR

## Error Handling

The API uses standard HTTP status codes:

- 200: Success
- 400: Bad request
- 404: Not found
- 409: Conflict (e.g., duplicate question)
- 500: Server error

## Rate Limiting

- 5 requests per minute per IP address
- Status code 429 returned when limit exceeded
```
