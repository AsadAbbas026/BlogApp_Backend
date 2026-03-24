
---

# Mini Blog API (Django DRF)

## Table of Contents

1. [Project Overview](#project-overview)
2. [Tech Stack](#tech-stack)
3. [Setup Instructions](#setup-instructions)
4. [Database Models](#database-models)
5. [API Endpoints](#api-endpoints)
6. [ORM Queries](#orm-queries)
7. [Swagger Documentation](#swagger-documentation)
8. [Deployment](#deployment)

---

## Project Overview

This project is a **Mini Blog Platform API** built using **Django** and **Django REST Framework (DRF)**.
Users can create posts and comment on others' posts. The API also provides analytics endpoints like **top posts** and **most active users**.

Key features:

* Create, list, and retrieve posts
* Add and list comments per post
* Custom endpoints: top 3 posts, most active user
* Swagger API documentation
* SQLite database for simplicity
* Ready for deployment

---

## Tech Stack

* **Backend Framework:** Django 4.x
* **API Framework:** Django REST Framework
* **Database:** SQLite
* **Documentation:** drf-yasg (Swagger)
* **Deployment:** Render

---

## Setup Instructions

1. **Clone the repository:**

```bash
git clone <YOUR_REPO_URL>
cd mini_blog
```

2. **Create and activate virtual environment:**

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Apply migrations:**

```bash
python manage.py migrate
```

5. **Create superuser (optional, for admin access):**

```bash
python manage.py createsuperuser
```

6. **Run the development server:**

```bash
python manage.py runserver
```

7. **Access API locally:**

* API Root: `http://127.0.0.1:8000/api/`
* Swagger docs: `http://127.0.0.1:8000/swagger/`

---

## Database Models

### User

| Field | Type                |
| ----- | ------------------- |
| id    | AutoField           |
| name  | CharField           |
| email | EmailField (unique) |

### Post

| Field      | Type              |
| ---------- | ----------------- |
| id         | AutoField         |
| title      | CharField         |
| content    | TextField         |
| created_at | DateTimeField     |
| user       | ForeignKey (User) |

### Comment

| Field        | Type              |
| ------------ | ----------------- |
| id           | AutoField         |
| user         | ForeignKey (User) |
| post         | ForeignKey (Post) |
| comment_text | TextField         |
| created_at   | DateTimeField     |

---

## API Endpoints

### Posts API

| Endpoint           | Method | Description            |
| ------------------ | ------ | ---------------------- |
| `/api/posts/`      | GET    | List all posts         |
| `/api/posts/`      | POST   | Create a new post      |
| `/api/posts/<id>/` | GET    | Retrieve a single post |

### Comments API

| Endpoint                         | Method | Description              |
| -------------------------------- | ------ | ------------------------ |
| `/api/posts/<post_id>/comments/` | GET    | List comments for a post |
| `/api/posts/<post_id>/comments/` | POST   | Add a comment to a post  |

### Custom Analytics Endpoints

| Endpoint                 | Method | Description                                 |
| ------------------------ | ------ | ------------------------------------------- |
| `/api/top-posts/`        | GET    | Top 3 posts with highest number of comments |
| `/api/most-active-user/` | GET    | User with the highest number of comments    |

---

## ORM Queries

1. **Top 3 posts with most comments:**

```python
Post.objects.annotate(comment_count=Count('comments')).order_by('-comment_count')[:3]
```

2. **Users with more than 3 comments:**

```python
User.objects.annotate(total_comments=Count('comments')).filter(total_comments__gt=3)
```

3. **Most active user:**

```python
User.objects.annotate(total_comments=Count('comments')).order_by('-total_comments').first()
```

4. **All comments for a post (newest first):**

```python
Comment.objects.filter(post_id=<POST_ID>).order_by('-created_at')
```

---

## Swagger Documentation

Swagger UI provides a visual interface to explore all API endpoints:

```
http://127.0.0.1:8000/swagger/   # Local testing
```

* Shows all available endpoints
* Allows testing POST and GET requests directly
* Displays request/response examples

---

## Deployment

The project is deployed on **Render**.

**Live API URL:** `https://mini-blog-api.onrender.com/`
**Swagger Documentation:** `https://mini-blog-api.onrender.com/swagger/`

**Deployment Steps:**

1. Push project to GitHub.

2. On Render, create a new **Web Service** and connect your GitHub repository.

3. Configure:

   * **Environment:** Python
   * **Build Command:**

     ```bash
     pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
     ```
   * **Start Command:**

     ```bash
     gunicorn mini_blog.wsgi:application
     ```

4. Render will automatically build and deploy the API.

5. Access API and Swagger docs using the Render URL.