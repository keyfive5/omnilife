import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

def check_dependencies():
    """Check if all required dependencies are installed"""
    try:
        import PyQt6
        import pandas
        import numpy
        import requests
        import dotenv
        import cryptography
        import openai
        import pymongo
        return True
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("\nPlease install all dependencies using:")
        print("pip install -r requirements.txt")
        return False

def main():
    """Main entry point for the application"""
    if not check_dependencies():
        sys.exit(1)
        
    try:
        from main import main
        main()
    except Exception as e:
        print(f"Error running application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 