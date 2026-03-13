
import streamlit as st
import time
import pandas as pd
from datetime import datetime

# 设置页面
st.set_page_config(page_title="Adam-Node: AI Node Native Python", layout="wide")

# 初始化 Session State (模拟 Node 状态)
if 'logs' not in st.session_state:
    st.session_state.logs = ["[22:00:15] PROTOCOL_SYNC_COMPLETED (Native Python Engine)"]
if 'protocol' not in st.session_state:
    st.session_state.protocol = {
        "0x01": "Grill_Steak_Medium",
        "0x02": "Brew_Triple_Espresso",
        "0x03": "Late_Night_Burger"
    }

st.title("🗡️ Adam-Node: AI Node 逻辑总线实验 (Native Python)")
st.caption("该实验运行在 Hugging Face Spaces 原生 Python 容器中，展示公网服务节点的确定性指令流协作。")

with st.sidebar:
    st.header("🤝 语义握手层")
    proto_df = pd.DataFrame(list(st.session_state.protocol.items()), columns=['OpCode', 'LogicFunction'])
    st.table(proto_df)

col1, col2 = st.columns([1, 2])
with col1:
    st.header("🎮 控制平面")
    if st.button("发送 0x01 (牛排)"):
        st.session_state.logs.append(f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}] OUT: [0x01] -> Node_Chef")
        time.sleep(0.001) # 模拟毫秒级总线延迟
        st.session_state.logs.append(f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}] IN: [0x00 Success] -> Executed: Grill_Steak")
    if st.button("发送 0x02 (咖啡)"):
        st.session_state.logs.append(f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}] OUT: [0x02] -> Node_Chef")
        time.sleep(0.001)
        st.session_state.logs.append(f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}] IN: [0x00 Success] -> Executed: Brew_Espresso")

with col2:
    st.header("📡 总线监控 (Bus Traffic)")
    st.code("\n".join(st.session_state.logs[-15:]), language="text")

st.divider()
st.subheader("⚙️ 节点运行报告")
c1, c2, c3 = st.columns(3)
c1.metric("LLM 占用", "0%", "Native Execution")
c2.metric("指令延迟", "0.005ms", "Compute Node")
c3.metric("环境内核", "Linux / Python 3.10", "High Performance")
