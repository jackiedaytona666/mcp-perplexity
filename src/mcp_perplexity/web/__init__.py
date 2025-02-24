import os
import logging
import sys
from pathlib import Path
from quart import Quart
from markdown2 import markdown
from ..database import DatabaseManager
from .database_extension import db

# Setup logging
logger = logging.getLogger(__name__)

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

# File handler for web operations
web_handler = logging.FileHandler('logs/web.log')
web_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(web_handler)

# File handler for template debugging
template_handler = logging.FileHandler('logs/templates.log')
template_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

# Set log level based on DEBUG_LOGS
if os.getenv('DEBUG_LOGS', 'false').lower() == 'true':
    logger.setLevel(logging.INFO)
    template_handler.setLevel(logging.INFO)
else:
    logger.setLevel(logging.CRITICAL)
    template_handler.setLevel(logging.CRITICAL)

# Add template handler to the template logger
template_logger = logging.getLogger('template_debug')
template_logger.addHandler(template_handler)
template_logger.propagate = False

# Disable propagation to prevent stdout logging
logger.propagate = False

# Environment variables
WEB_ENABLED = os.getenv('MCP_WEB_ENABLED', 'false').lower() == 'true'
WEB_PORT = int(os.getenv('MCP_WEB_PORT', '8050'))
WEB_HOST = os.getenv('MCP_WEB_HOST', '127.0.0.1')


def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
        template_logger.info(f"Running in PyInstaller environment. MEIPASS: {base_path}")
    except Exception:
        base_path = os.path.abspath(".")
        template_logger.info(f"Running in development environment. Base path: {base_path}")
    
    full_path = os.path.join(base_path, relative_path)
    template_logger.info(f"Full resource path for {relative_path}: {full_path}")
    template_logger.info(f"Path exists: {os.path.exists(full_path)}")
    if os.path.exists(full_path):
        template_logger.info(f"Directory contents: {os.listdir(full_path)}")
    
    return full_path


def create_app():
    if not WEB_ENABLED:
        logger.info("Web UI is disabled via environment variables")
        return None

    try:
        # Initialize Quart with template folder path
        template_path = get_resource_path('mcp_perplexity/web/templates')
        app = Quart(__name__, template_folder=template_path)

        # Add markdown filter
        app.jinja_env.filters['markdown'] = lambda text: markdown(
            text, extras=['fenced-code-blocks', 'tables'])

        # Initialize database extension
        db.init_app(app)

        # Register routes
        from .routes import register_routes
        register_routes(app)

        logger.info(
            f"Web UI initialized successfully on {WEB_HOST}:{WEB_PORT}")
        return app
    except Exception as e:
        logger.error(f"Failed to initialize web UI: {e}")
        return None
