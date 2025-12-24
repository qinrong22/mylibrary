import streamlit as st   # 导入streamlit库，用于构建交互式Web应用

# 设置页面标题为"音乐播放"，页面图标为🎵
st.set_page_config(page_title='音乐播放', page_icon='🎵')

# 定义图片数组，存储网易云音乐的专辑封面链接
images = [
    # 第一张图片链接
    'https://p1.music.126.net/mW53BkMgGy37I7yVrUg-aQ==/109951163117902077.jpg',
    # 第二张图片链接
    'https://p2.music.126.net/ixIs5kkukgNYMmeDsc35_g==/29686813955450.jpg'
]

# 定义音频数组，存储对应的音乐文件链接
audio_files = [
    # 第一首歌曲链接
    'https://music.163.com/song/media/outer/url?id=28059417.mp3',
    # 第二首歌曲链接
    'https://music.163.com/song/media/outer/url?id=191254.mp3'
]

# 检查session_state中是否存在current_index变量，用于记录当前播放的索引位置
if 'current_index' not in st.session_state:
    # 如果不存在，则初始化为0，即从第一首开始
    st.session_state.current_index = 0

# 从session_state中获取当前播放的索引值
current_index = st.session_state.current_index

# 显示当前索引对应的图片，并在标题中显示当前进度
st.image(images[current_index], caption=f'图片 {current_index + 1} / {len(images)}')

# 创建两列布局，用于放置上一首和下一首按钮
col1, col2 = st.columns([1, 1])

# 在第一列中放置上一首按钮
with col1:
    # 当current_index为0时禁用上一首按钮（已在第一首）
    if st.button('上一首', disabled=current_index == 0):
        # 点击上一首按钮，索引减1
        st.session_state.current_index -= 1
        # 重新运行脚本，更新界面显示
        st.rerun()

# 在第二列中放置下一首按钮
with col2:
    # 当current_index为最后一个索引时禁用下一首按钮（已在最后一首）
    if st.button('下一首', disabled=current_index == len(images) - 1):
        # 点击下一首按钮，索引加1
        st.session_state.current_index += 1
        # 重新运行脚本，更新界面显示
        st.rerun()

# 添加水平分隔线，用于分隔图片区域和音乐播放区域
st.markdown("---")

# 显示当前播放的歌曲信息
st.info(f"🎵 当前播放: 第 {current_index + 1} 首歌曲")

# 根据当前索引播放对应的音频文件
st.audio(audio_files[current_index])

# 显示播放列表标题
st.markdown("### 📋 播放列表")

# 遍历所有音频文件，生成播放列表
for i, audio_url in enumerate(audio_files):
    # 判断是否为当前正在播放的歌曲
    if i == current_index:
        # 是当前播放歌曲，用加粗格式显示并标注正在播放
        st.markdown(f"🎵 **歌曲 {i+1}** (正在播放)")
    else:
        # 不是当前播放歌曲，普通格式显示
        st.markdown(f"🎵 歌曲 {i+1}")
