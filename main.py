import uvicorn

if __name__ == "__main__":
    uvicorn.run("server:app", port=5000, log_level="info", reload=False)
