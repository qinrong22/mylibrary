import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime

# 设置页面配置
st.set_page_config(
    page_title="南宁服装店铺数据仪表盘",
    page_icon="👕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS样式（仅修改配色适配服装主题）
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #3182CE;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: bold;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #9F7AEA;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #A8DADC;
        padding-bottom: 0.5rem;
    }
    .card {
        background-color: #F1FAEE;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 15px;
    }
    .metric-card {
        background-color: #A8DADC;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .restaurant-card {
        background-color: #FFFFFF;
        border-radius: 8px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #3182CE;
    }
    .restaurant-name {
        font-size: 1.2rem;
        font-weight: bold;
        color: #1D3557;
    }
    .restaurant-info {
        color: #457B9D;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# 标题
st.markdown('<h1 class="main-header">👕 南宁服装店铺数据仪表盘</h1>', unsafe_allow_html=True)

# 创建模拟数据
def create_restaurant_data():
    """创建服装店铺基本信息（替换原餐厅数据）"""
    shops = [
        {
            'name': '优衣库万象城店',
            'category': '快时尚',
            'rating': 4.7,
            'avg_price': 320,
            'review_count': 1280,
            'address': '青秀区民族大道136号万象城4楼',
            'popular_dish': '基础款T恤',  # 改为核心单品
            'open_year': 2015,
            'district': '青秀区'
        },
        {
            'name': 'ZARA航洋城店',
            'category': '快时尚',
            'rating': 4.5,
            'avg_price': 580,
            'review_count': 1560,
            'address': '兴宁区民生路42号航洋城2楼',
            'popular_dish': '连衣裙',
            'open_year': 2018,
            'district': '兴宁区'
        },
        {
            'name': '梦之岛百货民族大道店',
            'category': '高端女装',
            'rating': 4.8,
            'avg_price': 890,
            'review_count': 890,
            'address': '西乡塘区大学路100号梦之岛百货',
            'popular_dish': '轻奢外套',
            'open_year': 2012,
            'district': '西乡塘区'
        },
        {
            'name': '以纯朝阳广场旗舰店',
            'category': '休闲装',
            'rating': 4.6,
            'avg_price': 260,
            'review_count': 760,
            'address': '良庆区五象大道28号朝阳广场3楼',
            'popular_dish': '休闲牛仔裤',
            'open_year': 2010,
            'district': '良庆区'
        },
        {
            'name': 'UR东盟盛天地店',
            'category': '快时尚',
            'rating': 4.4,
            'avg_price': 650,
            'review_count': 2100,
            'address': '江南区星光大道68号盛天地B1层',
            'popular_dish': '秋冬风衣',
            'open_year': 2008,
            'district': '江南区'
        },
        {
            'name': '李宁专卖店七星路店',
            'category': '运动装',
            'rating': 4.7,
            'avg_price': 420,
            'review_count': 1850,
            'address': '青秀区七星路128号',
            'popular_dish': '专业运动鞋',
            'open_year': 2005,
            'district': '青秀区'
        },
        {
            'name': '太平鸟兴宁店',
            'category': '休闲装',
            'rating': 4.5,
            'avg_price': 590,
            'review_count': 640,
            'address': '兴宁区朝阳路66号',
            'popular_dish': '通勤西装',
            'open_year': 2016,
            'district': '兴宁区'
        },
        {
            'name': 'HM万象汇店',
            'category': '快时尚',
            'rating': 4.3,
            'avg_price': 380,
            'review_count': 3200,
            'address': '青秀区中山路万象汇2楼',
            'popular_dish': '儿童服饰',
            'open_year': 2000,
            'district': '青秀区'
        }
    ]
    # 统一字段名（仅替换表述，不修改字段结构）
    df = pd.DataFrame(shops)
    df = df.rename(columns={'popular_dish': 'core_product'})  # 招牌菜→核心单品
    return df

def create_monthly_price_data():
    """创建每月服装价格走势数据"""
    months = ['1月', '2月', '3月', '4月', '5月', '6月', 
              '7月', '8月', '9月', '10月', '11月', '12月']
    
    shops = ['优衣库万象城店', 'ZARA航洋城店', '梦之岛百货民族大道店', '以纯朝阳广场旗舰店', 'UR东盟盛天地店', '李宁专卖店七星路店']
    
    data = []
    for shop in shops:
        # 根据服装类型设定基础价格
        if '快时尚' in shop or '休闲' in shop:
            base_price = random.randint(200, 400)
        elif '高端' in shop:
            base_price = random.randint(700, 1000)
        elif '运动' in shop:
            base_price = random.randint(350, 500)
        else:
            base_price = random.randint(300, 600)
        
        for i, month in enumerate(months):
            # 模拟服装季节性价格波动
            seasonal_factor = 1.0
            if month in ['1月', '2月']:  # 春节促销
                seasonal_factor = 0.9
            elif month in ['6月', '7月']:  # 夏季新品
                seasonal_factor = 1.1
            elif month in ['11月', '12月']:  # 双11/双12
                seasonal_factor = 0.85
            elif month in ['9月']:  # 秋季上新
                seasonal_factor = 1.05
            
            # 添加随机波动
            random_factor = random.uniform(0.98, 1.02)
            
            price = round(base_price * seasonal_factor * random_factor, 1)
            
            data.append({
                '餐厅': shop,  # 保留字段名，仅内容替换为服装店铺
                '月份': month,
                '价格指数': price,
                '月份序号': i+1
            })
    
    return pd.DataFrame(data)

def create_category_data():
    """创建服装类别数据（替换原美食类别）"""
    categories = ['快时尚', '高端女装', '休闲装', '运动装', '儿童服饰']
    counts = [45, 28, 32, 19, 52]
    avg_ratings = [4.5, 4.3, 4.2, 4.6, 4.4]
    avg_prices = [450, 850, 550, 480, 320]
    
    return pd.DataFrame({
        '美食类别': categories,  # 保留字段名，内容替换为服装类别
        '店铺数量': counts,
        '平均评分': avg_ratings,
        '平均价格': avg_prices
    })

def create_visitor_data():
    """创建每月进店客流量数据（替换原访客量）"""
    months = ['1月', '2月', '3月', '4月', '5月', '6月', 
              '7月', '8月', '9月', '10月', '11月', '12月']
    
    # 模拟不同类别服装店铺的客流量
    visitor_data = {
        '月份': months,
        '米粉类': [1200, 1500, 1300, 1400, 1600, 1550, 1650, 1700, 1450, 1600, 1400, 1550],  # 快时尚
        '广西菜类': [800, 950, 850, 900, 1000, 980, 1020, 1050, 920, 1000, 880, 950],  # 高端女装
        '烧烤类': [600, 700, 650, 680, 720, 750, 800, 850, 780, 820, 700, 750],  # 休闲装
        '小吃类': [900, 1000, 950, 980, 1050, 1100, 1150, 1200, 1050, 1100, 950, 1000]  # 运动装
    }
    
    return pd.DataFrame(visitor_data)

def create_district_data():
    """创建行政区划服装店铺分布数据"""
    districts = ['青秀区', '兴宁区', '西乡塘区', '江南区', '良庆区', '邕宁区']
    counts = [35, 28, 32, 24, 18, 12]
    
    return pd.DataFrame({
        '行政区': districts,
        '店铺数量': counts
    })

def create_map_data():
    """创建服装店铺地图数据"""
    # 模拟南宁服装店铺地理位置数据
    map_data = pd.DataFrame({
        'lat': [22.8167, 22.8190, 22.8370, 22.7550, 22.7800, 22.8100, 22.8230, 22.8150],
        'lon': [108.3667, 108.3200, 108.2900, 108.3700, 108.3100, 108.3400, 108.3180, 108.3250],
        'name': ['优衣库万象城店', 'ZARA航洋城店', '梦之岛百货民族大道店', '以纯朝阳广场旗舰店', 'UR东盟盛天地店', '李宁专卖店七星路店', '太平鸟兴宁店', 'HM万象汇店'],
        'category': ['快时尚', '快时尚', '高端女装', '休闲装', '快时尚', '运动装', '休闲装', '快时尚'],
        'rating': [4.7, 4.5, 4.8, 4.6, 4.4, 4.7, 4.5, 4.3],
        'size': [47, 45, 48, 46, 44, 47, 45, 43]
    })
    return map_data

# 加载数据
restaurant_df = create_restaurant_data()  # 变量名保留，内容为服装店铺
price_df = create_monthly_price_data()
category_df = create_category_data()
visitor_df = create_visitor_data()
district_df = create_district_data()
map_df = create_map_data()

# 侧边栏
with st.sidebar:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🎛️ 数据筛选")
    
    # 服装类别筛选（替换原美食类别）
    categories = ['全部'] + list(restaurant_df['category'].unique())
    selected_category = st.selectbox("选择服装类别", categories)
    
    # 行政区筛选
    districts = ['全部'] + list(restaurant_df['district'].unique())
    selected_district = st.selectbox("选择行政区", districts)
    
    # 评分筛选
    min_rating, max_rating = st.slider(
        "选择评分范围", 
        min_value=4.0, 
        max_value=5.0, 
        value=(4.0, 5.0),
        step=0.1
    )
    
    # 客单价筛选（替换原人均价格）
    min_price, max_price = st.slider(
        "选择客单价范围", 
        min_value=0, 
        max_value=1500, 
        value=(100, 1000),
        step=50
    )
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # 显示统计信息
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("店铺总数", len(restaurant_df))
    avg_rating = restaurant_df['rating'].mean()
    st.metric("平均评分", f"{avg_rating:.1f}")
    st.metric("数据更新时间", datetime.now().strftime("%Y-%m-%d"))
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📊 图表说明")
    st.info("""
    1. **价格走势图**: 显示6家服装店铺12个月的核心单品价格变化
    2. **类别分布图**: 显示不同服装类别的店铺数量
    3. **客流量面积图**: 显示各类服装店铺每月客流量变化
    4. **服装地图**: 显示店铺在南宁的分布位置
    """)

# 主页面布局
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.metric("最高评分", f"{restaurant_df['rating'].max():.1f}")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    avg_price = restaurant_df['avg_price'].mean()
    st.metric("平均客单价", f"¥{avg_price:.0f}")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    total_reviews = restaurant_df['review_count'].sum()
    st.metric("总评价数", f"{total_reviews:,}")
    st.markdown("</div>", unsafe_allow_html=True)

# 应用筛选
filtered_df = restaurant_df.copy()
if selected_category != '全部':
    filtered_df = filtered_df[filtered_df['category'] == selected_category]

if selected_district != '全部':
    filtered_df = filtered_df[filtered_df['district'] == selected_district]

filtered_df = filtered_df[
    (filtered_df['rating'] >= min_rating) & 
    (filtered_df['rating'] <= max_rating) &
    (filtered_df['avg_price'] >= min_price) & 
    (filtered_df['avg_price'] <= max_price)
]

# 价格走势折线图（服装核心单品价格）
st.markdown('<h2 class="sub-header">📈 服装店铺核心单品价格走势（12个月）</h2>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)

# 选择要显示的店铺
available_restaurants = price_df['餐厅'].unique()
selected_restaurants = st.multiselect(
    "选择要显示的店铺", 
    options=available_restaurants,
    default=available_restaurants[:5],
    key="line_chart_select"
)

if selected_restaurants:
    filtered_price_df = price_df[price_df['餐厅'].isin(selected_restaurants)]
    
    # 转换为宽格式，便于Streamlit绘制折线图
    price_pivot = filtered_price_df.pivot(index='月份序号', columns='餐厅', values='价格指数')
    
    # 按月份排序
    price_pivot = price_pivot.sort_index()
    
    # 使用Streamlit的line_chart
    st.line_chart(price_pivot, use_container_width=True)
    
    # 显示数据表格
    with st.expander("查看价格数据表格"):
        st.dataframe(price_pivot)
else:
    st.warning("请至少选择一家店铺以显示价格走势图")

st.markdown("</div>", unsafe_allow_html=True)

# 柱状图和面积图并排显示
col1, col2 = st.columns(2)

with col1:
    st.markdown('<h2 class="sub-header">📊 服装类别分布</h2>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # 使用Streamlit的bar_chart
    # 设置索引为服装类别
    bar_chart_data = category_df.set_index('美食类别')['店铺数量']
    st.bar_chart(bar_chart_data, use_container_width=True)
    
    # 显示详细数据
    with st.expander("查看类别详细数据"):
        st.dataframe(category_df)
    
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<h2 class="sub-header">📈 各类服装店铺客流量趋势</h2>', unsafe_allow_html=True)
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # 使用Streamlit的area_chart
    # 设置索引为月份
    area_chart_data = visitor_df.set_index('月份')[['米粉类', '广西菜类', '烧烤类', '小吃类']]
    # 重命名列名适配服装主题（仅显示用，不修改数据结构）
    area_chart_data_renamed = area_chart_data.rename(columns={
        '米粉类': '快时尚',
        '广西菜类': '高端女装',
        '烧烤类': '休闲装',
        '小吃类': '运动装'
    })
    st.area_chart(area_chart_data_renamed, use_container_width=True)
    
    # 显示详细数据
    with st.expander("查看客流量详细数据"):
        st.dataframe(visitor_df)
    
    st.markdown("</div>", unsafe_allow_html=True)

# 地图展示
st.markdown('<h2 class="sub-header">🗺️ 南宁服装店铺地图</h2>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)

# 使用Streamlit的map功能
st.map(map_df, size='size', color='#3182CE', use_container_width=True)

# 显示地图上的店铺信息
st.markdown("**地图上的服装店铺:**")
cols = st.columns(4)
for i, (idx, row) in enumerate(map_df.iterrows()):
    with cols[i % 4]:
        st.markdown(f"""
        <div style="border-left: 3px solid #3182CE; padding-left: 10px; margin-bottom: 10px;">
            <div style="font-weight: bold; color: #1d3557;">{row['name']}</div>
            <div style="color: #457b9d; font-size: 0.9rem;">
                类别: {row['category']}<br>
                评分: {row['rating']}
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# 行政区分布图
st.markdown('<h2 class="sub-header">🏙️ 南宁各行政区服装店铺分布</h2>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)

# 使用Streamlit的bar_chart
district_chart_data = district_df.set_index('行政区')['店铺数量']
st.bar_chart(district_chart_data, use_container_width=True)

# 显示详细数据
with st.expander("查看行政区详细数据"):
    st.dataframe(district_df)

st.markdown("</div>", unsafe_allow_html=True)

# 店铺详细信息
st.markdown('<h2 class="sub-header">📋 服装店铺详细信息</h2>', unsafe_allow_html=True)

# 显示筛选后的店铺
if len(filtered_df) > 0:
    # 使用Streamlit的columns布局
    cols = st.columns(2)
    for idx, row in filtered_df.iterrows():
        with cols[idx % 2]:
            # 替换文案为服装主题
            st.markdown(f"""
            <div class="restaurant-card">
                <div class="restaurant-name">{row['name']} ⭐ {row['rating']}</div>
                <div class="restaurant-info">
                    类别: {row['category']} | 客单价: ¥{row['avg_price']}<br>
                    评价数: {row['review_count']} | 行政区: {row['district']}<br>
                    核心单品: {row['core_product']}<br>
                    地址: {row['address']}<br>
                    开业年份: {row['open_year']}
                </div>
            </div>
            """, unsafe_allow_html=True)
else:
    st.warning("没有找到符合条件的店铺，请调整筛选条件")

# 数据表格
st.markdown('<h2 class="sub-header">📊 完整数据表格</h2>', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)

# 格式化显示
display_df = filtered_df.copy()
display_df = display_df.rename(columns={
    'name': '店铺名称',
    'category': '服装类别',
    'rating': '评分',
    'avg_price': '客单价(元)',
    'review_count': '评价数',
    'address': '地址',
    'core_product': '核心单品',
    'open_year': '开业年份',
    'district': '行政区'
})

# 重新排列列顺序
display_df = display_df[['店铺名称', '服装类别', '评分', '客单价(元)', '核心单品', '评价数', '开业年份', '行政区', '地址']]

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)

st.markdown("</div>", unsafe_allow_html=True)

# 页脚
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "南宁服装店铺数据仪表盘 © 2023 | 数据仅供参考 | 最后更新: " + 
    datetime.now().strftime("%Y-%m-%d %H:%M") +
    "</div>", 
    unsafe_allow_html=True
)
