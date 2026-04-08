import matplotlib.pyplot as plt
import os
import re

# 查找日志文件
def find_log_file():
    base_dir = "results_isic"
    if not os.path.exists(base_dir):
        return None
    
    # 遍历目录结构
    for root, dirs, files in os.walk(base_dir):
        if "stdout.txt" in files:
            return os.path.join(root, "stdout.txt")
    return None

# 查找日志文件
log_file = find_log_file()
if not log_file:
    print("未找到日志文件")
else:
    print(f"找到日志文件: {log_file}")

    # 提取准确率和损失数据
    accuracies = []
    losses = []
    epochs = []
    steps = []

    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            # 匹配准确率
            acc_match = re.search(r"epoch:\s*(\d+),\s*step:\s*\d+,\s*Average accuracy:\s*([\d\.]+)", line)
            if acc_match:
                epoch = int(acc_match.group(1))
                acc = float(acc_match.group(2))
                accuracies.append(acc)
                epochs.append(epoch)
            
            # 匹配损失
            loss_match = re.search(r"epoch:\s*\d+,\s*step:\s*(\d+),\s*CE loss:\s*\d+,\s*Noise Estimation loss:\s*([\d\.]+)", line)
            if loss_match:
                step = int(loss_match.group(1))
                loss = float(loss_match.group(2))
                losses.append(loss)
                steps.append(step)

    print(f"提取到 {len(accuracies)} 个准确率数据点")
    print(f"提取到 {len(losses)} 个损失数据点")

    # 绘制准确率曲线
    if accuracies:
        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.plot(epochs, accuracies, 'o-')
        plt.title("Test Accuracy")
        plt.xlabel("Epoch")
        plt.ylabel("Accuracy (%)")
        plt.grid(True)

    # 绘制损失曲线
    if losses:
        plt.subplot(1, 2, 2)
        plt.plot(steps, losses, 'o-')
        plt.title("Training Loss")
        plt.xlabel("Step")
        plt.ylabel("Loss")
        plt.grid(True)

    plt.tight_layout()
    plt.show()