# Copilot Requirements for career-bot

## Project Overview
A Python-based career bot application with environment variable configuration.

## Python Version
- Python 3.8+

## Required Python Packages
- python-dotenv

## Development Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd career-bot
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install python-dotenv
   # Or use requirements.txt if available:
   # pip install -r requirements.txt
   ```

4. Environment Configuration:
   - Copy `.env.example` to `.env` (if available)
   - Or create a `.env` file in the project root
   - Add necessary environment variables

5. Run the application:
   ```bash
   python app.py
   ```

## Project Structure
```
career-bot/
├── app.py              # Main application file
├── resources/          # Resource files
├── .env               # Environment variables (not tracked in git)
├── .gitignore         # Git ignore file
└── .github/           # GitHub configuration
```

## Environment Variables
Create a `.env` file with the following variables:
```env
# Add your environment variables here
# Example:
# API_KEY=your_api_key_here
# DATABASE_URL=your_database_url
```

## Notes
- The `.env` file is automatically ignored by git for security
- Add new dependencies to this file as the project evolves
- Consider creating a `requirements.txt` file for easier dependency management
