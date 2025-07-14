# 📊 Graph Neural Networks - Social Network Projects

This folder contains two mini-projects showcasing how Graph Neural Networks (GNNs) can be applied to different domains:

---

## 🧠 1. GNN-Based Social Network Analysis (`gnn_social_network_analysis.ipynb`)

### ✅ Description
This notebook explores the Cora citation network using a Graph Convolutional Network (GCN) model. It performs node classification to predict the subject category of each paper using only the graph structure and features.

### 🔧 Techniques
- PyTorch Geometric (PyG)
- GCNConv layers
- Graph visualization with NetworkX
- Accuracy tracking and performance improvement

### 📈 Results
Achieved ~80% accuracy with basic 2-layer GCN on the Cora dataset. Includes suggestions for dropout, GATConv, and hyperparameter tuning.

---

## 🎬 2. User-Movie Recommendation System (`User_movie_Reccomandation_System.ipynb`)

### ✅ Description
A simple recommender system based on user-item interactions (e.g., MovieLens data). Users and movies are represented as nodes in a bipartite graph, and edges represent ratings or interactions.

### 🔧 Techniques
- Graph-based collaborative filtering
- Graph construction with NetworkX or PyG
- Optionally: Personalized recommendations using user embeddings

### 💡 Next Steps
- Add GCN or GraphSAGE for link prediction
- Visualize user/movie embeddings
- Use real MovieLens 100k or 1M datasets

---

## 🚀 Future Improvements
- Use GATConv for improved performance
- Switch to a real social media graph (e.g., Reddit, Facebook)
- Try link prediction tasks using `torch_geometric.nn.LinkPredictor`
- Add t-SNE or PCA to visualize learned node embeddings

---

## 🗂 Folder Structure

