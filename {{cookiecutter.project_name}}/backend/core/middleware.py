import jwt
from fastapi import Request, HTTPException
from core.config import APP_CONFIG


def require_bearer_token(request: Request):
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        raise HTTPException(status_code=401, detail="Authorization header is missing!")

    if not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid Authorization header format!")

    token = auth_header.split(" ")[1]

    try:
        decoded_token = jwt.decode(
            token,
            APP_CONFIG.TOKEN_SECRET_KEY,
            algorithms=["HS256"]
        )

        if decoded_token.get("sub") != APP_CONFIG.SUB:
            raise HTTPException(status_code=403, detail="Invalid token data")

    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")

    except jwt.exceptions.InvalidTokenError:
        raise HTTPException(status_code=403, detail="Invalid token")

    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(exc)}")
