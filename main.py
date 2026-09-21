import pandas as pd
import plotly.express as px
import streamlit as st

# ----------------------------------
# 페이지 설정
# ----------------------------------
st.set_page_config(
    page_title="영화 데이터 그래프 도감 1 - 시간",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 영화 데이터 그래프 도감 1 - 시간")
st.markdown("KOBIS 일별 박스오피스(1년, TOP10) 데이터를 이용한 시간 그래프 모음")

# ----------------------------------
# 데이터 불러오기
# ----------------------------------
DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_daily.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)

    # 날짜를 datetime 형식으로 변환
    df["날짜"] = pd.to_datetime(df["날짜"].astype(str), format="%Y%m%d")

    return df

df = load_data()

st.success(f"데이터 불러오기 완료! ({len(df):,}개 행)")

# ----------------------------------
# 그래프 영역 1
# ----------------------------------
st.divider()
st.header("📈 그래프 1. 영화별 날짜에 따른 일관객 변화")

movie_list = sorted(df["영화명"].unique())

selected_movie = st.selectbox(
    "영화를 선택하세요.",
    movie_list
)

movie_df = (
    df[df["영화명"] == selected_movie]
    .sort_values("날짜")
)

fig1 = px.line(
    movie_df,
    x="날짜",
    y="일관객",
    markers=True,
    title=f"{selected_movie} 날짜별 일관객 변화",
    labels={
        "날짜": "날짜",
        "일관객": "일관객 수"
    },
    hover_data={
        "날짜": "|%Y-%m-%d",
        "일관객": ":,"
    }
)

fig1.update_traces(
    hovertemplate="<b>%{x|%Y-%m-%d}</b><br>일관객: %{y:,}명<extra></extra>"
)

fig1.update_layout(
    hovermode="x unified",
    xaxis_title="날짜",
    yaxis_title="일관객 수",
    height=500
)

st.plotly_chart(fig1, use_container_width=True)

st.info("📝 **이 그래프로 알 수 있는 것:** (여기에 설명 문장을 작성)")

# ----------------------------------
# 그래프 영역 2 (예정)
# ----------------------------------
st.divider()
st.header("📊 그래프 2. (추가 예정)")

st.info("📝 **이 그래프로 알 수 있는 것:** (여기에 설명 문장을 작성)")

# ----------------------------------
# 그래프 영역 3 (예정)
# ----------------------------------
st.divider()
st.header("📉 그래프 3. (추가 예정)")

st.info("📝 **이 그래프로 알 수 있는 것:** (여기에 설명 문장을 작성)")
