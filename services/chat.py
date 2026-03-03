from fastapi import UploadFile
from libs.translate import convert_mp3_to_text
async def get_summary_result(file: UploadFile):
    text = convert_mp3_to_text(file)
    return True