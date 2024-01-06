# API Documentation

This document provides information about the features and usage of the Notes API.

## Table of Contents
- [Authentication](#authentication)
- [Rate Limiting](#rate-limiting)
- [Endpoints](#endpoints)
  - [Signup](#signup)
  - [Login](#login)
  - [Get a Note by ID](#get-a-note-by-id)
  - [Create a Note](#create-a-note)
  - [Delete a Note](#delete-a-note)
  - [Edit a Note](#edit-a-note)
  - [Share a Note](#share-a-note)
  - [Search Notes](#search-notes)
  - [Get All Notes](#get-all-notes)

## Authentication

The API uses token-based authentication using JSON Web Tokens (JWT). To access protected endpoints, you need to include the generated token in the `Authorization` header of your requests.

## Rate Limiting

The API has rate limiting in place to manage server load. Exceeding the allowed number of requests within a specified time frame will result in a rate limit error. Each endpoint has different Rate Limits assigned to it 

## Endpoints

### Signup

**Endpoint:** `/api/auth/signup/`  
**Method:** `POST`  
**Description:** Create a new user account.

### Login

**Endpoint:** `/api/auth/login/`  
**Method:** `POST`  
**Description:** Log in to an existing user account and obtain an access token.

### Get a Note by ID

**Endpoint:** `/api/notes/{id}/`  
**Method:** `GET`  
**Description:** Retrieve details of a specific note by providing its ID.

### Create a Note

**Endpoint:** `/api/notes/`  
**Method:** `POST`  
**Description:** Create a new note by providing a title and content.

### Delete a Note

**Endpoint:** `/api/notes/{id}/`  
**Method:** `DELETE`  
**Description:** Delete a specific note by providing its ID.

### Edit a Note

**Endpoint:** `/api/notes/{id}/`  
**Method:** `PUT`  
**Description:** Update the title and/or content of a specific note by providing its ID.

### Share a Note

**Endpoint:** `/api/notes/{id}/share/`  
**Method:** `POST`  
**Description:** Share a specific note with another user by providing their username.

### Search Notes

**Endpoint:** `/api/search/`  
**Method:** `GET`  
**Description:** Search for notes based on a keyword.

### Get All Notes

**Endpoint:** `/api/notes/`  
**Method:** `GET`  
**Description:** Retrieve a list of all notes owned or shared with the authenticated user.

## Running and Testing

1. Clone the repository. `git clone https://github.com/utkarsh23kushwaha/notes_api.git` <br>
2. `cd notes_api/test_app`
3. Set up a virtual environment and install dependencies using `pip install -r requirements.txt`. 
4. Run the Django development server: `python manage.py runserver`
5. Use the provided test script or tools like `curl` to interact with the API :
   Go to `cd tests/` <br>
   Run `python tests.py`

---

