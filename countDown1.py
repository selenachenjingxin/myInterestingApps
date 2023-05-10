import streamlit as st
import datetime
from streamlit import session_state as SessionState

# 定义一个计算倒计时的函数
def calculate_countdown(event_date):
    today = datetime.datetime.now()
    time_remaining = event_date - today
    seconds_remaining = time_remaining.total_seconds()
    return int(seconds_remaining)

# 初始化SessionState
if not SessionState.__contains__('events'):
    SessionState.events = {}

# 界面布局
st.title("倒计时小程序")

# 侧边栏
st.sidebar.header("添加新倒计时")
event_name = st.sidebar.text_input("事件名称")
min_date = datetime.date.today()
event_date = st.sidebar.date_input("事件日期", min_date)

if st.sidebar.button("添加倒计时"):
    if event_name and event_date:
        SessionState.events[event_name] = event_date

# 删除事件部分
st.sidebar.header("删除倒计时")
event_to_remove = st.sidebar.selectbox("选择要删除的事件", list(SessionState.events.keys()), key="event_to_remove")

if st.sidebar.button("删除倒计时"):
    if event_to_remove:
        del SessionState.events[event_to_remove]
        st.experimental_rerun()

# 显示所有倒计时事件

for event_name, event_date in SessionState.events.items():
    countdown = calculate_countdown(event_date)
    st.write(f"距离 **{event_name}** 还有 {countdown} 天")
