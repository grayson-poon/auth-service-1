import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import login, signup, user, verify

ALLOW_ALL = ["*"]
app = FastAPI()
app.include_router(login.router)
app.include_router(signup.router)
app.include_router(user.router)
app.include_router(verify.router)
app.add_middleware(
   CORSMiddleware,
   allow_origins=ALLOW_ALL,
   allow_credentials=True,
   allow_methods=ALLOW_ALL,
   allow_headers=ALLOW_ALL
)

if __name__ == "__main__":
    uvicorn.run("main:app", port=1234, reload=True)