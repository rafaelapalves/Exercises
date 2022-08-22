import pytest
from requests import get, post
from json import loads

class TestAPI:
    def setup(self):
        self.url = "http://127.0.0.1:8000"

    def test_APIstatus(self):
        resp = get(self.url)
        assert resp.ok

    def test_APIresponse(self):
        resp = get(self.url)
        message = loads(resp.text)
        assert message["message"] == "Operações numéricas."

    def test_POSTmethod(self):
        resp = post(self.url + "/calculo", json = {"valor1":0,"valor2":0,"oper":"string"})
        message = loads(resp.text)
        esperada = {
            "valor1": 0,
            "valor2": 0,
            "oper": "string",
            }
        assert message == esperada 
