import pandas as pd
import matplotlib.pyplot as plt

class FleetDashboard():
    def __init__(self, path_archive):
        self.path_archive = path_archive
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.path_archive, header=None, names=["timestamp", "equipment_id", "engine_temperature", "operating_hour", "alert_triggered"],sep=",")

    def show_raw_data(self):
        print(self.df.head())

    def plot_max_temperatures(self):
        max_temperatures = self.df.groupby("equipment_id")["engine_temperature"].max()
        max_temperatures.plot( kind="bar", color="red")
        plt.title("Temperatura Máxima por Equipamento")
        plt.ylabel("Temperatura (°C)")
        plt.show()
