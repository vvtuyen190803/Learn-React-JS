import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import time
import matplotlib.pyplot as plt

# Dữ liệu
data = pd.DataFrame({
    'F1': [9.8, 1.3, 12.3, 1.6, 5.8, 6.8, 41.5, 2.8, 1.9, 6.8, 2.2, 7.7],
    'F2': [1.52, 4.61, 4.42, 3.8, 1.3, 3.62, 1.6, 3.82, 2.6, 4.22, 2.9, 1.4],
    'F3': [3.71, 3.12, 2.81, 2.9, 3.5, 2.3, 2.5, 2.5, 2.9, 2.9, 4.1, 2.5],
    'F4': [18.1, 2.2, 3, 2.2, 3.9, 40.7, 4.1, 3.9, 2.6, 3.9, 2.3, 3.1],
    'F5': [12.1, 2.9, 2.5, 2.7, 1.3, 2.3, 1.2, 3.9, 2.1, 1.8, 5.2, 1.5],
    'F6': [6.1, 9.1, 10, 11, 5.2, 5.8, 9.6, 9.7, 1.7, 2.4, 5.4, 7.3],
    'F7': [41.2, 5.8, 31.2, 7, 3.3, 21.7, 2.7, 2.7, 2.6, 4, 3.9, 4.3],
    'Class': ['H', 'L', 'H', 'H', 'L', 'H', 'L', 'L', 'H', 'L', 'H', 'L']
})

X = data.drop('Class', axis=1)
y = data['Class']

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-fold cross-validation
kf = KFold(n_splits=3, shuffle=True, random_state=42)

# Hàm đánh giá mô hình
def evaluate_model(model, X, y, kf):
    results = []
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        start_time = time.time()
        model.fit(X_train, y_train)
        end_time = time.time()

        y_pred = model.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, pos_label='H', zero_division=1) # Xử lý zero_division
        recall = recall_score(y_test, y_pred, pos_label='H', zero_division=1) # Xử lý zero_division
        f1 = f1_score(y_test, y_pred, pos_label='H', zero_division=1) # Xử lý zero_division
        time_taken = end_time - start_time

        results.append([accuracy, precision, recall, f1, time_taken])
    return np.array(results)

# Khởi tạo và đánh giá các mô hình
knn = KNeighborsClassifier(n_neighbors=3)
knn_results = evaluate_model(knn, X_scaled, y, kf)

bayes = GaussianNB()
bayes_results = evaluate_model(bayes, X_scaled, y, kf)

svm = SVC()
svm_results = evaluate_model(svm, X_scaled, y, kf)


# In kết quả
models = {'KNN': knn_results, 'Bayes': bayes_results, 'SVM': svm_results}
metrics = ['Accuracy', 'Precision', 'Recall', 'F1-score', 'Time']

for name, result in models.items():
    print(f"\n{name} Results (Averaged over 3 folds):")
    for i, metric in enumerate(metrics):
        print(f"{metric}: {result[:, i].mean():.4f}")

    print(f"\n{name} Results (Per Fold):")
    for i, fold_result in enumerate(result):
        print(f"Fold {i+1}:")
        for j, metric in enumerate(metrics):
            print(f"  {metric}: {fold_result[j]:.4f}")

# So sánh mô hình
print("\nComparison (Per Fold):")
for i in range(3):
    print(f"\nFold {i+1}:")
    for name, result in models.items():
        print(f"  {name}:")
        for j, metric in enumerate(metrics):
             print(f"    {metric}: {result[i, j]:.4f}")


# Vẽ biểu đồ
for name, result in models.items():
    for i, metric in enumerate(metrics[:-1]):  # Loại bỏ 'Time' khỏi biểu đồ so sánh
        plt.figure()
        plt.bar(range(3), result[:, i])
        plt.title(f"{name} {metric} per Fold")
        plt.xlabel("Fold")
        plt.ylabel(metric)
        plt.xticks(range(3), [f"Fold {j+1}" for j in range(3)])
        plt.show()



for i in range(3):
    plt.figure()
    width = 0.2  # Giảm độ rộng cột để hiển thị 3 mô hình
    x = np.arange(len(metrics[:-1]))

    plt.bar(x - width, bayes_results[i, :-1], width, label='Bayes')
    plt.bar(x , knn_results[i, :-1], width, label='KNN')
    plt.bar(x + width, svm_results[i, :-1], width, label='SVM')


    plt.title(f'Model Comparison - Fold {i+1}')
    plt.ylabel('Value')
    plt.xticks(x, metrics[:-1])
    plt.legend()
    plt.tight_layout()
    plt.show()
