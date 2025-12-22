import streamlit as st
st.set_page_config(
    page_title="学生小陆的数字档案",
    page_icon="📚",
    layout="wide"
)

# 标题居中
col_title = st.columns([1, 2, 1])
with col_title[1]:
    st.title("学生小陆的数字档案")

st.divider()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.subheader("基础信息")
    st.write(f"📇 学号：NSD-2023-001")
    st.write(f"📅 注册时间：2023-09-01 11:31:11")
with col2:
    st.subheader("状态信息")
    st.write(f"🧠 精神状态：正常")
    st.write(f"❤️ 健康度：良好（安全值：高）")
with col3:
    st.subheader("系统状态")
    st.write(f"🟢 在线状态：在线")
    st.write(f"⚡ 连接状态：已加速")
with col4:
    st.subheader("日志时间")
    st.write(f"📝 最后更新：2025-06-01 12:42:58")

st.divider()

# 技能矩阵居中
col_skill = st.columns([1, 2, 1])
with col_skill[1]:
    st.subheader("📊 技能矩阵")
    skill_data = {
        "C++": 95,
        "Python": 87,
        "Java": 68
    }

    for skill, score in skill_data.items():
        status = "（技能水平上升）" if score >= 85 else "（技能水平下降）" if score < 70 else ""
        st.write(f"**{skill}：** {score}% {status}")
        st.progress(score / 100)

    st.write(f"**Streamlit课程进度：** 75%")
    st.progress(0.75)

st.divider()

# 任务日志居中
col_task = st.columns([1, 2, 1])
with col_task[1]:
    st.subheader("📋 任务日志")
    task_data = [
        ["日期", "任务", "状态", "难度"],
        ["2023-10-01", "学生数字档案", "已完成", "★★☆☆☆"],
        ["2023-10-12", "成绩管理系统", "进行中", "★★★☆☆"],
        ["2023-12-12", "数据周期展示", "未完成", "★★★★☆"]
    ]
    st.table(task_data)

st.divider()

# 代码成果居中
col_code = st.columns([1, 2, 1])
with col_code[1]:
    st.subheader("💻 最新代码成果")
    code_content = '''import matplotlib.pyplot as plt

def detect_vulnerability(input_data):
    if input_data == "admin":
        return "ACCESS_GRANTED"
    else:
        return "SHOULD_BE_BLOCKED"

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
plt.plot(x, y)
plt.title("数据趋势图")
plt.show()
'''
    st.code(code_content, language="python")

st.divider()

# 底部提示居中
col_tip = st.columns([1, 2, 1])
with col_tip[1]:
    st.success("📌 系统提示：下一个任务目标已解锁")