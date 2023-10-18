from fastapi import FastAPI, Response

# I like to launch directly and not use the standard FastAPI startup
import uvicorn


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/pet")
async def say_hello(name: str):
    return {"message": f"Awesome cloud developer rm3959 says hello"}


@app.post("/pet")
async def say_hello_text(name: str):
    the_message = f"Awesome cloud developer rm3959 says Hello"
    rsp = Response(content=the_message, media_type="text/plain")
    return rsp


@app.get("/pet/{petId}")
async def say_hello_text(name: str):
    the_message = f"Awesome cloud developer rm3959 says Hello"
    rsp = Response(content=the_message, media_type="text/plain")
    return rsp


@app.post("/pet/{petId}")
async def say_hello_text(name: str):
    the_message = f"Awesome cloud developer rm3959 says Hello"
    rsp = Response(content=the_message, media_type="text/plain")
    return rsp


@app.delete("/pet/{petId}")
async def delete_pet():
    return {"message": "The World Ends With You"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8012)
