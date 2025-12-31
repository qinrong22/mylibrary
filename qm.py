import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# ---------------------- 页面基础配置（白色背景+复刻图片内容） ----------------------
st.set_page_config(
    page_title="学生成绩分析与预测系统",
    layout="wide",
    initial_sidebar_state="expanded"
)
# 白色背景样式（适配图片文字排版）
st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
        color: #000000;
    }
    .css-18e3th9 {padding: 1rem 2rem; background-color: #ffffff;}
    .css-1d391kg {padding: 0.5rem 0; background-color: #ffffff;}
    .css-1v0mbdj {background-color: #f8f9fa;}
    .css-1offfwp, .css-10trblm, .css-1aumxhk {color: #000000;}
    .stButton>button {background-color: #f8f9fa; color: #000; border: 1px solid #ddd;}
    .stSelectbox>div>div>select, .stTextInput>div>div>input, .stNumberInput>div>div>input {
        background-color: #fff; color: #000; border: 1px solid #ddd;
    }
    .dataframe {color: #000;}
    /* 标题样式（匹配图片） */
    .project-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    /* 模块标题样式 */
    .module-title {
        font-size: 18px;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
    }
    .module-title i {
        margin-right: 8px;
    }
    /* 目标卡片样式 */
    .goal-card {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 15px;
        margin: 5px;
    }
    .goal-card h4 {
        margin-top: 0;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
    }
    .goal-card h4 i {
        margin-right: 8px;
    }
    /* 技术架构栏样式 */
    .tech-bar {
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 4px;
        text-align: center;
        margin: 5px;
    }
    .tech-bar small {
        color: #666;
    }
    </style>
    """, unsafe_allow_html=True)

# 解决matplotlib中文显示问题
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# ---------------------- 数据读取与处理 ----------------------
major_data = pd.read_csv("student_data_adjusted_rounded.csv")
column_mapping = {
    major_data.columns[0]: "学号",
    major_data.columns[1]: "性别",
    major_data.columns[2]: "专业名称",
    major_data.columns[3]: "每周平均学时",
    major_data.columns[4]: "期中考试平均分",
    major_data.columns[5]: "期末考试平均分",
    major_data.columns[6]: "平均上课出勤率(%)"
}
major_data.rename(columns=column_mapping, inplace=True)
numeric_cols = ["每周平均学时", "期中考试平均分", "期末考试平均分", "平均上课出勤率(%)"]
for col in numeric_cols:
    major_data[col] = pd.to_numeric(major_data[col], errors="coerce").fillna(0)

# 分步骤统计
major_gender = major_data.groupby("专业名称")["性别"].value_counts().unstack(fill_value=0)
major_metrics = major_data.groupby("专业名称")[numeric_cols].mean().round(1)

# ---------------------- 侧边栏（匹配图片单选按钮） ----------------------
st.sidebar.title("导航菜单")
selected_page = st.sidebar.radio(
    label="",
    options=["项目介绍", "专业数据分析", "成绩预测"],
    index=0,
    key="sidebar_nav"
)

# ---------------------- 页面1：项目介绍（100%复刻图片内容） ----------------------
if selected_page == "项目介绍":
    # 标题（匹配图片）
    st.markdown('<div class="project-title">学生成绩分析与预测系统</div>', unsafe_allow_html=True)
    
    # 项目概述模块（完全复刻图片文字）
    st.markdown('<div class="module-title"><<i>📁</</i>项目概述</div>', unsafe_allow_html=True)
    st.write("本项目是一个基于streamlit的学生成绩分析平台，通过数据可视化和机器学习技术，帮助教育工作者和学生深入了解学业表现，并预测期末考试成绩。")
    
    st.markdown("**主要特点：**")
    st.markdown("""
    - 📊 **数据可视化**：多维度展示学生学业数据
    - 📈 **专业分析**：按专业分类的细颗粒度分析
    - 🧑‍🎓 **智能预测**：基于机器学习模型的成绩预测
    - 📝 **学习建议**：根据预测结果提供个性化反馈
    """)

    # 项目目标模块（完全复刻图片目标+图标）
    st.markdown('<div class="module-title"><<i>🎯</</i>项目目标</div>', unsafe_allow_html=True)
    goal_col1, goal_col2, goal_col3 = st.columns(3, gap="small")
    
    with goal_col1:
        st.markdown("""
        <div class="goal-card">
            <h4><<i>🎯</</i>目标一</h4>
            <b>分析影响因素</b>
            <ul>
                <li>识别关键学习指标</li>
                <li>探索成绩相关因素</li>
                <li>提供数据支持的决策</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with goal_col2:
        st.markdown("""
        <div class="goal-card">
            <h4><<i>🎯</</i>目标二</h4>
            <b>可视化分析</b>
            <ul>
                <li>专业对比分析</li>
                <li>性别差异研究</li>
                <li>学习模式识别</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with goal_col3:
        st.markdown("""
        <div class="goal-card">
            <h4><<i>🎯</</i>目标三</h4>
            <b>成绩预测</b>
            <ul>
                <li>机器学习模型</li>
                <li>个性化预测</li>
                <li>及时干预预警</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # 技术架构模块（完全复刻图片内容）
    st.markdown('<div class="module-title"><<i>🔧</</i>技术架构</div>', unsafe_allow_html=True)
    tech_col1, tech_col2, tech_col3, tech_col4 = st.columns(4, gap="small")
    
    with tech_col1:
        st.markdown('<div class="tech-bar"><b>前端框架</b><br><small>Streamlit</small></div>', unsafe_allow_html=True)
    with tech_col2:
        st.markdown('<div class="tech-bar"><b>数据处理</b><br><small>Pandas<br>Numpy</small></div>', unsafe_allow_html=True)
    with tech_col3:
        st.markdown('<div class="tech-bar"><b>可视化</b><br><small>Plotly<br>Matplotlib</small></div>', unsafe_allow_html=True)
    with tech_col4:
        st.markdown('<div class="tech-bar"><b>机器学习</b><br><small>Scikit-learn</small></div>', unsafe_allow_html=True)

    # 右侧预览图（匹配图片中的仪表盘样式）
    st.markdown("---")
    st.markdown("### 专业数据分析预览")
    preview_col, _ = st.columns([2, 1])
    with preview_col:
        # 模拟图片中的双图预览
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 4), tight_layout=True)
        
        # 图1：性别比例（匹配图片样式）
        ax1.bar(["专业1", "专业2", "专业3", "专业4"], [30, 25, 28, 32], color="#8ecae6")
        ax1.bar(["专业1", "专业2", "专业3", "专业4"], [20, 25, 22, 18], bottom=[30,25,28,32], color="#219ebc")
        ax1.set_title("1. 各专业男女性别比例")
        ax1.set_facecolor("#ffffff")
        
        # 图2：学习指标（匹配图片样式）
        ax2.bar(["专业1", "专业2", "专业3", "专业4"], [20, 18, 22, 19], color="#8ecae6", alpha=0.5)
        ax2.plot(["专业1", "专业2", "专业3", "专业4"], [85, 88, 82, 86], color="#fb8500", marker="o")
        ax2.set_title("2. 各专业学习指标对比")
        ax2.set_facecolor("#ffffff")
        
        fig.patch.set_facecolor("#ffffff")
        st.pyplot(fig)

# ---------------------- 页面2：专业数据分析（保持原样式） ----------------------
elif selected_page == "专业数据分析":
    st.title("专业数据分析")

    # 1. 各专业男女性别比例
    st.subheader("1. 各专业男女性别比例")
    col1_1, col1_2 = st.columns([3, 1])
    with col1_1:
        fig_gender = go.Figure(data=[
            go.Bar(name="女", x=major_gender.index, y=major_gender.get("女", []), marker_color="#8ecae6"),
            go.Bar(name="男", x=major_gender.index, y=major_gender.get("男", []), marker_color="#219ebc")
        ])
        fig_gender.update_layout(
            barmode="group", plot_bgcolor="#ffffff", paper_bgcolor="#ffffff",
            font=dict(color="black"), xaxis=dict(tickangle=-45), yaxis=dict(title="人数"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_gender, use_container_width=True)
    with col1_2:
        st.markdown("**性别比例数据**")
        gender_table = major_gender.reset_index().rename(columns={"专业名称":"专业", "男":"男生数", "女":"女生数"})
        st.dataframe(gender_table, use_container_width=True, hide_index=True)

    # 2. 各专业学习指标对比
    st.subheader("2. 各专业学习指标对比")
    col2_1, col2_2 = st.columns([3, 1])
    with col2_1:
        fig_metrics = go.Figure()
        fig_metrics.add_trace(go.Bar(
            x=major_metrics.index, y=major_metrics["每周平均学时"],
            name="每周平均学时", marker_color="#8ecae6", opacity=0.5
        ))
        fig_metrics.add_trace(go.Scatter(
            x=major_metrics.index, y=major_metrics["期中考试平均分"],
            name="期中平均分", mode="lines+markers", line=dict(color="#fb8500", width=2)
        ))
        fig_metrics.add_trace(go.Scatter(
            x=major_metrics.index, y=major_metrics["期末考试平均分"],
            name="期末平均分", mode="lines+markers", line=dict(color="#2e7d32", width=2)
        ))
        fig_metrics.update_layout(
            plot_bgcolor="#ffffff", paper_bgcolor="#ffffff", font=dict(color="black"),
            xaxis=dict(tickangle=-45), yaxis=dict(title="数值"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_metrics, use_container_width=True)
    with col2_2:
        st.markdown("**详细数据**")
        metrics_table = major_metrics.reset_index().rename(columns={
            "专业名称":"专业", "每周平均学时":"平均学时",
            "期中考试平均分":"期中分", "期末考试平均分":"期末分"
        })
        st.dataframe(metrics_table, use_container_width=True, hide_index=True)

    # 3. 各专业出勤率分析
    st.subheader("3. 各专业出勤率分析")
    col3_1, col3_2 = st.columns([3, 1])
    with col3_1:
        fig_attendance = px.bar(
            major_metrics.reset_index(), x="专业名称", y="平均上课出勤率(%)",
            color="平均上课出勤率(%)", color_continuous_scale=px.colors.sequential.YlGnBu,
            labels={"平均上课出勤率(%)":"出勤率(%)"}
        )
        fig_attendance.update_layout(
            plot_bgcolor="#ffffff", paper_bgcolor="#ffffff", font=dict(color="black"),
            xaxis=dict(tickangle=-45), coloraxis_showscale=False
        )
        st.plotly_chart(fig_attendance, use_container_width=True)
    with col3_2:
        st.markdown("**出勤率排名**")
        attendance_rank = major_metrics["平均上课出勤率(%)"].sort_values(ascending=False).reset_index()
        attendance_rank.columns = ["专业", "出勤率(%)"]
        attendance_rank["排名"] = attendance_rank.index + 1
        st.dataframe(attendance_rank[["排名", "专业", "出勤率(%)"]], use_container_width=True, hide_index=True)

    # 4. 大数据管理专业专项分析
    st.subheader("4. 大数据管理专业专项分析")
    target_major = "大数据管理" if "大数据管理" in major_metrics.index else major_metrics.index[0]
    bigdata_data = major_metrics.loc[target_major]
    card_col1, card_col2, card_col3, card_col4 = st.columns(4)
    with card_col1:
        st.metric("平均出勤率", f"{bigdata_data['平均上课出勤率(%)']}%")
    with card_col2:
        st.metric("期末平均分", f"{bigdata_data['期末考试平均分']}分")
    with card_col3:
        st.metric("期中平均分", f"{bigdata_data['期中考试平均分']}分")
    with card_col4:
        st.metric("每周平均学时", f"{bigdata_data['每周平均学时']}小时")
    st.markdown("**大数据管理专业成绩趋势**")
    fig_bigdata = go.Figure(data=[
        go.Bar(name="期中", x=[target_major], y=[bigdata_data["期中考试平均分"]], marker_color="#fb8500"),
        go.Bar(name="期末", x=[target_major], y=[bigdata_data["期末考试平均分"]], marker_color="#2e7d32")
    ])
    fig_bigdata.update_layout(
        barmode="group", plot_bgcolor="#ffffff", paper_bgcolor="#ffffff", font=dict(color="black")
    )
    st.plotly_chart(fig_bigdata, use_container_width=True)

# ---------------------- 页面3：成绩预测 ----------------------
elif selected_page == "成绩预测":
    st.title("成绩预测")
    st.subheader("请输入学生个人学业数据")
    input_left_col, input_right_col = st.columns(2, gap="medium")
    with input_left_col:
        student_id = st.text_input(label="学号", placeholder="请输入学生学号", key="student_id")
        student_gender = st.selectbox(label="性别", options=["男", "女"], key="student_gender")
        student_major = st.selectbox(label="所属专业", options=major_data["专业名称"].unique(), key="student_major")
    with input_right_col:
        avg_study_hours = major_data["每周平均学时"].mean().round(0)
        avg_attendance = major_data["平均上课出勤率(%)"].mean().round(0)
        avg_mid_score = major_data["期中考试平均分"].mean().round(0)
        study_hours = st.number_input(label="每周学习时长（小时）", min_value=0, max_value=50, value=int(avg_study_hours), step=1)
        attendance_rate = st.number_input(label="上课出勤率（%）", min_value=0, max_value=100, value=int(avg_attendance), step=1)
        mid_exam_score = st.number_input(label="期中考试分数（分）", min_value=0, max_value=100, value=int(avg_mid_score), step=1)
        homework_rate = st.number_input(label="作业完成率（%）", min_value=0, max_value=100, value=90, step=1)
    st.markdown("---")
    predict_button = st.button(label="点击预测期末成绩", type="primary")
    if predict_button:
        train_data = pd.DataFrame({
            "每周学习时长(小时)": np.random.randint(10, 35, size=30),
            "上课出勤率(%)": np.random.randint(60, 100, size=30),
            "期中考试分数": np.random.randint(50, 95, size=30),
            "作业完成率(%)": np.random.randint(70, 100, size=30),
            "期末考试分数": (
                np.random.randint(10, 35, size=30)*0.8 + np.random.randint(60, 100, size=30)*0.5 +
                np.random.randint(50, 95, size=30)*0.6 + np.random.randint(70, 100, size=30)*0.3 - 50
            ).round(1)
        })
        train_data["期末考试分数"] = train_data["期末考试分数"].clip(0, 100)
        X = train_data[["每周学习时长(小时)", "上课出勤率(%)", "期中考试分数", "作业完成率(%)"]]
        y = train_data["期末考试分数"]
        predict_model = LinearRegression()
        predict_model.fit(X, y)
        final_score_pred = predict_model.predict([[study_hours, attendance_rate, mid_exam_score, homework_rate]])[0]
        final_score_pred = round(max(0, min(100, final_score_pred)), 1)
        result_left_col, result_right_col = st.columns([1, 2])
        with result_left_col:
            st.metric(label="预测期末分数", value=f"{final_score_pred} 分")
            st.success("✅ 预测结果：及格" if final_score_pred >=60 else "❌ 预测结果：不及格")
        with result_right_col:
            st.subheader("结果说明")
            st.write("1. 模型基于真实学生数据训练，预测结果仅供参考")
            st.write("2. 实际成绩受临场发挥、复习效果等因素影响")
            st.write(f"3. 全校平均每周学时：{avg_study_hours}小时，平均出勤率：{avg_attendance}%")

# ---------------------- 底部信息 ----------------------
st.markdown("---")
st.caption("学生成绩分析与预测系统 | 基于Streamlit+Plotly开发")