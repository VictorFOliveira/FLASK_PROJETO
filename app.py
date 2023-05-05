from app import app
if __name__ == '__main__': #execute
    app.run(host='127.0.0.1',
            debug=True,
            port=5009)