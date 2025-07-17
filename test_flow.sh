#!/bin/bash

# ============================================
# Book Catalog API - Full Flow Test Script (.sh)
# --------------------------------------------
# This script:
# 1️⃣ Deletes all existing books
# 2️⃣ Creates Book One, extracts ID
# 3️⃣ Lists all books
# 4️⃣ Updates Book One
# 5️⃣ Creates Book Two, extracts ID
# 6️⃣ Lists all books
# 7️⃣ Deletes Book One
# 8️⃣ Lists all books (final check)
#
# Requirements:
# - FastAPI server running at http://127.0.0.1:8000
# - curl installed
# - Python installed (for JSON parsing)
# ============================================

API_URL="http://127.0.0.1:8000"

echo "🚀 Cleaning up all existing books..."
BOOK_IDS=$(curl -s $API_URL/books/ | python -c "import sys, json; print(' '.join(str(b['id']) for b in json.load(sys.stdin)))")
for id in $BOOK_IDS; do
    curl -s -X DELETE $API_URL/books/$id > /dev/null
done
echo "✅ All books deleted."

echo "1️⃣ Creating Book One..."
BOOK_ONE_ID=$(curl -s -X POST $API_URL/books/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Book One","author":"Shehroz First","published_year":2020}' | \
  python -c "import sys, json; print(json.load(sys.stdin)['id'])")
echo "✅ Book One ID: $BOOK_ONE_ID"

echo "2️⃣ Getting all books..."
curl -s $API_URL/books/
echo

echo "3️⃣ Updating Book One..."
curl -s -X PUT $API_URL/books/$BOOK_ONE_ID \
  -H "Content-Type: application/json" \
  -d '{"title":"Book One Updated","author":"Shehroz Updated","published_year":2021,"summary":"Updated summary"}'
echo

echo "4️⃣ Creating Book Two..."
BOOK_TWO_ID=$(curl -s -X POST $API_URL/books/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Book Two","author":"Shehroz Second Test","published_year":2022}' | \
  python -c "import sys, json; print(json.load(sys.stdin)['id'])")
echo "✅ Book Two ID: $BOOK_TWO_ID"

echo "5️⃣ Getting all books..."
curl -s $API_URL/books/
echo

echo "6️⃣ Deleting Book One..."
curl -s -X DELETE $API_URL/books/$BOOK_ONE_ID
echo

echo "7️⃣ Getting all books (final check)..."
curl -s $API_URL/books/
echo

echo "🎉 Flow test completed!"
