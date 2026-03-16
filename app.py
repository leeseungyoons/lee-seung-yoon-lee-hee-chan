import json
from urllib.parse import urlparse

import streamlit as st


st.set_page_config(
    page_title="스포츠 종목 관리",
    page_icon="⚽",
    layout="wide",
)

st.markdown(
    """
    <style>
    .sport-card {
        background: #111827;
        border: 1px solid #374151;
        border-radius: 18px;
        padding: 16px;
        margin-bottom: 16px;
    }
    .sport-title {
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 8px;
        color: white;
    }
    .sport-type {
        font-size: 15px;
        color: #d1d5db;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

SPORT_EMOJI = {
    "축구": "⚽",
    "농구": "🏀",
    "야구": "⚾",
    "배구": "🏐",
    "테니스": "🎾",
    "e스포츠": "🎮",
}

INITIAL_SPORTS = [
    {
        "name": "프리미어리그 축구",
        "types": ["축구"],
        "image_url": "https://images.unsplash.com/photo-1574629810360-7efbbe195018?q=80&w=1200&auto=format&fit=crop",
    },
    {
        "name": "NBA 농구",
        "types": ["농구"],
        "image_url": "https://images.unsplash.com/photo-1546519638-68e109498ffc?q=80&w=1200&auto=format&fit=crop",
    },
    {
        "name": "KBO 야구",
        "types": ["야구"],
        "image_url": "https://images.unsplash.com/photo-1508344928928-7165b67de128?q=80&w=1200&auto=format&fit=crop",
    },
]

EXAMPLE_SPORT = {
    "name": "챔피언스리그 축구",
    "types": ["축구"],
    "image_url": "https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?q=80&w=1200&auto=format&fit=crop",
}


def is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return result.scheme in ("http", "https") and bool(result.netloc)
    except Exception:
        return False


def normalize_name(name: str) -> str:
    return " ".join(name.strip().split()).lower()


def reset_data() -> None:
    st.session_state.sports = INITIAL_SPORTS.copy()


def save_json() -> str:
    return json.dumps(st.session_state.sports, ensure_ascii=False, indent=2)


if "sports" not in st.session_state:
    st.session_state.sports = INITIAL_SPORTS.copy()

st.title("⚽ 스포츠 종목 관리 앱")
st.markdown("종목을 **조회 / 검색 / 필터 / 추가 / 삭제**할 수 있는 Streamlit 미니 프로젝트")
st.divider()

with st.sidebar:
    st.header("검색 / 필터")
    keyword = st.text_input("종목명 검색", placeholder="예: 축구, NBA, 야구")
    selected_type = st.selectbox("종목 필터", ["전체"] + list(SPORT_EMOJI.keys()))

    st.divider()
    st.header("데이터 관리")

    if st.button("초기 데이터로 리셋", use_container_width=True):
        reset_data()
        st.success("초기화 완료")
        st.rerun()

    st.download_button(
        label="현재 목록 JSON 다운로드",
        data=save_json(),
        file_name="sports_data.json",
        mime="application/json",
        use_container_width=True,
    )

col1, col2, col3 = st.columns(3)
col1.metric("전체 종목 수", len(st.session_state.sports))
col2.metric("등록 가능한 카테고리", len(SPORT_EMOJI))
col3.metric(
    "현재 필터",
    "전체" if selected_type == "전체" else f"{SPORT_EMOJI[selected_type]} {selected_type}",
)

st.subheader("종목 추가")

auto_fill = st.toggle("예시 데이터 자동 입력", value=False)

with st.form("add_sport_form", clear_on_submit=True):
    name = st.text_input(
        "종목명",
        value=EXAMPLE_SPORT["name"] if auto_fill else "",
        placeholder="예: K리그 축구",
    )

    types = st.multiselect(
        "종목 분류",
        options=list(SPORT_EMOJI.keys()),
        default=EXAMPLE_SPORT["types"] if auto_fill else [],
        max_selections=2,
    )

    image_url = st.text_input(
        "이미지 URL",
        value=EXAMPLE_SPORT["image_url"] if auto_fill else "",
        placeholder="https://...",
    )

    submitted = st.form_submit_button("종목 추가")

    if submitted:
        clean_name = name.strip()

        if not clean_name:
            st.error("종목명을 입력해줘.")
        elif not types:
            st.error("종목 분류를 하나 이상 선택해줘.")
        elif image_url and not is_valid_url(image_url):
            st.error("이미지 URL 형식이 올바르지 않아.")
        else:
            duplicate = any(
                normalize_name(item["name"]) == normalize_name(clean_name)
                for item in st.session_state.sports
            )

            if duplicate:
                st.warning("같은 이름의 종목이 이미 있어.")
            else:
                st.session_state.sports.append(
                    {
                        "name": clean_name,
                        "types": types,
                        "image_url": image_url if image_url else "https://via.placeholder.com/600x400?text=No+Image",
                    }
                )
                st.success("종목이 추가됐어.")
                st.rerun()

filtered_sports = []
for sport in st.session_state.sports:
    match_keyword = keyword.lower() in sport["name"].lower() if keyword else True
    match_type = selected_type == "전체" or selected_type in sport["types"]
    if match_keyword and match_type:
        filtered_sports.append(sport)

st.divider()
st.subheader("종목 목록")

if not filtered_sports:
    st.info("조건에 맞는 종목이 없어.")
else:
    for i in range(0, len(filtered_sports), 3):
        cols = st.columns(3)
        for j, sport in enumerate(filtered_sports[i:i+3]):
            with cols[j]:
                st.markdown(
                    f"""
                    <div class="sport-card">
                        <div class="sport-title">{sport["name"]}</div>
                        <div class="sport-type">
                            {" / ".join(f"{SPORT_EMOJI[t]} {t}" for t in sport["types"])}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.image(sport["image_url"], use_container_width=True)

                delete_key = f"delete_{i+j}_{sport['name']}"
                if st.button("삭제", key=delete_key, use_container_width=True):
                    target_index = next(
                        (idx for idx, item in enumerate(st.session_state.sports)
                         if item["name"] == sport["name"] and item["image_url"] == sport["image_url"]),
                        None
                    )
                    if target_index is not None:
                        del st.session_state.sports[target_index]
                        st.success("삭제 완료")
                        st.rerun()
