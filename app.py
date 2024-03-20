#202284062 이희찬. 202284061 이승윤

import streamlit as st

st.set_page_config(
    page_title="스포츠의 종류",
    page_icon="https://search.pstatic.net/sunny/?src=https%3A%2F%2Fpng.pngtree.com%2Fpng-vector%2F20210129%2Fourlarge%2Fpngtree-balls-sports-ball-volleyball-rugby-sport-baseball-tennis-football-golf-basketball-png-image_2859324.jpg&type=sc960_832"
)
st.markdown("""
<style>
img {
    max-height: 390px;
}
.streamlit-expanderContent div{
    display:flex;
    justify-content:center;
    front-size: 34px;
}
[data-testid="stExpandetToggleIcon"] {
            visibility:hidden;
}
</style>
""", unsafe_allow_html=True)
            

st.title("⚽🏀⚾스포츠 종목⚽🏀⚾")
st.markdown("⚽🏀⚾⚽🏀⚾스포츠를 맘껏 검색해보세요⚽🏀⚾⚽🏀⚾ !!")

type_emoji_dict = {
    "축구": "⚽",
    "농구": "🏀",
    "야구": "⚾"


}
initial_Sport = [
    {
        "name": "🏀농구🏀",
        "types": ["농구"],
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F003%2F2014%2F09%2F25%2FNISI20140925_0010165449_web_99_20140925190907.jpg&type=sc960_832",
    },
    {
        "name": "🏀농구🏀",
        "types": ["농구"],
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxODA2MDhfODEg%2FMDAxNTI4NDI3OTk2Njcw._fxW51ySvMW41Ak0Y6TkX3htMxoEEoJHUzDRHZmHJaYg.tH5XgIWLygFmS0BQpdrjUidyRRfPnnSoD1cBudmEs4Ag.JPEG.ljhsch%2F20180607014.jpg&type=sc960_832",
    },
    {
        "name": "⚽축구⚽",
        "types": ["축구"],
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F477%2F2023%2F10%2F15%2F0000455506_005_20231015113902339.jpg&type=sc960_832",
    },
    {
        "name": "⚽축구⚽",
        "types": ["축구"],
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNDAyMThfOTEg%2FMDAxNzA4MjQ0NDEzOTMz.QkKyey-zucDnVFnUShNyBkg63m9oAnAMRqPL2Byr8-wg.iTS8538Aj-WY5RTjuLKwVV8B81NxrQcH6tAUClbxdlog.JPEG.secondhuz%2F2024-02-18_17_20_02.jpg&type=sc960_832   "
    },
     {
        "name": "⚾야구⚾",
        "types": ["야구"],
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F396%2F2015%2F04%2F30%2F20150430004302_0_99_20150430190013.jpg&type=sc960_832"
    },
     {
        "name": "⚾야구⚾",
        "types": ["야구"],
        "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20150329_202%2Fviviwa_1427588190429YEN7I_JPEG%2F%25C4%25C9%25C0%25CC%25C6%25BC%25BC%25B1%25B9%25DF_%25BE%25D8%25B5%25E5%25B7%25F9%25BD%25C3%25BD%25BA%25C4%25DA.jpg&type=sc960_832 "
    },

        
]



if "Sport" not in st.session_state:
    st.session_state.Sport = initial_Sport

auto_complete = st.toggle("예시 데이터로 채우기")
print("page_reload, auto_complete", auto_complete)
with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(
            label="스포츠 종류명⚽🏀⚾",
            value=example_Sport["name"] if auto_complete else " "
        )
    with col2:
        types = st.multiselect(
            label="종목⚽🏀⚾",
            options=list(type_emoji_dict.keys()),
            max_selections=2,
            default=example_Sport["types"] if auto_complete else []
        )
    image_url = st.text_input(
        label="⚽🏀⚾스포츠 url ",
        value=example_Sport["image_url"] if auto_complete else ""
        )
    submit = st.form_submit_button(label="Submit")
    if submit:
        if not name:
            st.error("스포츠 종목을 선택해주세요.")
        elif len(types) == 0:
            st.error("스포츠 종목을 선택해주세요.")
        else:
            st.success("종목을 추가할수있습니다.")
            st.session_state.Sport.append({
                "name": name,
                "types": types,
                "image_url": image_url if image_url else "./image/default.png"
            })

for i in range(0, len(st.session_state.Sport), 3):
    row_Sport =st.session_state.Sport[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_Sport)):
        with cols[j]:
            Sport = row_Sport[j]
            with st.expander(label=f"**{i+j+1}. {Sport['name']}**", expanded=True):
                st.image(Sport["image_url"])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in Sport["types"]]
                st.subheader(" / ".join(emoji_types))
                delete_button = st.button(label="삭제", key=i+j, use_container_width=True)
                if delete_button:
                    del st.session_state.Sport[i+j]
                    st.rerun()