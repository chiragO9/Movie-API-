# 🎬 Movie API

A RESTful API built with FastAPI for managing a movie collection. Features complete CRUD operations, advanced filtering, search functionality, and proper error handling.

## Features

- Get all movies or filter by specific criteria
- Search across multiple fields (title, director)
- Filter by year, year range, genre, director, and rating
- Create, update, and delete movies
- Proper error handling with descriptive messages
- Case-insensitive search and filtering
- Interactive API documentation

## Technologies

- Python 3.8+
- FastAPI
- Uvicorn

## 📦 Installation

1. Clone the repository
```bash
git clone https://github.com/ChiragO9/Movie-API-.git
cd Movie-API-
```

2. Create and activate virtual environment
```bash
# Create virtual environment
python -m venv fastapienv

# Activate on Windows
fastapienv\Scripts\activate

# Activate on Mac/Linux
source fastapienv/bin/activate
```

3. Install dependencies
```bash
pip install fastapi uvicorn
```

## Running the API
```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

**Interactive Documentation:** `http://127.0.0.1:8000/docs`

## API Endpoints

### Movies Collection

| Method | Endpoint | Description | Example |
|--------|----------|-------------|---------|
| GET | `/movies` | Get all movies | `/movies` |
| GET | `/movies/{title}` | Get movie by title | `/movies/Inception` |
| POST | `/movies/create_movie` | Create new movie | Request body required |
| PUT | `/movies/update_movie` | Update existing movie | Request body required |
| DELETE | `/movies/delete_movie/{title}` | Delete movie | `/movies/delete_movie/Avatar` |

### Filtering

| Method | Endpoint | Description | Example |
|--------|----------|-------------|---------|
| GET | `/movies/?genre={genre}` | Filter by genre | `/movies/?genre=sci-fi` |
| GET | `/movies/bydirector/?director={name}` | Filter by director | `/movies/bydirector/?director=Christopher Nolan` |
| GET | `/movies/byyear/?year={year}` | Filter by year | `/movies/byyear/?year=2010` |
| GET | `/movies/years/?start={year}&end={year}` | Filter by year range | `/movies/years/?start=2000&end=2010` |
| GET | `/movies/byrating/?min_rating={rating}` | Filter by minimum rating | `/movies/byrating/?min_rating=8.5` |
| GET | `/movies/{director}/?genre={genre}` | Filter by director AND genre | `/movies/Christopher Nolan/?genre=sci-fi` |

### Search

| Method | Endpoint | Description | Example |
|--------|----------|-------------|---------|
| GET | `/search/?q={query}` | Search in title and director | `/search/?q=nolan` |

## Usage Examples

### Get all movies
```
GET http://127.0.0.1:8000/movies
```

### Get sci-fi movies
```
GET http://127.0.0.1:8000/movies/?genre=sci-fi
```

### Search for "nolan"
```
GET http://127.0.0.1:8000/search/?q=nolan
```

### Create a movie
```
POST http://127.0.0.1:8000/movies/create_movie

Body:
{
  "title": "The Shawshank Redemption",
  "director": "Frank Darabont",
  "genre": "drama",
  "year": 1994,
  "rating": 9.3
}
```

### Update a movie
```
PUT http://127.0.0.1:8000/movies/update_movie

Body:
{
  "title": "Inception",
  "director": "Christopher Nolan",
  "genre": "thriller",
  "year": 2010,
  "rating": 8.8
}
```

### Delete a movie
```
DELETE http://127.0.0.1:8000/movies/delete_movie/Avatar
```

## 📁 Project Structure
```
Movie-API/
├── main.py          # Main application file with all endpoints
├── README.md        # This file
└── .gitignore       # Git ignore file
```

## What I Learned

This project demonstrates:
- RESTful API design principles
- FastAPI route decorators and parameter handling
- Path parameters, query parameters, and request bodies
- HTTP methods (GET, POST, PUT, DELETE)
- Error handling with proper HTTP status codes
- Data filtering and searching algorithms
- Case-insensitive string matching
- Working with lists and dictionaries in Python



## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Chirag**
- GitHub: [@ChiragO9](https://github.com/ChiragO9)

---
