from fastapi import FastAPI
from roller import RollerCipher
import os
from dotenv import load_dotenv
from pydantic import BaseModel


class ToEncryptRequest(BaseModel):
    plain_text: str
    n: int
    m: int

class ToDecryptRequest(BaseModel):
    bytes: list[int]
    n: int
    m: int

app = FastAPI()
load_dotenv()

@app.get("/flag")
def get_secured_flag():
    plain_flag = os.getenv('plain_flag')
    print(plain_flag)
    n = int(os.getenv('n'))
    m = int(os.getenv('m'))


    roller = RollerCipher(n, m)

    return roller.encrypt(plain_flag)

@app.get("/sample")
def get_sample_flag():
    sample_flag = os.getenv('sample_flag')
    print(sample_flag)
    n = int(os.getenv('n'))
    m = int(os.getenv('m'))


    roller = RollerCipher(n, m)

    return f"{sample_flag}: {roller.encrypt(sample_flag)}"


    roller = RollerCipher(n, m)

    return roller.encrypt(plain_flag)

@app.post("/encrypt")
def encrypt_string(req: ToEncryptRequest):
    roller = RollerCipher(req.n, req.m)

    return roller.encrypt(req.plain_text)

@app.post("/decrypt")
def decrypt_bytes(req: ToDecryptRequest):
    roller = RollerCipher(req.n, req.m)

    return roller.decrypt(req.bytes)