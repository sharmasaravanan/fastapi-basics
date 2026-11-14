import os
from typing import List, Literal, Optional
from fastapi import FastAPI, HTTPException, Security, Depends
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
import uvicorn


app = FastAPI(title="Power Operations Health Monitor (Simulated)")

API_KEY = "1234567asdfgh"
API_KEY_NAME = "access_token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)

def get_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

class Reading(BaseModel):
    equipment_id: str
    name: str
    voltage_kv: float
    status: str

class Alert(BaseModel):
    alert_id: str
    equipment_id: str
    message: str
    status: str

# Simulated data only. Nothing here connects to real power equipment.
READINGS = [
    Reading(equipment_id="SUB-101", name="North Substation", voltage_kv=220.1, status="normal"),
    Reading(equipment_id="SUB-102", name="East Substation", voltage_kv=218.7, status="normal"),
    Reading(equipment_id="SUB-103", name="West Substation", voltage_kv=205.2, status="investigate"),
]

ALERTS = [
    Alert(alert_id="ALT-001", equipment_id="SUB-103", message="Voltage below normal range", status="active"),
    Alert(alert_id="ALT-002", equipment_id="SUB-103", message="Voltage trend under review", status="active"),
    Alert(alert_id="ALT-003", equipment_id="SUB-101", message="Routine inspection completed", status="resolved"),
    Alert(alert_id="ALT-004", equipment_id="SUB-102", message="Cooling fan warning cleared", status="resolved"),
]


@app.get("/")
def home():
    return {
        "application": "Power Operations Health Monitor (Simulated)",
        "environment": os.getenv("APP_ENV", "training"),
    }


@app.get("/health")
def health():
    return {"status": "running"}


@app.get("/readings", response_model=List[Reading])
def list_readings(api_key: str = Depends(get_api_key)):
    return READINGS


@app.get("/readings/{equipment_id}", response_model=Reading)
def get_reading(equipment_id: str, api_key: str = Depends(get_api_key)):
    for reading in READINGS:
        if reading.equipment_id == equipment_id:
            return reading
    raise HTTPException(status_code=404, detail=f"Equipment {equipment_id} not found")


@app.get("/alerts", response_model=List[Alert])
def list_alerts(status: Optional[Literal["active", "resolved"]] = None):
    if status is None:
        return ALERTS
    return [alert for alert in ALERTS if alert.status == status]

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)