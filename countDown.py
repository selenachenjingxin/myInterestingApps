import streamlit as st
from datetime import datetime, date

def days_until(date):
    """计算距离给定日期的天数"""
    today = date.today()
    delta = date - today
    return delta.days

# Streamlit应用程序开始
st.title("倒计时小程序")

# 用户输入日期
date = st.date_input("请选择日期")

# 计算距离该日期的天数
if date is not None:
    days = days_until(date)
    st.write(f"距离{date}还有{days}天")
