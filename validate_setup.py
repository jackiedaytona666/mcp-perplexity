#!/usr/bin/env python3
"""
API Key Validation Script for MCP Perplexity
Run this script to validate your API key setup and configuration.
"""

import os
import sys
import logging
from pathlib import Path

# Add the src directory to the Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

try:
    # Import only what we need to avoid server initialization
    from mcp_perplexity.perplexity_client import PERPLEXITY_API_KEY
    from mcp_perplexity.perplexity_client import PerplexityClient
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Make sure you have installed the package with 'pip install -e .'")
    sys.exit(1)
except ValueError as e:
    # This happens when server.py tries to create client without API key
    # We'll handle this in our validation
    print(f"⚠️  Note: {e}")
    try:
        from mcp_perplexity.perplexity_client import PERPLEXITY_API_KEY
        PerplexityClient = None  # We'll create it manually in our checks
    except ImportError as e:
        print(f"❌ Import error: {e}")
        sys.exit(1)

def check_api_key():
    """Check if API key is properly configured."""
    print("🔍 Checking API key configuration...")
    
    if not PERPLEXITY_API_KEY:
        print("❌ PERPLEXITY_API_KEY is not set")
        print("\nPlease set your API key using one of these methods:")
        print("1. Environment variable: export PERPLEXITY_API_KEY=pplx-your-key")
        print("2. .env file: echo 'PERPLEXITY_API_KEY=pplx-your-key' > .env")
        print("3. See API_KEY_SETUP.md for detailed instructions")
        return False
    
    if not PERPLEXITY_API_KEY.startswith('pplx-'):
        print("⚠️  Warning: API key doesn't start with 'pplx-'. This might not be a valid Perplexity API key.")
    
    print("✅ PERPLEXITY_API_KEY is set")
    print(f"✅ API key format: {PERPLEXITY_API_KEY[:8]}...")
    return True

def check_client_creation():
    """Test if PerplexityClient can be created."""
    print("\n🔧 Testing client creation...")
    
    if not PERPLEXITY_API_KEY:
        print("⚠️  Skipping client creation test (no API key set)")
        return False
    
    try:
        # Import PerplexityClient class directly to avoid server initialization
        from mcp_perplexity.perplexity_client import PerplexityClient
        client = PerplexityClient()
        print("✅ PerplexityClient created successfully")
        return True
    except ValueError as e:
        print(f"❌ Client creation failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def check_environment_variables():
    """Check all relevant environment variables."""
    print("\n🌍 Checking environment variables...")
    
    env_vars = {
        'PERPLEXITY_API_KEY': os.getenv('PERPLEXITY_API_KEY'),
        'PERPLEXITY_MODEL': os.getenv('PERPLEXITY_MODEL', 'sonar-pro (default)'),
        'PERPLEXITY_MODEL_ASK': os.getenv('PERPLEXITY_MODEL_ASK', 'Not set (uses PERPLEXITY_MODEL)'),
        'PERPLEXITY_MODEL_CHAT': os.getenv('PERPLEXITY_MODEL_CHAT', 'Not set (uses PERPLEXITY_MODEL)'),
        'DB_PATH': os.getenv('DB_PATH', 'chats.db (default)'),
        'WEB_UI_ENABLED': os.getenv('WEB_UI_ENABLED', 'false (default)'),
        'WEB_UI_PORT': os.getenv('WEB_UI_PORT', '8050 (default)'),
        'WEB_UI_HOST': os.getenv('WEB_UI_HOST', '127.0.0.1 (default)'),
        'DEBUG_LOGS': os.getenv('DEBUG_LOGS', 'false (default)'),
    }
    
    for var, value in env_vars.items():
        if var == 'PERPLEXITY_API_KEY' and value:
            # Don't show the full API key
            print(f"  {var}: {value[:8]}... (length: {len(value)})")
        else:
            print(f"  {var}: {value}")

def check_files():
    """Check if important files exist."""
    print("\n📁 Checking files...")
    
    files_to_check = [
        'API_KEY_SETUP.md',
        '.env.example',
        'setup.sh',
        'examples/claude_desktop_config.json',
        'examples/cline_config.json',
        'examples/docker-compose.yml',
    ]
    
    for file_path in files_to_check:
        if Path(file_path).exists():
            print(f"✅ {file_path} exists")
        else:
            print(f"⚠️  {file_path} not found")

def main():
    """Run all validation checks."""
    print("🚀 MCP Perplexity API Key Validation")
    print("=" * 40)
    
    # Run checks
    api_key_ok = check_api_key()
    client_ok = check_client_creation() if api_key_ok else False
    
    check_environment_variables()
    check_files()
    
    print("\n" + "=" * 40)
    print("📊 Summary:")
    
    if api_key_ok and client_ok:
        print("✅ Configuration is valid! You're ready to use MCP Perplexity.")
    elif api_key_ok:
        print("⚠️  API key is set but there were issues with client creation.")
    else:
        print("❌ API key is not properly configured.")
        print("\nNext steps:")
        print("1. Get your API key from https://www.perplexity.ai/settings/api")
        print("2. Set it using: export PERPLEXITY_API_KEY=pplx-your-key")
        print("3. Or create a .env file with: PERPLEXITY_API_KEY=pplx-your-key")
        print("4. See API_KEY_SETUP.md for detailed instructions")

if __name__ == "__main__":
    main()