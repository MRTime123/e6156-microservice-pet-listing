import flask

app = flask.Flask(__name__)


@app.get("/")
def root():
    return "Hello World!\n"


@app.get("/pet")
def say_hello():
    return "Hello Pet!\n"


@app.post("/pet")
def say_hello_text():
    return "Awesome cloud developer rm3959 says Hello\n"


@app.get("/pet/{petId}")
def say_pet_id():
    return "Awesome cloud developer rm3959 says Hello\n"


@app.post("/pet/{petId}")
def return_pet_id():
    return "Awesome cloud developer rm3959 says Hello\n"


@app.delete("/pet/{petId}")

def delete_pet():
    return "The World Ends With You\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)