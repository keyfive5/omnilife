from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QPen, QFont
from PyQt6.QtCore import Qt, QRectF

class BatteryGauge(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._value = 0  # 0-100
        self.setMinimumSize(80, 80)

    def setValue(self, value):
        self._value = max(0, min(100, value))
        self.update()

    def value(self):
        return self._value

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        rect = QRectF(10, 10, self.width() - 20, self.height() - 20)
        # Draw background circle
        painter.setPen(QPen(QColor("#444"), 8))
        painter.drawEllipse(rect)
        # Draw arc for battery level
        painter.setPen(QPen(QColor("#00e1d6"), 8))
        span_angle = int(360 * self._value / 100)
        painter.drawArc(rect, 90 * 16, -span_angle * 16)
        # Draw percentage text
        painter.setPen(Qt.GlobalColor.white)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        painter.setFont(font)
        text = f"{self._value}%"
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, text) 