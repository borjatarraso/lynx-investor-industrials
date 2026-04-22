# Development Guide

## Architecture

The application follows the shared Lince Investor Suite architecture with
industrials-specific adaptations. Cross-agent plumbing lives in the
`lynx-investor-core` package; only sector-specific logic lives here.

### Data Flow

```
User Input (ticker/ISIN/name)
    ↓
CLI/Interactive/TUI/GUI → cli.py
    ↓
analyzer.py: run_progressive_analysis()
    ↓
ticker.py: resolve_identifier() → (ticker, isin)
    ↓
storage.py: check cache → return if cached
    ↓
fetcher.py: yfinance data (profile + financials)
    ↓
models.py: classify_stage / classify_segment / classify_jurisdiction
    ↓
analyzer.py: _validate_sector (industrials gate)
    ↓
calculator.py: calc_valuation / profitability / solvency / growth / efficiency
    ↓
calculator.py: calc_share_structure + calc_business_quality
    ↓
calculator.py: calc_market_intelligence (insider, analyst, short, technicals, XLI + peer ETF)
    ↓
calculator.py: calc_intrinsic_value
    ↓
[parallel] reports.py + news.py
    ↓
conclusion.py: generate_conclusion() → verdict + industrials screening
    ↓
storage.py: save_analysis_report()
    ↓
display.py / tui/app.py / gui/app.py → render
```

### Key Design Decisions

1. **Stage > Tier**: Industrial operator maturity is the primary analysis
   axis, not market-cap tier. Mature industrial franchises (CAT, HON, UNP)
   and emerging industrial-tech upstarts demand entirely different metric
   sets.

2. **Cyclical Tagging**: Business-quality scoring does **not** penalize
   cyclical sub-segments (airlines, shipping, trucking, heavy construction)
   — it simply surfaces the exposure as a qualitative tag so investors can
   size positions appropriately. Aerospace & defense primes and commercial
   services are tagged as low cyclical sensitivity.

3. **Lease-Adjusted Leverage**: Airlines, trucking, and marine shipping
   have material off-balance-sheet lease commitments (aircraft, trailers,
   vessels). We capitalize rent at 8× and include it in a lease-adjusted
   Debt/EBITDAR ratio alongside the raw Debt/EBITDA.

4. **Relevance-Driven Display**: All 4 UI modes use `get_relevance()` to
   determine which metrics to highlight, dim, or hide. For industrial
   operators this means ROIC, operating ratio, book-to-bill, and backlog
   growth stay Critical across mature stages, while cash runway only
   surfaces for Early Stage / Emerging operators.

5. **Organic-Growth Proxy**: Most filings don't expose organic growth
   directly. We approximate by subtracting asset growth from revenue
   growth — positive values indicate same-base productivity gains rather
   than M&A- or capacity-driven growth, a key distinction for industrial
   roll-ups.

6. **Book-to-Bill / Backlog Proxies**: Where reported backlog and order
   intake are not disclosed, we use inventory-growth direction as a
   directional forward-revenue-visibility signal. Users analyzing A&D
   primes or E&C contractors should always consult the actual filings for
   hard backlog figures.

7. **Industrials Disclaimers**: Every analysis includes stage-specific
   risk disclosures around end-market cyclicality, backlog quality,
   input-cost inflation, supply-chain disruption, and program-execution
   risk.

### Adding New Metrics

1. Add field to the appropriate dataclass in `models.py`
2. Calculate in `calculator.py` (in the relevant `calc_*` function)
3. Add relevance entry in `relevance.py` (_STAGE_OVERRIDES and tier tables)
4. Add explanation in `explanations.py`
5. Add display row in `display.py`, `tui/app.py`, `gui/app.py`

### Adding New Industrials Sub-Segments

1. Add to `Segment` enum in `models.py`
2. Add keywords to `_SEGMENT_KEYWORDS`
3. Add sector-ETF mapping in `_INDUSTRIAL_PROXIES` in `calculator.py`
4. Classify cyclicality in `_MILDLY_CYCLICAL_SEGMENTS`,
   `_MODERATELY_CYCLICAL_SEGMENTS`, or `_HIGHLY_CYCLICAL_SEGMENTS` in
   `calculator.py`
5. Add industry insight in `sector_insights.py`

### Adding New Stages

1. Add to `CompanyStage` enum
2. Add keywords to `_STAGE_KEYWORDS`
3. Add weights to `_WEIGHTS` in `conclusion.py`
4. Add relevance overrides in `relevance.py`

## Running Tests

```bash
# Python unit tests
pytest tests/ -v --tb=short

# Robot Framework (requires robotframework)
pip install robotframework
robot --outputdir results robot/

# Syntax check all files
python -c "import py_compile, glob; [py_compile.compile(f, doraise=True) for f in glob.glob('lynx_industrials/**/*.py', recursive=True)]"
```

## Code Style

- Python 3.10+ with type hints
- Dataclasses for all data models
- Rich for console rendering
- Textual for TUI
- Tkinter for GUI
