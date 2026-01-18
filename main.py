from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def  first_api():
  return {'hi there'}