# Todos Learning FastAPI

This is a simple Todo application built using FastAPI. The purpose of this project is to learn and demonstrate the capabilities of FastAPI for building web applications.

## Features

- Create, read, update, and delete (CRUD) todo items
- Fast and efficient API with asynchronous support
- Easy to extend and customize

## Requirements

- Python 3.13 or higher
- Poetry for dependency management

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/todo.git
    cd todo
    ```

2. Install dependencies using Poetry:
    ```sh
    poetry install
    ```

## Usage

1. Run the FastAPI application:
    ```sh
    poetry run uvicorn todo.main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000` to access the API.

## Running Tests

To run the tests, use the following command:
```sh
poetry run pytest