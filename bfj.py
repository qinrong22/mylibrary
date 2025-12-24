import streamlit as st

# 设置页面标题和图标
st.set_page_config(page_title='音乐播放', page_icon='🎵')

# 专辑封面图片数组 - 存储不同歌曲的封面图片URL
images = [
    'https://p1.music.126.net/mW53BkMgGy37I7yVrUg-aQ==/109951163117902077.jpg',
    'https://p2.music.126.net/ixIs5kkukgNYMmeDsc35_g==/29686813955450.jpg'
]

# 歌曲信息数组 - 包含每首歌曲的详细信息
songs = [
    {
        'title': '他不懂',  # 歌曲名称
        'artist': '张杰',   # 歌手
        'duration': '5:55', # 歌曲时长
        'audio': 'https://music.126.com/song/media/outer/url?id=28059417.mp3'  # 音频文件URL
    },
    {
        'title': '天下',
        'artist': '张杰',
        'duration': '3:45',
        'audio': 'https://music.126.com/song/media/outer/url?id=191254.mp3'
    },
    {
        'title': '不眠之夜',
        'artist': '张杰',
        'duration': '2:18',
        'audio': 'https://music.126.com/song/media/outer/url?id=2122308127.mp3'
    }
]

# 初始化 session_state 来保存当前歌曲索引
# 如果'song_index'不存在于session_state中，则初始化为0
if 'song_index' not in st.session_state:
    st.session_state.song_index = 0

# 获取当前歌曲信息
current_index = st.session_state.song_index  # 获取当前播放的歌曲索引
current_song = songs[current_index]  # 根据索引获取当前歌曲的详细信息

# 创建左右两列布局，增加更大的间距
# col1用于显示专辑封面，col2用于显示歌曲信息和控制按钮
col1, col2 = st.columns([1, 2], gap="large")  # gap参数控制列之间的间距

with col1:
    # 显示专辑封面 - 使用 width 参数设置图片宽度
    st.image(images[current_index], width=250, caption='专辑封面')  # caption参数添加图片说明文字

with col2:
    # 显示歌曲信息，使用markdown调整间距
    # 通过CSS样式增加左间距和上间距，使布局更美观
    st.markdown("<div style='margin-left: 50px; margin-top: 20px;'>", unsafe_allow_html=True)
    st.title(current_song['title'])  # 显示歌曲标题
    st.write(f"歌手: {current_song['artist']}")  # 显示歌手名称
    st.write(f"时长: {current_song['duration']}")  # 显示歌曲时长
    st.markdown("</div>", unsafe_allow_html=True)
    
    # 添加分隔线 - 用于分隔歌曲信息和控制按钮
    st.markdown("---")
    
    # 创建控制按钮行 - 分为两列，分别放置上一首和下一首按钮
    col2_1, col2_2 = st.columns([1, 1])
    
    with col2_1:
        # 上一首按钮
        # disabled参数控制按钮是否可用，当是第一首歌时禁用
        if st.button('⬅️ 上一首', disabled=current_index == 0):
            st.session_state.song_index -= 1  # 切换到上一首歌
            st.rerun()  # 重新运行应用以更新显示
    
    with col2_2:
        # 下一首按钮
        # disabled参数控制按钮是否可用，当是最后一首歌时禁用
        if st.button('下一首 ➡️', disabled=current_index == len(songs) - 1):
            st.session_state.song_index += 1  # 切换到下一首歌
            st.rerun()  # 重新运行应用以更新显示

# 音乐播放器 - 显示当前歌曲的音频播放器
st.audio(current_song['audio'])  # 传入音频文件的URL
