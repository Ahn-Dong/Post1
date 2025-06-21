import streamlit as st

# 🌈 설정
st.set_page_config(page_title="MBTI 진로 추천 테스트", page_icon="🧠", layout="centered")

# 🎨 타이틀
st.markdown("<h1 style='text-align: center;'>🌟 나의 MBTI는? 그리고 어울리는 직업은? 💼</h1>", unsafe_allow_html=True)
st.markdown("---")

# 📋 간단한 MBTI 테스트 질문지
questions = [
    ("사교적인 편이다", 'E'),
    ("혼자 있는 시간이 필요하다", 'I'),
    ("직관적으로 문제를 이해한다", 'N'),
    ("현실적으로 문제를 본다", 'S'),
    ("감정보다 논리를 우선한다", 'T'),
    ("논리보다 감정을 중시한다", 'F'),
    ("계획을 세우고 실천한다", 'J'),
    ("즉흥적으로 움직인다", 'P'),
]

# 📩 사용자 선택 저장할 변수
responses = {}

# 🧠 테스트 시작
with st.form("mbti_test"):
    st.write("👇 다음 질문에 답해주세요!")
    for q, trait in questions:
        responses[trait] = st.radio(f"{q}", [f"{trait} 성향", f"반대 성향"], key=q)
    
    submitted = st.form_submit_button("MBTI 결과 보기 🚀")

if submitted:
    # 🔍 MBTI 계산
    result = ''
    result += 'E' if responses['E'].startswith('E') else 'I'
    result += 'N' if responses['N'].startswith('N') else 'S'
    result += 'T' if responses['T'].startswith('T') else 'F'
    result += 'J' if responses['J'].startswith('J') else 'P'

    st.markdown(f"<h2 style='text-align:center;'>✨ 당신의 MBTI는 <span style='color:#6C5CE7'>{result}</span> 입니다! ✨</h2>", unsafe_allow_html=True)

    # 🧑‍🎨 캐릭터 아바타 (예시 이미지)
    st.image(f"https://avatars.dicebear.com/api/personas/{result}.svg", width=200, caption=f"{result} 캐릭터 아바타")

    # 📌 직업 추천 목록
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

    # 🥇 추천 직업 출력
    st.markdown(f"### 💼 {result}에게 어울리는 추천 직업!")
    for job in career_dict.get(result, []):
        st.markdown(f"- {job}")

    # 🔎 다른 MBTI 직업 보기
    with st.expander("다른 MBTI의 직업 추천도 보기 🔍"):
        for mbti_type, jobs in career_dict.items():
            if mbti_type != result:
                st.markdown(f"**{mbti_type}** 👇")
                st.markdown(" / ".join(jobs))
                st.markdown("---")
