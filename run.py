from flaskblog import create_app
#will import from init.py

app = create_app()

if (__name__ == '__main__'):
    app.run(debug=True)
#only is main if run in python!!!