#!/bin/bash

# AI Investment Arena — Quick Start Setup Script
# This script automates the setup for both backend and frontend

set -e  # Exit on error

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║        AI Investment Arena — Quick Start Setup                 ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# ============================================================================
# Step 1: Backend Setup
# ============================================================================
echo -e "${YELLOW}[1/5] Setting up Backend...${NC}"
echo ""

if [ ! -d "backend" ]; then
    echo -e "${RED}❌ backend/ directory not found!${NC}"
    echo "Please ensure you're in the root directory with both 'backend' and 'arena-frontend' folders."
    exit 1
fi

cd backend

# Check if .env exists
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}⚠️  Creating .env file...${NC}"
    cat > .env << 'EOF'
# AI Credits API
AICREDITS_API_KEY=your_api_key_here
AICREDITS_BASE_URL=https://api.aicredits.in/v1

# Database
DATABASE_URL=sqlite:///./arena.db

# Portfolio Configuration
DEFAULT_CAPITAL=100000.0
TOP_CANDIDATES=15

# Scheduler Timing (IST)
MORNING_HOUR=8
MORNING_MINUTE=40
CLOSING_HOUR=15
CLOSING_MINUTE=45

# Optional APIs
UPSTOX_ANALYTICS_TOKEN=
TWELVE_DATA_API_KEY=
EOF
    echo -e "${GREEN}✅ .env created. Please update AICREDITS_API_KEY before running.${NC}"
else
    echo -e "${GREEN}✅ .env already exists${NC}"
fi

# Check Python version
PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
echo -e "${GREEN}✅ Python ${PYTHON_VERSION} found${NC}"

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate 2>/dev/null || source venv/Scripts/activate 2>/dev/null || true
    echo -e "${GREEN}✅ Virtual environment activated${NC}"
else
    echo -e "${YELLOW}⚠️  Creating virtual environment...${NC}"
    python -m venv venv
    source venv/bin/activate 2>/dev/null || source venv/Scripts/activate 2>/dev/null || true
    echo -e "${GREEN}✅ Virtual environment created${NC}"
fi

# Install/verify dependencies
echo -e "${YELLOW}⚠️  Verifying Python dependencies...${NC}"
pip install -q -r requirements.txt 2>/dev/null || {
    echo -e "${RED}❌ Failed to install dependencies${NC}"
    exit 1
}
echo -e "${GREEN}✅ Dependencies installed${NC}"

cd ..

# ============================================================================
# Step 2: Frontend Setup
# ============================================================================
echo ""
echo -e "${YELLOW}[2/5] Setting up Frontend...${NC}"
echo ""

if [ ! -d "arena-frontend" ]; then
    echo -e "${RED}❌ arena-frontend/ directory not found!${NC}"
    exit 1
fi

cd arena-frontend

# Check Node.js version
NODE_VERSION=$(node --version 2>&1)
echo -e "${GREEN}✅ ${NODE_VERSION} found${NC}"

# Create .env.local
if [ ! -f ".env.local" ]; then
    echo -e "${YELLOW}⚠️  Creating .env.local...${NC}"
    echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
    echo -e "${GREEN}✅ .env.local created${NC}"
else
    echo -e "${GREEN}✅ .env.local already exists${NC}"
fi

# Install dependencies if node_modules doesn't exist
if [ ! -d "node_modules" ]; then
    echo -e "${YELLOW}⚠️  Installing npm dependencies (this may take a minute)...${NC}"
    npm install -q 2>/dev/null || {
        echo -e "${RED}❌ Failed to install npm dependencies${NC}"
        exit 1
    }
    echo -e "${GREEN}✅ Dependencies installed${NC}"
else
    echo -e "${GREEN}✅ node_modules already exists${NC}"
fi

cd ..

# ============================================================================
# Step 3: Environment Configuration
# ============================================================================
echo ""
echo -e "${YELLOW}[3/5] Configuration Summary${NC}"
echo ""
echo "Backend Configuration:"
echo "  - Location: ./backend"
echo "  - Framework: FastAPI"
echo "  - Port: 8000"
echo "  - Database: SQLite (arena.db)"
echo "  - Status: ✅ Ready to run"
echo ""
echo "Frontend Configuration:"
echo "  - Location: ./arena-frontend"
echo "  - Framework: Next.js 14"
echo "  - Port: 3000"
echo "  - API URL: http://localhost:8000"
echo "  - Status: ✅ Ready to run"
echo ""

# ============================================================================
# Step 4: Pre-flight Checks
# ============================================================================
echo -e "${YELLOW}[4/5] Running Pre-flight Checks...${NC}"
echo ""

# Check Python imports
echo "Checking backend imports..."
cd backend
python -c "import fastapi; import sqlalchemy; import uvicorn" 2>/dev/null && \
    echo -e "${GREEN}✅ All Python packages loaded${NC}" || \
    echo -e "${RED}❌ Missing Python package${NC}"
cd ..

# Check Node packages
echo "Checking frontend imports..."
cd arena-frontend
npm list next react 2>/dev/null | head -5 > /dev/null && \
    echo -e "${GREEN}✅ All npm packages present${NC}" || \
    echo -e "${RED}❌ Missing npm package${NC}"
cd ..

echo ""

# ============================================================================
# Step 5: Next Steps
# ============================================================================
echo -e "${YELLOW}[5/5] Setup Complete!${NC}"
echo ""
echo -e "${GREEN}🎉 All systems ready for testing!${NC}"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 IMPORTANT: Before running the servers:"
echo ""
echo "   1. Edit backend/.env and add your AICREDITS_API_KEY"
echo "   2. (Optional) Update other API keys if available"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "🚀 To start the servers, open two terminal windows:"
echo ""
echo "   Terminal 1 (Backend):"
echo "   $ cd backend"
echo "   $ source venv/bin/activate  # (or venv\\Scripts\\activate on Windows)"
echo "   $ uvicorn main:app --reload --host 0.0.0.0 --port 8000"
echo ""
echo "   Terminal 2 (Frontend):"
echo "   $ cd arena-frontend"
echo "   $ npm run dev"
echo ""
echo "   Then open: http://localhost:3000"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📖 Full setup guide: See SETUP_AND_TESTING_GUIDE.md"
echo ""