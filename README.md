# Flask Web Application

## Overview

This is a Flask-based web application that includes authentication, a help page, and basic routing functionality. The application is structured to handle user login, logout, and form submissions securely and efficiently.

## Features

- **User Authentication:**
  - Login functionality with redirection upon successful login.
  - Logout functionality to securely log out users.

- **Help Page:**
  - A form where users can submit queries or messages.
  - Form validation for user input (email and message).
  - Flash messages for feedback based on input validation.      


### Setup

 1. Clone the repository

 ```bash
  git clone https://github.com/harizonelopez/my_portfolio.git
  cd my-portfolio
 ```

 2. Create a virtual environment and activate it:

 ```bash
  python -m venv venv
  source venv/Scripts/activate   # On Mac, use `venv\bin\activate`
 ```

 3. Install the required packages:
 ```bash
  pip install -r requirements.txt
 ```


## Run the application:
 ```bash
  python main.py
 ```

## Access the application:

 Open your browser and navigate to `http://127.0.0.1:5000/`
