import streamlit as st

# 웹 서비스 제목 설정
st.title('나의 첫 웹 서비스 만들기!!')

# 사용자 입력 받기
name = st.text_input('이름을 입력해주세요 : ')
personality = st.text_input('성격을 한 단어로 입력해주세요 : ')

# 인사말 생성 버튼 클릭 시 실행되는 코드
if st.button('특성 분석 결과 보기'):
    if name and personality:
        # 성격별 특징 설명
        personality_details = {
            '외향적': {
                '특징': '외향적인 사람들은 사교적이고 활발하며, 다양한 사람들과의 상호작용을 즐김...',
                '기록부': f'{name} 학생은 매우 사교적이고 활동적인 성격을 가짐...'
            },
            # 다른 성격 유형도 여기에 추가
        }

        # 성격 유형에 따른 결과 출력
        if personality in personality_details:
            st.write(f"**특징:** {personality_details[personality]['특징']}")
            st.write(f"**기록부:** {personality_details[personality]['기록부']}")
        else:
            st.write("알려지지 않은 성격 유형입니다. 다시 입력해주세요.")
    else:
        st.write("이름과 성격을 입력해주세요!")
