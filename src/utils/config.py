import os
import json
from pathlib import Path
from typing import Any, Dict

class Config:
    """Configuration manager for OmniLife"""
    
    def __init__(self):
        self.config_dir = Path.home() / ".omnilife"
        self.config_file = self.config_dir / "config.json"
        self.config: Dict[str, Any] = {}
        self._ensure_config_dir()
        self.load()
    
    def _ensure_config_dir(self):
        """Ensure the configuration directory exists"""
        self.config_dir.mkdir(exist_ok=True)
    
    def load(self):
        """Load configuration from file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
            except json.JSONDecodeError:
                self.config = {}
        else:
            self.config = self._get_default_config()
            self.save()
    
    def save(self):
        """Save configuration to file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=4)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value"""
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set a configuration value"""
        self.config[key] = value
        self.save()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration"""
        return {
            "theme": "light",
            "modules": {
                "energy": {
                    "enabled": True,
                    "update_interval": 1000  # milliseconds
                },
                "ai": {
                    "enabled": True,
                    "model": "gpt-3.5-turbo"
                },
                "security": {
                    "enabled": True,
                    "encryption_level": "high"
                },
                "investment": {
                    "enabled": True,
                    "update_interval": 5000  # milliseconds
                },
                "health": {
                    "enabled": True,
                    "data_sources": []
                }
            },
            "api_keys": {},
            "user_preferences": {
                "notifications": True,
                "auto_update": True
            }
        } 