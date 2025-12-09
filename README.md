Simple Contract for FastAPI Development on Upwork

This is a simple endpoint template to demonstrate a FastAPI application for development on Upwork.

How to run the application:
1. Make sure you have Python installed on your machine.
2. Install FastAPI and Uvicorn using pip inside a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate
   pip install fastapi uvicorn
   ```
3. run uvicorn to start the server:
   ```bash
   uvicorn main:app --reload
   ```