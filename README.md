# Sajda Feed App

## Description
Small islamic reminders applications.

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- Django 3.0.1

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your_username/your_repository.git
   ```
2. **Navigate to the project directory:**
```bash
cd your_repository
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```
### Database Setup

1. **Apply database migrations:**
```bash
python manage.py migrate
```
2. **(Optional) Populate the database with seed data:**
```bash
python manage.py seed
```

### Running the Server

*Start the Django development server:**
```bash
python manage.py runserver
```

Open your web browser and navigate to http://127.0.0.1:8000/ to view the application.

### API Endpoints

GET /: List all feed cards and hompage.
POST /api/likes/: Create a new like.

## Note
Make sure to populate the database with seed data before running the server locally.