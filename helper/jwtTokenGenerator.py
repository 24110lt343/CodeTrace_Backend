from datetime import datetime,timedelta,timezone
from os import getenv
from dotenv import load_dotenv
from jose import jwt
load_dotenv()

EXPIRY = int(getenv("ACCESS_TOKEN_EXPIRY"))
ALGORITHM = getenv("ENCRYPTION_ALGORITHM")

def jwtGenerator(payload:dict)->str:
    expiry = datetime.now(timezone.utc) + timedelta(days=EXPIRY)
    payload.update({
        "exp":expiry
    })
    token = jwt.encode(payload,getenv("JWT_SECRET"),ALGORITHM)
    return token

