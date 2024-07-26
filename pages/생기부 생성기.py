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
                '특징': '외향적인 사람들은 사교적이고 활발하며, 다양한 사람들과의 상호작용을 즐김. 새로운 경험과 활동에 열려 있으며, 주로 그룹 활동을 선호함. 타인과의 소통을 통해 에너지를 얻고, 종종 리더십을 발휘함.',
                '기록부': f'{name} 학생은 매우 사교적이고 활동적인 성격을 가짐. 새로운 사람들과 쉽게 친해지며 다양한 활동에 적극적으로 참여하는 모습이 돋보임. 학교 행사나 프로젝트에서도 리더십을 발휘하여 팀을 이끌어가는 경우가 많음.'
            },
            '내향적': {
                '특징': '내향적인 사람들은 조용하고 신중하며, 혼자만의 시간을 즐김. 깊이 있는 사고를 중시하며, 종종 독립적인 활동을 선호함. 타인과의 상호작용보다는 자신의 내면 세계에서 에너지를 얻음.',
                '기록부': f'{name} 학생은 매우 조용하고 신중한 성격을 가짐. 혼자만의 시간을 소중히 여기며, 깊이 있는 사고를 통해 문제를 분석하고 해결하는 능력이 뛰어남. 새로운 지식을 탐구하는 열정을 가지고 있음.'
            },
            '분석적': {
                '특징': '분석적인 사람들은 논리적이고 객관적인 사고를 중시하며, 문제를 체계적으로 해결하는 데 뛰어난 능력을 가짐. 종종 데이터를 분석하고, 패턴을 발견하며, 사실에 근거한 결정을 내림.',
                '기록부': f'{name} 학생은 매우 논리적이고 분석적인 성격을 가짐. 문제를 체계적으로 분석하고 해결하는 능력이 뛰어나며, 데이터를 기반으로 한 합리적인 결정을 내리는 것이 특징임.'
            },
            '감정적': {
                '특징': '감정적인 사람들은 타인의 감정을 잘 이해하고, 공감하는 능력이 뛰어남. 종종 강한 감정을 경험하며, 자신의 감정을 솔직하게 표현함. 인간관계를 중시하며, 타인과의 정서적인 유대를 중요하게 생각함.',
                '기록부': f'{name} 학생은 타인의 감정을 잘 이해하고 공감하는 능력이 뛰어난 학생임. 강한 감정을 경험하며, 자신의 감정을 솔직하게 표현하는 모습을 보임.'
            },
            '창의적': {
                '특징': '창의적인 사람들은 새로운 아이디어를 생각해내고, 독창적으로 문제를 해결하는 능력이 뛰어남. 예술과 과학 등 다양한 분야에서 창의성을 발휘함.',
                '기록부': f'{name} 학생은 매우 창의적이고 독창적인 성격을 가짐. 새로운 아이디어를 생각해내는 능력이 뛰어나며, 문제를 해결하는 데 있어 창의적인 접근을 시도함.'
            },
            '리더십': {
                '특징': '리더십 있는 사람들은 주도적으로 팀을 이끌며, 타인을 동기부여하는 능력이 뛰어남. 책임감이 강하며, 결정을 내리는 데 자신감이 있음.',
                '기록부': f'{name} 학생은 매우 주도적이고 리더십이 강한 성격을 가짐. 팀을 이끌고 타인을 동기부여하는 능력이 뛰어나며, 책임감이 강함.'
            },
            '완벽주의': {
                '특징': '완벽주의적인 사람들은 높은 기준을 가지고 있으며, 모든 일을 완벽하게 수행하려는 성향이 있음. 세부 사항에 주의를 기울이며, 꼼꼼하게 일을 처리함.',
                '기록부': f'{name} 학생은 매우 꼼꼼하고 완벽주의적인 성격을 가짐. 모든 일을 높은 기준으로 수행하려는 성향이 있으며, 세부 사항에 주의를 기울임.'
            },
            '모험적': {
                '특징': '모험적인 사람들은 새로운 경험과 도전을 즐기며, 위험을 감수하는 성향이 있음. 다양한 활동에 열정적으로 참여하며, 새로운 것을 배우는 것을 좋아함.',
                '기록부': f'{name} 학생은 매우 모험적이고 도전적인 성격을 가짐. 새로운 경험과 도전을 즐기며, 다양한 활동에 열정적으로 참여함.'
            },
            '사교성': {
                '특징': '사교적인 사람들은 사람들과의 상호작용을 즐기며, 다양한 사람들과 쉽게 친해지는 성향이 있음. 다양한 사회적 활동에 적극적으로 참여함.',
                '기록부': f'{name} 학생은 매우 사교적이고 사람들과의 상호작용을 즐기는 성격을 가짐. 다양한 사람들과 쉽게 친해지며, 사회적 활동에 적극적으로 참여함.'
            },
            '책임감': {
                '특징': '책임감 있는 사람들은 주어진 일을 성실하게 수행하며, 약속을 지키는 성향이 있음. 신뢰할 수 있는 사람으로 인정받음.',
                '기록부': f'{name} 학생은 매우 책임감 있고 성실한 성격을 가짐. 주어진 일을 성실하게 수행하며, 약속을 지키는 모습을 보임.'
            },
            '낙천적': {
                '특징': '낙천적인 사람들은 긍정적이고 밝은 성격을 가지고 있으며, 어려움에도 불구하고 희망을 잃지 않음. 주변 사람들에게 긍정적인 에너지를 전달함.',
                '기록부': f'{name} 학생은 매우 긍정적이고 밝은 성격을 가짐. 어려움에도 불구하고 희망을 잃지 않으며, 주변 사람들에게 긍정적인 에너지를 전달함.'
            },
            '조직적': {
                '특징': '조직적인 사람들은 체계적이고 계획적으로 일을 처리하는 성향이 있음. 효율적으로 시간을 관리하며, 일을 체계적으로 수행함.',
                '기록부': f'{name} 학생은 매우 조직적이고 체계적인 성격을 가짐. 계획적으로 일을 처리하며, 효율적으로 시간을 관리함.'
            },
            '혁신적': {
                '특징': '혁신적인 사람들은 새로운 아이디어와 접근 방식을 통해 변화를 이끌어내는 능력이 있음. 기존의 틀을 깨고 새로운 길을 개척함.',
                '기록부': f'{name} 학생은 매우 혁신적이고 창의적인 성격을 가짐. 새로운 아이디어와 접근 방식을 통해 변화를 이끌어내는 능력이 뛰어남.'
            },
            '열정적': {
                '특징': '열정적인 사람들은 자신이 하는 일에 대한 열정과 에너지가 넘침. 목표를 달성하기 위해 최선을 다하며, 주위 사람들에게도 열정을 전달함.',
                '기록부': f'{name} 학생은 매우 열정적이고 에너지가 넘치는 성격을 가짐. 자신이 하는 일에 대한 열정이 강하며, 목표를 달성하기 위해 최선을 다함.'
            },
            '직관적': {
                '특징': '직관적인 사람들은 감각보다 직관에 의존하여 결정을 내리는 경향이 있음. 종종 창의적이고 혁신적인 사고를 함.',
                '기록부': f'{name} 학생은 매우 직관적이고 창의적인 성격을 가짐. 직관에 의존하여 결정을 내리며, 종종 혁신적인 아이디어를 제시함.'
            },
            '현실적': {
                '특징': '현실적인 사람들은 현실적이고 실용적인 사고를 중시하며, 실제 경험과 사실에 기반하여 결정을 내림.',
                '기록부': f'{name} 학생은 매우 현실적이고 실용적인 성격을 가짐. 실제 경험과 사실에 기반하여 결정을 내리며, 실용적인
