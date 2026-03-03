import time

from fastapi import UploadFile
from faster_whisper import WhisperModel

from utils.error import AppException, ErrorCode, ERROR_MESSAGES

whisper_model: WhisperModel | None = None
# 최초 로드 이후부터는 ~/.cache/huggingface/hub에 저장된 모델을 참조.
# => "models--Systran--faster-whisper-small"

def load_whisper():
    global whisper_model
    if whisper_model is not None:
        return True
    try:
        print("start load whisper....")
        start = time.time()
        whisper_model = WhisperModel(
            "small",
            device="cpu",
            compute_type="int8"
        )
        print(f"Success to load whisper! ({time.time() - start:.2f}s)")
        return True
    except (OSError, FileNotFoundError):
        raise AppException(code=ErrorCode.MODEL_FILE_ERROR, message=ERROR_MESSAGES[ErrorCode.MODEL_FILE_ERROR])
    except RuntimeError:
        raise AppException(code=ErrorCode.MODEL_RUNTIME_ERROR, message=ERROR_MESSAGES[ErrorCode.MODEL_RUNTIME_ERROR])
    except Exception:
        raise AppException(code=ErrorCode.MODEL_LOAD_ERROR, message=ERROR_MESSAGES[ErrorCode.MODEL_LOAD_ERROR])


def get_model():
    global whisper_model
    if whisper_model is not None:
        return whisper_model
    load_whisper()
    return whisper_model

def convert_mp3_to_text(mp3: UploadFile):
    print(mp3)
    model = get_model()
    print(model)


