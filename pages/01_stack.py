import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

# 📌 시가총액 기준 TOP10 (2025년 기준 예시)
top10_stocks = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'NVIDIA': 'NVDA',
    'Amazon': 'AMZN',
    'Alphabet (Google)': 'GOOGL',
    'Meta (Facebook)': 'META',
    'Berkshire Hathaway': 'BRK-B',
    'Tesla': 'TSLA',
    'TSMC': 'TSM',
    'Eli Lilly': 'LLY'
}

# 🗓️ 기간 설정: 최근 1년
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 🧠 Streamlit 설정
st.set_page_config(page_title="Global TOP10 시가총액 주가 추이", layout="wide")
st.title("📈 글로벌 시가총액 TOP10 기업 주가 변화 (최근 1년)")
st.markdown("Plotly 그래프를 통해 최근 1년간 주가 흐름을 비교해보세요.")

# ✅ 사용자 선택: 기업 선택 (기본값은 5개)
selected_companies = st.multiselect(
    "🔎 비교할 기업을 선택하세요:",
    list(top10_stocks.keys()),
    default=['Apple', 'Microsoft', 'NVIDIA', 'Amazon', 'Alphabet (Google)']
)

if selected_companies:
    fig = go.Figure()

    for name in selected_companies:
        ticker = top10_stocks[name]
        data = yf.download(ticker, start=start_date, end=end_date)
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data['Close'],
            mode='lines',
            name=name
        ))

    fig.update_layout(
        title="📊 최근 1년간 주가 비교",
        xaxis_title="날짜",
        yaxis_title="종가 (USD)",
        hovermode="x unified",
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("왼쪽에서 비교할 회사를 선택해주세요.")
