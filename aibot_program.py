import json
import tempfile
from datetime import datetime

import streamlit as st
from gtts import gTTS
from openai import OpenAI


SYSTEM_PROMPT = """
너는 친근하고 센스 있게 답하는 한국어 채팅 비서다.
답변은 핵심부터 말하고, 너무 길지 않게 정리한다.
필요하면 예시를 들어 쉽게 설명한다.
"""


def reset_chat() -> None:
    st.session_state.messages = []
    st.session_state.chat_log = []


def text_to_speech_bytes(text: str) -> bytes:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        temp_name = tmp.name

    tts = gTTS(text=text, lang="ko")
    tts.save(temp_name)

    with open(temp_name, "rb") as f:
        audio_bytes = f.read()

    return audio_bytes


def ask_gpt(client: OpenAI, model: str, messages: list[dict], temperature: float) -> str:
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + messages,
    )
    return response.choices[0].message.content.strip()


def render_chat_log() -> None:
    for item in st.session_state.chat_log:
        with st.chat_message(item["role"]):
            st.markdown(item["content"])
            st.caption(item["time"])


def main() -> None:
    st.set_page_config(page_title="채팅 비서 프로그램", page_icon="📱", layout="wide")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "chat_log" not in st.session_state:
        st.session_state.chat_log = []

    st.title("📱 채팅 비서 프로그램")
    st.markdown("OpenAI API를 활용한 **대화형 AI 비서**입니다.")
    st.divider()

    with st.expander("프로그램 소개", expanded=True):
        st.write(
            """
            - Streamlit 기반으로 만든 대화형 챗봇 앱입니다.
            - 사용자가 질문하면 OpenAI 모델이 답변합니다.
            - 답변은 화면에 표시되고, 원하면 음성으로도 들을 수 있습니다.
            - 이전 대화 내용을 기억해 이어서 대화할 수 있습니다.
            """
        )

    with st.sidebar:
        st.header("설정")

        api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="sk-...",
        )

        model = st.text_input("모델명", value="gpt-4o-mini")
        temperature = st.slider("창의성(temperature)", 0.0, 1.5, 0.7, 0.1)
        use_tts = st.toggle("답변 음성 재생", value=True)

        st.divider()

        if st.button("대화 초기화", use_container_width=True):
            reset_chat()
            st.success("대화가 초기화되었습니다.")
            st.rerun()

        if st.session_state.chat_log:
            chat_json = json.dumps(st.session_state.chat_log, ensure_ascii=False, indent=2)
            st.download_button(
                label="대화 기록 다운로드",
                data=chat_json,
                file_name="chat_log.json",
                mime="application/json",
                use_container_width=True,
            )

    left, right = st.columns([1.2, 1.8])

    with left:
        st.subheader("질문 입력")
        user_input = st.chat_input("질문을 입력하세요")

        if user_input:
            if not api_key:
                st.warning("먼저 OpenAI API Key를 입력해줘.")
                st.stop()

            now = datetime.now().strftime("%H:%M")

            st.session_state.messages.append({"role": "user", "content": user_input})
            st.session_state.chat_log.append(
                {"role": "user", "content": user_input, "time": now}
            )

            client = OpenAI(api_key=api_key)

            try:
                answer = ask_gpt(
                    client=client,
                    model=model,
                    messages=st.session_state.messages,
                    temperature=temperature,
                )
            except Exception as e:
                st.error(f"응답 생성 중 오류 발생: {e}")
                st.stop()

            now = datetime.now().strftime("%H:%M")
            st.session_state.messages.append({"role": "assistant", "content": answer})
            st.session_state.chat_log.append(
                {"role": "assistant", "content": answer, "time": now}
            )

            st.rerun()

        st.info("왼쪽 입력창에 질문을 넣으면 오른쪽에 대화가 누적돼.")

    with right:
        st.subheader("대화 화면")
        if not st.session_state.chat_log:
            st.caption("아직 대화가 없습니다. 질문을 입력해보세요.")
        else:
            render_chat_log()

            last_item = st.session_state.chat_log[-1]
            if use_tts and last_item["role"] == "assistant":
                try:
                    audio_bytes = text_to_speech_bytes(last_item["content"])
                    st.audio(audio_bytes, format="audio/mp3")
                except Exception as e:
                    st.warning(f"TTS 생성 실패: {e}")


if __name__ == "__main__":
    main()
