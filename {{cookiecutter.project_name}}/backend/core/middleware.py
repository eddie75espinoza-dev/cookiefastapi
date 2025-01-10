import jwt
from fastapi import Request, HTTPException
from functools import wraps
from config import APP_CONFIG


def require_bearer_token(func):
    @wraps(func)
    async def decorated(request: Request, *args, **kwargs):
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

            # Validar cualquier otro campo relevante en el token
            if decoded_token.get("iss") != "your-issuer-name":
                raise HTTPException(status_code=403, detail="Invalid token issuer")

        except jwt.ExpiredSignatureError as jwt_exc_exp:
            raise HTTPException(status_code=401, detail="Token has expired")

        except jwt.InvalidTokenError as jwt_exc_invalid:
            raise HTTPException(status_code=403, detail="Invalid token")

        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"An error occurred: {str(exc)}")

        return await func(request, *args, **kwargs)
    return decorated
