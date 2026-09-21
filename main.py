# ----------------------------------
# 그래프 영역 2
# ----------------------------------
st.divider()
st.header("📊 그래프 2. 일관객 합계 TOP5 영화의 날짜별 일관객 변화")

# 기간 동안 일관객 합계가 가장 큰 영화 5편 선택
top5_movies = (
    df.groupby("영화명", as_index=False)["일관객"]
    .sum()
    .sort_values("일관객", ascending=False)
    .head(5)
)

top5_names = top5_movies["영화명"].tolist()

# TOP5 영화 데이터만 추출
top5_df = (
    df[df["영화명"].isin(top5_names)]
    .sort_values("날짜")
)

# 선 그래프
fig2 = px.line(
    top5_df,
    x="날짜",
    y="일관객",
    color="영화명",
    markers=True,
    title="기간 내 일관객 합계 TOP5 영화의 날짜별 일관객 변화",
    labels={
        "날짜": "날짜",
        "일관객": "일관객 수",
        "영화명": "영화"
    },
    hover_data={
        "날짜": "|%Y-%m-%d",
        "일관객": ":,"
    }
)

# 호버 정보
fig2.update_traces(
    hovertemplate="<b>%{x|%Y-%m-%d}</b><br>%{fullData.name}<br>일관객: %{y:,}명<extra></extra>"
)

# 범례 클릭으로 켜기/끄기 가능 (Plotly 기본 기능)
fig2.update_layout(
    hovermode="x unified",
    xaxis_title="날짜",
    yaxis_title="일관객 수",
    height=550,
    legend_title_text="영화"
)

st.plotly_chart(fig2, use_container_width=True)

st.info("📝 **이 그래프로 알 수 있는 것:** (여기에 설명 문장을 작성)")
