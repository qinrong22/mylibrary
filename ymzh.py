import streamlit as st

# 页面基础配置（你的代码，完全保留）
st.set_page_config(
    page_title="花花小世界",
    layout="wide",
    page_icon="🏫"
)

# ========== 仅新增：顶部导航栏（不改动你的任何核心代码） ==========
# 顶部导航栏样式美化
st.markdown("""
    <style>
        /* 顶部导航栏容器 */
        .top-nav {
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: #2c3e50;
            padding: 10px 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }
        /* 顶部导航按钮 */
        .top-nav a {
            color: white;
            text-decoration: none;
            padding: 8px 16px;
            margin: 0 8px;
            border-radius: 4px;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        /* 导航按钮hover效果 */
        .top-nav a:hover {
            background-color: #34495e;
        }
        /* 当前页按钮样式 */
        .top-nav .current {
            background-color: #3498db;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# 渲染顶部导航栏（链接和侧边栏保持一致）
st.markdown("""
    <div class="top-nav">
        <a href="#" class="current">首页</a>
        <a href="https://qinrong1.streamlit.app/">数字档案</a>
        <a href="https://qinrong3.streamlit.app/">南宁服装数据仪表</a>
        <a href="https://qinrong4.streamlit.app/">相册</a>
        <a href="https://qinrong5.streamlit.app/">音乐播放器</a>
        <a href="https://qinrong6.streamlit.app/">视频播放</a>
        <a href="https://qinrong7.streamlit.app/">档案生成器</a>

    </div>
""", unsafe_allow_html=True)

# ========== 你的原始代码（一字未改） ==========
# 侧边栏导航
with st.sidebar:
    st.markdown("### 🧭 导航栏")
    st.markdown("#### 当前页：首页")
    st.link_button("数字档案", "https://qinrong1.streamlit.app/")
    st.link_button("南宁美服装数据表", "https://qinrong3.streamlit.app/")
    st.link_button("相册", "https://qinrong4.streamlit.app/")
    st.link_button("音乐播放器", "https://qinrong5.streamlit.app/")
    st.link_button("视频播放", "https://qinrong6.streamlit.app/")
    st.link_button("档案生成器", "https://qinrong7.streamlit.app/")

# 首页内容
st.title("广西职业师范学院")

# 校园图片
st.image(
    "https://www.gxvnu.edu.cn/lib/images/n_ba.png",
    caption="广西职业师范学院校园风貌",
    use_container_width=True
)

# 学校简介
st.header("学校简介")
st.markdown("""
广西职业师范学院（原广西经济管理干部学院）坐落于广西首府南宁市风景秀丽的邕江之滨、相思湖畔，是自治区人民政府直属、自治区教育厅主管的公办全日制普通本科学校，致力于培养区域经济社会发展所需要的高素质应用型、技术技能型人才和职业教育师资。
""")

# 历史沿革
with st.expander("📜 查看历史沿革"):
    st.markdown("""
    学校随着广西的解放而诞生，其前身为创建于1951年5月的广西省行政干部训练班。其后，为适应不同历史时期广西经济建设需要，学校历经了广西人民革命大学、广西行政干部学校、广西经济干部学校、广西经济管理干部学院等历史沿革，并于2019年5月经教育部批准设置为广西职业师范学院。

    在不同历史时期，学校聚焦"服务广西经济建设"发展主线，不忘初心、勇担办学使命，为广西经济建设和社会发展作出了不可磨灭的突出贡献，享有良好的办学声誉和广泛的社会影响。

    """)
