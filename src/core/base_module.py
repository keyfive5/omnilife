from abc import ABC, abstractmethod
from PyQt6.QtWidgets import QWidget

class BaseModule(ABC):
    """Base class for all OmniLife modules"""
    
    def __init__(self, name: str):
        self.name = name
        self.widget = QWidget()
        self._init_ui()
    
    @abstractmethod
    def _init_ui(self):
        """Initialize the module's user interface"""
        pass
    
    @abstractmethod
    def start(self):
        """Start the module's functionality"""
        pass
    
    @abstractmethod
    def stop(self):
        """Stop the module's functionality"""
        pass
    
    @abstractmethod
    def get_status(self) -> dict:
        """Get the current status of the module"""
        return {
            "name": self.name,
            "status": "stopped",
            "error": None
        }
    
    def get_widget(self) -> QWidget:
        """Get the module's widget for display in the main application"""
        return self.widget 