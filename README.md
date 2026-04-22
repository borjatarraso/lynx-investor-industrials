# Lynx Industrials Analysis

> Fundamental analysis specialized for industrial-sector companies — aerospace & defense, industrial conglomerates, machinery & capital goods, electrical equipment, building products, construction & engineering, industrial distribution, air freight & logistics, railroads, airlines, trucking, marine shipping, and commercial & professional services.

Part of the **Lince Investor Suite**.

## Overview

Lynx Industrials is a comprehensive fundamental analysis tool built specifically for industrials investors. It evaluates cyclical industrial operators across all maturity stages — from emerging industrial-tech upstarts to mature Dividend Aristocrats — using industrials-specific metrics, stage-aware valuation methods, and cyclical-sensitivity assessments.

### Key Features

- **Stage-Aware Analysis**: Automatically classifies operators as Early Stage / Pre-Profit, Emerging Industrial Operator, Scaling Industrial Operator, Mature Industrial Franchise, or IP Licensor / Asset-Light — and adapts all metrics and scoring accordingly
- **Industrials-Specific Metrics**: Backlog growth, book-to-bill ratio, organic revenue growth, operating ratio (rails / LTL), FCF conversion, ROIC, capex intensity, lease-adjusted leverage, SG&A leverage, and segment operating margin proxy
- **4-Level Relevance System**: Marks each metric as Critical, Relevant, Contextual, or Irrelevant based on the operator's maturity stage
- **Market Intelligence**: Insider transactions, institutional holders, analyst consensus, short interest, price technicals with golden/death cross detection, and XLI / sub-segment ETF comparisons (ITA, IYT, JETS, XAR, PAVE, BOAT, XTN, etc.)
- **10-Point Industrials Screening Checklist**: Evaluates margin quality, ROIC, leverage, growth, dilution, insider ownership, FCF generation, and valuation discipline
- **Cyclical-Sensitivity Tagging**: Flags aerospace & defense and commercial services as low-cyclical; airlines, shipping, trucking, and heavy construction as highly cyclical
- **Sub-Segment Detection**: Automatically identifies primary industrials segment (Aerospace & Defense, Industrial Conglomerates, Machinery, Electrical Equipment, Building Products, Construction & Engineering, Trading & Distribution, Air Freight & Logistics, Railroads, Airlines, Trucking, Marine Shipping, Commercial Services, Professional Services)
- **Multiple Interface Modes**: Console CLI, Interactive REPL, Textual TUI, Tkinter GUI
- **Export**: TXT, HTML, and PDF report generation
- **Sector & Industry Insights**: Deep context for Aerospace & Defense, Industrial Conglomerates, Machinery, Electrical Equipment, Building Products, Construction & Engineering, Trading Companies & Distributors, Air Freight & Logistics, Railroads, Passenger Airlines, Ground Freight & Trucking, Marine Shipping, Commercial Services & Supplies, and Professional Services

### Target Companies

Designed for analyzing companies like:
- **Aerospace & Defense**: BA, LMT, RTX, NOC, GD, LHX, HEI, TDG, TXT, HWM
- **Industrial Conglomerates**: GE, HON, MMM, ITT
- **Machinery & Capital Goods**: CAT, DE, ITW, PCAR, CMI, DOV, OTIS, FTV, XYL
- **Electrical Equipment**: ETN, ROK, EMR, PH, AME, ROP
- **Building Products**: CARR, JCI, TT, LII, MAS, AOS, ALLE, FBIN
- **Construction & Engineering**: PWR, ACM, FIX, FLR, MTZ, EMCOR, DY, TPC
- **Trading & Distribution**: FAST, GWW, URI, WSO, MSM
- **Air Freight & Logistics**: UPS, FDX, CHRW, EXPD, ODFL, XPO
- **Railroads**: UNP, CSX, NSC, CP, CNI
- **Airlines**: DAL, UAL, LUV, AAL, ALK, JBLU
- **Trucking**: ODFL, SAIA, KNX, JBHT, LSTR, WERN
- **Marine Shipping**: KEX, MATX, ZIM, DAC, STNG
- **Commercial Services**: CTAS, RSG, WM, VRSK, ROL, CPRT, RBA
- **Professional Services**: BAH, LDOS, CACI, FCN, RHI, MAN

## Installation

```bash
# Clone the repository
git clone https://github.com/borjatarraso/lynx-investor-industrials.git
cd lynx-investor-industrials

# Install in editable mode (creates the `lynx-industrials` command)
pip install -e .
```

### Dependencies

| Package        | Purpose                              |
|----------------|--------------------------------------|
| yfinance       | Financial data from Yahoo Finance    |
| requests       | HTTP calls (OpenFIGI, EDGAR, etc.)   |
| beautifulsoup4 | HTML parsing for SEC filings         |
| rich           | Terminal tables and formatting       |
| textual        | Full-screen TUI framework            |
| feedparser     | News RSS feed parsing                |
| pandas         | Data analysis                        |
| numpy          | Numerical computing                  |

All dependencies are installed automatically via `pip install -e .`.

## Usage

### Direct Execution
```bash
# Via the runner script
./lynx-investor-industrials.py -p CAT

# Via Python
python3 lynx-investor-industrials.py -p BA

# Via pip-installed command
lynx-industrials -p LMT
```

### Execution Modes

| Flag | Mode | Description |
|------|------|-------------|
| `-p` | Production | Uses `data/` for persistent cache |
| `-t` | Testing | Uses `data_test/` (isolated, always fresh) |

### Interface Modes

| Flag | Interface | Description |
|------|-----------|-------------|
| (none) | Console | Progressive CLI output |
| `-i` | Interactive | REPL with commands |
| `-tui` | TUI | Textual terminal UI with themes |
| `-x` | GUI | Tkinter graphical interface |

### Examples

```bash
# Analyze a mega-cap machinery operator
lynx-industrials -p CAT

# Force fresh data download
lynx-industrials -p BA --refresh

# Search by company name
lynx-industrials -p "Caterpillar"

# Interactive mode
lynx-industrials -p -i

# Export HTML report
lynx-industrials -p LMT --export html

# Explain a metric
lynx-industrials --explain operating_ratio

# Skip filings and news for faster analysis
lynx-industrials -t UNP --no-reports --no-news
```

## Analysis Sections

1. **Company Profile** — Tier, operator stage, industrials sub-segment, market-exposure classification
2. **Sector & Industry Insights** — Industrials-specific context and benchmarks
3. **Valuation Metrics** — Traditional (P/E, P/FCF, EV/EBITDA, P/S, dividend yield) + industrials-specific (EV per backlog, EV per employee)
4. **Profitability Metrics** — ROE, ROIC, margins with trend, SG&A%, segment operating margin proxy, operating ratio (rails / trucking), FCF conversion
5. **Solvency & Survival** — Debt/EBITDA, lease-adjusted leverage (airlines / trucking), interest coverage, cash runway for emerging operators
6. **Growth & Capital Discipline** — Revenue / earnings growth, organic-growth proxy, book-to-bill, backlog growth, capex intensity, dilution / buyback CAGR
7. **Operating Efficiency** — Asset turnover, inventory turnover, days inventory, revenue per employee, working-capital intensity
8. **Share Structure** — Outstanding/diluted shares, insider/institutional ownership
9. **Business Quality** — Backlog / margin strength, unit economics, financial position, cyclical sensitivity, aftermarket / services mix
10. **Intrinsic Value** — DCF, Dividend Discount Model, Graham Number, Asset-Based (method selection by stage)
11. **Market Intelligence** — Analysts, short interest, technicals, insider trades, XLI / sub-segment ETF context
12. **Financial Statements** — 5-year annual summary
13. **SEC Filings** — Downloadable regulatory filings
14. **News** — Yahoo Finance + Google News RSS
15. **Assessment Conclusion** — Weighted score, verdict, strengths/risks, screening checklist
16. **Industrials Disclaimers** — Stage-specific risk disclosures

## Relevance System

Each metric is classified by importance for the operator's maturity stage:

| Level | Display | Meaning |
|-------|---------|---------|
| **Critical** | `*` bold cyan star | Must-check for this stage |
| **Relevant** | Normal | Important context |
| **Contextual** | Dimmed | Informational only |
| **Irrelevant** | Hidden | Not meaningful for this stage |

Example: For a Mature Industrial Franchise, ROIC, operating ratio, backlog growth, and Debt/EBITDA are **Critical** while Cash Runway is **Irrelevant**.

## Scoring Methodology

The overall score (0-100) is a weighted average of 5 categories, with weights adapted by both company tier AND operator stage:

| Stage                             | Valuation | Profitability | Solvency | Growth | Business Quality |
|-----------------------------------|-----------|---------------|----------|--------|------------------|
| Early Stage                       | 5%        | 5%            | 40-45%   | 15-20% | 30%              |
| Emerging Industrial Operator      | 5-10%     | 5-10%         | 30-40%   | 25%    | 25%              |
| Scaling Industrial Operator       | 10-15%    | 10-20%        | 15-35%   | 25%    | 25%              |
| Mature Industrial Franchise       | 15-20%    | 15-25%        | 10-30%   | 15-20% | 25%              |
| IP Licensor / Asset-Light         | 20%       | 30%           | 10%      | 15%    | 25%              |

Verdicts: Strong Buy (>=75), Buy (>=60), Hold (>=45), Caution (>=30), Avoid (<30).

## Project Structure

```
lynx-investor-industrials/
├── lynx-investor-industrials.py       # Runner script
├── pyproject.toml                          # Build configuration
├── requirements.txt                        # Dependencies
├── img/                                    # Logo images
├── data/                                   # Production cache
├── data_test/                              # Testing cache
├── docs/                                   # Documentation
│   └── API.md                              # API reference
├── robot/                                  # Robot Framework tests
│   ├── cli_tests.robot
│   ├── api_tests.robot
│   └── export_tests.robot
├── tests/                                  # Unit tests
└── lynx_industrials/                       # Main package
```

## Testing

```bash
# Unit tests
pytest tests/ -v

# Robot Framework acceptance tests
robot robot/
```

## License

BSD 3-Clause License. See LICENSE in source.

## Author

**Borja Tarraso** — borja.tarraso@member.fsf.org
