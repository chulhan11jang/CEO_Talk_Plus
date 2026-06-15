import streamlit as st

st.set_page_config(
    page_title="CEO Talk Plus",
    page_icon="🌿",
    layout="centered"
)

# =========================
# CSS
# =========================
st.markdown("""
<style>
.block-container {
    padding-top: 1.2rem;
    padding-bottom: 2rem;
    max-width: 760px;
}

.hero {
    color: white;
    padding: 82px 24px 34px 24px;
    border-radius: 24px;
    margin-bottom: 22px;
    ...
}
background-image:
    linear-gradient(rgba(0,0,0,0.20), rgba(0,0,0,0.58)),
    url("https://raw.githubusercontent.com/chulhan11jang/CEO_Talk_Plus/main/bamboo.jpeg");
    background-size: cover;
    background-position: center;
    overflow: hidden;
}

.hero h1 {
    font-size: 38px;
    margin-bottom: 10px;
    font-weight: 800;
    letter-spacing: -0.5px;
}

.hero p {
    margin: 6px 0;
    font-size: 15px;
    font-weight: 600;
}

.card {
    background: white;
    border: 1px solid #E7E7E7;
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

.info-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 0;
    border-bottom: 1px solid #EEEEEE;
}

.info-row-last {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 0;
}

.info-label {
    font-weight: 700;
    font-size: 16px;
}

.info-value {
    font-weight: 800;
    font-size: 18px;
    color: #1F2937;
    text-align: right;
}

.info-value-normal {
    font-weight: 700;
    font-size: 18px;
    text-align: right;
}

.small {
    color: #666;
    font-size: 14px;
    line-height: 1.6;
}

.tag {
    display: inline-block;
    background: #F3F3F3;
    padding: 6px 10px;
    border-radius: 999px;
    font-size: 13px;
    margin: 3px;
}

.timeline {
    border-left: 3px solid #A50020;
    padding-left: 16px;
    margin-left: 6px;
}

.timeline-item {
    margin-bottom: 18px;
}

.timeline-time {
    font-weight: 800;
    color: #A50020;
    font-size: 15px;
}

.timeline-title {
    font-weight: 800;
    font-size: 18px;
    margin-top: 3px;
}

.timeline-desc {
    color: #666;
    font-size: 14px;
    margin-top: 3px;
}

.group-title {
    font-weight: 800;
    font-size: 18px;
    color: #A50020;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)


# =========================
# Hero
# =========================
st.markdown("""
<div class="hero">
    <h1>CEO Talk Plus</h1>
    <p>with 모빌리티솔루션</p>
    <p>2026.06.18 · 담양 죽녹원</p>
</div>
""", unsafe_allow_html=True)


# =========================
# Program Intro
# =========================
st.markdown("""
<div class="card">
    <h2>프로그램 소개</h2>
    <p><b>CEO와 함께하는 Talk Plus, 소통에 의미를 더하다</b></p>
    <p>
    CEO와 리더 간 직접적인 소통을 통해<br>
    조직의 방향성과 생각을 공유하는 자리
    </p>
</div>
""", unsafe_allow_html=True)


# =========================
# Main Tabs
# =========================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "집결 정보", "일정", "조 편성", "죽녹원", "석식"
])


# =========================
# Tab 1: 집결 정보
# =========================
with tab1:

    st.markdown("""
<div class="card">
<div class="info-row">
<div class="info-label">🚍 배차 정보</div>
<div class="info-value">광주77사 1911</div>
</div>
<div class="info-row">
<div class="info-label">📍 탑승 위치</div>
<div class="info-value-normal">A동 정문 앞</div>
</div>
<div class="info-row-last">
<div class="info-label">⏰ 집결 시간</div>
<div class="info-value">15:25까지 탑승 완료</div>
</div>
</div>
""", unsafe_allow_html=True)

# =========================
# Tab 2: 일정
# =========================
with tab2:
    st.markdown("""
    <div class="card">
        <h3>전체 일정</h3>
        <div class="timeline">

            <div class="timeline-item">
                <div class="timeline-time">15:30</div>
                <div class="timeline-title">광주 사업장 출발</div>
                <div class="timeline-desc">차량 탑승 및 인원 확인</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-time">16:00</div>
                <div class="timeline-title">담양 종합체육관 주차장 도착</div>
                <div class="timeline-desc">집결지 이동 및 조별 정렬</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-time">16:05</div>
                <div class="timeline-title">프로그램 안내</div>
                <div class="timeline-desc">산책코스, 포토미션, Activity 안내</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-time">16:12</div>
                <div class="timeline-title">단체사진 촬영</div>
                <div class="timeline-desc">현수막 활용 전체 기념촬영</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-time">16:20</div>
                <div class="timeline-title">물품 수령</div>
                <div class="timeline-desc">넥쿨러, 생수, 벌레퇴치제 등 수령</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-time">16:30</div>
                <div class="timeline-title">조별 산책 출발</div>
                <div class="timeline-desc">1조 출발 후 3~5분 간격으로 2·3조 출발</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-time">17:00</div>
                <div class="timeline-title">Goal-In 미니축구</div>
                <div class="timeline-desc">조별 Activity 진행</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-time">18:00 ~ 20:00</div>
                <div class="timeline-title">석식 및 소통</div>
                <div class="timeline-desc">사진 공유, CEO 인사말씀, 식사, Lucky Draw, 시상</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# Tab 3: 조 편성
# =========================
with tab3:
    st.markdown("""
    <div class="card">
        <h3>조 편성</h3>
        <p class="small">※ 세부 조 편성은 최종 확정 후 업데이트 예정입니다.</p>
    </div>
    """, unsafe_allow_html=True)

    groups = {
        "1조": ["유병국", "유인수", "장용재", "김민규", "박무룡", "최영민", "신기수", "박갑동", "김성수", "장성덕"],
        "2조": ["강용호", "백남산", "김진호", "유기주", "문종인", "김웅", "김성훈", "유선수", "오영춘", "최낙주"],
        "3조": ["남형기", "김형근", "장승우", "이동훈", "전희진", "조정민", "정재희", "이재광", "박창혁", "이영화", "조성재"],
    }

    for group, members in groups.items():
        with st.expander(group):
            st.write(" · ".join(members))


# =========================
# Tab 4: 죽녹원
# =========================
with tab4:
    sub1, sub2, sub3, sub4 = st.tabs([
        "루트", "Talking Point", "포토미션", "Activity"
    ])

    with sub1:
        st.markdown("""
        <div class="card">
            <h3>죽녹원 산책 루트</h3>
            <p>
            조별로 죽녹원 산책로를 이동하며 CEO와 자유롭게 소통합니다.
            </p>
            <p class="small">
            세부 동선 및 출발 순서는 현장 안내에 따라 진행됩니다.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with sub2:
        st.markdown("""
        <div class="card">
            <h3>Talking Point</h3>
            <p><b>‘사후 대응’이 아닌 ‘선제적 대비’를 통한 목표 달성을 위해<br>
            리더로서 해야 할 것은 무엇인가?</b></p>
            <ul>
                <li>모빌리티솔루션이 더 높이 도약하기 위해 먼저 준비해야 할 것은 무엇인가?</li>
                <li>빠른 실행을 위해 리더가 바꿔야 할 일하는 방식은 무엇인가?</li>
                <li>Enable the Next를 실제 업무에서 구현하기 위해 필요한 리더십은 무엇인가?</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with sub3:
        st.markdown("""
        <div class="card">
            <h3>포토미션</h3>
            <p><b>주제: Enable the Next를 표현하는 사진</b></p>
            <p>
            조별로 산책 중 모빌리티솔루션의 미래, 도전, One Team의 의미가 드러나는 장면을 사진으로 남겨주세요.
            </p>
            <ul>
                <li>조장이 대표 사진을 업로드합니다.</li>
                <li>석식 중 일부 사진을 함께 공유합니다.</li>
                <li>자연스러운 분위기와 메시지가 잘 드러나는 사진을 권장합니다.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.link_button("포토미션 업로드 바로가기", "https://padlet.com/")

    with sub4:
        st.markdown("""
        <div class="card">
            <h3>Activity</h3>
            <p><b>Goal-In 미니축구</b></p>
            <p>
            조별로 진행되는 가벼운 Activity입니다.
            </p>
            <ul>
                <li>조별 대표 또는 전원이 참여합니다.</li>
                <li>정해진 방식에 따라 점수를 획득합니다.</li>
                <li>우수 조는 석식 중 시상 예정입니다.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)


# =========================
# Tab 5: 석식
# =========================
with tab5:
    st.markdown("""
    <div class="card">
        <h3>석식 장소 안내</h3>
        <p><b>장소:</b> 한상근대통밥집</p>
        <p><b>진행:</b><br>
        오프닝 · 포토미션 사진 공유 · CEO 인사말씀 및 건배사 · 식사 · Lucky Draw · Activity 우수 조 시상
        </p>
        <p><b>현수막 문구:</b><br>
        세상을 움직이는 모빌리티 혁신의 중심<br>
        Solution & Value Creator for future Mobility
        </p>
    </div>

    <div class="card">
        <h3>운영 문의</h3>
        <p>인재육성팀 장철한</p>
        <p class="small">비상 연락처는 필요 시 업데이트 예정</p>
    </div>
    """, unsafe_allow_html=True)


st.markdown("---")
st.caption("CEO Talk Plus · Mobility Solution")
