"""
Debug script to check vector store contents.
"""
from pathlib import Path
from qdrant_client import QdrantClient

def debug_vectorstore():
    db_path = Path("data/qdrant_db_multi_subject")
    
    print("=" * 60)
    print("Vector Store Debug")
    print("=" * 60)
    
    # Check if DB exists
    if not db_path.exists():
        print(f"❌ Database not found at {db_path}")
        return
    
    print(f"✓ Database found at {db_path}")
    
    # Connect
    client = QdrantClient(path=str(db_path))
    
    # List collections
    collections = client.get_collections()
    print(f"\n📚 Collections found: {len(collections.collections)}")
    for col in collections.collections:
        print(f"  - {col.name}")
    
    # Check our collection
    collection_name = "textbook_content_multi_subject"
    try:
        collection_info = client.get_collection(collection_name)
        print(f"\n✓ Collection '{collection_name}' found")
        print(f"  Vector count: {collection_info.points_count}")
        print(f"  Vector size: {collection_info.config.params.vectors.size}")
        
        # Try to get a sample point
        points = client.scroll(
            collection_name=collection_name,
            limit=1
        )
        
        if points[0]:
            sample = points[0][0]
            print(f"\n📄 Sample document:")
            print(f"  ID: {sample.id}")
            print(f"  Payload keys: {list(sample.payload.keys())}")
            
            # Check structure
            if 'page_content' in sample.payload:
                print(f"  Text preview: {sample.payload['page_content'][:100]}...")
            
            if 'metadata' in sample.payload:
                print(f"  Metadata: {sample.payload['metadata']}")
        
    except Exception as e:
        print(f"\n❌ Error checking collection: {e}")
    
    client.close()
    print("\n" + "=" * 60)

if __name__ == "__main__":
    debug_vectorstore()