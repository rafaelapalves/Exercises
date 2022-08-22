from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def home():
    return {"message" : "Operações numéricas."}

class OpMat(BaseModel):
    valor1: int
    valor2: int
    oper: str

@app.post("/calculo")
async def calculo(resp: OpMat):
    return resp

@app.post("/{oper}")
async def resultado(valor1: int, valor2: int, oper: str):
    oper.lower()
    if oper == "soma":
        result = valor1 + valor2
    elif oper == "sub":
        result = valor1 - valor2
    elif oper == "mult":
        result = valor1 * valor2
    elif oper == "div":
        result = valor1 / valor2
    else:
        return {"message" : "Operação Inválida. Tente soma, sub, mult ou div."}
    return {"Resultado" : result}
