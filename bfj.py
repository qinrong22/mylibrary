# 导入streamlit库，用于创建Web应用
import streamlit as st

# 设置页面配置：标题为"音乐播放"，图标为🎵
st.set_page_config(page_title='音乐播放', page_icon='🎵')

# 定义专辑封面图片URL列表
images = [
    # Queen乐队的波西米亚狂想曲专辑封面
    'https://p1.music.126.net/mW53BkMgGy37I7yVrUg-aQ==/109951163117902077.jpg',
    # 第二首歌曲的专辑封面
    'https://p2.music.126.net/ixIs5kkukgNYMmeDsc35_g==/29686813955450.jpg',
    # 第三首歌曲的专辑封面
    'https://p2.music.126.net/sZ-rACbFrybF0x_lI6XNMw==/109951169297766755.jpg'
]

# 定义音频文件URL列表
audio_files = [
    # 第一首歌曲的音频文件URL
    'https://music.163.com/song/media/outer/url?id=28059417.mp3',
    # 第二首歌曲的音频文件URL
    'https://music.163.com/song/media/outer/url?id=191254.mp3',
    # 第三首歌曲的音频文件URL
    'https://music.163.com/song/media/outer/url?id=2122308127.mp3'
]

# 定义歌曲名称列表
song_names = [
    # 第一首歌曲名称
    "Bohemian Rhapsody",
    # 第二首歌曲名称
    "Another Song",
    # 第三首歌曲名称
    "Third Song"
]

# 定义歌手列表
artists = [
    # 第一首歌曲歌手
    "Queen",
    # 第二首歌曲歌手
    "Artist 2",
    # 第三首歌曲歌手
    "Artist 3"
]

# 检查session_state中是否存在current_index变量（用于记录当前播放索引）
if 'current_index' not in st.session_state:
    # 如果不存在，初始化为0（从第一首开始）
    st.session_state.current_index = 0

# 从session_state获取当前播放索引
current_index = st.session_state.current_index

# 显示页面主标题
st.title("音乐播放器")

# 创建两列布局：第一列显示专辑封面，第二列显示歌曲信息
col1, col2 = st.columns([1, 1.5])

# 在第一列中显示专辑封面
with col1:
    # 显示当前歌曲对应的专辑封面图片，宽度为250像素
    st.image(images[current_index], width=250)

# 在第二列中显示歌曲信息
with col2:
    # 显示歌曲名称（使用header级别）
    st.header(song_names[current_index])
    # 显示歌手信息（使用subheader级别）
    st.subheader(f"歌手: {artists[current_index]}")

# 添加水平分隔线
st.divider()

# 创建两列布局：用于放置控制按钮
col3, col4 = st.columns(2)

# 在第一列中放置"上一首"按钮
with col3:
    # 当当前索引为0时禁用按钮（已是第一首）
    # 点击按钮时，当前索引减1，然后重新运行应用
    if st.button('上一首', disabled=current_index == 0):
        # 更新session_state中的索引值
        st.session_state.current_index -= 1
        # 重新运行应用以更新界面
        st.rerun()

# 在第二列中放置"下一首"按钮
with col4:
    # 当当前索引为最后一项时禁用按钮（已是最后一首）
    # 点击按钮时，当前索引加1，然后重新运行应用
    if st.button('下一首', disabled=current_index == len(images) - 1):
        # 更新session_state中的索引值
        st.session_state.current_index += 1
        # 重新运行应用以更新界面
        st.rerun()

# 显示音频播放器组件，播放当前索引对应的音频
st.audio(audio_files[current_index])

# 显示播放列表标题
st.subheader("播放列表")

# 遍历所有音频文件，生成播放列表
for i, audio_url in enumerate(audio_files):
    # 判断是否为当前正在播放的歌曲
    if i == current_index:
        # 如果是当前播放歌曲，显示为粗体并标记"正在播放"
        st.markdown(f"**{i+1}. {song_names[i]}** (正在播放)")
    else:
        # 如果不是当前播放歌曲，显示普通文本
        st.markdown(f"{i+1}. {song_names[i]}")
