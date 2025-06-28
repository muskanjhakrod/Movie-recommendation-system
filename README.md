# 🎬 Movie Recommendation System

This is my first Machine Learning project — a **Content-Based Movie Recommender System** built using Python, Jupyter Notebook, and Streamlit for the frontend.

It recommends movies based on the one you select using cosine similarity of genres, keywords, etc. I'm currently learning machine learning and this is my first step toward building intelligent applications.

---

## 💡 Features

- Recommend 5 similar movies based on a selected movie
- Uses content-based filtering
- Simple and clean Streamlit interface
- Poster images fetched via OMDB API

---

## 🛠 Technologies Used

- Python 🐍
- Pandas & NumPy
- Scikit-learn (Cosine Similarity)
- Streamlit (Frontend)
- OMDB API (for fetching posters)

---

## 📁 Project Structure

movie_recommendation_system/
├── recommandation_web/
│ ├── app.py # Streamlit frontend
│ ├── movies.pkl # Pickled movie dataframe
├── recom_sys.ipynb # Jupyter notebook for model building
├── requirements.txt # Python dependencies
└── README.md # Project description

---

## 🔗 Dataset Links (from Kaggle)

You need the following datasets to run the notebook:

- [tmdb_5000_movies.csv](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- [tmdb_5000_credits.csv](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

📥 Download both CSV files and place them in your project folder.  
🧠 Then, run `recom_sys.ipynb` to generate `movies.pkl` and `similarity.pkl`.

---

## ⚙️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/movie_recommendation_system.git
cd movie_recommendation_system 
```
### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```bash
streamlit run recommandation_web/app.py
```

⚠️ Make sure movies.pkl and similarity.pkl exist before running app.py.
If not, run recom_sys.ipynb to generate them.

### 👩‍💻 About Me
I'm Muskan, a Computer Science student learning Python and ML.
This is just the beginning of my journey in AI/ML and web development. 🌱
