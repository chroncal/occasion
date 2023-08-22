import matplotlib.pyplot as plt

def visualize_eval_results(file_path):
    epochs = []
    mAP_values = []

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('Epoch'):
                epoch = int(line.strip().split(':')[1])
                epochs.append(epoch)
            elif line.startswith('mAP'):
                mAP_value = float(line.strip().split(':')[1])
                mAP_values.append(mAP_value)

    plt.plot(epochs, mAP_values, marker='o')
    plt.xlabel('Epoch')
    plt.ylabel('mAP')
    plt.title('mAP vs. Epoch')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 使用示例：
file_path = 'D:\\nanodet-0.2.0\\nanodet-0.2.0\\workspace\\nanodet_m\\7.29晚上（1队数据集+2队数据集-只有果实+500x2干扰板）\\eval_results.txt'
visualize_eval_results(file_path)
