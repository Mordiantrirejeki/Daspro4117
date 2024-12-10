from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pydotplus
from sklearn import tree
from IPython.display import Image

# **1. Dataset Iris**
iris = datasets.load_iris()
features = iris['data']
target = iris['target']

# Membuat dan melatih Decision Tree Classifier
decisiontree = DecisionTreeClassifier(
    random_state=0,
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    min_weight_fraction_leaf=0,
    max_leaf_nodes=None,
    min_impurity_decrease=0,
)
model = decisiontree.fit(features, target)

# Prediksi dan probabilitas prediksi untuk sebuah observasi
observation = [[5, 4, 3, 2]]
print("Prediksi: ", model.predict(observation))
print("Probabilitas: ", model.predict_proba(observation))

# **2. Visualisasi Pohon Keputusan**
# Membuat representasi DOT dari pohon keputusan
dot_data = tree.export_graphviz(
    decisiontree,
    out_file=None,
    feature_names=iris['feature_names'],
    class_names=iris['target_names'],
    filled=True,
    rounded=True,
    special_characters=True,
)

# Membuat grafik dari data DOT
graph = pydotplus.graph_from_dot_data(dot_data)

# Menampilkan gambar di Jupyter Notebook (opsional jika menggunakan Jupyter)
Image(graph.create_png())

# Menyimpan gambar dalam format PNG ke direktori tertentu
graph.write_png(r'E:\Folder kuliah\smstr5\Penambangan data\P7\iris_graph.png')

# **3. Dataset Iris dalam CSV**
# Membaca dataset dari file CSV ke dalam DataFrame
irisDataset = pd.read_csv(
    'E:\Folder kuliah\smstr5\Penambangan data\P7\datasetIris.csv',
    delimiter=';',  # Menggunakan delimiter titik koma
    header=0  # Baris pertama sebagai header
)


# Mengubah kelas (kolom "Species") dari string ke integer
irisDataset["Species"] = pd.factorize(irisDataset["Species"])[0]

# Menghapus kolom "Id" yang tidak relevan untuk analisis
irisDataset = irisDataset.drop(labels="Id", axis=1)

# Mengubah DataFrame menjadi array NumPy
irisDataset = irisDataset.to_numpy()

# Membagi dataset: 40 baris data untuk training, dan 20 baris untuk testing
dataTraining = np.concatenate((irisDataset[0:40, :], irisDataset[50:90, :]), axis=0)
dataTesting = np.concatenate((irisDataset[40:50, :], irisDataset[90:100, :]), axis=0)

# Memisahkan dataset menjadi input (fitur) dan label
inputTraining = dataTraining[:, 0:4]
labelTraining = dataTraining[:, 4]
inputTesting = dataTesting[:, 0:4]
labelTesting = dataTesting[:, 4]

# **4. Training dan Prediksi**
model = DecisionTreeClassifier()
model = model.fit(inputTraining, labelTraining)
hasilPrediksi = model.predict(inputTesting)

# **5. Evaluasi**
print("Label sebenarnya: ", labelTesting)
print("Hasil prediksi: ", hasilPrediksi)

prediksiBenar = (hasilPrediksi == labelTesting).sum()
prediksiSalah = (hasilPrediksi != labelTesting).sum()
akurasi = prediksiBenar / (prediksiBenar + prediksiSalah) * 100

print("Prediksi benar: ", prediksiBenar, "data")
print("Prediksi salah: ", prediksiSalah, "data")
print("Akurasi: {:.2f}%".format(akurasi))
