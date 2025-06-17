import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt
from modules.energy.energy_module import EnergyModule
from ui.theme import APP_STYLESHEET

class HeaderBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("HeaderBar")
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)
        # Placeholder for logo (could add QPixmap here)
        title = QLabel("OmniLife")
        title.setObjectName("HeaderTitle")
        layout.addWidget(title)
        layout.addStretch()

class OmniLifeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OmniLife")
        self.setMinimumSize(1200, 800)
        
        # Apply stylesheet
        self.setStyleSheet(APP_STYLESHEET)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(8, 8, 8, 8)
        main_layout.setSpacing(0)
        
        # Add header bar
        self.header = HeaderBar()
        main_layout.addWidget(self.header)
        
        # Create tab widget for different modules
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)
        
        # Initialize modules
        self.init_modules()
        
    def init_modules(self):
        """Initialize all OmniLife modules"""
        # Energy Module
        self.energy_module = EnergyModule()
        self.tabs.addTab(self.energy_module.get_widget(), "Energy")
        
        # AI Assistant Module (placeholder)
        ai_tab = QWidget()
        self.tabs.addTab(ai_tab, "AI Assistant")
        
        # Security Module (placeholder)
        security_tab = QWidget()
        self.tabs.addTab(security_tab, "Security")
        
        # Investment Module (placeholder)
        investment_tab = QWidget()
        self.tabs.addTab(investment_tab, "Investment")
        
        # Health Module (placeholder)
        health_tab = QWidget()
        self.tabs.addTab(health_tab, "Health")

def main():
    app = QApplication(sys.argv)
    window = OmniLifeApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 