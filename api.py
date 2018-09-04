from ends.api import create_app

app, db = create_app()

if __name__ == '__main__':
    app.run(port='5002', debug=True)
