# Institutional AI/LLM Capabilities Catalog

This document registers all AI and LLM features integrated into the Indian Stock Analysis AI Workstation. Every execution routes through the provider-agnostic model routing layer defined in [llm_config.py](file:///c:/Users/dheer/Desktop/AI/indian-stock-analyzer/backend/llm_config.py).

---

## 📋 Feature & Subfeature AI Mapping

### 1. Portfolio Management & Optimization
*   **AI Rebalancing Advisory**
    *   **Subfeature**: Portfolio Stress Testing & Optimization
    *   **Endpoint**: `POST /api/portfolio/stress-test` (Invokes `call_llm` with `TASK_FAST`)
    *   **Function**: Generates quantitative and tactical rebalancing commentary based on Sharpe ratio optimization runs.
*   **AI Portfolio Doctor**
    *   **Subfeature**: Custom Portfolio Review & Health Diagnostics
    *   **Source File**: `backend/agent.py` (Invokes `call_llm` with `TASK_HEAVY`)
    *   **Function**: Performs expert review of the portfolio weight allocations, HHI concentration risks, and proposes trade tickets.
*   **AI Backtest Performance Synthesis**
    *   **Subfeature**: Historical Simulation Attribution Analysis
    *   **Source File**: `backend/agent.py` (Invokes `call_llm` with `TASK_HEAVY`)
    *   **Function**: Interprets maximum drawdowns, transaction drag, and attributes alpha compared to Nifty 50.

### 2. Equity Research Terminal
*   **CIO Strategic Investment Thesis**
    *   **Subfeature**: Single Stock Core Analysis Boot-up
    *   **Source File**: `backend/agent.py` (Invokes `call_llm` with `TASK_HEAVY`)
    *   **Function**: Consolidates DCF intrinsic margin of safety, sector momentum, and generates target entry ranges.
*   **CFA & Technical Prospectus**
    *   **Subfeature**: Multi-Agent Single Stock Deeper Drill-down
    *   **Source File**: `backend/agent.py` (Invokes `call_llm` with `TASK_HEAVY`)
    *   **Function**: Triggers a simulated multi-agent breakdown for corporate governance and technician timing indicators.
*   **Investment Committee Memo (Pitchbook)**
    *   **Subfeature**: Corporate Catalysts & Deal Pitchbook Generation
    *   **Endpoint**: `GET /api/analyze/pitchbook` (Invokes `call_llm` with `TASK_FAST`)
    *   **Function**: Generates a print-ready Investment Committee Memo parsing peer multiples and significant corporate block deals.

### 3. Market Regime & News Feed
*   **AI Sector Rotational Commentary**
    *   **Subfeature**: Macro Cap and Horizon Sector Radar Analysis
    *   **Source File**: `backend/main.py` (Invokes `call_llm` with `TASK_FAST`)
    *   **Function**: Synthesizes relative strength regimes of the NSE sector indices under active filters.
*   **AI News Sentiment & Price Anomaly Audit**
    *   **Subfeature**: Corporate Catalysts Sentiment auditing
    *   **Source File**: `backend/main.py` (Invokes `call_llm` with `TASK_FAST`)
    *   **Function**: Correlates live-scraped articles cleaned via Jina Reader against price anomalies.

### 4. Technical Indicators & Charting
*   **Custom Indicator AI Insights**
    *   **Subfeature**: Technical Chart indicator summaries
    *   **Endpoint**: `GET /api/chart/indicator-synthesis` (Invokes `call_llm` with `TASK_FAST`)
    *   **Function**: Compiles professional technical analysis summaries of active charting channels (LuxAlgo, SMC, Maxwell).

### 5. Smart Scanner & Rule Builder
*   **AI Natural Language Scan Command Station**
    *   **Subfeature**: Plain English Scanning Query Parser
    *   **Endpoint**: `POST /api/screener/parse-nl-scan` (Invokes `call_llm` with `TASK_FAST`)
    *   **Function**: Translates plain English prompt triggers into SQL filtering rules and indicators.
*   **AI Screener Scan Synthesis**
    *   **Subfeature**: Scan Universe summary compilation
    *   **Endpoint**: `POST /api/screener/scan-synthesis` (Invokes `call_llm` with `TASK_FAST`)
    *   **Function**: Analyzes sector clusters and technical positioning from custom scanner results.
*   **AI Natural Language Alert Builder**
    *   **Subfeature**: Plain English Alert Builder
    *   **Endpoint**: `POST /api/alerts/parse-nl` (Invokes `call_llm` with `TASK_FAST`)
    *   **Function**: Compiles plain English instructions into active stock alerts and parameters.
