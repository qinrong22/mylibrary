import streamlit as st

st.set_page_config(page_title="视频中心")

# 替换为Streamlit官方测试视频链接（直接的mp4文件，保证能播放）
video_arr = [
    {
        'url': 'https://static.streamlit.io/examples/star.mp4',
        'title': '喜羊羊与灰太狼-第一部-第1集'
    },
    {
        'url': 'https://static.streamlit.io/examples/sea.mp4',
        'title': '喜羊羊与灰太狼-第一部-第2集'
    },
    {
        'url': 'https://static.streamlit.io/examples/rain.mp4',
        'title': '喜羊羊与灰太狼-第一部-第3集'
    },
    {
        'url': 'https://static.streamlit.io/examples/waves.mp4',
        'title': '喜羊羊与灰太狼-第一部-第4集'
    },
    {
        'url': 'https://static.streamlit.io/examples/butterfly.mp4',
        'title': '喜羊羊与灰太狼-第一部-第5集'
    },
]

# 初始化索引
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 显示当前视频标题
st.title(video_arr[st.session_state['ind']]['title'])

# 显示当前视频（添加格式指定，增强兼容性）
st.video(
    video_arr[st.session_state['ind']]['url'],
    format="video/mp4",  # 指定视频格式
    start_time=0  # 从开头播放
)

def playVideo(i):
    """播放指定索引的视频"""
    st.session_state['ind'] = int(i)

# 在视频下方创建三列布局的按钮
st.subheader("选择集数")

# 创建三列
num_cols = 3
cols = st.columns(num_cols)

# 创建按钮并分配到三列中
for i in range(len(video_arr)):
    col_index = i % num_cols
    with cols[col_index]:
        st.button(
            f'第{i+1}集',
            on_click=playVideo,
            args=(i,),  # 元组传参
            key=f'btn_{i}',  # 唯一key
            use_container_width=True
        )
