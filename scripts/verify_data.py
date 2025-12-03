"""
Verify that all required data is properly downloaded and structured.
"""
import sys
from pathlib import Path

def verify_setup():
    """Verify data directory structure."""
    errors = []
    warnings = []
    
    # Check data folder
    data_dir = Path("data")
    if not data_dir.exists():
        errors.append("'data/' folder not found")
        return errors, warnings
    
    # Check vector database
    db_path = data_dir / "qdrant_db_multi_subject"
    if not db_path.exists():
        errors.append("Vector database not found at data/qdrant_db_multi_subject/")
    else:
        collections = db_path / "collections"
        if not collections.exists():
            errors.append("Database structure invalid (missing 'collections' folder)")
        print("✓ Vector database found")
    
    # Check images
    images_dir = data_dir / "extracted_images"
    if not images_dir.exists():
        warnings.append("Images folder not found (optional)")
    else:
        subjects = ['gees', 'gemh', 'gepr', 'ghml', 'hesc']
        for subject in subjects:
            subject_dir = images_dir / subject
            if subject_dir.exists():
                count = len(list(subject_dir.glob("*.jpeg"))) + len(list(subject_dir.glob("*.png")))
                print(f"✓ {subject}: {count} images found")
            else:
                warnings.append(f"Images for {subject} not found")
    
    # Check PDFs (optional)
    pdfs_dir = data_dir / "pdfs"
    if not pdfs_dir.exists():
        print("ℹ  PDFs folder not found (optional)")
    else:
        print("✓ PDFs folder found")
    
    return errors, warnings

if __name__ == "__main__":
    print("=" * 60)
    print("Data Verification")
    print("=" * 60 + "\n")
    
    errors, warnings = verify_setup()
    
    print("\n" + "=" * 60)
    if errors:
        print("\n❌ ERRORS:")
        for error in errors:
            print(f"  - {error}")
        print("\nPlease download required files from the links in data/README.md")
        sys.exit(1)
    
    if warnings:
        print("\n⚠️  WARNINGS:")
        for warning in warnings:
            print(f"  - {warning}")
    
    print("\n✓ Setup verification complete!")
    print("=" * 60)