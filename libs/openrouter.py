import logging
from os import getenv
from openai import OpenAI

logger = logging.getLogger("api")

_client: OpenAI | None = None

OPENROUTER_API_KEY = getenv("OPENROUTER_API_KEY", "")
OPENROUTER_MODEL = "google/gemma-3-27b-it:free "
# deepseek/deepseek-v3.2-20251201:free
def init():
    global _client
    print("OpenRouter 연결 시작... (model: %s)", OPENROUTER_MODEL)
    _client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY,
    )
    print("OpenRouter 연결 완료!")

def chat(messages: list[dict]) -> str:
    """OpenRouter 모델로 추론한다."""
    try:
        print("Start inference by openrouter.ai ....")
        response = _client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=messages,
        )
        print("Finished inference..!")
        return response.choices[0].message.content
    except Exception as e:
        print(e)
        return ""

def chat_stream(messages: list[dict]):
    """OpenRouter 모델로 추론한다. (streaming)"""
    try:
        print("Start inference by openrouter.ai ....")
        stream = _client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=messages,
            stream=True
        )
        print("Finished inference..!")
        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                yield content
    except Exception as e:
        print(e)
        return False

