from evomac_main import EvoMAC_Main
from utils import load_config # 导入 load_config 函数

# input
sample = {
    "query": "Write a Python function to calculate the factorial of a number. It should handle non-negative integers."
}
# load llm config
general_config = load_config("general_config.yaml")


evomac = EvoMAC_Main(general_config=general_config)


result = evomac.inference(sample)


print("--- Final Generated Code ---")
print(result["response"])
