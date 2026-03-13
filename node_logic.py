
import json
import time

class AINode:
    def __init__(self, name):
        self.name = name
        self.protocol_table = {}
        self.log = []

    def handshake(self, alignment_map):
        # 模拟 LLM 介入的握手对齐
        self.protocol_table = alignment_map
        self.add_log(f"Handshake Success: Aligned {len(alignment_map)} operations.")

    def execute_binary(self, opcode, payload=None):
        # 纯静态逻辑执行，不经过 LLM 推理
        if opcode in self.protocol_table:
            func_name = self.protocol_table[opcode]
            start_time = time.time()
            # 模拟逻辑层执行（确定性且极速）
            result = f"DONE: {func_name} with {payload}"
            latency = (time.time() - start_time) * 1000  # ms
            self.add_log(f"BUS IN: [{opcode}] -> EXEC: {func_name} -> {latency:.2f}ms")
            return {"status": 0x00, "data": result}
        else:
            return {"status": 0x01, "error": "Unknown OpCode"}

    def add_log(self, text):
        self.log.append(f"[{time.strftime('%H:%M:%S')}] {text}")
        if len(self.log) > 10: self.log.pop(0)

# 初始化 MVP 实验数据
chef_node = AINode("Chef-Node")
chef_node.handshake({
    "0x01": "Grill_Steak_Medium_Rare",
    "0x02": "Brew_Triple_Espresso",
    "0x03": "Assemble_Cheese_Burger"
})

def get_state():
    return {
        "node_name": chef_node.name,
        "protocol": chef_node.protocol_table,
        "recent_logs": chef_node.log
    }
