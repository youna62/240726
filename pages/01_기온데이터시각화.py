import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 데이터 불러오기
data = pd.read_csv('daily_temp.csv')

# 날짜를 datetime 형식으로 변환
data['날짜'] = pd.to_datetime(data['날짜'].str.strip(), format='%Y-%m-%d')

# 연도 추출
data['연도'] = data['날짜'].dt.year

# 연도별 평균, 최저, 최고 기온 계산
yearly_data = data.groupby('연도').agg({
    '평균기온(℃)': 'mean',
    '최저기온(℃)': 'mean',
    '최고기온(℃)': 'mean'
}).reset_index()

# 그래프 선택
st.title('연도별 기온 변화 추이')
graph_type = st.selectbox('그래프 타입을 선택하세요', ['꺾은선 그래프', '막대 그래프'])

# 그래프 그리기
fig, ax = plt.subplots()
if graph_type == '꺾은선 그래프':
    ax.plot(yearly_data['연도'], yearly_data['평균기온(℃)'], label='평균기온(℃)', marker='o')
    ax.plot(yearly_data['연도'], yearly_data['최저기온(℃)'], label='최저기온(℃)', marker='o')
    ax.plot(yearly_data['연도'], yearly_data['최고기온(℃)'], label='최고기온(℃)', marker='o')
elif graph_type == '막대 그래프':
    width = 0.25
    ax.bar(yearly_data['연도'] - width, yearly_data['평균기온(℃)'], width=width, label='평균기온(℃)')
    ax.bar(yearly_data['연도'], yearly_data['최저기온(℃)'], width=width, label='최저기온(℃)')
    ax.bar(yearly_data['연도'] + width, yearly_data['최고기온(℃)'], width=width, label='최고기온(℃)')

ax.set_xlabel('연도')
ax.set_ylabel('기온(℃)')
ax.set_title('연도별 기온 변화 추이')
ax.legend()
st.pyplot(fig)
