from fastapi import FastAPI
from routers import load_SQLite, curl_test

app = FastAPI()
app.include_router(load_SQLite.router)
app.include_router(curl_test.router)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=9000)

# run command : uvicorn main:app --host 0.0.0.0 --port 9000