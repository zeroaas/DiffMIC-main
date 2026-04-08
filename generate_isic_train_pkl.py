import os
import pickle

# 训练图片目录路径
train_dir = 'dataset/isic2018/images/train'

# 获取所有图片文件
image_files = [f for f in os.listdir(train_dir) if f.endswith('.jpg')]

# 创建数据列表
data_list = []
for img_file in image_files:
    # 构建相对路径
    img_path = os.path.join('dataset/isic2018/images/train', img_file)
    # 添加到列表，标签暂时设为0（如果有真实标签，需要替换）
    data_list.append({'img_root': img_path, 'label': 0})

# 保存为pickle文件
output_file = 'dataset/isic2018/isic2018_train.pkl'
with open(output_file, 'wb') as f:
    pickle.dump(data_list, f)

print(f"已生成 {output_file}，包含 {len(data_list)} 张图片")
print("前5个条目：")
for i, entry in enumerate(data_list[:5]):
    print(f"{i+1}: {entry}")