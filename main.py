import sys
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
import streamlit as st

# 환경 변수를 불러오는 경우
# load_dotenv()

# OpenAI API 키를 직접 전달
openai_api_key = "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"  # 여러분의 실제 OpenAI API 키로 교체하세요
chat_model = ChatOpenAI(openai_api_key=openai_api_key)

st.title('AI Poet made by SEO')

content = st.text_input('시의 주제를 적어보세요')

if st.button('시 작성하기'):
    with st.spinner('시 생성 중...'):
        result = chat_model.predict(content + "에 대한 시를 써줘")
    st.write('시의 주제는', content)
    st.write(result)