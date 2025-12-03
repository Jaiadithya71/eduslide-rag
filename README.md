# EduSlide RAG System

A Retrieval-Augmented Generation (RAG) system for educational content from multiple textbooks.

## 📁 Project Structure
```
eduslide-rag/
├── data/
│   ├── qdrant_db_multi_subject/  # Vector database (~12.6 MB)
│   ├── extracted_images/          # Images from PDFs
│   └── pdfs/                      # Source PDFs
├── src/
│   ├── load_vectorstore.py       # Vector store loader
│   └── query_system.py           # Interactive query system
├── notebooks/
│   └── QdrantClient.ipynb        # Original processing notebook
├── .gitignore
├── requirements.txt
└── README.md
```

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone <your-repo-url>
cd eduslide-rag
```

### 2. Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run Query System
```bash
python src/query_system.py
```

## 📊 Data Details

- **Total Documents**: 1,164 pages with images
- **Subjects**: Geography (GEES), Mathematics (GEMH), Programming (GEPR), ML (GHML), Science (HESC)
- **Vector Dimensions**: 384 (sentence-transformers/all-MiniLM-L6-v2)
- **Total Size**: ~12.6 MB (all files included)

## 🔍 Usage Example
```python
from src.load_vectorstore import VectorStoreLoader

# Load vector store
loader = VectorStoreLoader("./data/qdrant_db_multi_subject")
loader.initialize()

# Search
results = loader.search("What are geographical divisions of India?")

# Display results
for result in results:
    print(f"{result['source']}: {result['text'][:100]}...")
```

## 📝 Notes

- First run downloads the embedding model (~90MB)
- GPU recommended but not required
- All data files are included in the repository

## 🤝 Contributing

This is an educational project. Feel free to fork and modify!

## 📄 License

MIT License - See LICENSE file for details