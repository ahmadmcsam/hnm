# Hello World Python Project

A simple "Hello, World!" project in Python, showcasing basic structure, testing, and packaging.

## Setup

1.  Clone the repository:

    bash
    git clone <repository_url>
    cd hello-world-py
    

2.  Create a virtual environment (recommended):

    bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate  On Windows
    

3.  Install dependencies:

    bash
    pip install -r requirements.txt
    

## Usage

Run the application:

bash
python src/hello_world/main.py


## Testing

Run the tests:

bash
python -m unittest discover -s tests


## Packaging

Build the package:

bash
python setup.py sdist bdist_wheel


Install the package:

bash
pip install dist/hello_world_py-0.1.0-py3-none-any.whl
