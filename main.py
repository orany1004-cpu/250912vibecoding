import streamlit as st
import pandas as pd
import altair as alt
import os

# 제목
st.title("국가별 MBTI 유형 분포 Top 10 시각화")

# 기본 데이터 파일명
file_name = "countriesMBTI_16types.csv"

# 데이터 로드: 로컬 파일 우선, 없으면 업로드 파일 사용
df = None
if os.path.exists(file_name):
    df = pd.read_csv(file_name)
else:
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

if df is not None:
    # MBTI 유형 리스트 (Country 제외)
    mbti_types = df.columns.tolist()[1:]

    # 드롭다운으로 MBTI 유형 선택
    selected_mbti = st.selectbox("MBTI 유형을 선택하세요", mbti_types)

    # Top 10 국가 추출
    top10 = df.sort_values(by=selected_mbti, ascending=False).head(10)

    # Altair 차트 생성
    chart = (
        alt.Chart(top10)
        .mark_bar()
        .encode(
            x=alt.X(selected_mbti, title=f"{selected_mbti} 비율"),
            y=alt.Y("Country", sort='-x', title="국가"),
            tooltip=["Country", selected_mbti]
        )
        .properties(width=600, height=400, title=f"{selected_mbti} 비율 Top 10 국가")
        .interactive()
    )

    st.altair_chart(chart, use_container_width=True)
else:
    st.info("기본 CSV 파일이 없으면 업로드해 주세요.")
