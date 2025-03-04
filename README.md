# News API

This project is a FastAPI application that fetches news articles from the NewsAPI based on a query or a specific topic, including news about Sri Lanka.

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/Pahinithi/News-API.git
    cd News_Api
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `settings.py` file in the root directory with your API key:
    ```python
    from pydantic_settings import BaseSettings

    class Settings(BaseSettings):
        api_key: str = "your_api_key_here"
        base_url: str = "https://newsapi.org/v2/everything"

    settings = Settings()
    ```

## Running the Application

### Run in Development Mode

Start the FastAPI server in development mode:
```sh
uvicorn app:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

### Run in Production Mode

Start the FastAPI server in production mode:
```sh
uvicorn app:app
```

## Endpoints

### Get News by Query

- **URL:** `/news`
- **Method:** `GET`
- **Query Parameters:**
  - `query` (required): The search query for fetching news articles.
  - `page_size` (optional): The number of articles to fetch (default is 5).
- **Response:** A list of news articles.

### Get News about Sri Lanka

- **URL:** `/news/sri_lanka`
- **Method:** `GET`
- **Query Parameters:**
  - `page_size` (optional): The number of articles to fetch (default is 5).
- **Response:** A list of news articles about Sri Lanka.

## Example Requests

### Get News by Query
```sh
curl -X GET "http://127.0.0.1:8000/news?query=technology&page_size=5"
```

### Get News about Sri Lanka
```sh
curl -X GET "http://127.0.0.1:8000/news/sri_lanka?page_size=5"
```

## License

This project is licensed under the MIT License.