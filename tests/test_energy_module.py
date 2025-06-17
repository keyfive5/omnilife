import pytest
from PyQt6.QtWidgets import QApplication
from src.modules.energy.energy_module import EnergyModule

@pytest.fixture
def app():
    """Create a QApplication instance for testing"""
    return QApplication([])

@pytest.fixture
def energy_module(app):
    """Create an EnergyModule instance for testing"""
    return EnergyModule()

def test_energy_module_initialization(energy_module):
    """Test that the energy module initializes correctly"""
    assert energy_module.name == "Energy Management"
    assert energy_module.solar_power == 0
    assert energy_module.battery_level == 0
    assert energy_module.grid_usage == 0

def test_energy_module_start_stop(energy_module):
    """Test starting and stopping the energy module"""
    # Start monitoring
    energy_module.start()
    assert not energy_module.start_button.isEnabled()
    assert energy_module.stop_button.isEnabled()
    
    # Stop monitoring
    energy_module.stop()
    assert energy_module.start_button.isEnabled()
    assert not energy_module.stop_button.isEnabled()

def test_energy_module_status(energy_module):
    """Test getting the module status"""
    status = energy_module.get_status()
    assert status["name"] == "Energy Management"
    assert "solar_power" in status
    assert "battery_level" in status
    assert "grid_usage" in status 