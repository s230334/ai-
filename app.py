# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('linear_regression_model__1_.pkl')



# 2. 모델 설명
st.title('신용 등급 분류 에이전트')
st.subheader('모델 설명')
st.write('- 기계학습 알고리즘: 선형회귀')
st.write('- 학습 데이터 출처: ')
st.write('- 훈련 데이터: ')
st.write('- 테스트 데이터: ')
st.write('- 인공지능 모델 정확도: ')
 

# 3. 데이터시각화
col1, col2 = st.columns(2)
with col1:
 st.subheader('')


# 4. 모델 활용
