class Equipment:
    def __init__(self, equipment_id, equipment_type, max_safe_temperature):
        self._equipment_id = equipment_id
        self._equipment_type = equipment_type
        self._max_safe_temperature = max_safe_temperature
        self._status = "OPERACIONAL"

    @property
    def equipment_id(self):
        return self._equipment_id
    
    @property
    def equipment_type(self):
        return self._equipment_type

    @property
    def max_safe_temperature(self):
        return self._max_safe_temperature
    
    @max_safe_temperature.setter
    def max_safe_temperature(self, valor):
        self._max_safe_temperature = valor

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, valor):
        VALID_STATUSES  = {"OPERACIONAL", "ALERTA", "MANUTENCAO"}

        if valor not in VALID_STATUSES:
            raise ValueError("Invalid status.")
        
        if self._status == valor:
            raise ValueError("The new value is equal to the current status.")
        
        self._status = valor

    def update_status(self, new_status):
        self.status = new_status
        return True
