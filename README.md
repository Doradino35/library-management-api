# Library Management API

## Overview
This is a Django-based Library Management API that allows users to manage books, including adding, updating, retrieving, and deleting book records. It also includes rate limiting to control excessive requests.

## Features
- CRUD operations for books (Create, Read, Update, Delete)
- Rate limiting to prevent abuse
- API documentation using Postman
- Deployment on PythonAnywhere

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3
- Django
- PostgreSQL (if using a database other than SQLite)
- Git

### Steps to Set Up Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Deployment on PythonAnywhere
1. Clone your repository on PythonAnywhere.
2. Set up a virtual environment and install dependencies.
3. Configure `ALLOWED_HOSTS` in `settings.py`.
4. Run database migrations.
5. Collect static files and configure the web app.
6. Reload the web app from PythonAnywhere’s dashboard.

## API Endpoints
### Get All Books
- **Method**: `GET`
- **URL**: `/api/v1/books/`
- **Response**:
  ```json
  {
    "books": [
        {
            "id": "uuid",
            "title": "Book Title",
            "author": "Author Name",
            "genre": "Genre",
            "publication_date": "YYYY-MM-DD",
            "availability": "available",
            "edition": "Edition",
            "summary": "Summary of the book"
        }
    ]
  }
  ```

### Rate Limiting
- Headers:
  ```json
  {
    "X-RateLimit-Limit": "",
    "X-RateLimit-Remaining": "4",
    "X-RateLimit-Reset": "timestamp"
  }
  ```
- **Exceeded Rate Limit Response**:
  ```json
  {
    "detail": "Request was throttled. Expected available in 50 seconds."
  }
  ```

## Contributing
Feel free to fork this repository and submit pull requests.

## License
This project is licensed under the MIT License.

## Author
Developed by Dora.

