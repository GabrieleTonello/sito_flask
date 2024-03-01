from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return """
        <html>
            <head>
                <title>
                    Test flask
                </title>
            </head>
            <body>
                <h1>ciao mondo</h1>
            </body>
        </html>
        """

if __name__ == "__main__": 
    app.run(debug=True, port= 81)