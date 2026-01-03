import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, KFold
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

import matplotlib.pyplot as plt

# Đọc file dữ liệu (đặt cpu.csv cùng thư mục notebook)
df = pd.read_csv("cpu.csv")

df.head()

#Câu a chuẩn hóa dữ liệu

# Chuẩn hoá MYCT, MMIN về [0, 10]
scaler_minmax = MinMaxScaler(feature_range=(0, 10))
df[['MYCT', 'MMIN']] = scaler_minmax.fit_transform(df[['MYCT', 'MMIN']])

# Standardize các cột còn lại (trừ class)
scaler_std = StandardScaler()
cols_std = ['MMAX', 'CACH', 'CHMIN', 'CHMAX']
df[cols_std] = scaler_std.fit_transform(df[cols_std])

# Mã hoá cột class
le = LabelEncoder()
df['class'] = le.fit_transform(df['class'])

df.head()

#Câu b Fourier Transform

from numpy.fft import fft, ifft

data_10 = df.iloc[:10, :-1].values  # bỏ cột class
fft_data = fft(data_10, axis=0)
ifft_data = ifft(fft_data, axis=0)
print("Dữ liệu ban đầu:\n", data_10)
print("Sau FFT:\n", fft_data)
print("Sau IFFT (lấy phần thực):\n", np.real(ifft_data))

#Câu c Chia tập dữ liệu

X = df.drop('class', axis=1)
y = df['class']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42, stratify=y
)
print("Số mẫu Train:", X_train.shape)
print("Số mẫu Test:", X_test.shape)

#câu d 5-Fold Cross Validation trên tập train

kf = KFold(n_splits=5, shuffle=True, random_state=42)

for i, (train_idx, val_idx) in enumerate(kf.split(X_train)):
    print(f"Fold {i+1}: Train = {len(train_idx)}, Validation = {len(val_idx)}")


#Câu 2

#Câu a Naive Bayes – Đếm đúng/sa

nb = GaussianNB()
correct_nb = 0
wrong_nb = 0

for train_idx, val_idx in kf.split(X_train):
    X_tr = X_train.iloc[train_idx]
    X_val = X_train.iloc[val_idx]
    y_tr = y_train.iloc[train_idx]
    y_val = y_train.iloc[val_idx]

    nb.fit(X_tr, y_tr)
    y_pred = nb.predict(X_val)

    correct_nb += np.sum(y_pred == y_val)
    wrong_nb += np.sum(y_pred != y_val)

print("Naive Bayes")
print("Số mẫu phân lớp đúng:", correct_nb)
print("Số mẫu phân lớp sai:", wrong_nb)

#Câu b KNN – Đếm đúng/sai

knn = KNeighborsClassifier(n_neighbors=5)
correct_knn = 0
wrong_knn = 0

for train_idx, val_idx in kf.split(X_train):
    X_tr = X_train.iloc[train_idx]
    X_val = X_train.iloc[val_idx]
    y_tr = y_train.iloc[train_idx]
    y_val = y_train.iloc[val_idx]

    knn.fit(X_tr, y_tr)
    y_pred = knn.predict(X_val)

    correct_knn += np.sum(y_pred == y_val)
    wrong_knn += np.sum(y_pred != y_val)

print("KNN")
print("Số mẫu phân lớp đúng:", correct_knn)
print("Số mẫu phân lớp sai:", wrong_knn)

#Câu c Accuracy – Precision – Recall từng fold

accs = []
pres = []
recs = []

for train_idx, val_idx in kf.split(X_train):
    X_tr = X_train.iloc[train_idx]
    X_val = X_train.iloc[val_idx]
    y_tr = y_train.iloc[train_idx]
    y_val = y_train.iloc[val_idx]

    knn.fit(X_tr, y_tr)
    y_pred = knn.predict(X_val)

    accs.append(accuracy_score(y_val, y_pred))
    pres.append(precision_score(y_val, y_pred, average='macro'))
    recs.append(recall_score(y_val, y_pred, average='macro'))

print("Accuracy từng fold:", accs)
print("Precision từng fold:", pres)
print("Recall từng fold:", recs)

print("\nGiá trị trung bình:")
print("Accuracy:", np.mean(accs))
print("Precision:", np.mean(pres))
print("Recall:", np.mean(recs))

#Vẽ biểu đồ hiện thị kết quả 
plt.figure()
plt.plot(accs, marker='o', label='Accuracy')
plt.plot(pres, marker='s', label='Precision')
plt.plot(recs, marker='^', label='Recall')

plt.xlabel("Fold")
plt.ylabel("Score")
plt.title("Kết quả 5-Fold Cross Validation (KNN)")
plt.legend()
plt.grid(True)
plt.show()
