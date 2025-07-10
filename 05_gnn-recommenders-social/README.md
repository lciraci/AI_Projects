# 05_gnn-recommenders-social

This folder contains two projects using Graph Neural Networks (GNNs) for real-world applications:

---

## 📘 1. User-Movie Recommendation System

A GNN-based collaborative filtering system built on the [MovieLens 100k](https://grouplens.org/datasets/movielens/) dataset.

**Key Features:**
- Bipartite graph (users ↔ movies)
- GCN for link prediction
- Cosine embedding loss
- Top-K movie recommendations per user
- Visualization with NetworkX

📓 Notebook: `User_movie_Reccomandation_System.ipynb`

---

## 📘 2. Social Network Analysis with GNN

A node classification project using **Zachary’s Karate Club** social graph dataset.

**Key Features:**
- Semi-supervised GCN
- Predicts community membership
- Visualizes learned communities
- One-hot encoded features + simple GCN model

📓 Notebook: `GNN_Based_Social_Network_Analysis.ipynb`

