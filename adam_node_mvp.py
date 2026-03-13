
import time
import struct

# 模拟 AI Node 逻辑层
class ChefNode:
    def __init__(self):
        # 初始握手产生的静态映射表
        self.protocol_stack = {
            0x01: "ACTION_GRILL_STEAK_MEDIUM",
            0x02: "ACTION_BREW_ESPRESSO_TRIPLE",
            0x03: "ACTION_GENERATE_BURGER_DELUXE"
        }
        self.is_llm_active = False

    def handle_bus_packet(self, packet):
        # 模拟二进制解包 (Header: 2B, OpCode: 1B, PayloadSize: 1B)
        header, opcode, psize = struct.unpack('!HBB', packet[:4])
        
        if header != 0xAD01: # 私有协议头 (替换为合法的进制)
            return "ERROR_INVALID_PROTOCOL"

        # 重点：此处 LLM 处于 SLEEPING 状态
        self.is_llm_active = False 
        
        if opcode in self.protocol_stack:
            action = self.protocol_stack[opcode]
            # 模拟 CPU 逻辑操作
            start = time.perf_counter()
            time.sleep(0.0001) # 极速执行
            end = time.perf_counter()
            return f"RESULT: {action} | LATENCY: {(end-start)*1000:.4f}ms | LLM_USAGE: 0%"
        return "ERROR_UNKNOWN_OP"

# 实验模拟器
node = ChefNode()

print("--- PHASE 1: SEMANTIC HANDSHAKE (LLM ON) ---")
print("[Adam] -> [ChefNode]: 'Let's align. Use 0x01 for my favorite steak.'")
print("[ChefNode] -> [Adam]: 'Acknowledged. 0x01 bound to Grill_Steak_Medium.'")
time.sleep(1)

print("\n--- PHASE 2: BINARY BUS EXECUTION (LLM SLEEPING) ---")
# 构造一个 4 字节的二进制包: [0xAD 0xAM] [0x01] [0x00]
test_packet = struct.pack('!HBB', 0xAD01, 0x01, 0x00)

for i in range(3):
    res = node.handle_bus_packet(test_packet)
    print(f"[BUS_TRAFFIC] {test_packet.hex().upper()} | {res}")
    time.sleep(0.5)

print("\n--- EXPERIMENT SUMMARY ---")
print("Total Sent: 12 Bytes | LLM Calls: 0 | Reliability: 100%")
