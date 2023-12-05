# controllers/BrilhoController.py
from fastapi import APIRouter, HTTPException
from typing import List
from services.BrilhoService import BrilhoService
from models.CupomModel import CupomRequest, CupomResponse

router = APIRouter()
brilho_service = BrilhoService()

@router.get("/", response_model=List[CupomRequest])
def get_all_cupons():
    return brilho_service.get_cupons()

@router.get("/{cupom_id}")
def get_cupom_by_id(cupom_id: int):
    return brilho_service.get_cupom_by_id(cupom_id)

@router.post("/", response_model=CupomResponse)
def post_cupom(cupom_request: CupomRequest):
    return brilho_service.post_cupom(cupom_request)

@router.delete("/{cupom_id}")
def delete_cupom(cupom_id: int):
    return brilho_service.delete_cupom(cupom_id)
