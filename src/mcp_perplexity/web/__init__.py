import os
import logging
from pathlib import Path
from quart import Quart
from ..database import DatabaseManager
from .database_extension import db

# Setup logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Ensure logs directory exists
os.makedirs('logs', exist_ok=True)

# File handler for web operations
web_handler = logging.FileHandler('logs/web.log')
web_handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(web_handler)

# Disable propagation to prevent stdout logging
logger.propagate = False

# Environment variables
WEB_ENABLED = os.getenv('MCP_WEB_ENABLED', 'false').lower() == 'true'
WEB_PORT = int(os.getenv('MCP_WEB_PORT', '8050'))
WEB_HOST = os.getenv('MCP_WEB_HOST', '127.0.0.1')


def create_app():
    if not WEB_ENABLED:
        logger.info("Web UI is disabled via environment variables")
        return None

    try:
        app = Quart(__name__)

        # Configure template and static directories
        app.template_folder = str(Path(__file__).parent / 'templates')
        app.static_folder = str(Path(__file__).parent / 'static')

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
