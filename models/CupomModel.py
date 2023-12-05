from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class CupomRequest(BaseModel):
    id: Optional[int] = None
    cupomName: str
    cupomValue: int
    cupomCode: str
    cupomDate: str

class CupomResponse(BaseModel):
    createDate: datetime
    message: str
    cupomId: int
