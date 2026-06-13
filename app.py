import streamlit as st

st.set_page_config(
    page_title="CEO Talk Plus",
    page_icon="🌿",
    layout="centered"
)

st.markdown("""
<style>
    .main {
        background-color: #FAFAFA;
    }
    .hero {
        padding: 32px 24px;
        border-radius: 20px;
        background: linear-gradient(135deg, #7A0019, #B00020);
        color: white;
        margin-bottom: 24px;
    }
    .hero h1 {
        font-size: 34px;
        margin-bottom: 8px;
    }
    .hero p {
        font-size: 16px;
        opacity: 0.95;
    }
    .section-card {
        padding: 22px 20px;
        border-radius: 16px;
        background-color: white;
        border: 1px solid #E6E6E6;
        margin-bottom: 18px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.04);
    }
    .small-text {
        color: #666666;
        font-size: 14px;
    }
    .tag {
        display: inline-block;
        padding: 5px 10px;
        border-radius: 999px;
        background-color: #F3F3F3;
        color: #333333;
        font-size: 13px;
        margin-right: 6px;
        margin-bottom: 6px;
    }
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <h1>CEO Talk Plus</h1>
    <p>모빌리티솔루션 리더 대상 소통 프로그램</p>
    <p class="small-text">산책 · Talking Point · 포토미션 · 석식 소통</p>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="section-card">
    <h3>프로그램 소개</h3>
    <p>
    CEO Talk Plus는 모빌리티솔루션 리더들이 CEO와 함께 산책과 석식을 통해
    사업 방향, 리더십 역할, 실행 과제를 자연스럽게 논의하는 소통 프로그램입니다.
    </p>
    <span class="tag">Mobility Solution</span>
    <span class="tag">Leader Communication</span>
    <span class="tag">One Team</span>
</div>
""", unsafe_allow_html=True)


st.markdown("### 일정표")

schedule = [
    ["15:30 ~ 16:00", "집결 및 이동", "참석자 확인, 이동 준비"],
    ["16:00 ~ 17:30", "죽녹원 산책", "조별 산책 및 CEO Talking Point 진행"],
    ["17:30 ~ 18:00", "포토미션", "조별 미션 사진 촬영"],
    ["18:00 ~ 20:00", "석식", "리더 간 교류 및 CEO 소통"],
]

for time, title, desc in schedule:
    st.markdown(f"""
    <div class="section-card">
        <b>{time}</b><br>
        <h4>{title}</h4>
        <p class="small-text">{desc}</p>
    </div>
    """, unsafe_allow_html=True)


st.markdown("### 산책 Talking Point")

st.markdown("""
<div class="section-card">
    <h4>사후 대응이 아닌 선제적 대비를 통한 목표 달성</h4>
    <p>
    변화하는 시장과 고객 요구에 대응하기 위해, 리더로서 무엇을 먼저 준비하고
    어떤 실행 속도를 만들어야 할지 논의합니다.
    </p>
</div>
""", unsafe_allow_html=True)


st.markdown("### 조 편성")

with st.expander("조 편성 보기"):
    st.write("※ 세부 조 편성은 확정 후 업데이트 예정입니다.")
    st.table({
        "조": ["1조", "2조", "3조", "4조"],
        "참석자": ["업데이트 예정", "업데이트 예정", "업데이트 예정", "업데이트 예정"]
    })


st.markdown("### 포토미션")

st.markdown("""
<div class="section-card">
    <h4>오늘의 한 장면을 남겨주세요</h4>
    <p>
    조별로 산책 중 가장 인상적인 순간을 사진으로 남겨주세요.
    이후 석식 장소에서 함께 공유할 예정입니다.
    </p>
</div>
""", unsafe_allow_html=True)

st.button("포토미션 참여하기")


st.markdown("### 석식 장소 안내")

st.markdown("""
<div class="section-card">
    <h4>석식 장소</h4>
    <p>장소명: 업데이트 예정</p>
    <p>메뉴: 백숙 / 오리 / 지역 특화 메뉴 검토</p>
    <p class="small-text">※ 세부 장소 및 이동 동선은 확정 후 업데이트 예정입니다.</p>
</div>
""", unsafe_allow_html=True)


st.markdown("---")
st.caption("CEO Talk Plus | Mobility Solution")
