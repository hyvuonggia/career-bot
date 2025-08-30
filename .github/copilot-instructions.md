# GitHub Copilot Instructions for career-bot

## Project Overview
A virtual representation of myself for professional networking and recruitment interactions. This bot is designed to be showcased on LinkedIn profile, allowing recruiters and potential employers to engage with my professional persona in an interactive and informative way. The application uses OpenAI API for intelligent conversations, environment variables for configuration, and follows Python best practices.

## Technical Stack
- **Language**: Python 3.8+
- **AI**: OpenAI API for natural language processing
- **Environment Management**: python-dotenv
- **Architecture**: Modular Python application with function calling capabilities
- **Configuration**: Environment variables (.env)
- **Notifications**: Telegram integration for real-time alerts
- **Document Processing**: PDF handling for resume analysis

## Required Python Packages
- python-dotenv (for environment variable management)
- openai (for AI-powered conversations)
- pypdf (for PDF document processing)
- Additional packages will be added as project evolves

## Code Style & Conventions
- Follow PEP 8 Python style guide
- Use type hints where appropriate
- Include docstrings for functions and classes
- Use meaningful variable and function names
- Prefer f-strings for string formatting
- Handle exceptions gracefully with try/except blocks

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
   pip install -r requirements.txt
   ```

4. Environment Configuration:
   - Create a `.env` file in the project root
   - Add necessary environment variables:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   TELEGRAM_CHAT_ID=your_telegram_chat_id
   ```

5. Run the application:
   ```bash
   python app.py
   ```

## Copilot Code Generation Guidelines

### When generating Python code:
1. **Always import required modules at the top**
2. **Use environment variables for sensitive data**:
   ```python
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   api_key = os.getenv('API_KEY')
   ```
3. **Include error handling**:
   ```python
   try:
       # Your code here
       pass
   except Exception as e:
       print(f"Error: {e}")
   ```
4. **Add logging for debugging**:
   ```python
   import logging
   logging.basicConfig(level=logging.INFO)
   logger = logging.getLogger(__name__)
   ```
5. **Use classes for related functionality**
6. **Create separate modules for different features**
7. **Include docstrings and type hints**

### File Organization Patterns:
- `app.py` - Main application entry point
- `config.py` - Configuration management
- `models/` - Data models and classes
- `services/` - Business logic and external API calls
- `utils/` - Helper functions and utilities
- `resources/` - Static files, templates, data files

## Project Structure
```
career-bot/
├── app.py              # Main application file
├── resources/          # Resource files
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── .env               # Environment variables (not tracked in git)
├── .gitignore         # Git ignore file
└── .github/           # GitHub configuration
```

## Environment Variables
Create a `.env` file with the following variables:
```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Telegram Notifications
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
```

## Notes
- The `.env` file is automatically ignored by git for security
- Add new dependencies to requirements.txt as the project evolves
- This bot is designed to be showcased on LinkedIn profile for recruiter interactions

## Common Patterns for Copilot

### Career Bot Specific Patterns:
- **Job Search Functions**: Functions that search job boards, parse job descriptions
- **Resume Analysis**: Functions that analyze resumes, suggest improvements
- **Interview Preparation**: Generate interview questions, practice scenarios
- **Career Guidance**: Provide career path recommendations, skill assessments
- **Networking Tools**: LinkedIn integration, contact management

### Example Function Templates:
```python
def search_jobs(keywords: str, location: str, experience_level: str) -> List[Dict]:
    """Search for jobs based on criteria."""
    pass

def analyze_resume(resume_text: str) -> Dict[str, Any]:
    """Analyze resume and provide feedback."""
    pass

def generate_interview_questions(job_description: str) -> List[str]:
    """Generate relevant interview questions."""
    pass
```
