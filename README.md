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
cd sajda_feed_app
```

3. **Install dependencies:**
```bash
pip3 install -r requirements.txt
```
### Database Setup
1. **Create database:**
```bash
createdb sajda_feed_db 
```
2. **Make migrations**
```bash
python3 manage.py makemigrations
```
3. **Apply database migrations:**
```bash
python3 manage.py migrate
```
4. **Populate the database with seed data:**
```bash
python3 manage.py seed
```
**Please make ImageCards yourself by uploading images**
### Running the Server

**Start the Django development server:**

- Collect static files

```bash
python3 manage.py collectstatic
```
- To run server locally

```bash
python3 manage.py runserver
```

Open your web browser and navigate to http://127.0.0.1:8000/ to view the application.

### Authorization

- Default admin user: ` username: admin , password: 1234 `
- In order to see personal cards(e.g Dhikr Card) and use Like functionalities you need to pass `access_token` as param.

**Default `access_token` is `some-random-access-token` which is generated in seed file tied to one-to-one admin user**

Open your web browser and navigate to http://localhost:8000/?access_token=some-random-access-token to view the application as user.

### API Endpoints

- GET /: List all feed cards and hompage.
- POST /api/likes/: Create a new like.

## Note
- `Like` functionality was implemented by adding separate class for it and as you may saw there are different type of likes for future easy implementation.
- Every card type is a child class of `FeedCard`. `FeedCard` works as and abstract class even though can be initiated. Has common field like `title`, `description`, `number_of_likes`.
- `FeedCard.number_of_likes` field is connected to a sender `Like` class via signals so everytime `Like` instance is created `FeedCard.instance.number_of_likes` increases by 1.
- It could  be optimized by implementing `through caching` but due to time limit and sickness could not do it properly.
- Pagination was implemented separately on every type of FeedCard class child classes. Fixed number is 5 but can be transfered to `env_vars`.
