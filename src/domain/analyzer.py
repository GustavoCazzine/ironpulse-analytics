class RiskAnalyzer:
    def __init__(self):
        self.alerts_log = []

    def evaluate_telemetry(self, equipment, telemetry_read):
        if telemetry_read.engine_temperature >= equipment.max_safe_temperature:
            equipment.update_status("ALERTA")
            alert = f"ID:{equipment.equipment_id} - Hour: {telemetry_read.timestamp} - Excess temperature: {telemetry_read.engine_temperature}"
            self.alerts_log.append(alert)
            return True    
        
        return False