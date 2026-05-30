import streamlit as st
import base64
st.set_page_config(
    page_title="速度美学 · 跑车世界",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded",
)
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(45deg, #0d0d0d, #1a1a1a, #220000, #0d0d0d);
    background-size: 400% 400%;
    animation: raceBg 10s ease infinite;
}
@keyframes raceBg {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
h1 {
    color: #ff0000 !important;
    font-size: 48px !important;
    font-weight: 900 !important;
    text-shadow: 0 0 15px #ff0000;
    letter-spacing: 2px;
}
h2, h3 {
    color: #ffffff !important;
    font-weight: 800 !important;
}
.st-emotion-cache-10trblm {
    color: #ffcc00 !important;
    font-size: 22px !important;
    text-shadow: 0 0 10px #ffcc00;
}
img {
    border-radius: 10px !important;
    box-shadow: 0 0 25px rgba(255,0,0,0.4) !important;
}
table {
    background: #111 !important;
    color: #fff !important;
    border-radius: 10px !important;
    box-shadow: 0 0 20px red !important;
}
th {
    color: #ff0000 !important;
    font-size: 18px !important;
}
td {
    color: #fff !important;
}
.stTextInput, .stRadio {
    background: #151515 !important;
    border-radius: 10px !important;
    padding: 10px !important;
    box-shadow: 0 0 10px #ff0000 !important;
}
input, label {
    color: #fff !important;
}
audio, video {
    border-radius: 10px !important;
    box-shadow: 0 0 20px red !important;
}
</style>
""", unsafe_allow_html=True)
st.title("🏁 硬核机械美学，突出动力与机甲质感")
st.header("🚀 凌驾风速，尽显极致性能")
st.subheader("🔥 踏疾风、驭锋芒、战赛道、纵狂影、啸长空")
st.image("./supercar/blake-meyer-CRNbHjNaljo-unsplash.jpg", width="stretch")
st.logo(
    "./supercar/jack-lucas-smith-4-MxVqPiPk0-unsplash.jpg",
    size="large",
    link="https://www.byd.com/cn"
)
st.image("./supercar/spencer-davis-DFnCCRExDdc-unsplash.jpg", width="stretch")
col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🔊 超跑声浪 - 听觉盛宴")
    st.audio(
        "./supercar/【跑车混剪声浪高燃完整版】带上耳机，带你感受不一样的速度与激情！！！.mp3",loop=True,start_time=7,end_time=7
    )
with col2:
    st.markdown("### 🎬 兰博基尼 - 视觉冲击")
    st.video("./supercar/哪个男人能拒绝新一代兰博基尼？.mp4",width="stretch")
st.markdown("---")
st.markdown("## 🌪️ 全球顶级超跑排名")
car_order = {
    "科尼赛克 Jesko Absolut（瑞典）": {"极速": "500 km/h", "动力": "5.0L 双涡轮 V8，1600 马力"},
    "仰望 U9 Xtreme（中国）": {"极速": "496 km/h", "动力": "四电机纯电，1300 马力"},
    "SSC Tuatara（美国）": {"极速": "474 km/h", "动力": "5.9L 双涡轮 V8，1750 马力"}
}
st.table(car_order)
st.markdown("---")
st.markdown("## 📸 传奇超跑图鉴")
images = [
    "./supercar/1.png",
    "./supercar/2.png",
    "./supercar/3.png"
]
st.image(images, width=500)
st.markdown('<h1 style="color:red; font-size:40px;">🔥 兰博基尼 V12 气浪声浪</h1>', unsafe_allow_html=True)
st.audio("./supercar/a1.mp3",width=500)
st.markdown( '<h1 style="font-size:40px;"><span style="color:green;">🔥 兰博基尼 V11 气浪声浪</span></h1>', unsafe_allow_html=True)
st.audio("./supercar/a2.mp3",width=500)
st.markdown('<h1 style="font-size:40px;"><span style="color:white;">🔥 兰博基尼 V10 气浪声浪</span></h1>', unsafe_allow_html=True)
st.audio("./supercar/a3.mp3",width=500)
st.markdown("---")
st.markdown("## 🏎️ 定制你的专属超跑")
car_name = st.text_input("输入你梦想中的超跑名称：")
if car_name:
    st.success(f"🏁 尊贵的用户，恭喜你成功拥有【{car_name}】，愿它永远照亮你的前程！")
key = st.radio("选择车辆国籍", ["中 🇨🇳", "美 🇺🇸", "意大利 🇮🇹"], index=1)
st.write(f"✅ 你已选择：{key} 制造超跑！")
st.markdown("<br><br><center><h3>⚡ 速度无止境 · 激情永不熄 ⚡</h3></center>", unsafe_allow_html=True)