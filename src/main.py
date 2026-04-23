from domain.equipment import Equipment
from domain.analyzer import RiskAnalyzer
from domain.telemetry import TelemetryRead

e1 = Equipment("TR-99", "Trator", 90)
analyzer = RiskAnalyzer()

t1 = TelemetryRead(e1.equipment_id, 85, 4000)

analyzer.evaluate_telemetry(e1, t1)

print(e1.status)

t1 = TelemetryRead(e1.equipment_id, 92, 4000)

analyzer.evaluate_telemetry(e1, t1)

print(e1.status)

print(analyzer.alerts_log)