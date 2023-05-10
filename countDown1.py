import streamlit as st
import datetime
from streamlit import session_state as SessionState

# 定义一个计算倒计时的函数
def calculate_countdown(event_datetime):
    now = datetime.datetime.now()
    time_remaining = event_datetime - now
    days_remaining = time_remaining.days
    hours_remaining = time_remaining.seconds // 3600
    minutes_remaining = (time_remaining.seconds // 60) % 60
    seconds_remaining = time_remaining.seconds % 60
    return days_remaining, hours_remaining, minutes_remaining, seconds_remaining

# 初始化SessionState
if not SessionState.__contains__('events'):
    SessionState.events = {}

# 界面布局
st.title("倒计时小程序")

# 侧边栏
st.sidebar.title("添加新倒计时")
event_name = st.sidebar.text_input("事件名称")
min_date = datetime.date.today()
event_date = st.sidebar.date_input("事件日期", min_date, min_value=min_date)
min_time = datetime.datetime.now().time()
event_time = st.sidebar.time_input("事件时间", min_time, key="event_time", min_value=min_time)

if st.sidebar.button("添加倒计时"):
    if event_name and event_date and event_time:
        event_datetime = datetime.datetime.combine(event_date, event_time)
        SessionState.events[event_name] = event_datetime

# 删除事件部分
with st.sidebar:
    st.header("删除倒计时")
    event_to_remove = st.selectbox("选择要删除的事件", list(SessionState.events.keys()), key="event_to_remove")
    if st.button("删除倒计时"):
        if event_to_remove:
            del SessionState.events[event_to_remove]
            st.experimental_rerun()

# 显示所有倒计时事件
st.header("所有倒计时")

for event_name, event_datetime in SessionState.events.items():
    days_remaining, hours_remaining, minutes_remaining, seconds_remaining = calculate_countdown(event_datetime)
    st.write(f"距离 **{event_name}** 还有 {days_remaining} 天 {hours_remaining} 小时 {minutes_remaining} 分钟 {seconds_remaining} 秒")
