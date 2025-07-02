📚 BiblioNest — A Read-Only Library API with Django REST Framework

**BiblioNest** is a structured, read-only API designed with Django REST Framework to model the dynamic relationships of a library system — books, genres, authors, branches, and members — using a clean architecture powered by advanced serializer techniques.

> Designed as a deep-dive learning project to practice **ModelSerializer**, **Nested Serializer**, **Plain Serializer**, **@property**, **SerializerMethodField**, `ForeignKey`, and `ManyToManyField`, all wrapped in a clean, GET-only API endpoint.

---

## 🔗 API Endpoint: /library-data/
BASE URL: http://localhost:8000/api

## Usage

### 1. Clone the repository

```
git clone https://github.com/raghav-patidar1/biblionest-api.git
cd biblionest-api

```

### 2. Set up a virtual environment

```
python -m venv env
.\env\Scripts\activate

```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Apply migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 5. Populate sample data

```
python manage.py populate_data
```

### 6. Run server

```
python manage.py runserver
```

## API Access

Once the server is running, you can send a **GET request** to:

```
Base URL: http://localhost:8000/api
Endpoint: /library-data/
```