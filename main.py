import streamlit as st

# 🎨 웹페이지 설정
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🧠", layout="centered")

# 🌈 제목과 설명
st.markdown("""
    <h1 style='text-align: center; color: #6C5CE7;'>🌟 MBTI 기반 진로 추천 사이트 🌟</h1>
    <h3 style='text-align: center; color: #00B894;'>당신의 성격에 꼭 맞는 직업을 추천해드려요! 💼✨</h3>
""", unsafe_allow_html=True)

st.markdown("---")

# 🧠 MBTI 선택
mbti = st.selectbox("당신의 MBTI를 선택해주세요! 🔍", [
    "INTJ 🧠 전략가",
    "INTP 🧪 논리학자",
    "ENTJ 👑 지휘관",
    "ENTP 💡 변론가",
    "INFJ 🦄 선의의 옹호자",
    "INFP 🎨 중재자",
    "ENFJ 🧚‍♂️ 언변 능숙형",
    "ENFP 🌈 활동가",
    "ISTJ 🛠️ 청렴결백한 논리주의자",
    "ISFJ 🧺 용감한 수호자",
    "ESTJ 📋 엄격한 관리자",
    "ESFJ 💖 사교적인 외교관",
    "ISTP 🧩 현실적인 장인",
    "ISFP 🍃 호기심 많은 예술가",
    "ESTP 🏍️ 모험을 즐기는 사업가",
    "ESFP 🎤 자유로운 영혼의 연예인"
])

st.markdown("")

# 📚 MBTI별 추천 직업
career_dict = {
    "INTJ": ["데이터 과학자 📊", "전략 컨설턴트 🧠", "소프트웨어 개발자 💻"],
    "INTP": ["이론 물리학자 🧪", "AI 연구자 🤖", "게임 개발자 🎮"],
    "ENTJ": ["CEO 🧑‍💼", "기업 전략가 🏢", "정치가 🏛️"],
    "ENTP": ["스타트업 창업자 🚀", "광고 기획자 📢", "발명가 🔧"],
    "INFJ": ["심리상담가 🧘‍♀️", "인권운동가 ✊", "작가 ✍️"],
    "INFP": ["소설가 📖", "시나리오 작가 🎬", "일러스트레이터 🎨"],
    "ENFJ": ["교사 👩‍🏫", "인사담당자 🤝", "강연가 🎤"],
    "ENFP": ["유튜버 📹", "이벤트 기획자 🎉", "예술 감독 🎭"],
    "ISTJ": ["회계사 📈", "법률 전문가 ⚖️", "공무원 🏛️"],
    "ISFJ": ["간호사 🏥", "사회복지사 🤲", "초등교사 👶"],
    "ESTJ": ["경영 관리자 🗂️", "군인 🪖", "프로젝트 매니저 📅"],
    "ESFJ": ["호텔리어 🏨", "상담 교사 📘", "홍보 담당자 💬"],
    "ISTP": ["엔지니어 🛠️", "파일럿 ✈️", "응급 구조사 🚑"],
    "ISFP": ["플로리스트 💐", "보석 디자이너 💎", "사진작가 📸"],
    "ESTP": ["세일즈 매니저 📞", "스턴트맨 🎬", "기업가 💼"],
    "ESFP": ["배우 🎭", "패션 디자이너 👗", "MC 🎙️"]
}

# 🌟 직업 추천 출력
selected_mbti = mbti.split()[0]  # "INTJ"만 추출
careers = career_dict.get(selected_mbti, [])

if careers:
    st.markdown(f"### 🎯 {mbti}에게 추천하는 직업은 다음과 같아요!")
    for job in careers:
        st.markdown(f"- {job}")
else:
    st.warning("직업 정보를 찾을 수 없습니다 😢")

# 🎉 마무리 메시지
st.markdown("---")
st.markdown("""
    <div style='text-align: center; font-size:18px;'>
        🧭 당신만의 길을 찾아 떠나보세요!<br>✨ 모든 성격은 고유하며, 어떤 직업도 당신과 잘 맞을 수 있어요 💖
    </div>
""", unsafe_allow_html=True)
