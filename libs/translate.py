import logging
import time
from faster_whisper import WhisperModel

logger = logging.getLogger(__name__)

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
    except (OSError, FileNotFoundError) as e:
        logger.error(f"모델 파일 다운로드/경로 오류: {e}")
        return False
    except RuntimeError as e:
        logger.error(f"모델 로드 중 런타임 오류: {e}")
        return False
    except Exception as e:
        logger.error(f"예상하지 못한 오류: {e}")
        return False