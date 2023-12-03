from datetime import datetime
from pydantic import BaseModel

class CupomRequest(BaseModel):
    cupomName: str
    cupomValue: int
    cupomCode: str
    cupomDate: str

class CupomResponse(BaseModel):
    createDate: datetime
    message: str
    cupomId: int
