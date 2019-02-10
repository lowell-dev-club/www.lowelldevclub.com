"""
Imports
"""

# Flask imports
from flask import Flask

# Create Flask app
app = Flask(__name__)

# Add Configurations to app
app.config.from_pyfile('config.py', silent=True)

# Import all views
import lowelldevclub.views
