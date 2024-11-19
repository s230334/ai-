# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('linear_regression_model__1_.pkl')



# 2. 모델 설명
st.title('신용 등급 분류 에이전트')
col1, col2, col3=st.column(3)
with col1:
 st.subheader('모델 설명')
 st.write('-')
 st.write('-')
 st.write('-')
 st.write('-')
 st.write('-')
 

# 3. 데이터시각화
with col2:
 st.subheader('')


# 4. 모델 활용
