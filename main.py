from evomac_main import EvoMAC_Main
from utils import load_config # 导入 load_config 函数

# 示例输入
sample = {
    "query": "Write a Python function to calculate the factorial of a number. It should handle non-negative integers."
}

# 1. 从 YAML 文件加载通用配置
#    这将加载你在 general_config.yaml 中定义的所有模型信息
general_config = load_config("general_config.yaml")

# 2. 初始化 EvoMAC，并传入加载的配置
#    EvoMAC_Main 的基类 MAS 会使用这个 general_config 来设置 LLM 调用
evomac = EvoMAC_Main(general_config=general_config)

# 3. 运行推理
result = evomac.inference(sample)

# 4. 打印最终生成的代码
print("--- Final Generated Code ---")
print(result["response"])