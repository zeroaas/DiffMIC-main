import os
import pickle
import random

# 图片目录路径
train_dir = 'dataset/isic2018/images/train'

# 获取所有图片文件
image_files = [f for f in os.listdir(train_dir) if f.endswith('.jpg')]
print(f"找到 {len(image_files)} 张图片")

# 随机划分训练集和测试集（80%训练，20%测试）
random.seed(42)  # 固定随机种子，确保结果可重复
random.shuffle(image_files)
train_size = int(len(image_files) * 0.8)
train_files = image_files[:train_size]
test_files = image_files[train_size:]

print(f"训练集: {len(train_files)} 张图片")
print(f"测试集: {len(test_files)} 张图片")

# 生成训练集pkl
train_data = []
for img_file in train_files:
    img_path = f'./dataset/isic2018/images/train/{img_file}'
    train_data.append({'img_root': img_path, 'label': 0})

with open('dataset/isic2018/isic2018_train.pkl', 'wb') as f:
    pickle.dump(train_data, f)
print("已生成 isic2018_train.pkl")

# 生成测试集pkl
test_data = []
for img_file in test_files:
    img_path = f'./dataset/isic2018/images/train/{img_file}'
    test_data.append({'img_root': img_path, 'label': 0})

with open('dataset/isic2018/isic2018_test.pkl', 'wb') as f:
    pickle.dump(test_data, f)
print("已生成 isic2018_test.pkl")

print("\n前5个训练集条目：")
for i, entry in enumerate(train_data[:5]):
    print(f"{i+1}: {entry}")

print("\n前5个测试集条目：")
for i, entry in enumerate(test_data[:5]):
    print(f"{i+1}: {entry}")