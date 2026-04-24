import streamlit as st
import json
import time

st.set_page_config(page_title="2026 득근 가이드", page_icon="⚡", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #050a10; color: #e0e0e0; }
    .stButton>button { background-color: #00ff41; color: black; font-weight: bold; border-radius: 8px; border: none; width: 100%; height: 3em; }
    .stTextInput>div>div>input { background-color: #101820; color: #00ff41; border: 1px solid #00ff41; }
    .result-box { background-color: #101820; padding: 25px; border-radius: 12px; border: 2px solid #00ff41; margin-top: 20px; line-height: 1.8; }
    .tip-section { background-color: #1e262e; padding: 15px; border-radius: 8px; border-left: 4px solid #00ff41; margin-top: 15px; font-size: 0.95em; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ 2026 AI 신체 최적화 분석기")
st.markdown(f"""
    <div style="background-color: #101820; padding: 18px; border-radius: 10px; border-left: 5px solid #00ff41; margin-bottom: 25px;">
        <p style="margin: 0; color: #00ff41; font-weight: bold; font-size: 0.9em;">[ 시스템 설계자 ]</p>
        <h2 style="margin: 5px 0; color: #ffffff;">정보융합학부 박성준</h2>
        <p style="margin: 0; color: #888; font-size: 0.9em;">학번: 2023204076 | 성향: ESTP-A (활동가형)</p>
    </div>
    """, unsafe_allow_html=True)

@st.cache_data
def load_workout_content():
    with open('quiz_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    time.sleep(1.5)
    return data

if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.subheader("🔑 시스템 접속 인증")
    
    id_input = st.text_input("학번 입력", placeholder="학번 10자리를 입력하세요")
    pw_input = st.text_input("비밀번호 입력", type="password", placeholder="기본 비밀번호: 1234")
    login_btn = st.button("인증 시작")
    
    if login_btn:
        if id_input == "2023204076" and pw_input == "1234":
            st.session_state.auth = True
            st.success("인증에 성공했습니다. 분석 세션을 시작합니다.")
            time.sleep(0.5)
            st.rerun()
        else:
            st.error("입력하신 정보가 틀렸습니다. 다시 확인해 주세요.")

else:
    st.sidebar.markdown(f"""
        ### 👤 사용자 프로필
        - **이름:** 박성준
        - **전공:** 정보융합학부
        - **성향:** ESTP-A
        - **기록:** 벤치프레스 110kg, 데드리프트 160kg
    """)
    if st.sidebar.button("로그아웃"):
        st.session_state.auth = False
        st.rerun()

    st.header("🔍 신체 데이터 정밀 스캔")
    st.write("아래 문항에 답변하면 당신의 성향을 분석하여 최적의 루틴과 실전 팁을 제안합니다.")
    
    quiz_data = load_workout_content()
    
    if quiz_data:
        with st.form("optimizer_form"):
            total_points = 0
            for i, q in enumerate(quiz_data):
                st.write(f"**질문 {i+1}. {q['question']}**")
                ans = st.selectbox(f"선택_{i}", q['options'], key=f"q_{i}", label_visibility="collapsed")
                idx = q['options'].index(ans)
                total_points += q['points'][idx]
            
            submit = st.form_submit_button("분석 결과 및 운동 팁 확인")
            
            if submit:
                st.divider()
                with st.spinner('데이터를 기반으로 최적의 경로를 계산 중입니다...'):
                    time.sleep(2)
                
                st.markdown("<div class='result-box'>", unsafe_allow_html=True)
                
                if total_points >= 70:
                    st.subheader("🚀 분석 결과: [압도적인 파워 리프터]")
                    st.write("당신의 신체 데이터는 폭발적인 힘을 내는 데 최적화되어 있습니다. 고중량 저반복 위주의 스트렝스 훈련을 추천합니다.")
                    st.markdown("""
                    <div class='tip-section'>
                        <strong>🏋️‍♂️ 박성준의 실전 루틴 팁:</strong><br>
                        "무게에 압도당하지 않는 게 중요합니다. 주 종목은 5회 5세트(5x5) 루틴으로 가져가세요. 
                        벤치프레스 110kg를 넘기려면 가슴만 쓰는 게 아니라 <strong>견갑을 벤치에 단단히 고정</strong>하고 다리 힘(레그 드라이브)까지 써야 합니다. 
                        데드도 160kg 이상 치려면 복압 유지가 핵심이니 리프팅 벨트를 아끼지 마세요!"
                    </div>
                    """, unsafe_allow_html=True)
                    
                elif total_points >= 50:
                    st.subheader("💪 분석 결과: [밸런스 보디빌더]")
                    st.write("근육의 모양과 성장에 집중하는 보디빌딩 방식이 적합합니다. 부위별 타겟팅과 적절한 식단 관리를 병행해 보세요.")
                    st.markdown("""
                    <div class='tip-section'>
                        <strong>🏋️‍♂️ 박성준의 실전 루틴 팁:</strong><br>
                        "조각 같은 몸을 만들려면 중량보다는 <strong>근육의 이완과 수축</strong>에 집중하세요. 
                        세트 사이 휴식 시간을 1분 내외로 짧게 가져가서 펌핑감을 극대화하는 게 팁입니다. 
                        단백질은 본인 체중 1.5배 이상 무조건 챙겨 드세요. 조각 같은 몸 기대할게요!!"
                    </div>
                    """, unsafe_allow_html=True)
                    
                elif total_points >= 30:
                    st.subheader("⚡ 분석 결과: [기능성 애슬릿]")
                    st.write("유연성과 회복 능력이 뛰어난 타입입니다. 크로스핏이나 서킷 트레이닝처럼 전신을 사용하는 고강도 운동을 추천합니다.")
                    st.markdown("""
                    <div class='tip-section'>
                        <strong>🏋️‍♂️ 박성준의 실전 루틴 팁:</strong><br>
                        "수행 능력을 올리려면 전신 협응력이 필수입니다. 루틴에 턱걸이(풀업)와 맨몸 스쿼트를 섞어서 체력을 키워보세요. 
                        고강도 훈련 후에는 무조건 폼롤러로 근막 이완을 해줘야 부상을 방지할 수 있습니다. 부상 조심하세요!"
                    </div>
                    """, unsafe_allow_html=True)
                    
                else:
                    st.subheader("🌱 분석 결과: [건강한 웰니스 입문자]")
                    st.write("기초 체력을 다지는 단계입니다. 부상 방지를 위해 기본기에 충실한 전신 운동부터 차근차근 시작해 보세요.")
                    st.markdown("""
                    <div class='tip-section'>
                        <strong>🏋️‍♂️ 박성준의 실전 루틴 팁:</strong><br>
                        "처음부터 무리하게 무게를 올릴 필요 없습니다. 빈 봉으로 정확한 자세를 만드는 것부터 시작하세요. 
                        주 3회 헬스장에 출석하는 습관만 들여도 성공입니다. 
                        멋있습니다!! 꾸준함이 답입니다. 득근하세요!"
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("</div>", unsafe_allow_html=True)
                st.balloons()