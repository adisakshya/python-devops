from app import app

if __name__ == "__main__":
    # Start the application
    port = os.environ.get("PORT", 5000)
    app.run(debug=True, host="localhost", port=port)