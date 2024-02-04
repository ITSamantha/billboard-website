from fastapi import Request, HTTPException


class IsAuthenticated:
    async def __call__(self, request: Request):
        print("middleware triggered")
        # token = request.cookies.get("auth_token")
        token = "secret"
        if token != "secret":
            raise HTTPException(status_code=403, detail="Invalid authorization code.")
