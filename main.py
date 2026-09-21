# ----------------------------------
# 그래프 영역 5
# ----------------------------------
st.divider()
st.header("🔥 그래프 5. 월 × 요일별 일관객 합계 히트맵")

# 월과 요일 추출
heatmap_df = df.copy()
heatmap_df["월"] = heatmap_df["날짜"].dt.month

weekday_order = ["월", "화", "수", "목", "금", "토", "일"]
weekday_map = {
    0: "월",
    1: "화",
    2: "수",
    3: "목",
    4: "금",
    5: "토",
    6: "일"
}

heatmap_df["요일"] = heatmap_df["날짜"].dt.dayofweek.map(weekday_map)

# 월 × 요일별 일관객 합계
pivot = (
    heatmap_df.groupby(["요일", "월"])["일관객"]
    .sum()
    .reset_index()
    .pivot(index="요일", columns="월", values="일관객")
    .reindex(weekday_order)   # 월요일 → 일요일 순서
    .fillna(0)
)

# 히트맵
fig5 = px.imshow(
    pivot,
    text_auto=True,
    aspect="auto",
    color_continuous_scale="YlOrRd",
    labels={
        "x": "월",
        "y": "요일",
        "color": "일관객 합계"
    },
    title="월 × 요일별 일관객 합계"
)

fig5.update_traces(
    hovertemplate="월: %{x}월<br>요일: %{y}<br>일관객 합계: %{z:,}명<extra></extra>"
)

fig5.update_layout(
    xaxis_title="월",
    yaxis_title="요일",
    height=500
)

st.plotly_chart(fig5, use_container_width=True)

st.info("📝 **이 그래프로 알 수 있는 것:** (여기에 설명 문장을 작성)")
