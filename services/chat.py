from fastapi import UploadFile

from libs.openrouter import chat
# from libs.openrouter import chat_stream
from libs.translate import convert_mp3_to_text

def get_summary_result(file: UploadFile):
    text = convert_mp3_to_text(file)
    messages = [
        {"role": "user", "content": f"다음 텍스트를 요약해줘.\n\n{text}"},
    ]
    summary = chat(messages)
    return {"original": text, "summary": summary}
    # return chat_stream(messages)