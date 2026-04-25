from .analyzer import RiskAnalyzer
from ..infrastructure.data_logger import CSVLogger


class FleetManager:
    def __init__(self):
        self._equipments = {}
        self._analyzer = RiskAnalyzer()
        self._csv_logger = CSVLogger("database.csv")

    def register_equipment(self, equipment):
        if equipment.equipment_id in self._equipments:
            return False
        
        self._equipments[equipment.equipment_id] = equipment
        return True
    
    def process_telemetry(self, telemetry_read):
        id_equipment = telemetry_read.equipment_id
        if not id_equipment:
            return False
        
        if id_equipment not in self._equipments:
            return False
        
        equipment = self._equipments[id_equipment]
        has_alert = self._analyzer.evaluate_telemetry(equipment, telemetry_read)
        self._csv_logger.log_telemetry(telemetry_read, has_alert)

    def get_fleet_status(self):
        cont_operacional = 0
        cont_alerta = 0
        cont_manutencao = 0
        for equipment in self._equipments.values():
            match equipment.status:
                case "OPERACIONAL":
                    cont_operacional +=1
                case "ALERTA":
                    cont_alerta += 1
                case "MANUTENCAO":
                    cont_manutencao +=1

        return {"operacional" : cont_operacional, "alerta": cont_alerta, "manutencao" : cont_manutencao}