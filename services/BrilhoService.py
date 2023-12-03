# services/BrilhoService.py
from datetime import datetime
from typing import List
from fastapi import HTTPException
from models.CupomModel import CupomRequest, CupomResponse
from repository.BrilhoRepository import BrilhoRepository

class BrilhoService:
    def __init__(self):
        self.brilho_repository = BrilhoRepository()

    def get_cupons(self) -> List[str]:
        return self.brilho_repository.consultar_cupons()

    def get_cupom_by_id(self, cupom_id: int) -> str:
        return self.brilho_repository.consultar_cupom_por_id(cupom_id)

    def post_cupom(self, cupom_request: CupomRequest) -> CupomResponse:
        try:
            id = self.brilho_repository.cadastrar_cupom(cupom_request)
            cupom_response = CupomResponse(
                createDate=datetime.now(),
                message="Cupom cadastrado com sucesso!",
                cupomId=id,
            )
            return cupom_response
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Erro ao cadastrar o cupom: {str(e)}"
            )

    def delete_cupom(self, cupom_id: int) -> str:
        try:
            self.brilho_repository.resgatar_cupom(cupom_id)
            return "Cupom resgatado com sucesso!"
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Erro ao resgatar o cupom: {str(e)}"
            )
