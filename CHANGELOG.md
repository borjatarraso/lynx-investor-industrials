# Changelog

## [4.0] - 2026-04-23

Part of **Lince Investor Suite v4.0** coordinated release.

### Added
- URL-safety enforcement for every RSS-sourced news URL and every
  `webbrowser.open(...)` site — powered by
  `lynx_investor_core.urlsafe`.
- Sector-specific ASCII art in easter-egg visuals (replaces the shared
  pickaxe motif that leaked into non-mining sectors).

### Changed
- Aligned every user-visible sector string with the package's real
  sector: titles, subtitles, app class names, splash taglines, news
  keywords, User-Agent headers, themes, export headers, and fortune
  quotes no longer carry template leftovers.
- Depends on `lynx-investor-core>=4.0`.

All notable changes to **Lynx Industrials Analysis** are documented here.

## [3.0] - 2026-04-22

Part of **Lince Investor Suite v3.0** coordinated release.

### Added
- Uniform PageUp / PageDown navigation across every UI mode (GUI, TUI,
  interactive, console). Scrolling never goes above the current output
  in interactive and console mode; Shift+PageUp / Shift+PageDown remain
  reserved for the terminal emulator's own scrollback.
- Sector-mismatch warning now appends a `Suggestion: use
  'lynx-investor-<other>' instead.` line sourced from
  `lynx_investor_core.sector_registry`. The original warning text is
  preserved as-is.

### Changed
- TUI wires `lynx_investor_core.pager.PagingAppMixin` and
  `tui_paging_bindings()` into the main application.
- Graphical mode binds `<Prior>` / `<Next>` / `<Control-Home>` /
  `<Control-End>` via `bind_tk_paging()`.
- Interactive mode pages long output through `console_pager()` /
  `paged_print()`.
- Depends on `lynx-investor-core>=2.0`.

## [1.0] — 2026-04-22

Initial release as a standalone agent in the Lince Investor Suite. Forked
from `lynx-investor-consumer-staples` (shared plumbing in
`lynx-investor-core`) and specialized for industrial-sector companies.

### Added — Industrials Fundamental Analysis

- **Sector validator** restricts analysis to industrials (GICS:
  "Industrials" in Yahoo Finance taxonomy) companies, with allow-lists
  for aerospace & defense, industrial conglomerates, machinery & capital
  goods, electrical equipment, building products, construction &
  engineering, industrial distribution, rental & leasing, air freight &
  logistics, railroads, airlines, trucking, marine shipping, and
  commercial & professional services.
- **Stage classifier** labels operators Early Stage / Pre-Profit, Emerging
  Industrial Operator, Scaling Industrial Operator, Mature Industrial
  Franchise, or IP Licensor / Asset-Light based on revenue scale,
  operating margin, and description heuristics.
- **Sub-segment classifier** maps companies to Aerospace & Defense,
  Industrial Conglomerates, Machinery & Capital Goods, Electrical
  Equipment, Building Products, Construction & Engineering, Trading
  Companies & Distributors, Air Freight & Logistics, Railroads,
  Passenger Airlines, Trucking & Ground Freight, Marine Shipping,
  Commercial Services & Supplies, or Professional Services.
- **Market-exposure tier** measures geographic revenue-concentration risk
  (developed / mixed / high concentration).
- **Industrials-specific metrics**:
  - Gross margin trend (expanding / stable / compressing)
  - Organic-growth proxy (revenue growth minus asset growth)
  - Book-to-bill ratio proxy and backlog growth (from inventory / revenue delta)
  - Operating ratio (opex / revenue) — hallmark metric for rails and LTL
  - FCF conversion (FCF / net income) — capex-discipline signal
  - Lease-adjusted leverage (Debt + 8× rent) / EBITDAR — airlines, trucking, shipping
  - SG&A as % of revenue (overhead intensity)
  - Segment operating-margin proxy
  - Inventory turnover + days inventory
  - Working-capital intensity
  - Revenue per employee
  - CAPEX intensity, R&D intensity
  - EV per backlog, EV per employee (valuation anchors)
- **Business-quality scoring** over five dimensions:
  - Backlog / margin resilience (25 pts) — industrials-calibrated
    thresholds (>45% premium / 30-45% strong / 20-30% moderate)
  - Unit economics — ROIC + operating margin (25 pts)
  - Financial position — leverage + liquidity (20 pts)
  - Management alignment — insider ownership (15 pts)
  - Capital discipline — dilution / buybacks (15 pts)
- **Cyclical-sensitivity tagging** distinguishes defensive industrials
  (aerospace & defense primes, commercial / professional services,
  industrial conglomerates) from moderately cyclical (machinery, rails,
  building products, distribution) and highly cyclical (airlines,
  shipping, trucking, heavy construction).
- **10-point industrials screening checklist**: positive operating
  margin, gross margin ≥ 30%, ROIC > 10%, reasonable leverage, revenue
  growth > 3%, low dilution (< 3%/yr), insider ownership ≥ 5%, positive
  FCF margin, reasonable P/E (< 25), developed-market exposure.
- **Stage-appropriate intrinsic-value methods**: DCF through-cycle +
  mid-cycle EV/EBITDA comps for mature franchises; EV/EBITDA peer comps
  for scaling; EV/Revenue with margin ramp for emerging; DCF on royalty
  stream for IP licensors.
- **Sector context** now fetches the Industrial Select Sector SPDR
  (XLI) as the broad demand proxy, plus a sub-segment peer ETF (ITA for
  aerospace & defense, IYT / XTN for transports, JETS for airlines,
  ITB for building products, PAVE for infrastructure, BOAT for marine
  shipping).
- **Industrials disclaimers** cover end-market cyclicality, backlog
  quality (cancellations, escalators, concentration), input-cost
  inflation (steel, aluminium, copper, semiconductors, fuel), labour
  and supply-chain disruption, and program-execution risk.

### Changed

- `CompanyStage` enum string values updated: `GRASSROOTS="Early Stage / Pre-Profit"`,
  `EXPLORER="Emerging Industrial Operator"`, `DEVELOPER="Scaling Industrial Operator"`,
  `PRODUCER="Mature Industrial Franchise"`, `ROYALTY="IP Licensor / Asset-Light"`.
- `Segment` enum redefined with industrials sub-segments (Aerospace & Defense,
  Industrial Conglomerates, Machinery, Electrical Equipment, Building
  Products, Construction & Engineering, Trading & Distribution, Air
  Freight & Logistics, Railroads, Airlines, Trucking, Marine Shipping,
  Commercial Services, Professional Services).
- `BusinessQualityIndicators` re-tuned for industrials — cyclical-
  sensitivity tag, backlog-strength thresholds calibrated for industrial
  gross margins, aftermarket / services mix indicator.
- Scoring weights rebalanced: mature / IP-licensor operators weight
  profitability and business quality at 25% each; emerging / early-stage
  operators keep solvency + growth dominance.
- All sector insights, metric explanations, and peer examples rewritten
  for industrials context (CAT, DE, BA, LMT, HON, MMM, UNP, UPS, etc.).

### Infrastructure

- Shared plumbing continues to come from `lynx-investor-core` (storage,
  sector gate, ticker resolution, logo, about, easter-egg renderer).
