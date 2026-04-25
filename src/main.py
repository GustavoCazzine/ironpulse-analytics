from domain.equipment import Equipment
from domain.fleet import FleetManager
from domain.telemetry import TelemetryRead

manager = FleetManager()
if manager.register_equipment(Equipment("ESC-01", "Escavadeira", 100)):
    print("Equipamento adicionado com sucesso!")
if manager.register_equipment(Equipment("CAM-99", "Caminhão Articulado", 90)):
    print("Equipamento adicionado com sucesso!")

manager.process_telemetry(TelemetryRead("CAM-99", 95, 5000))
manager.process_telemetry(TelemetryRead("ESC-01", 95, 1000))

print(manager.get_fleet_status())
