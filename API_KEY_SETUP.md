# API Key Setup Guide for MCP Perplexity

This guide provides comprehensive instructions on how to add and configure your Perplexity API key for the MCP Perplexity server.

## 🔑 Getting a Perplexity API Key

1. **Sign up for Perplexity Pro**: Visit [perplexity.ai](https://www.perplexity.ai/) and sign up for a Pro account
2. **Access API Settings**: Go to your account settings and navigate to the API section
3. **Generate API Key**: Create a new API key (it will start with `pplx-`)
4. **Copy the Key**: Save your API key securely - you won't be able to see it again

⚠️ **Important**: Keep your API key secure and never share it publicly or commit it to version control.

## 📋 Quick Setup Methods

### Method 1: Environment Variable (Recommended)

Set the environment variable in your shell:

```bash
export PERPLEXITY_API_KEY="pplx-your-api-key-here"
```

### Method 2: Using .env File

Create a `.env` file in your project root:

```bash
echo "PERPLEXITY_API_KEY=pplx-your-api-key-here" > .env
```

### Method 3: MCP Client Configuration

Configure directly in your MCP client settings:

```json
{
  "mcpServers": {
    "mcp-perplexity": {
      "command": "uvx",
      "args": ["mcp-perplexity"],
      "env": {
        "PERPLEXITY_API_KEY": "pplx-your-api-key-here"
      }
    }
  }
}
```

## 🔧 Detailed Configuration Guide

### For Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jackiedaytona666/mcp-perplexity.git
   cd mcp-perplexity
   ```

2. **Create a .env file**:
   ```bash
   cp .env.example .env  # If example exists, otherwise create new
   nano .env  # or your preferred editor
   ```

3. **Add your API key**:
   ```env
   PERPLEXITY_API_KEY=pplx-your-api-key-here
   PERPLEXITY_MODEL=sonar-pro
   DB_PATH=chats.db
   ```

4. **Set up virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   # or .venv\Scripts\activate  # Windows
   ```

5. **Install dependencies**:
   ```bash
   pip install -e .
   ```

### For Production

#### Using Docker

1. **Create environment file**:
   ```bash
   echo "PERPLEXITY_API_KEY=pplx-your-api-key-here" > .env
   ```

2. **Run with Docker**:
   ```bash
   docker run --env-file .env mcp-perplexity
   ```

#### Using systemd (Linux)

1. **Create service file**:
   ```bash
   sudo nano /etc/systemd/system/mcp-perplexity.service
   ```

2. **Add configuration**:
   ```ini
   [Unit]
   Description=MCP Perplexity Server
   After=network.target

   [Service]
   Type=simple
   User=your-username
   WorkingDirectory=/path/to/mcp-perplexity
   Environment=PERPLEXITY_API_KEY=pplx-your-api-key-here
   ExecStart=/usr/bin/uvx mcp-perplexity
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

### For Different MCP Clients

#### Claude Desktop

Edit your Claude Desktop configuration file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "mcp-perplexity": {
      "command": "uvx",
      "args": ["mcp-perplexity"],
      "env": {
        "PERPLEXITY_API_KEY": "pplx-your-api-key-here",
        "PERPLEXITY_MODEL": "sonar-pro"
      }
    }
  }
}
```

#### Cline (VS Code Extension)

In VS Code settings or Cline configuration:

```json
{
  "mcp.servers": {
    "mcp-perplexity": {
      "command": "uvx",
      "args": ["mcp-perplexity"],
      "env": {
        "PERPLEXITY_API_KEY": "pplx-your-api-key-here"
      }
    }
  }
}
```

#### Using Smithery CLI

```bash
npx -y @smithery/cli@latest run @daniel-lxs/mcp-perplexity \
  --config '{"perplexityApiKey":"pplx-your-api-key-here","perplexityModel":"sonar-pro"}'
```

## 🔧 Configuration Options

The following environment variables can be configured:

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `PERPLEXITY_API_KEY` | Your Perplexity API key | None | **Yes** |
| `PERPLEXITY_MODEL` | Default model for interactions | `sonar-pro` | No |
| `PERPLEXITY_MODEL_ASK` | Model for ask_perplexity tool | Uses `PERPLEXITY_MODEL` | No |
| `PERPLEXITY_MODEL_CHAT` | Model for chat_perplexity tool | Uses `PERPLEXITY_MODEL` | No |
| `DB_PATH` | Database file path | `chats.db` | No |
| `WEB_UI_ENABLED` | Enable web interface | `false` | No |
| `WEB_UI_PORT` | Web interface port | `8050` | No |
| `WEB_UI_HOST` | Web interface host | `127.0.0.1` | No |
| `DEBUG_LOGS` | Enable debug logging | `false` | No |

## 🧪 Testing Your Setup

1. **Test with the included test script**:
   ```bash
   cd tests
   python test_perplexity_api.py
   ```

2. **Test using the MCP server directly**:
   ```bash
   mcp-perplexity
   ```

3. **Verify API key is loaded**:
   Look for log messages indicating whether the API key is set (without revealing the key).

## 🚨 Security Best Practices

### ✅ Do

- Use environment variables or secure configuration files
- Set appropriate file permissions (600) for .env files: `chmod 600 .env`
- Use different API keys for development and production
- Regularly rotate your API keys
- Monitor API usage for unusual activity

### ❌ Don't

- Commit API keys to version control
- Share API keys in plain text
- Use production API keys in development
- Leave .env files world-readable
- Log API keys in application logs

### Example .gitignore entries:

```gitignore
.env
.env.local
.env.*.local
*.key
secrets.json
```

## 🛠️ Troubleshooting

### Common Issues

#### 1. "PERPLEXITY_API_KEY is not set" warning

**Symptom**: Warning message in logs
**Solution**: Ensure your API key is properly set in environment variables

#### 2. "API calls will fail with unauthorized errors"

**Symptom**: 401/403 HTTP errors
**Solutions**:
- Verify API key is correct and starts with `pplx-`
- Check if your Perplexity Pro subscription is active
- Ensure you haven't exceeded rate limits

#### 3. "Perplexity API key is required" error

**Symptom**: Application won't start
**Solution**: Set the `PERPLEXITY_API_KEY` environment variable

#### 4. Environment variables not loading

**Solutions**:
- Restart your terminal/application after setting environment variables
- Check if you're using the correct syntax for your shell (bash vs zsh vs cmd)
- For .env files, ensure they're in the correct location and properly formatted

### Debugging Steps

1. **Check environment variables**:
   ```bash
   echo $PERPLEXITY_API_KEY  # Should show your key (be careful in shared environments)
   env | grep PERPLEXITY     # Shows all Perplexity-related variables
   ```

2. **Verify file permissions**:
   ```bash
   ls -la .env  # Should show -rw------- (600 permissions)
   ```

3. **Test API connectivity**:
   ```bash
   python -c "
   import os
   from src.mcp_perplexity.perplexity_client import PerplexityClient
   client = PerplexityClient()
   print('API key loaded successfully!')
   "
   ```

## 📚 Additional Resources

- [Perplexity API Documentation](https://docs.perplexity.ai/)
- [MCP Server Documentation](https://github.com/modelcontextprotocol/servers)
- [Environment Variables Guide](https://12factor.net/config)

## 💡 Tips

1. **Use descriptive variable names** in your environment files
2. **Document your configuration** for team members
3. **Set up monitoring** for API usage and costs
4. **Use secrets management tools** in production environments
5. **Test configuration changes** in development first

---

For more help, check the main [README.md](README.md) or open an issue on GitHub.