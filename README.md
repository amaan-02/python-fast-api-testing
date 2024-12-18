# Python FastAPI Project

A FastAPI project with 50+ endpoints across multiple features.

## Features
- User Management
- Role Management
- Authentication
- Admin Operations
- System Monitoring
- Utilities

## Getting Started

### Prerequisites
- Python 3.10+
- Docker (optional)

### Running Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ScalableFastAPIProject.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Access the API at:
   ```
   http://localhost:8000
   ```

5. Explore the interactive API documentation at:
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

### Running with Docker
1. Build the Docker image:
   ```bash
   docker build -t scalable-fastapi-project .
   ```

2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 scalable-fastapi-project
   ```

3. Access the API at:
   ```
   http://localhost:8000
   ```

## License
This project is licensed under the MIT License.
