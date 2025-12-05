# Online Store Project

## Description

This is an educational web application built with Django, simulating a simple online store. The project was created as part of a training course.

The current version includes the following features:
*   A main application homepage.
*   A "Contacts" page with a functional feedback form.
*   Basic project setup, including models, views, and URL routing.

The project is built using Python and the Django framework.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Lemur946/OnlineStore.git
    ```
    *(Please replace the URL with your actual repository link if it's different)*

2.  **Navigate to the project directory:**
    ```bash
    cd OnlineStore
    ```

3.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # For Windows:
    venv\Scripts\activate
    # For macOS/Linux:
    source venv/bin/activate
    ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(If this file does not exist yet, you can create it with the command: `pip freeze > requirements.txt`)*

## Usage

To run the project, follow these steps:

1.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

2.  **Create a superuser to access the admin panel:**
    ```bash
    python manage.py createsuperuser
    ```

3.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

4.  Open your web browser and navigate to **http://127.0.0.1:8000/**

## Tests

The project includes tests for its core features. To run the tests, execute the following command in your terminal:
```bash
python manage.py test


## Feedback:
Please send your feedback and suggestions by email taifyn932802@gmail.com
## Developer:
Artem Lemur Stytsko on instructions from [SkyPro](https://sky.pro/)
## License:
Not yet