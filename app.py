## __init__.py

from pages import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8000)
