# CHANGELOG


## v0.5.0 (2025-02-24)

### Continuous Integration

- Add Python setup and dependencies to release workflow
  ([`1ef0095`](https://github.com/daniel-lxs/mcp-perplexity/commit/1ef0095ea79f090d5856fb7079242fafcc80e9fa))

- Set up Python 3.10 in release workflow - Install build dependencies for Python package - Prepare
  environment for semantic release process

- Refactor release workflow with improved semantic release and publishing
  ([`fb80404`](https://github.com/daniel-lxs/mcp-perplexity/commit/fb8040418c3757f996c15db5ce64e7c9e30144a2))


## v0.4.2 (2025-02-21)

### Bug Fixes

- Increase API call timeout to 60 seconds
  ([`1df2a42`](https://github.com/daniel-lxs/mcp-perplexity/commit/1df2a42ba22336992201e293c7bc88c78ec4044a))

Extend timeout duration to allow for longer-running API requests in the server module Bump version

### Documentation

- Fix missing model on smithery command (ty @cartjacked)
  ([`abed600`](https://github.com/daniel-lxs/mcp-perplexity/commit/abed600a68f11b2348b1e186a8a0cf76430ed1e3))

- Update badge
  ([`ae5b456`](https://github.com/daniel-lxs/mcp-perplexity/commit/ae5b4564e21d38e3e14370f56acb1eb2aa63f843))

- Update name
  ([`d5c3f68`](https://github.com/daniel-lxs/mcp-perplexity/commit/d5c3f68b131177e621872d2b53961f14c0e7fe9d))


## v0.4.1 (2025-02-18)

### Bug Fixes

- Preserve citation order and duplicates in Perplexity client
  ([`4e292fc`](https://github.com/daniel-lxs/mcp-perplexity/commit/4e292fcd28f6fbe265401abe699b8a388db4f17c))

- Update citation handling to maintain original order and duplicates - Replace
  `list(dict.fromkeys())` with direct citation list in perplexity_client.py and server.py - Ensure
  consistent citation rendering across response generation

- Title argument is no longer required as this argument is not necessary for existing chats
  ([`42180a5`](https://github.com/daniel-lxs/mcp-perplexity/commit/42180a5d9a984302b5301949d2147918d28e3999))

### Chores

- Add MIT license to project configuration
  ([`829ed82`](https://github.com/daniel-lxs/mcp-perplexity/commit/829ed825c847db4db4e94cb79c9f4e387dc69386))

- Add PyInstaller spec and development dependencies
  ([`854132b`](https://github.com/daniel-lxs/mcp-perplexity/commit/854132bcfb31280e764571202d9b18007d9af778))

- Bump version to 0.4.1
  ([`eea247d`](https://github.com/daniel-lxs/mcp-perplexity/commit/eea247db17bf9d1d2576c705e3fe3ffd1f7e7842))

- Bump version to 0.4.1 in pyproject.toml
  ([`7a15333`](https://github.com/daniel-lxs/mcp-perplexity/commit/7a15333842d5b2bd92f796642f1de384f1fe8f3a))

- Bump version to 0.5.0
  ([`2752793`](https://github.com/daniel-lxs/mcp-perplexity/commit/2752793e43d590c461243d08c0bc194ce4081751))

- Consolidate PyPI publish workflow into release workflow
  ([`989afdf`](https://github.com/daniel-lxs/mcp-perplexity/commit/989afdf8550524102496438bbe25b8b666e7b9b5))

- Enhance release and PyPI publish workflows
  ([`f8ec70d`](https://github.com/daniel-lxs/mcp-perplexity/commit/f8ec70d83d7c487b0aaf969d3c4a25dc75b91532))

- Fix ci missing hatch
  ([`259bb18`](https://github.com/daniel-lxs/mcp-perplexity/commit/259bb182da9aeb519dc28bc88751c9e2f6a5d469))

- Increase default timeout for Perplexity API client
  ([`724aae0`](https://github.com/daniel-lxs/mcp-perplexity/commit/724aae0f936b449a37a21e4abed0aea71c953380))

- Extend default timeout from 60 to 120 seconds to accommodate longer-running queries - Improve API
  request resilience by allowing more time for complex responses

- Migrate from Hatch to setuptools for project build system
  ([`c73bb7a`](https://github.com/daniel-lxs/mcp-perplexity/commit/c73bb7a4b1c5018f862996bf6c62ec0c1ef334f9))

- Migrate from hatchling to setuptools build system
  ([`b2e507b`](https://github.com/daniel-lxs/mcp-perplexity/commit/b2e507b02fdc45ac854b86170735923f71af8cfd))

- Refactor PyPI and release GitHub Actions workflows
  ([`a8350ef`](https://github.com/daniel-lxs/mcp-perplexity/commit/a8350ef14107159f03742574d62b970fcd9c73f9))

- Simplify release workflow and build configuration
  ([`7d320a0`](https://github.com/daniel-lxs/mcp-perplexity/commit/7d320a0400339fb7526b558c25bca9a363e98c15))

- Update GitHub Actions checkout configuration
  ([`3fbab5c`](https://github.com/daniel-lxs/mcp-perplexity/commit/3fbab5cd35b42b201c415690340bd51bcd62d559))

- Update GitHub Actions release workflow configuration
  ([`5f16fc9`](https://github.com/daniel-lxs/mcp-perplexity/commit/5f16fc90c2e3fec2d770b15bd667d5d379769051))

- Update semantic release configuration
  ([`7f48f97`](https://github.com/daniel-lxs/mcp-perplexity/commit/7f48f9796c2874b90e599d7fb4f116d898f49994))

- Refine changelog generation settings in pyproject.toml - Add explicit build command for Hatch -
  Configure commit parser to use Angular standard - Adjust changelog sections and visibility -
  Enable more precise version tagging

### Code Style

- Enhance interactive <think> block styling and rendering
  ([`dd2ccfa`](https://github.com/daniel-lxs/mcp-perplexity/commit/dd2ccfa484f955f86783c734195080a106c16509))

- Add detailed CSS styling for <think> details and summary elements - Wrap processed content in a
  dedicated div for better styling control - Implement hover and open state transitions for think
  blocks - Add subtle animations and color variations for improved user experience

### Documentation

- Add comprehensive CONTRIBUTING.md and update README.md
  ([`8698330`](https://github.com/daniel-lxs/mcp-perplexity/commit/8698330c915fb5cf8a098d843f70bcd5017f2a4c))

- Add screenshots of webui to the readme file
  ([`441832c`](https://github.com/daniel-lxs/mcp-perplexity/commit/441832c89e32e0e08990534f0a692a5df54fc8a3))

- Revamp README with comprehensive environment variables and web UI documentation
  ([`19f9fb8`](https://github.com/daniel-lxs/mcp-perplexity/commit/19f9fb8ca33361f51c76e105aecef208f1ff9e16))

- Update README with detailed environment variable configuration table - Add web UI section with
  features, screenshots, and access instructions - Remove installation scripts and Cursor-specific
  setup details - Streamline documentation for better readability and clarity

- Update README.md
  ([`d00badb`](https://github.com/daniel-lxs/mcp-perplexity/commit/d00badba16dd33a5c110c37b5b3255831db5d9ac))

### Features

- Add chat deletion functionality and debug logging control
  ([`031a826`](https://github.com/daniel-lxs/mcp-perplexity/commit/031a82621014a9290ed0b7185ab1ac91e86550e8))

- Implement chat deletion across database, web routes, and frontend - Add environment-based logging
  configuration with DEBUG_LOGS support - Create reusable dialog component for confirmation and
  error messages - Enhance session management in database operations - Improve logging flexibility
  with conditional log level and file handling

- Add Markdown rendering support for chat messages
  ([`249e807`](https://github.com/daniel-lxs/mcp-perplexity/commit/249e807d5796cb7bec8009d7cd73e5f3188eea67))

- Add markdown2 dependency to pyproject.toml - Implement Markdown filter in Jinja2 environment -
  Update message list template to render Markdown content - Configure Tailwind Typography plugin for
  styled Markdown rendering - Support code blocks, tables, and improved text formatting

- Add port availability check and prevent multiple web UI instances
  ([`ac4c668`](https://github.com/daniel-lxs/mcp-perplexity/commit/ac4c66853d3ff0bf34122f59c28735412342c0fa))

- Implement `is_port_in_use()` function to check port availability - Add global flag
  `web_ui_running` to prevent multiple web UI launches - Enhance `run_web_ui()` with safety checks
  and state management - Ensure graceful handling of web UI startup and shutdown

- Add web interface for chat history management
  ([`a20fdb5`](https://github.com/daniel-lxs/mcp-perplexity/commit/a20fdb5494db3bec0050590f1bc3c2b53db23ef4))

- Implement web UI with Quart and SQLAlchemy for browsing chat history - Add routes for listing
  chats, viewing individual chat messages - Create responsive templates with HTMX for dynamic
  updates - Integrate database management for chat and message storage - Configure environment
  variables for web UI control - Add logging and error handling for web components

- Enhance logging configuration with environment-based control
  ([`15b88f9`](https://github.com/daniel-lxs/mcp-perplexity/commit/15b88f908366d39e2749d7911608e4ce2838bc36))

- Add conditional logging setup for Hypercorn based on DEBUG_LOGS environment variable - Modify log
  directory creation to only occur when debug logs are enabled - Improve logging flexibility by
  dynamically configuring log handlers and levels - Reduce default logging noise by disabling
  stdout/stderr logging

- Enhance markdown processing with interactive <think> block rendering
  ([`a9d05fd`](https://github.com/daniel-lxs/mcp-perplexity/commit/a9d05fdebabd9d5f7117777b65badbcc66805fab))

- Implement custom markdown filter to preserve and transform <think> tags - Add collapsible details
  element for thought process blocks - Improve message update mechanism with intelligent content
  comparison - Update base template styling for better details and summary rendering

- Enhance message storage with source citations
  ([`d19c71e`](https://github.com/daniel-lxs/mcp-perplexity/commit/d19c71e76b851fe0ad5476f2983c6b3b19c7d107))

- Include source citations in assistant responses when storing messages - Format response text to
  display sources alongside the main content - Modify message storage to preserve full response with
  source information

- Enhance Perplexity API client with model-specific configurations
  ([`78766b9`](https://github.com/daniel-lxs/mcp-perplexity/commit/78766b96f111261b2ca0dca44513fc530da51997))

- Add MODEL_PROFILES dictionary to define model-specific settings - Implement dynamic model
  configuration with temperature, top_p, and system message handling - Add fallback model selection
  for ask and chat methods - Increase default timeout to 60 seconds - Improve model parameter
  validation and flexibility

- Implement Perplexity API client and refactor server interactions
  ([`5c68f45`](https://github.com/daniel-lxs/mcp-perplexity/commit/5c68f455f3e3693bf4dbdda938457e19e9e04636))

- Create `perplexity_client.py` with async streaming client for Perplexity API - Refactor
  `server.py` to use new `PerplexityClient` for API interactions - Migrate from direct SQLite
  connections to SQLAlchemy ORM database management - Improve error handling and progress tracking
  for API requests - Simplify chat and ask methods with centralized client logic

- Implement Tokyo Night dark theme for web interface
  ([`d8dfe25`](https://github.com/daniel-lxs/mcp-perplexity/commit/d8dfe250d2b6ac67e52e07dd453c2ce3b49c2c65))

- Refactor HTML templates with dark mode color scheme - Add CSS variables for Tokyo Night theme
  colors - Update Tailwind configuration to support dark mode - Enhance UI with smooth color
  transitions - Improve readability and visual consistency across pages

- Improve web application resource path handling and logging
  ([`35be31b`](https://github.com/daniel-lxs/mcp-perplexity/commit/35be31b11323a8858720dc8d71e879f37ddc76e0))

### Refactoring

- Improve message rendering and typography in web templates
  ([`abe031c`](https://github.com/daniel-lxs/mcp-perplexity/commit/abe031c2654689e1c51f43483c5991739e4700dc))

- Enhance message list template with better text wrapping and overflow handling - Add Tailwind CSS
  classes for improved responsiveness and readability - Update base template with more robust
  typography and code block styling - Optimize message container width and break-word behavior

- Improve UI layout and spacing in chat list and base templates
  ([`3461ecf`](https://github.com/daniel-lxs/mcp-perplexity/commit/3461ecf7a956defd530191d316959c56b2f5cb87))

- Adjust padding and margin in chat list items for better visual balance - Update base template with
  flexbox layout for full-height page - Enhance responsive design with container and spacing
  adjustments - Refine typography and alignment in headers and list items

- Optimize web UI styling and layout
  ([`8b2fcae`](https://github.com/daniel-lxs/mcp-perplexity/commit/8b2fcae212c574a5676539c26aa118202e5d5f32))

- Reduce message margins for better space utilization - Improve code and pre-block styling with
  enhanced readability - Add scrollable overflow for code blocks and messages - Adjust typography
  and spacing in headers, navigation, and footer - Implement subtle hover and interaction styles for
  code and think blocks

- Streamline release workflow and build process
  ([`4fd2ca8`](https://github.com/daniel-lxs/mcp-perplexity/commit/4fd2ca86a9b37b5bbeaf1ee1644513d9f6f72d77))

- Update release workflow to use latest semantic-release version - Add multi-platform binary builds
  with PyInstaller - Implement automated artifact generation and checksum verification - Remove
  separate PyPI publish workflow in favor of integrated process - Enhance release asset upload and
  GitHub release management

- Update error page styling with Tokyo Night theme colors
  ([`fd0514a`](https://github.com/daniel-lxs/mcp-perplexity/commit/fd0514ab6e58bf38437c1de498625920be691456))

- Update web UI environment variables and configuration
  ([`410d0b9`](https://github.com/daniel-lxs/mcp-perplexity/commit/410d0b981ed5b5563d5bc878722384e902296d50))

- Rename web-related environment variables from `MCP_*` to `WEB_UI_*` - Update README documentation
  to reflect new environment variable names - Modify web module to use new environment variable
  names consistently - Maintain default values and functionality of web UI configuration


## v0.4.0 (2025-02-14)

### Chores

- Bump version to 0.4.0 for new chat functionality release
  ([`001f268`](https://github.com/daniel-lxs/mcp-perplexity/commit/001f268a4bc9305adc0845172b025deff686bc6f))

- Update semantic release configuration and version tracking
  ([`7cf3678`](https://github.com/daniel-lxs/mcp-perplexity/commit/7cf3678ec71de3bfafc7b309d293b3fa8a628e36))

### Features

- Add list and read chat functionality for Perplexity conversations
  ([`8aeb0ff`](https://github.com/daniel-lxs/mcp-perplexity/commit/8aeb0ff32cb143c6dad82d9edfdbee71e8cd8ada))

- Implement `list_chats_perplexity` to retrieve paginated chat list with details - Add
  `read_chat_perplexity` to fetch complete chat history from local storage - Update README.md with
  documentation for new chat-related tools - Introduce relative time formatting for chat creation
  timestamps


## v0.3.4 (2025-02-13)

### Bug Fixes

- Simplify Windows architecture detection in install script since the script is only available for
  amd64
  ([`2ce8977`](https://github.com/daniel-lxs/mcp-perplexity/commit/2ce8977a4bd60d09d57d2bbe3bb5b96cd4474140))

### Chores

- Bump project version to 0.3.4
  ([`44c305b`](https://github.com/daniel-lxs/mcp-perplexity/commit/44c305be590893306143d56082bfb398212c2f44))

### Documentation

- Update README.md
  ([`31c47e5`](https://github.com/daniel-lxs/mcp-perplexity/commit/31c47e5c15eb29ba2f062bee1820a94227b9b4ca))


## v0.3.1 (2025-02-11)

### Bug Fixes

- Update database path environment variable name to match the documentation
  ([`9ee1ceb`](https://github.com/daniel-lxs/mcp-perplexity/commit/9ee1ceb88259cb28fd3d0f2913f8ee3b8e281172))

### Chores

- Add cross-platform installation scripts for mcp-starter
  ([`729eb2a`](https://github.com/daniel-lxs/mcp-perplexity/commit/729eb2a3b7732d49db5780c50ec6f9fbe64b46b2))

- Bump project version to 0.3.2
  ([`c269f1d`](https://github.com/daniel-lxs/mcp-perplexity/commit/c269f1d4ed1d332df22d4387ffc65fb29de60c26))

- Improve installation scripts with enhanced error handling and user experience
  ([`0a55af5`](https://github.com/daniel-lxs/mcp-perplexity/commit/0a55af5b56588afb3ab015d0afb7dae08b13625c))

### Documentation

- Add usage section for ask_perplexity and chat_perplexity tools
  ([`f8037dc`](https://github.com/daniel-lxs/mcp-perplexity/commit/f8037dca9cbf4ea7ce013c34171067fe40958bda))

- Update README with Smithery CLI usage and MacOS note
  ([`449f172`](https://github.com/daniel-lxs/mcp-perplexity/commit/449f1720598fa91bb53e586f0d40789ae406f54e))

- Update Windows and unix installation instructions
  ([`663d7c6`](https://github.com/daniel-lxs/mcp-perplexity/commit/663d7c6bbd6585f6c3e26b38eb077807a71f321c))


## v0.3.0 (2025-02-10)

### Bug Fixes

- Package naming and version
  ([`cf29a51`](https://github.com/daniel-lxs/mcp-perplexity/commit/cf29a511a02a6c3e3f33e346e6dcfbab87925355))

### Build System

- Update hatch build configuration for package sources
  ([`84db846`](https://github.com/daniel-lxs/mcp-perplexity/commit/84db8465993c7a69359f0fce0fac1e3aa0aa7c48))

### Chores

- Bump project version to 0.3.0
  ([`35c981b`](https://github.com/daniel-lxs/mcp-perplexity/commit/35c981b56e70648cc7b8021dd8b12ada567d18a8))

### Continuous Integration

- Enable manual workflow dispatch for PyPI package publishing
  ([`f8a48ad`](https://github.com/daniel-lxs/mcp-perplexity/commit/f8a48adbd504cf327e71243e7f77c499b199203f))

### Documentation

- Revamp README with comprehensive installation and configuration guide
  ([`b8a5a86`](https://github.com/daniel-lxs/mcp-perplexity/commit/b8a5a86bac65fdd0d7e0127ec8aa2c6a4e77b2a8))

- Remove Smithery installation section - Add detailed uvx installation instructions for Windows and
  Unix systems - Enhance MCP client configuration documentation - Include more detailed environment
  variable explanations - Add link to Perplexity model documentation

### Features

- Add configuration options for Perplexity model and chat database
  ([`1228278`](https://github.com/daniel-lxs/mcp-perplexity/commit/12282788e4f586e424eaaa1ca72fb9c8e9644085))

### Refactoring

- Enhance Dockerfile for development and runtime configuration
  ([`b06a8fa`](https://github.com/daniel-lxs/mcp-perplexity/commit/b06a8fa8f9c30e68e14a6174eb89481bcb4c0a5c))

- Optimize Dockerfile and dependency management
  ([`c406e59`](https://github.com/daniel-lxs/mcp-perplexity/commit/c406e59a632e53a1a3d63f733dc6b472f5b97a5c))

- Update Dockerfile to use multi-stage build with more efficient dependency installation - Improve
  virtual environment setup and package installation process - Add Hatch build configuration in
  pyproject.toml - Update uv.lock with latest dependency versions

- Update MCP start command and add Dockerfile configuration
  ([`56cebde`](https://github.com/daniel-lxs/mcp-perplexity/commit/56cebde6e35c2c04cf4cdfba6acf6494db4b7b28))


## v0.2.1 (2025-02-06)

### Chores

- Bump project version to 0.2.1
  ([`862ed70`](https://github.com/daniel-lxs/mcp-perplexity/commit/862ed708aab049ac212c6b55f92825247682df19))

- Update release workflow permissions configuration
  ([`d4e16f7`](https://github.com/daniel-lxs/mcp-perplexity/commit/d4e16f70506eb7d8c4498b42317f54ebe03ada73))

- Move permissions to top-level workflow configuration - Add explicit write permissions for
  contents, actions, and id-token

### Documentation

- Add PyPI publish workflow badge to README
  ([`ad4de00`](https://github.com/daniel-lxs/mcp-perplexity/commit/ad4de0026e8c096fddfb62ac12cf20057fa5c27f))

- Update Glama.ai server badge URL in README
  ([`1565bf0`](https://github.com/daniel-lxs/mcp-perplexity/commit/1565bf01bc3b36e469b6b1ba4548f3d46dd84852))

- Update README with improved feature descriptions and model information
  ([`a92e563`](https://github.com/daniel-lxs/mcp-perplexity/commit/a92e563e1432d898e562dd88543aa665262cbf62))


## v0.2.0 (2025-02-06)

### Bug Fixes

- Lower the amount of numbers generated for chat ids
  ([`2dc5e01`](https://github.com/daniel-lxs/mcp-perplexity/commit/2dc5e013a152e4aed0d0b2706cd8d4b967691107))

- Remove invalid property from progress notification
  ([`51673ef`](https://github.com/daniel-lxs/mcp-perplexity/commit/51673efecd536a3161bbf3849fe4f22df34bc30f))

### Chores

- Adjust Hatch build and GitHub Actions configuration
  ([`096dd8c`](https://github.com/daniel-lxs/mcp-perplexity/commit/096dd8c8008ac8433f32c46da58aba5dfed43e8d))

- Update pyproject.toml to use explicit Python command for Hatch build - Add Hatch to PATH in GitHub
  Actions workflow

- Configure semantic release for automated versioning and GitHub releases
  ([`6c0a6cc`](https://github.com/daniel-lxs/mcp-perplexity/commit/6c0a6ccaad58c4bee60d7fbf0fcfcfc49c39e2e7))

- Improve Hatch installation and verification in GitHub Actions workflow
  ([`feebf4a`](https://github.com/daniel-lxs/mcp-perplexity/commit/feebf4a1c25924def776c76aefabc725601d41d6))

- Optimize GitHub Actions release workflow for semantic release
  ([`700bb61`](https://github.com/daniel-lxs/mcp-perplexity/commit/700bb619d05df7bfc204873129954955a015bfda))

- Refine release workflow Hatch integration
  ([`91949e0`](https://github.com/daniel-lxs/mcp-perplexity/commit/91949e01adc2736aa351dce3d363b5927842c5c0))

- Remove VSCode Python settings file
  ([`e956e37`](https://github.com/daniel-lxs/mcp-perplexity/commit/e956e37c45917b6c2a90b84d0a0471fa3486f846))

- Update artifact upload configuration in release workflow
  ([`bea6336`](https://github.com/daniel-lxs/mcp-perplexity/commit/bea633666e6621b52d1b23c63d454d138f56c7a9))

- Upgrade actions/upload-artifact to v4 - Add retention-days and compression-level settings - Ensure
  error handling for missing distribution files

- Update build and release workflow to use Hatch
  ([`15468d5`](https://github.com/daniel-lxs/mcp-perplexity/commit/15468d58717757f509b532b86699aaa11772ffbb))

- Update Hatch GitHub Action to latest version
  ([`3bd663d`](https://github.com/daniel-lxs/mcp-perplexity/commit/3bd663de613d94e95bc956d110dbae1f1596e475))

- Update VSCode configuration in .gitignore
  ([`c33ac58`](https://github.com/daniel-lxs/mcp-perplexity/commit/c33ac58e00bc163fba8f682ffedd1f056d0614e6))

### Documentation

- Update mcp-server-starter reference to mcp-starter in README
  ([`3462012`](https://github.com/daniel-lxs/mcp-perplexity/commit/34620126be7fc41a13adcddebd3ea8d78d2fe1cf))

### Features

- Enhance database initialization with robust error handling and path support
  ([`42150e5`](https://github.com/daniel-lxs/mcp-perplexity/commit/42150e5139a7c5842023ce3365ac7023febe0a01))

- Add support for configurable database path via PERPLEXITY_DB_PATH - Implement directory creation
  for database file - Improve error handling during database initialization - Use os.path for more
  flexible path management

### Refactoring

- Simplify system prompt and improve code formatting
  ([`3750cf6`](https://github.com/daniel-lxs/mcp-perplexity/commit/3750cf64526199783e312667123c662bb27c7d29))

- Extract system prompt to a constant for reusability - Remove redundant system prompt definition -
  Improve code formatting and consistency - Reduce code duplication in tool handling methods


## v0.1.2 (2025-02-05)

### Chores

- Bump version to 0.1.2
  ([`db10e3f`](https://github.com/daniel-lxs/mcp-perplexity/commit/db10e3f739ee3101d2c0a5eb7c939dc5f5acac80))

### Documentation

- Update README with new Perplexity model configuration details
  ([`b19ff40`](https://github.com/daniel-lxs/mcp-perplexity/commit/b19ff4008d00383e9bd385952a547aaa4f950346))

### Features

- Add configurable Perplexity models for ask and chat tools
  ([`904cf82`](https://github.com/daniel-lxs/mcp-perplexity/commit/904cf82a13c8f9ed845bccc13d1f5173480f93ae))

- Introduce PERPLEXITY_MODEL_ASK and PERPLEXITY_MODEL_CHAT environment variables - Allow separate
  model selection for ask and chat tools - Fallback to default PERPLEXITY_MODEL if specific models
  are not set - Increase chat ID token length for more unique identifiers


## v0.1.1 (2025-02-05)

### Bug Fixes

- Add note about timeout to README
  ([`e332ed3`](https://github.com/daniel-lxs/mcp-perplexity/commit/e332ed322a9dd29b4edd44f1ca5bd61131405dce))

### Chores

- Add PyPI publish GitHub Actions workflow
  ([`ca8e5dc`](https://github.com/daniel-lxs/mcp-perplexity/commit/ca8e5dcd48a95094e23b14e2f090429861f3f146))

- Bump version to 0.1.1
  ([`99b8bc7`](https://github.com/daniel-lxs/mcp-perplexity/commit/99b8bc70f193071f701aa3ada4b5428aac625628))

- Make version match release
  ([`996739a`](https://github.com/daniel-lxs/mcp-perplexity/commit/996739ad688a247e23f26e7e2b405cba3ba8492e))

- Remove Hirofumi Tanigami from project authors
  ([`9c80a0a`](https://github.com/daniel-lxs/mcp-perplexity/commit/9c80a0acd8537efa4289fa2480d2f39b54c368c0))

- Rename package to mcp-perplexity
  ([`3c6fbe6`](https://github.com/daniel-lxs/mcp-perplexity/commit/3c6fbe6100f392a63351cef35e7ef8514a3acf36))

- Update project metadata and version
  ([`f8b98fd`](https://github.com/daniel-lxs/mcp-perplexity/commit/f8b98fdaa46f1a28aef3dcf8c57c12107a6fdc21))

- Bump version from 0.1.2 to 0.2.3 - Add Daniel Riccio as a project author

### Documentation

- Update MCP client configuration instructions in README
  ([`8314f4a`](https://github.com/daniel-lxs/mcp-perplexity/commit/8314f4ae56bb6a3c9c856f2e1ad712bcfa064584))

- Update project repository and README with new features and installation instructions
  ([`0570610`](https://github.com/daniel-lxs/mcp-perplexity/commit/05706108253589d977af0e72d2b0cbb1077262b7))

- Update README with comprehensive installation instructions for MCP server
  ([`3fd6c1a`](https://github.com/daniel-lxs/mcp-perplexity/commit/3fd6c1a5511585ae825a965f2583d524cb527137))

### Features

- Add persistent chat functionality and database storage
  ([`a56c875`](https://github.com/daniel-lxs/mcp-perplexity/commit/a56c8753c04b2578527ebd7bfd1924bde1e1d73b))

- Implement chat history tracking with SQLite database - Add new `chat_perplexity` tool for
  maintaining conversation context - Introduce chat ID generation and message storage - Enhance
  progress tracking for chat responses - Update dependencies to include `haikunator` and `httpx` -
  Bump version to 0.2.5

- Enhance Perplexity tool with streaming response and improved error handling
  ([`bdce645`](https://github.com/daniel-lxs/mcp-perplexity/commit/bdce64515fba45f614c60c3053bdb32cf30cdd32))

- Refactored Perplexity API interaction to support streaming responses - Added robust JSON parsing
  for API chunks - Implemented progress tracking and detailed response formatting - Added system
  prompt to guide response generation - Improved error handling and logging - Updated tool input
  schema for more focused querying

### Testing

- Add comprehensive Perplexity API test suite
  ([`c7a4327`](https://github.com/daniel-lxs/mcp-perplexity/commit/c7a43276d5b67c58f98539636fe0bba431c0e118))
