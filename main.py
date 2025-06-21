import streamlit as st

# 🌈 페이지 기본 설정
st.set_page_config(page_title="MBTI 진로 추천 테스트", page_icon="🧠", layout="centered")

# 🎨 타이틀
st.markdown("<h1 style='text-align: center;'>🌟 재미있는 MBTI 테스트와 진로 추천 💼</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>10개의 질문으로 알아보는 당신의 성격과 어울리는 직업은?</h4>", unsafe_allow_html=True)
st.markdown("---")

# 📋 질문지 구성
questions = [
    ("사람들과 어울릴 때 에너지가 생긴다", 'E'),
    ("혼자 있는 시간이 필요하다", 'I'),
    ("상상하고 공상하는 것을 좋아한다", 'N'),
    ("현실적인 편이다", 'S'),
    ("논리적으로 판단하는 편이다", 'T'),
    ("감정에 따라 움직이는 경우가 많다", 'F'),
    ("계획을 세우고 따르는 것이 편하다", 'J'),
    ("즉흥적으로 행동하는 것이 좋다", 'P'),
    ("감정보다 사실이 더 중요하다고 느낀다", 'T'),
    ("사람들의 고민을 잘 들어주는 편이다", 'F')
]

scores = {
    'E': 0, 'I': 0,
    'N': 0, 'S': 0,
    'T': 0, 'F': 0,
    'J': 0, 'P': 0
}

options = {
    "그렇다": 2,
    "보통이다": 1,
    "아니다": 0
}

with st.form("mbti_form"):
    st.write("👇 아래 문항에 응답해주세요!")
    answers = []
    for i, (q, trait) in enumerate(questions):
        response = st.radio(f"{i+1}. {q}", ["그렇다", "보통이다", "아니다"], key=q)
        answers.append((trait, response))
    submitted = st.form_submit_button("결과 보기 🚀")

if submitted:
    for trait, response in answers:
        if trait == 'E':
            scores['E'] += options[response]
            scores['I'] += 2 - options[response]
        elif trait == 'I':
            scores['I'] += options[response]
            scores['E'] += 2 - options[response]
        elif trait == 'N':
            scores['N'] += options[response]
            scores['S'] += 2 - options[response]
        elif trait == 'S':
            scores['S'] += options[response]
            scores['N'] += 2 - options[response]
        elif trait == 'T':
            scores['T'] += options[response]
            scores['F'] += 2 - options[response]
        elif trait == 'F':
            scores['F'] += options[response]
            scores['T'] += 2 - options[response]
        elif trait == 'J':
            scores['J'] += options[response]
            scores['P'] += 2 - options[response]
        elif trait == 'P':
            scores['P'] += options[response]
            scores['J'] += 2 - options[response]

    result = ''
    result += 'E' if scores['E'] >= scores['I'] else 'I'
    result += 'N' if scores['N'] >= scores['S'] else 'S'
    result += 'T' if scores['T'] >= scores['F'] else 'F'
    result += 'J' if scores['J'] >= scores['P'] else 'P'

    st.markdown(f"<h2 style='text-align:center;'>✨ 당신의 MBTI는 <span style='color:#6C5CE7'>{result}</span> 입니다! ✨</h2>", unsafe_allow_html=True)
    st.markdown("---")

    # 🎯 추천 직업
    career_dict = {
        "INTJ": ["데이터 과학자 📊", "전략 컨설턴트 🧠", "IT 아키텍트 💻", "경영 분석가 📈", "UX 기획자 🧩"],
        "INTP": ["AI 연구자 🤖", "이론 물리학자 🧪", "게임 개발자 🎮", "시스템 엔지니어 🧮", "수학자 🔢"],
        "ENTJ": ["CEO 🧑‍💼", "기획 전략가 🏢", "정치가 🏛️", "투자 분석가 📊", "사업 개발자 🔍"],
        "ENTP": ["창업가 🚀", "광고 기획자 📢", "변리사 ⚖️", "방송 작가 ✍️", "디지털 마케터 📱"],
        "INFJ": ["심리상담가 🧘‍♀️", "교육 콘텐츠 개발자 🎓", "비영리단체 활동가 🤝", "작가 ✍️", "사서 📚"],
        "INFP": ["소설가 📖", "시나리오 작가 🎬", "일러스트레이터 🎨", "뮤지션 🎼", "콘텐츠 크리에이터 📹"],
        "ENFJ": ["교사 👩‍🏫", "HR 담당자 🤝", "연설가 🎤", "사회운동가 ✊", "홍보 전문가 📣"],
        "ENFP": ["유튜버 📹", "이벤트 기획자 🎉", "에디터 ✏️", "광고 크리에이티브 🎭", "에듀테크 개발자 💡"],
        "ISTJ": ["회계사 📈", "법률 전문가 ⚖️", "세무사 💰", "공무원 🏛️", "시스템 관리자 🖥️"],
        "ISFJ": ["간호사 🏥", "사회복지사 🤲", "초등교사 👶", "비서 📋", "고객지원 담당자 ☎️"],
        "ESTJ": ["프로젝트 매니저 📅", "군인 🪖", "행정직 공무원 🏢", "시설 관리자 🛠️", "팀 리더 📋"],
        "ESFJ": ["호텔리어 🏨", "상담 교사 📘", "홍보 담당자 💬", "영양사 🥗", "이벤트 운영자 🎊"],
        "ISTP": ["기계공 🛠️", "응급 구조사 🚑", "항공정비사 ✈️", "드론 기술자 🚁", "목수 🔨"],
        "ISFP": ["플로리스트 💐", "보석 디자이너 💎", "사진작가 📸", "인테리어 디자이너 🛋️", "요리사 👩‍🍳"],
        "ESTP": ["세일즈 매니저 📞", "스턴트맨 🎬", "기업가 💼", "스포츠 트레이너 🏋️", "파일럿 ✈️"],
        "ESFP": ["배우 🎭", "패션 디자이너 👗", "MC 🎙️", "뷰티 크리에이터 💄", "무대 감독 🎬"]
    }

    st.markdown(f"### 💼 {result} 유형에게 추천하는 직업들!")
    for job in career_dict.get(result, []):
        st.markdown(f"- {job}")

    with st.expander("다른 MBTI 유형의 추천 직업도 보기 🔍"):
        for mbti_type, jobs in career_dict.items():
            if mbti_type != result:
                st.markdown(f"**{mbti_type}** 👇")
                st.markdown(" / ".join(jobs))
                st.markdown("---")
