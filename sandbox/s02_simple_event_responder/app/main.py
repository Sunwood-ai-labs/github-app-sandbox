from fastapi import FastAPI, Request
from .github_bot import GithubBot

app = FastAPI()
github_bot = GithubBot()

@app.post("/")
async def handle_webhook(request: Request):
    payload = await request.json()
    return github_bot.process_event(payload)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
