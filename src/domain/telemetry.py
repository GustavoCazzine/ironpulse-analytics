from datetime import datetime

class TelemetryRead:
    def __init__(self, equipment_id, engine_temperature, operating_hours):
        self._equipment_id = equipment_id
        self._engine_temperature = engine_temperature
        self._operating_hour = operating_hours
        self._timestamp = datetime.now()

    @property
    def equipment_id(self):
        return self._equipment_id
    
    @property
    def engine_temperature(self):
        return self._engine_temperature
    
    @property
    def operating_hour(self):
        return self._operating_hour
    
    @property
    def timestamp(self):
        return self._timestamp