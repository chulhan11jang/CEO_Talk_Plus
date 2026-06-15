import streamlit as st

st.set_page_config(
    page_title="CEO Talk Plus",
    page_icon="🌿",
    layout="centered"
)

st.markdown("""
<style>
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 760px;
}
.hero {
    position: relative;
    color: white;
    padding: 80px 24px 32px 24px;
    border-radius: 24px;
    margin-bottom: 22px;
    background-image:
        linear-gradient(rgba(0,0,0,0.25), rgba(0,0,0,0.55)),
        url("https://source.unsplash.com/1200x700/?bamboo,forest");
    background-size: cover;
    background-position: center;
    overflow: hidden;
}
.hero h1 {
    font-size: 36px;
    margin-bottom: 8px;
    font-weight: 800;
    letter-spacing: -0.5px;
}
.hero p {
    margin: 4px 0;
    font-size: 15px;
}
.card {
    background: white;
    border: 1px solid #E7E7E7;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 14px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
.time {
    font-weight: 700;
    color: #A50020;
}
.small {
    color: #666;
    font-size: 14px;
}
.tag {
    display: inline-block;
    background: #F3F3F3;
    padding: 6px 10px;
    border-radius: 999px;
    font-size: 13px;
    margin: 3px;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <h1>CEO Talk Plus</h1>
    <p>with 모빌리티솔루션</p>
    <p>2026.06.18 · 담양 죽녹원</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h3>Today's Message</h3>
    <p><b>사후 대응이 아닌, 선제적 대비를 통한 목표 달성</b></p>
    <p class="small">
    변화에 먼저 준비하고 빠르게 실행하는 리더십을 생각하는 시간입니다.
    </p>
    <span class="tag">One Team</span>
    <span class="tag">선제적 대비</span>
    <span class="tag">빠른 실행</span>
</div>
""", unsafe_allow_html=True)


tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "소개", "일정", "Talking Point", "조 편성", "포토미션", "석식"
])


with tab1:
    st.markdown("""
    <div class="card">
        <h3>프로그램 소개</h3>
        <p>
        CEO Talk Plus는 모빌리티솔루션 리더들이 CEO와 함께 산책, Activity, 석식을 통해
        사업 방향과 리더의 역할을 자연스럽게 논의하는 소통 프로그램입니다.
        </p>
        <p class="small">
        본 페이지는 행사 당일 참가자가 일정, 조 편성, 미션, 장소 안내를 빠르게 확인하기 위한 모바일 가이드입니다.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.info("세부 내용은 행사 운영안 확정에 따라 계속 업데이트됩니다.")


with tab2:
    st.subheader("전체 일정")

    schedule = [
        ("15:30 ~ 16:00", "집결 및 이동", "참석자 확인, 이동 준비"),
        ("16:00 ~ 16:10", "오프닝 및 단체사진", "행사 안내 및 전체 기념촬영"),
        ("16:10 ~ 17:30", "죽녹원 산책", "조별 산책 및 CEO Talking 진행"),
        ("17:30 ~ 18:00", "Activity / 포토미션", "조별 미션 수행 및 사진 촬영"),
        ("18:00 ~ 20:00", "석식", "리더 간 교류 및 CEO 소통"),
    ]

    for time, title, desc in schedule:
        st.markdown(f"""
        <div class="card">
            <div class="time">{time}</div>
            <h4>{title}</h4>
            <p class="small">{desc}</p>
        </div>
        """, unsafe_allow_html=True)


with tab3:
    st.subheader("산책 Talking Point")

    st.markdown("""
    <div class="card">
        <h4>핵심 주제</h4>
        <p><b>‘사후 대응’이 아닌 ‘선제적 대비’를 통한 목표 달성을 위해 리더로서 해야 할 것은 무엇인가?</b></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h4>생각해볼 질문</h4>
        <ul>
            <li>우리 조직이 미리 준비해야 할 변화는 무엇인가?</li>
            <li>목표 달성을 위해 리더가 먼저 제거해야 할 장애요인은 무엇인가?</li>
            <li>빠른 실행을 위해 조직 간 협업 방식은 어떻게 달라져야 하는가?</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


with tab4:
    st.subheader("조 편성")

    st.caption("※ 실제 명단 확정 후 업데이트 예정")

    groups = {
        "1조": ["업데이트 예정", "업데이트 예정", "업데이트 예정"],
        "2조": ["업데이트 예정", "업데이트 예정", "업데이트 예정"],
        "3조": ["업데이트 예정", "업데이트 예정", "업데이트 예정"],
        "4조": ["업데이트 예정", "업데이트 예정", "업데이트 예정"],
    }

    for group, members in groups.items():
        with st.expander(group):
            for member in members:
                st.write(f"- {member}")


with tab5:
    st.subheader("포토미션")

    st.markdown("""
    <div class="card">
        <h4>미션 안내</h4>
        <p>조별로 산책 중 가장 인상적인 순간을 사진으로 남겨주세요.</p>
        <ul>
            <li>우리 조의 One Team 사진</li>
            <li>오늘 가장 인상 깊은 장면</li>
            <li>모빌리티솔루션의 힘찬 도약을 표현하는 사진</li>
        </ul>
        <p class="small">※ 우수 사진은 석식 중 공유 또는 별도 선정 예정입니다.</p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button("포토미션 업로드 바로가기", "https://padlet.com/")


with tab6:
    st.subheader("석식 장소 안내")

    st.markdown("""
    <div class="card">
        <h4>석식 장소</h4>
        <p><b>장소명:</b> 업데이트 예정</p>
        <p><b>메뉴:</b> 백숙 / 오리 / 지역 특화 메뉴 검토</p>
        <p><b>이동:</b> 죽녹원 산책 종료 후 이동</p>
        <p class="small">※ 세부 장소 및 지도 링크는 확정 후 업데이트 예정입니다.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h4>운영 문의</h4>
        <p>인재육성팀 장철한</p>
        <p class="small">비상 연락처는 필요 시 업데이트</p>
    </div>
    """, unsafe_allow_html=True)


st.markdown("---")
st.caption("CEO Talk Plus · Mobility Solution")
