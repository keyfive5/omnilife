from core.base_module import BaseModule
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QProgressBar, QSizePolicy
)
from PyQt6.QtCore import Qt, QTimer
from .battery_gauge import BatteryGauge

class EnergyModule(BaseModule):
    def __init__(self):
        super().__init__("Energy Management")
        self.solar_power = 0
        self.battery_level = 0
        self.grid_usage = 0
        
    def _init_ui(self):
        """Initialize the energy module UI"""
        layout = QVBoxLayout(self.widget)
        layout.setContentsMargins(32, 24, 32, 24)
        layout.setSpacing(24)
        
        # Dashboard row
        dash_layout = QHBoxLayout()
        dash_layout.setSpacing(40)
        
        # Solar Power
        solar_col = QVBoxLayout()
        solar_icon = QLabel("\U0001F31E")  # Sun emoji
        solar_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        solar_icon.setStyleSheet("font-size: 32px;")
        solar_col.addWidget(solar_icon)
        solar_label = QLabel("Solar Power")
        solar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        solar_col.addWidget(solar_label)
        self.solar_value = QLabel("0 kW")
        self.solar_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.solar_value.setStyleSheet("font-size: 18px; font-weight: bold;")
        solar_col.addWidget(self.solar_value)
        dash_layout.addLayout(solar_col)
        
        # Battery Gauge
        battery_col = QVBoxLayout()
        battery_icon = QLabel("\U0001F50B")  # Battery emoji
        battery_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        battery_icon.setStyleSheet("font-size: 32px;")
        battery_col.addWidget(battery_icon)
        battery_label = QLabel("Battery Level")
        battery_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        battery_col.addWidget(battery_label)
        self.battery_gauge = BatteryGauge()
        battery_col.addWidget(self.battery_gauge, alignment=Qt.AlignmentFlag.AlignCenter)
        dash_layout.addLayout(battery_col)
        
        # Grid Usage
        grid_col = QVBoxLayout()
        grid_icon = QLabel("\U0001F50C")  # Plug emoji
        grid_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid_icon.setStyleSheet("font-size: 32px;")
        grid_col.addWidget(grid_icon)
        grid_label = QLabel("Grid Usage")
        grid_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid_col.addWidget(grid_label)
        self.grid_value = QLabel("0 kW")
        self.grid_value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.grid_value.setStyleSheet("font-size: 18px; font-weight: bold;")
        grid_col.addWidget(self.grid_value)
        dash_layout.addLayout(grid_col)
        
        layout.addLayout(dash_layout)
        
        # Control Buttons
        button_layout = QHBoxLayout()
        self.start_button = QPushButton("Start Monitoring")
        self.stop_button = QPushButton("Stop Monitoring")
        self.stop_button.setEnabled(False)
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        layout.addLayout(button_layout)
        
        # Connect signals
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        
        # Add stretch to push everything to the top
        layout.addStretch()
        
    def start(self):
        """Start energy monitoring"""
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        # In a real implementation, this would connect to actual energy monitoring devices
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_values)
        self.update_timer.start(1000)  # Update every second
        
    def stop(self):
        """Stop energy monitoring"""
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        if hasattr(self, 'update_timer'):
            self.update_timer.stop()
            
    def update_values(self):
        """Update the displayed values (simulated for now)"""
        # Simulate some values - in real implementation, these would come from actual devices
        self.solar_power = max(0, self.solar_power + (0.1 if self.solar_power < 5 else -0.1))
        self.battery_level = max(0, min(100, self.battery_level + (1 if self.battery_level < 80 else -1)))
        self.grid_usage = max(0, self.grid_usage + (0.05 if self.grid_usage < 2 else -0.05))
        
        # Update UI
        self.solar_value.setText(f"{self.solar_power:.1f} kW")
        self.battery_gauge.setValue(int(self.battery_level))
        self.grid_value.setText(f"{self.grid_usage:.1f} kW")
        
    def get_status(self) -> dict:
        """Get the current status of the energy module"""
        status = super().get_status()
        status.update({
            "solar_power": self.solar_power,
            "battery_level": self.battery_level,
            "grid_usage": self.grid_usage
        })
        return status 