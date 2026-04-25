class CSVLogger:
    def __init__(self, path_archive):
        self._path_archive = path_archive


    def log_telemetry(self, telemetry_read, alert_triggered):
        with open(self._path_archive, 'a', encoding="utf-8") as archive:
            archive.write(f"{telemetry_read.timestamp}, {telemetry_read.equipment_id}, {telemetry_read.engine_temperature}, {telemetry_read.operating_hour}, {alert_triggered}\n")
            print("Registro adicionado com sucesso!")
