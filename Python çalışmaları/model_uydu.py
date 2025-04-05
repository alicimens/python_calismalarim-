import sys
import serial
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig, self.ax = plt.subplots(figsize=(5, 3))
        super().__init__(fig)
        self.setParent(parent)
        self.x = []
        self.y = []

    def plot_data(self):
        self.ax.clear()  # Eski grafiği temizle
        self.ax.plot(self.x, self.y)  # Yeni verileri çiz
        self.draw()

    def update_data(self, data):
        # Veriyi güncelle
        sicaklik, basinc = data.split(',')
        self.x.append(len(self.x) + 1)
        self.y.append(float(sicaklik))  # Sadece sıcaklık verisini alıyoruz
        self.plot_data()

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerçek Zamanlı Veri Grafiği")
        self.setGeometry(100, 100, 800, 600)

        self.canvas = MplCanvas(self)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # Timer ile her saniye veri alacağız
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)  # Her saniye veri al

        # Seri port üzerinden ESP32'den veri okuma
        self.ser = serial.Serial('COM3', 115200)  # COM3 portu (ESP32'nin bağlı olduğu port)

    def update_data(self):
        if self.ser.in_waiting > 0:
            data = self.ser.readline().decode('utf-8').strip()  # Veriyi oku
            self.canvas.update_data(data)  # Veriyi grafiğe ekle

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
