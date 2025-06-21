import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

# 📌 글로벌 시가총액 TOP10 (2025년 기준 예시)
top10_stocks = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'NVIDIA': 'NVDA',
    'Amazon': 'AMZN',
    'Alphabet (Google)': 'GOOGL',
    'Meta (Facebook)': 'META',
    'Berkshire Hathaway': 'BRK-B',  # 주의: yfinance에서는 BRK-B → BRK.B로 처리
    'Tesla': 'TSLA',
    'TSMC': 'TSM',
    'Eli Lilly': 'LLY'
}

# 🗓️ 1년간 데이터
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 🧠 페이지 설정
st.set_page_config(page_title="글로벌 주가 추이 비교", layout="wide")
st.title("📈 글로벌 시가총액 TOP10 기업 주가 변화")
st.markdown("최근 1년간의 주가 흐름을 비교해보세요. (Plotly 기반 시각화)")
st.markdown("---")

# ✅ 기업 선택
selected_companies = st.multiselect(
    "🔎 비교할 기업을 선택하세요:",
    list(top10_stocks.keys()),
    default=['Apple', 'Microsoft', 'NVIDIA', 'Amazon', 'Alphabet (Google)']
)

# 📊 그래프 초기화
fig = go.Figure()

if selected_companies:
    for name in selected_companies:
        ticker = top10_stocks[name].replace("-", ".")  # ⚠️ BRK-B → BRK.B 형태 처리
        data = yf.download(ticker, start=start_date, end=end_date, progress=False)

        # ✅ 유효성 검사
        if not data.empty and "Close" in data.columns:
            data = data.dropna(subset=["Close"])
            if not data["Close"].isnull().all():
                fig.add_trace(go.Scatter(
                    x=data.index,
                    y=data["Close"],
                    mode='lines',
                    name=name
                ))
            else:
                st.warning(f"⚠️ {name}의 종가 데이터가 없습니다.")
        else:
            st.warning(f"⚠️ {name}의 주가 데이터를 불러올 수 없거나 유효하지 않습니다.")

    # 📈 그래프 설정
    fig.update_layout(
        title="📊 최근 1년간 주가 비교",
        xaxis_title="날짜",
        yaxis_title="종가 (USD)",
        hovermode="x",  # unified 대신 일반 hover
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("👆 위에서 기업을 선택해 주세요.")
