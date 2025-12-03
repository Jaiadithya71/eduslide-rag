# Data Directory

## Required Files (Not in Repository)

Due to size limitations, these files are not included in the repository:

### 1. Vector Database (~500MB compressed)
- **Download**: [Google Drive Link]
- **Extract to**: `qdrant_db_multi_subject/`
- **Contents**: Pre-computed vector embeddings of all textbooks

### 2. Extracted Images (~200MB)
- **Download**: [Google Drive Link]
- **Extract to**: `extracted_images/`
- **Contents**: Images extracted from PDFs, organized by subject

### 3. Source PDFs (Optional, ~100MB)
- **Download**: [Google Drive Link]
- **Extract to**: `pdfs/`
- **Contents**: Original textbook PDFs

## Directory Structure After Download
```
data/
├── qdrant_db_multi_subject/
│   ├── collections/
│   ├── meta.json
│   └── ...
├── extracted_images/
│   ├── gees/
│   ├── gemh/
│   ├── gepr/
│   ├── ghml/
│   └── hesc/
└── pdfs/
    ├── gees/
    ├── gemh/
    └── ...
```

## Verification

After downloading, verify the setup:
```bash
python scripts/verify_data.py
```