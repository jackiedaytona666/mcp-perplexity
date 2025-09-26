# Configuration Examples

This directory contains example configuration files for different use cases and MCP clients.

## Files

### `claude_desktop_config.json`
Example configuration for Claude Desktop application. Place this content in your Claude Desktop configuration file:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

### `cline_config.json`
Example configuration for the Cline VS Code extension. Add this to your VS Code settings.json or Cline configuration.

### `docker-compose.yml`
Example Docker Compose configuration for running MCP Perplexity in a container with web UI enabled.

## Usage

1. **Copy the relevant example file**
2. **Replace `pplx-your-api-key-here` with your actual Perplexity API key**
3. **Customize other settings as needed**
4. **Follow the specific instructions for your client/environment**

## Getting Your API Key

1. Sign up for Perplexity Pro at [perplexity.ai](https://www.perplexity.ai/)
2. Go to [API Settings](https://www.perplexity.ai/settings/api)
3. Generate a new API key
4. Copy and use it in your configuration

## Security Note

⚠️ **Never commit your actual API key to version control!** Always use placeholders like `pplx-your-api-key-here` in example files and replace them with your real key only in your private configuration.

## Need Help?

See the comprehensive setup guide: [../API_KEY_SETUP.md](../API_KEY_SETUP.md)