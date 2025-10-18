# Hello Web App

A simple Python web application built with Flask that displays "Hello World Ahmad".

## Setup

1.  Clone the repository:
   bash
   git clone <repository_url>
   cd hello_web
   

2.  Create a virtual environment (recommended):
   bash
   python3 -m venv venv
   source venv/bin/activate
   

3.  Install dependencies:
   bash
   pip install -r requirements.txt
   

## Running the Application

bash
python src/app.py


Open your web browser and navigate to `http://127.0.0.1:5000` (or the address printed in the console).

## Project Structure


hello_web/
├── README.md
├── requirements.txt
├── src/
│   ├── app.py
│   └── templates/
│       └── index.html
└── tests/
    └── test_app.py
