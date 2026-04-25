from fastapi import FastAPI
from ..domain.fleet import FleetManager
from ..domain.equipment import Equipment
from ..domain.telemetry import TelemetryRead
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

manager = FleetManager()

manager.register_equipment(Equipment("ESC-01", "Escavadeira", 95))
manager.register_equipment(Equipment("CAM-99", "Caminhão Articulado", 95))
manager.register_equipment(Equipment("PCU-20", "Caminhão Articulado", 95))
manager.register_equipment(Equipment("TBN-100", "Caminhão Articulado", 95))


manager.process_telemetry(TelemetryRead("CAM-99", 110, 5000))
manager.process_telemetry(TelemetryRead("ESC-01", 89, 1000))
manager.process_telemetry(TelemetryRead("PCU-20", 105, 10000))
manager.process_telemetry(TelemetryRead("TBN-100", 94, 8500))

@app.get("/status")
async def check_status():
    return {"projeto": "IronPulse Analytics", "status": "Servidor Online"}

@app.get("/api/fleet")
async def get_fleetStatus():
    return manager.get_fleet_status()