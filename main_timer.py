import sys

from PyQt6.QtCore import Qt, QTimer

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLCDNumber,
    QSlider,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)



class MainWindow(QWidget):

    def __init__(self, default_value=7, min_value=1, max_value=120):
        super().__init__()

        lcd = QLCDNumber(self)
        lcd.display(default_value)

        self.lcd = lcd

        slider = QSlider(Qt.Orientation.Horizontal, self)
        # устанавливаем минмальное и максимальное значение слайдера
        slider.setMinimum(min_value)
        slider.setMaximum(max_value)
        slider.setValue(default_value)
        slider.valueChanged[int].connect(lcd.display)
        self.slider = slider

        start_button = QPushButton("Start", self)
        start_button.clicked[bool].connect(self.start_button_clicked)
        self.start_button = start_button

        # stop_button = QPushButton("Stop", self)
        # stop_button.clicked[bool].connect(self.stop_button_clicked)
        # self.stop_button = stop_button

        hbox = QHBoxLayout()
        hbox.addWidget(slider)
        hbox.addWidget(start_button)
        # hbox.addWidget(stop_button)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setWindowTitle("Timer")
        self.resize(400, 300)

    def toggle_interface(self, value=True):
        self.slider.setEnabled(value)

    def start_button_clicked(self):
        # запустить отсчёт
        self.toggle_interface(False)
        self.tick_timer()

    # def stop_button_clicked(self):
        # остановить отсчёт
        # self.reset_timer()

    def tick_timer(self):
        lcd_value = self.lcd.value()
        if lcd_value > 0:
            self.lcd.display(lcd_value - 1)
            QTimer().singleShot(1000, self.tick_timer)
        else:
            self.toggle_interface(True)
            self.lcd.display(self.slider.value())

    def reset_timer(self):
        self.toggle_interface(True)
        



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exit(app.exec())

if __name__ == "__main__":
    main()
