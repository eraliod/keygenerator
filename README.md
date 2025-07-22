# RSA Key Generator

A simple GUI application for generating RSA key pairs with different output formats.

## Requirements

- Python 3.8+ (tested with Python 3.12)
- uv (recommended) or pip

## Installation and Usage

### Using uv (recommended)

1. Install uv if you haven't already:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Install Python 3.12 through uv (includes tkinter support):
   ```bash
   uv python install 3.12
   ```

3. Run the application directly with uv:
   ```bash
   uv run python -m src.app
   ```
   
   Or use the entry point:
   ```bash
   uv run keygenerator
   ```

   This will automatically:
   - Create a virtual environment using Python 3.12
   - Install all dependencies from pyproject.toml
   - Run the key generator application

### Alternative: Traditional setup

If you prefer the traditional approach:

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python -m src.app
   ```

## Features

- Generate RSA key pairs (2048-bit)
- Display private and public keys
- Multiple output formats:
  - Multiline (standard PEM format)
  - Single line (key content only)
  - Base64 encoded
- Copy to clipboard functionality

## Notes

- On macOS, the application uses Python 3.12 to ensure compatibility with tkinter
- The uv configuration automatically handles dependency management and virtual environment creation
