# Home Assignment 

**Project Description:**
Flask server that exposes an endpoint to ask a question. The server sends the
question to an OpenAI API, receives the answer, and saves both the question and the answer
in a PostgreSQL database. The application includes testing support using pytest and 
can be deployed easily using Docker Compose.


## Features
- Flask-based web application
- SQLAlchemy ORM for database management
- Alembic for handling database migrations
- Docker and Docker Compose for containerization
- Unit and integration tests with pytest
- Environment variable management with `.env` file

## Getting Started

### Prerequisites
- Python 3.x
- Docker
- PostgreSQL 

### Installation

1. Clone the repository:
   git clone https://github.com/ReutShainfeld/openAI-assesmnet.git
2. Navigate to the project directory:
   cd openAI-assesmnet
3. Create a virtual environment:
   python -m venv .venv
   source .venv/bin/activate  
4. Install dependencies:
   pip install -r requirements.txt

### Setting up the Environment Variables
1. Create a .env file in the root directory and add the following variables (of yours): 
   OPENAI_API_KEY=key
   POSTGRES_USER=user
   POSTGRES_PASSWORD=password
   POSTGRES_DB=db
   DATABASE_URI=postgresql://user:password@localhost/dbname
2. Running the Application
   flask run
   in http://localhost:5000 you can see see the app.

### Database Migrations
1. Generate a new migration file:
   alembic revision --autogenerate -m "your message"
2. Apply the migration:
   alembic upgrade head

### Running the Application with Docker
1. Build the Docker image:
   docker-compose build
2. Start the application:
   docker-compose up

### Running Tests
1. to run the test use the command:
   pytest




   
   







