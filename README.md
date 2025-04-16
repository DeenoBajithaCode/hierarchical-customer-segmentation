# 📦 Hierarchical Customer Segmentation

This project demonstrates how to use **Agglomerative Hierarchical Clustering** to segment mall customers based on their **Annual Income** and **Spending Score**. The project includes:

- Data Cleaning & Preparation  
- Dendrogram Analysis  
- Agglomerative Clustering  
- Visualization of Clustered Segments

---

## 🗂️ Project Structure

```
hierarchical-customer-segmentation/
├── data/                     # Raw input data
├── notebooks/               # Jupyter notebook for experimentation
├── src/                     # Source code modules
│   ├── dendrogram.py        # Plotting cluster hierarchy
│   ├── clustering.py        # Agglomerative clustering logic
│   └── visualization.py     # Scatter plot visualization
├── dendrogram_plot.png      # Saved dendrogram plot
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 📊 Dataset

- **Source:** Customer Shopping Dataset (Kaggle or custom)
- **Original Features:**
  - CustomerID  
  - Genre  
  - Age  
  - Annual Income (k$)  
  - Spending Score (1–100)

- **Features Used for Clustering:**
  - Annual Income (k$)  
  - Spending Score (1–100)

- **Excluded Columns:**
  - CustomerID, Genre, Age  

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/DeenoBajithaCode/hierarchical-customer-segmentation
cd hierarchical-customer-segmentation
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Plot the Dendrogram

```bash
python src/dendrogram.py
```

This saves a dendrogram image as `dendrogram_plot.png` to visually determine the optimal number of clusters.

### 4. Run Clustering

```bash
python src/clustering.py
```

### 5. Visualize Clusters

```bash
python src/visualization.py
```

---

## 🔍 Key Techniques

- 🌲 **Dendrograms**: Visualize how clusters are formed using `scipy.cluster.hierarchy`  
- 🧠 **Agglomerative Clustering**: Bottom-up clustering using `scikit-learn`  
- 🎨 **Cluster Visualization**: Scatter plot of customer segments using `matplotlib`  

---

## 🛠️ Tech Stack

- Python  
- Scikit-learn  
- Pandas & NumPy  
- Matplotlib  
- SciPy

---

## 📌 Notes

- The dendrogram helps decide the ideal number of clusters by identifying large vertical gaps.  
- Only `Annual Income` and `Spending Score` are used to retain a clean 2D visualization.  
- You can experiment with linkage methods (`ward`, `average`, `complete`) for different clustering behavior.

---

## 📬 Contact

For questions, ideas, or contributions, feel free to open an issue or PR on the [GitHub repo](https://github.com/DeenoBajithaCode/hierarchical-customer-segmentation).