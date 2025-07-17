@echo off
REM ============================================
REM Book Catalog API - Full Flow Test Script (.bat)
REM --------------------------------------------
REM This script:
REM 1️⃣ Deletes all existing books
REM 2️⃣ Creates Book One, extracts ID
REM 3️⃣ Lists all books
REM 4️⃣ Updates Book One
REM 5️⃣ Creates Book Two, extracts ID
REM 6️⃣ Lists all books
REM 7️⃣ Deletes Book One
REM 8️⃣ Lists all books (final check)
REM
REM Requirements:
REM - FastAPI server running at http://127.0.0.1:8000
REM - curl (Windows 10+ has curl.exe)
REM - Python installed (to parse JSON)
REM ============================================

setlocal enabledelayedexpansion
set API_URL=http://127.0.0.1:8000

echo Cleaning up all existing books...
for /f %%i in ('curl -s %API_URL%/books/ ^| python -c "import sys, json; [print(b['id']) for b in json.load(sys.stdin)]"') do (
    curl -s -X DELETE %API_URL%/books/%%i >nul
)


echo Creating Book One...
for /f %%i in ('curl -s -X POST %API_URL%/books/ -H "Content-Type: application/json" -d "{\"title\":\"Book One\",\"author\":\"Shehroz First\",\"published_year\":2020}" ^| python -c "import sys, json; print(json.load(sys.stdin)['id'])"') do set BOOK_ONE_ID=%%i
echo ✅ Book One ID: %BOOK_ONE_ID%

echo Getting all books...
curl -s %API_URL%/books/
echo.

echo Updating Book One...
curl -s -X PUT %API_URL%/books/%BOOK_ONE_ID% -H "Content-Type: application/json" -d "{\"title\":\"Book One Updated\",\"author\":\"Shehroz Updated\",\"published_year\":2021,\"summary\":\"Updated summary\"}"
echo.

echo Creating Book Two...
for /f %%i in ('curl -s -X POST %API_URL%/books/ -H "Content-Type: application/json" -d "{\"title\":\"Book Two\",\"author\":\"Shehroz Second Test\",\"published_year\":2022}" ^| python -c "import sys, json; print(json.load(sys.stdin)['id'])"') do set BOOK_TWO_ID=%%i
echo ✅ Book Two ID: %BOOK_TWO_ID%

echo Getting all books...
curl -s %API_URL%/books/
echo.

echo Deleting Book One...
curl -s -X DELETE %API_URL%/books/%BOOK_ONE_ID%
echo.

echo Getting all books (final check)...
curl -s %API_URL%/books/
echo.

echo 🎉 Flow test completed!
pause
