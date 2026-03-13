
import streamlit as st
import time
import pandas as pd
from datetime import datetime

# 设置页面
st.set_page_config(page_title="Adam-Node: AI Bus Monitor", layout="wide")

# 初始化 Session State (模拟 Node 状态)
if 'logs' not in st.session_state:
    st.session_state.logs = []
if 'protocol' not in st.session_state:
    st.session_state.protocol = {
        "0x01": "Grill_Steak_Medium",
        "0x02": "Brew_Triple_Espresso",
        "0x03": "Late_Night_Burger"
    }

st.title("🛡️ Adam-Node: AI Node 逻辑总线实验 (MVP)")
st.caption("基于『二进制指令流』的高效 AI 协同架构演示")

# 侧边栏：协议握手
with st.sidebar:
    st.header("🤝 语义握手层")
    st.info("LLM 首次对齐结果 (Static Mapping)")
    proto_df = pd.DataFrame(list(st.session_state.protocol.items()), columns=['OpCode', 'LogicFunction'])
    st.table(proto_df)
    
    if st.button("重启协议对齐 (Reset)"):
        st.session_state.logs = ["[System] Handshake Refreshed."]

col1, col2 = st.columns([1, 2])

with col1:
    st.header("🎮 控制平面")
    st.write("模拟用户发起指令 (Fast Path)")
    
    if st.button("发送 0x01 (牛排)"):
        st.session_state.logs.append(f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}] OUT: [0x01] -> Node_Chef")
        time.sleep(0.01) # 模拟总线延迟
        st.session_state.logs.append(f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}] IN: [0x00 Success] -> Executed: Grill_Steak")

    if st.button("发送 0x02 (咖啡)"):
        st.session_state.logs.append(f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}] OUT: [0x02] -> Node_Chef")
        time.sleep(0.01)
        st.session_state.logs.append(f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}] IN: [0x00 Success] -> Executed: Brew_Espresso")

with col2:
    st.header("📡 总线监控 (Bus Traffic)")
    st.code("\n".join(st.session_state.logs[-15:]), language="text")

st.divider()
st.subheader("⚙️ 节点运行报告")
c1, c2, c3 = st.columns(3)
c1.metric("LLM 占用", "0%", "Sleep Mode")
c2.metric("指令延迟", "0.15ms", "Network IO")
c3.metric("传输损耗", "4 Bytes", "Binary Optim")
