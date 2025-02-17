import asyncio
import os
import sys
import logging
from typing import Optional

from mcp.server import Server

from .server import server as mcp_server, main as server_main
from .web import create_app, WEB_ENABLED, WEB_PORT, WEB_HOST

__version__ = "0.4.0"


async def run_web_ui():
    app = create_app()
    if app:
        try:
            from hypercorn.asyncio import serve
            from hypercorn.config import Config

            # Set up file logging for Hypercorn
            hypercorn_logger = logging.getLogger('hypercorn')
            hypercorn_logger.handlers = []  # Remove any existing handlers
            handler = logging.FileHandler('logs/hypercorn.log')
            handler.setFormatter(logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            hypercorn_logger.addHandler(handler)
            hypercorn_logger.propagate = False

            config = Config()
            config.bind = [f"{WEB_HOST}:{WEB_PORT}"]
            # Completely disable all Hypercorn logging to stdout/stderr
            config.accesslog = None
            config.errorlog = None
            # Set log level to critical to minimize logging
            hypercorn_logger.setLevel(logging.CRITICAL)

            await serve(app, config)
        except Exception as e:
            # Log to file instead of stdout
            with open('logs/web_error.log', 'a') as f:
                f.write(f"Failed to start web UI: {e}\n")


async def run_server(args: Optional[list] = None):
    if args is None:
        args = sys.argv[1:]

    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)

    # Start both the web UI and MCP server
    tasks = []

    # Add web UI task if enabled
    if WEB_ENABLED:
        tasks.append(run_web_ui())

    # Add MCP server task - this is the only one that should use stdio
    tasks.append(server_main())

    # Run both tasks concurrently
    await asyncio.gather(*tasks)


def main(args: Optional[list] = None):
    """Main entry point for the package."""
    try:
        # Configure logging based on DEBUG_LOGS environment variable
        if os.getenv('DEBUG_LOGS', 'false').lower() != 'true':
            # Disable all root logging to prevent any stdout logging
            logging.getLogger().handlers = []
            # Set root logger level to CRITICAL to minimize any accidental logging
            logging.getLogger().setLevel(logging.CRITICAL)
        else:
            # Ensure logs directory exists
            os.makedirs('logs', exist_ok=True)
            # Configure root logger for debug mode
            root_logger = logging.getLogger()
            root_logger.setLevel(logging.INFO)
            # Add file handler for general logs
            handler = logging.FileHandler('logs/app.log')
            handler.setFormatter(logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            root_logger.addHandler(handler)

        asyncio.run(run_server(args))
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()

__all__ = ["main", "server"]
