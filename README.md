# mamago API Server

MP3 음성 파일을 텍스트로 변환(STT)하고, LLM을 통해 요약하여 반환하는 PoC 프로젝트

## 처리 흐름

```
클라이언트 MP3 업로드 → faster-whisper(STT) → OpenRouter LLM 요약 → 클라이언트 응답
```

## 기술 스택

- **Python 3.10 / FastAPI**
- **faster-whisper** - 음성 → 텍스트 변환
- **OpenRouter.ai** - LLM 텍스트 요약 (Google Gemma 3 27B)

## 실행

```bash
pipenv install
# .env 파일 설정
# OPENROUTER_AI_KEY=your_api_key
# OPENROUTER_AI_MODEL=google/gemma-3-27b-it:free
pipenv run dev
```

> 최초 실행 시 faster-whisper 모델 다운로드 및 로드로 인해 최대 1분 정도 소요될 수 있습니다.
