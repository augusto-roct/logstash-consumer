import uvicorn

from logstash_consumer.app.main import app

if __name__ == "__main__":
    print("Start Server")

    uvicorn.run(app, "0.0.0.0", "8000", reload=True)
