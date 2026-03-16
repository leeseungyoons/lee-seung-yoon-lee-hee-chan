# OpenAI Chatbot Streamlit

링크 : https://openai-chatbot-app-m94cx3i2qmcw8b2q7cxuci.streamlit.app/

Streamlit을 기반으로 구현한 **대화형 AI 챗봇 프로젝트**입니다.  
OpenAI API를 활용해 사용자의 질문에 자연스럽게 응답하며, 간단한 웹 UI를 통해 누구나 쉽게 사용할 수 있도록 구성했습니다.

이 프로젝트는 대학 실습 및 개인 학습 과정에서 진행한 미니 프로젝트로,  
**Streamlit 기반 웹앱 구현**, **OpenAI API 연동**, **대화형 인터페이스 구성**을 직접 경험하고 익히는 데 목적을 두었습니다.

---

## 프로젝트 소개

이 레포지토리는 두 개의 Streamlit 앱으로 구성되어 있습니다.

### 1. `aibot_program.py`
OpenAI API를 활용한 **대화형 AI 챗봇 앱**입니다.

- 사용자의 질문 입력
- OpenAI 모델 응답 생성
- 채팅 형태 UI 구성
- 답변 음성 재생(TTS)
- 대화 기록 유지 및 관리

### 2. `app.py`
스포츠 종목 데이터를 카드 형태로 조회/추가/삭제할 수 있는 **스포츠 종목 관리 앱**입니다.

- 스포츠 종목 목록 조회
- 종목 추가 및 삭제
- 이미지 URL 기반 카드 UI 출력
- Streamlit 기반 간단한 CRUD 실습

---

## 프로젝트 목적

이 프로젝트는 단순히 챗봇을 사용하는 수준이 아니라,  
직접 웹 인터페이스를 만들고 외부 API를 연결해보며 **AI 서비스의 기본 구조를 구현하는 경험**을 쌓기 위해 진행했습니다.

특히 다음과 같은 부분을 학습하는 데 초점을 두었습니다.

- Streamlit 기반 웹 애플리케이션 제작
- OpenAI API 연동 방식 이해
- 사용자 입력 처리 및 응답 출력 흐름 구현
- 세션 상태 관리
- 간단한 음성 출력(TTS) 기능 확장
- 미니 서비스 형태의 UI/UX 구성

---

## 주요 기능

### AI 챗봇 앱 (`aibot_program.py`)
- OpenAI API를 활용한 질문-응답형 챗봇
- 대화형 채팅 UI
- 이전 대화 내용 유지
- 답변 음성 재생 기능
- 설정값 관리 및 대화 초기화 기능

### 스포츠 앱 (`app.py`)
- 스포츠 종목 목록 조회
- 종목 검색 및 필터링
- 종목 추가 / 삭제
- 이미지 기반 카드형 UI
- JSON 다운로드 기능

---

## 폴더 구조

```bash
openai-chatbot-streamlit/
├── aibot_program.py
├── app.py
├── requirements.txt
└── README.md
```

---

## 기술 스택

- Python
- Streamlit
- OpenAI API
- gTTS

---

## 실행 방법

### 1. 저장소 클론

```bash
git clone https://github.com/leeseungyoons/openai-chatbot-streamlit.git
cd openai-chatbot-streamlit
```

### 2. 가상환경 생성 및 활성화

#### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. 라이브러리 설치

```bash
pip install -r requirements.txt
```

---

## requirements.txt

```txt
streamlit
openai
gTTS
```

---

## OpenAI API Key 설정

이 프로젝트의 챗봇 앱(`aibot_program.py`)은 OpenAI API Key가 필요합니다.

### 로컬 실행 시
직접 입력받는 방식 또는 환경변수 방식으로 설정할 수 있습니다.

### Streamlit Cloud 배포 시
`Advanced settings` 또는 `Secrets`에 아래처럼 등록합니다.

```toml
OPENAI_API_KEY = "sk-YOUR_API_KEY"
```

코드에서는 다음과 같이 사용할 수 있습니다.

```python
api_key = st.secrets["OPENAI_API_KEY"]
```

---

## 실행 명령어

### AI 챗봇 앱 실행
```bash
streamlit run aibot_program.py
```

### 스포츠 종목 앱 실행
```bash
streamlit run app.py
```

---

## 배포 기준

### 챗봇 앱 배포 시
- **Main file path**: `aibot_program.py`

### 스포츠 앱 배포 시
- **Main file path**: `app.py`

---

## 구현 내용

### `aibot_program.py`
- OpenAI API 연동
- 사용자 입력 처리
- 챗봇 응답 출력
- 대화 세션 상태 관리
- TTS 기반 답변 음성 재생

### `app.py`
- 스포츠 데이터 조회
- Streamlit 폼 기반 입력 처리
- 카드형 UI 구성
- 종목 삭제 기능
- JSON 다운로드 기능

---

## 프로젝트를 통해 배운 점

이 프로젝트를 통해 다음과 같은 부분을 직접 구현하며 학습할 수 있었습니다.

- OpenAI API를 활용한 AI 서비스 개발 흐름
- Streamlit 기반 웹앱 구조 이해
- 사용자 입력 → API 요청 → 결과 출력의 전체 사이클 구현
- 세션 상태를 활용한 대화형 인터페이스 구성
- 외부 라이브러리를 활용한 기능 확장(TTS)
- 간단한 CRUD 기능이 포함된 웹앱 구현 경험

---

## 한계점

- 챗봇 품질은 사용하는 모델과 프롬프트 구성에 따라 달라질 수 있습니다.
- 음성 입력(STT)은 현재 완전히 연결되지 않았거나 확장 여지가 있습니다.
- 스포츠 앱은 학습용 CRUD 미니 프로젝트 성격이 강합니다.
- 실제 서비스 수준보다는 **실습 및 포트폴리오용 구현 경험**에 초점을 둔 프로젝트입니다.

---

## 프로젝트 한 줄 소개

**Streamlit과 OpenAI API를 활용해 대화형 AI 챗봇과 미니 웹앱을 구현하며 AI 서비스 개발 흐름을 학습한 프로젝트**
