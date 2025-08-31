# Career Bot 🤖

A virtual representation of myself for professional networking and recruitment interactions. This bot is designed to be showcased on my LinkedIn profile, allowing recruiters and potential employers to engage with my professional persona in an interactive and informative way.

## 🎯 Purpose

This career bot serves as an intelligent interface between me and recruiters, providing:
- Instant responses to common career-related questions
- Information about my skills, experience, and background
- Professional networking capabilities
- 24/7 availability for initial recruitment conversations

## 🚀 Features

- **Intelligent Conversation**: Powered by OpenAI's API for natural language understanding
- **Function Calling**: Structured responses for specific queries like recording user details and unknown questions
- **Telegram Notifications**: Real-time alerts when recruiters interact with the bot
- **Professional Focus**: Tailored responses for career and recruitment scenarios

## 🛠️ Technology Stack

- **Language**: Python 3.8+
- **AI**: OpenAI API for natural language processing
- **Environment Management**: python-dotenv for configuration
- **Notifications**: Telegram integration for real-time alerts
- **Architecture**: Modular Python application with function calling capabilities

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Telegram Bot token (for notifications)

## 🔧 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd career-bot
   ```

2. **Create and activate virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Get Telegram Bot Token**:
   - Open Telegram and search for `@BotFather`
   - Start a chat with BotFather and send `/newbot`
   - Follow the instructions to create your bot (choose a name and username)
   - BotFather will provide you with a token like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`
   - Save this token for the next step

5. **Get Telegram Chat ID**:
   - Start a chat with your newly created bot
   - Send any message to your bot
   - Open this URL in your browser (replace `YOUR_BOT_TOKEN` with your actual token):
     ```
     https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
     ```
   - Look for the `"chat":{"id":` value in the response (it will be a number like `123456789`)
   - This number is your Chat ID

6. **Environment setup**:
   Create a `.env` file in the project root with:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   TELEGRAM_CHAT_ID=your_telegram_chat_id
   ```

7. **Run the application**:
   ```bash
   python app.py
   ```

## 💼 Use Cases

### For Recruiters
- Get instant information about my professional background
- Ask questions about my skills and experience
- Schedule preliminary discussions
- Receive quick responses outside business hours

### For Me
- Screen initial recruitment inquiries
- Maintain professional presence 24/7
- Track recruiter interactions and interests
- Automate responses to common questions

## 🔄 Function Capabilities

The bot includes structured functions for:
- **User Detail Recording**: Captures recruiter contact information
- **Question Tracking**: Logs questions that need human follow-up
- **Telegram Notifications**: Real-time alerts for all interactions

## 🌐 LinkedIn Integration

This bot is designed to be featured on my LinkedIn profile as:
- A professional showcase of technical skills
- An interactive resume experience
- A modern approach to networking
- A demonstration of AI integration capabilities

## 📞 Contact

When the bot can't answer a question or needs human intervention, it will:
1. Record the inquiry with timestamp
2. Send notification via Telegram
3. Provide my direct contact information for follow-up

*This project demonstrates the intersection of AI technology and professional networking, showcasing how modern tools can enhance career development and recruitment processes.*
