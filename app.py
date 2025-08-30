from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
import gradio
import json
import os
from datetime import datetime
import requests

load_dotenv(override=True)

def send_notification_to_telegram(message: str):
    """Send a notification message to Telegram."""
    try:
        chat_id = os.getenv('TELEGRAM_CHAT_ID')
        bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        
        if not chat_id:
            print("Warning: TELEGRAM_CHAT_ID not set in environment variables")
            return False
            
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "HTML"
        }
        
        response = requests.post(url, data=data, timeout=10)
        
        if response.status_code == 200:
            print(f"Telegram notification sent successfully: {message}")
            return True
        else:
            print(f"Failed to send Telegram notification. Status: {response.status_code}, Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"Error sending Telegram notification: {e}")
        return False


def record_user_detail(email):
    """Record user details and notify via Telegram."""
    send_notification_to_telegram(f"New user detail recorded: {email}")
    return {"recorded_email": email}


def record_unknown_question(question: str):
    """Record an unknown question and notify via Telegram."""
    send_notification_to_telegram(f"Unknown question recorded: {question}")
    return {"recorded_question": question}


def get_current_date() -> str:
    """Get the current date and time."""
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_date": current_date}


# OpenAI function descriptions
record_user_detail_json = {
    "type": "function",
    "function": {
        "name": "record_user_detail",
        "description": "Record user details and send a notification via Telegram",
        "parameters": {
            "type": "object",
            "properties": {
                "email": {
                    "type": "string",
                    "description": "The user's email address to record"
                }
            },
            "required": ["email"]
        }
    }
}

record_unknown_question_json = {
    "type": "function",
    "function": {
        "name": "record_unknown_question",
        "description": "Record an unknown question and send a notification via Telegram",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "The unknown question to record"
                }
            },
            "required": ["question"]
        }
    }
}

get_current_date_json = {
    "type": "function",
    "function": {
        "name": "get_current_date",
        "description": "Get the current date and time",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
}

# Tools array for OpenAI API
tools = [
    record_user_detail_json,
    record_unknown_question_json,
    get_current_date_json
]

class CareerBot:

    def __init__(self):
        self.openai = OpenAI()
        self.name = "Vuong Gia Hy"
        reader = PdfReader("resources/linkedin.pdf")
        self.linkedin = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                self.linkedin += text
        with open("resources/summary.txt", "r", encoding="utf-8") as f:
            self.summary = f.read()


    def system_prompt(self):
        system_prompt = f"You are acting as {self.name}. You are answering questions on {self.name}'s website, \
        particularly questions related to {self.name}'s career, background, skills and experience. \
        Your responsibility is to represent {self.name} for interactions on the website as faithfully as possible. \
        You are given a summary of {self.name}'s background and LinkedIn profile which you can use to answer questions. \
        Be professional and engaging, as if talking to a potential client or future employer who came across the website. \
        If you don't know the answer to any question, use your record_unknown_question tool to record the question that you couldn't answer, even if it's about something trivial or unrelated to career. \
        If the user is engaging in discussion, try to steer them towards getting in touch via email; ask for their email and record it using your record_user_details tool. "

        system_prompt += f"\n\n## Summary:\n{self.summary}\n\n## LinkedIn Profile:\n{self.linkedin}\n\n"
        system_prompt += f"With this context, please chat with the user, always staying in character as {self.name}."
        return system_prompt
    

    def handle_tool_call(self, tool_calls):
        results = []
        for tool_call in tool_calls:
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            print(f"Tool called: {tool_name}", flush=True)
            tool = globals().get(tool_name)
            result = tool(**arguments) if tool else {}
            results.append({"role": "tool","content": json.dumps(result),"tool_call_id": tool_call.id})
        return results


    def chat(self, message, history):
        messages = [{"role": "system", "content": self.system_prompt()}] + history + [{"role": "user", "content": message}]
        done = False
        while not done:
            response = self.openai.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=tools)
            if response.choices[0].finish_reason=="tool_calls":
                message = response.choices[0].message
                tool_calls = message.tool_calls
                results = self.handle_tool_call(tool_calls)
                messages.append(message)
                messages.extend(results)
            else:
                done = True
        return response.choices[0].message.content


if __name__ == "__main__":
    career_bot = CareerBot()
    gradio.ChatInterface(career_bot.chat, type="messages").launch()


