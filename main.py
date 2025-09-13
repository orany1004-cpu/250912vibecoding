# app.py
import streamlit as st

st.set_page_config(page_title="MBTI 공부법 추천", page_icon="📚")

st.title("📚 MBTI 기반 공부법 추천 사이트")
st.write("자신의 MBTI 유형을 선택하면, 가장 적합한 공부 방법을 알려드립니다!")

# MBTI 리스트
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# MBTI별 추천 공부법 데이터
study_tips = {
    "ISTJ": "계획적으로 학습 일정을 세우고, 체크리스트를 활용하면 효율이 높습니다.",
    "ISFJ": "조용한 환경에서 반복 학습과 정리 노트를 활용하는 것이 좋습니다.",
    "INFJ": "큰 목표를 설정하고, 의미 있는 맥락 속에서 공부하면 집중이 잘 됩니다.",
    "INTJ": "장기적 계획을 세우고 독학 + 심화 자료 탐구가 효과적입니다.",
    "ISTP": "실습 위주의 학습과 문제 해결 중심 학습이 잘 맞습니다.",
    "ISFP": "자유로운 환경에서 흥미를 느낄 수 있는 과목을 시각적으로 정리하세요.",
    "INFP": "감정과 가치를 연결해 학습하면 몰입이 잘 됩니다. 마인드맵 활용 추천!",
    "INTP": "호기심 기반으로 개념을 탐구하고, 스스로 질문을 던지며 학습하세요.",
    "ESTP": "경험을 통해 배우는 학습법이 효과적입니다. 스터디 그룹 활동 추천!",
    "ESFP": "게임화된 학습, 친구와 함께 하는 학습이 동기부여에 도움이 됩니다.",
    "ENFP": "다양한 주제를 탐색하며 창의적인 방식으로 공부하세요. 브레인스토밍 추천!",
    "ENTP": "토론과 디베이트를 통해 개념을 확장하면 이해도가 높아집니다.",
    "ESTJ": "체계적인 계획과 규칙적인 학습 습관이 가장 큰 무기입니다.",
    "ESFJ": "함께 공부하면서 가르치고 배우는 방식이 잘 맞습니다.",
    "ENFJ": "목표를 명확히 세우고 동기부여 요소를 곁들이면 꾸준히 학습할 수 있습니다.",
    "ENTJ": "전략적인 계획과 성과 측정을 통해 학습 효율을 극대화하세요."
}

# 선택 박스
selected_mbti = st.selectbox("👉 당신의 MBTI 유형을 선택하세요:", mbti_types)

if selected_mbti:
    st.subheader(f"✅ {selected_mbti} 유형에게 추천하는 공부 방법")
    st.write(study_tips[selected_mbti])
