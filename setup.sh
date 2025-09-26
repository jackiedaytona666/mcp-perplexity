#!/bin/bash

# Setup script for MCP Perplexity
# Run this script to quickly set up your development environment

set -e

echo "🚀 Setting up MCP Perplexity..."

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not found. Please install Python 3.10 or higher."
    exit 1
fi

# Check Python version
python_version=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
required_version="3.10"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" = "$required_version" ]; then
    echo "✅ Python $python_version found"
else
    echo "❌ Python $required_version or higher required, but found $python_version"
    exit 1
fi

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv .venv

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -e .

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file from example..."
    cp .env.example .env
    echo "⚠️  Please edit .env file and add your Perplexity API key!"
else
    echo "✅ .env file already exists"
fi

# Set proper permissions for .env file
chmod 600 .env
echo "🔒 Set secure permissions for .env file"

# Test installation
echo "🧪 Testing installation..."
if python -c "from src.mcp_perplexity.perplexity_client import PERPLEXITY_API_KEY; print('✅ Installation successful!')"; then
    echo "✅ MCP Perplexity is ready!"
    echo ""
    
    # Run validation script
    echo "🔍 Running setup validation..."
    python validate_setup.py
    
    echo ""
    echo "Next steps:"
    echo "1. Edit .env file and add your Perplexity API key"
    echo "2. Run 'source .venv/bin/activate' to activate the environment" 
    echo "3. Run 'python validate_setup.py' to validate your configuration"
    echo "4. Run 'mcp-perplexity' to start the server"
    echo ""
    echo "For detailed setup instructions, see: API_KEY_SETUP.md"
else
    echo "❌ Installation test failed"
    exit 1
fi