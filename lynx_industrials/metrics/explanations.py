"""Metric explanations for Lynx Industrials Analysis."""

from __future__ import annotations
from lynx_industrials.models import MetricExplanation

METRIC_EXPLANATIONS: dict[str, MetricExplanation] = {}


def _add(key, full_name, description, why_used, formula, category):
    METRIC_EXPLANATIONS[key] = MetricExplanation(
        key=key, full_name=full_name, description=description,
        why_used=why_used, formula=formula, category=category,
    )


# Valuation
_add("pe_trailing", "Price-to-Earnings Ratio (TTM)",
     "Compares stock price to trailing 12-month earnings per share.",
     "Primary industrials valuation metric. Quality compounders (HON, "
     "MMM, CAT, DE) trade in the 18-25x range through cycle; airlines "
     "and heavy machinery swing from <8x trough to >20x peak.",
     "P/E = Price / EPS (TTM)", "valuation")
_add("pe_forward", "Forward P/E",
     "Price divided by consensus forward earnings.",
     "Forward-looking comparable. Useful when current earnings are "
     "depressed by cyclical downturns, program cost overruns, or "
     "tariff-driven margin compression.",
     "Forward P/E = Price / Forward EPS", "valuation")
_add("pb_ratio", "Price-to-Book Ratio",
     "Compares stock price to book value per share.",
     "Relevant for asset-heavy industrials (rails, airlines, marine "
     "shipping, heavy machinery, E&C); less informative for asset-light "
     "services (commercial / professional services) where value sits in "
     "contracts and relationships.",
     "P/B = Price / Book Value per Share", "valuation")
_add("ps_ratio", "Price-to-Sales Ratio",
     "Compares stock price to revenue per share.",
     "Useful anchor for emerging industrial operators and for cyclical "
     "names when trailing earnings are depressed. <1x is cheap for "
     "mature industrials; 3-5x often reflects premium services / IP.",
     "P/S = Market Cap / Revenue", "valuation")
_add("p_fcf", "Price-to-Free-Cash-Flow",
     "Compares market cap to free cash flow.",
     "Best valuation anchor for mature industrial operators — harder "
     "to manipulate than EPS and aligns with the capital-return profile. "
     "Target <22x for healthy mature operators.",
     "P/FCF = Market Cap / Free Cash Flow", "valuation")
_add("ev_ebitda", "Enterprise Value / EBITDA",
     "Capital-structure-neutral valuation.",
     "Preferred cross-sector comp for industrials. Quality compounders: "
     "14-18x. Machinery / building products: 10-14x. Rails: 12-15x. "
     "Airlines / shipping: trough 5x, peak >12x.",
     "EV/EBITDA = (Market Cap + Debt - Cash) / EBITDA", "valuation")
_add("ev_revenue", "Enterprise Value / Revenue",
     "EV divided by trailing revenue.",
     "Useful for emerging industrials and cross-comparing operators of "
     "similar margin profile. <1x is cheap for commodity transport / "
     "distribution; >3x requires strong margin or backlog visibility.",
     "EV/Revenue = EV / Revenue", "valuation")
_add("peg_ratio", "PEG Ratio",
     "P/E adjusted by growth rate.",
     "PEG < 1 suggests undervaluation relative to growth. Useful for "
     "scaling industrial operators; misleading for cyclicals near "
     "earnings peaks.",
     "PEG = P/E / Annual EPS Growth Rate", "valuation")
_add("dividend_yield", "Dividend Yield",
     "Annual dividend as percentage of price.",
     "Meaningful for mature industrials — many machinery, conglomerate, "
     "and aerospace primes are Dividend Aristocrats. Quality compounders "
     "yield 1.5-3% with strong dividend growth; airlines / shipping often "
     "pay no dividend or cut through downturns.",
     "Yield = Annual Dividends / Price", "valuation")
_add("earnings_yield", "Earnings Yield",
     "Inverse of P/E ratio.",
     "Compare to treasury yields for a relative-attractiveness read. "
     "Quality industrials trade at 4-6% earnings yields mid-cycle.",
     "Earnings Yield = EPS / Price", "valuation")
_add("ev_per_backlog", "EV per Backlog",
     "Enterprise value per dollar of reported backlog (when disclosed).",
     "A forward-revenue-anchored valuation for aerospace & defense primes "
     "and construction & engineering contractors, comparable across peers "
     "within the same sub-segment.",
     "EV / Reported Backlog", "valuation")
_add("ev_per_employee", "EV per Employee",
     "Enterprise value per employee.",
     "A productivity-anchored valuation for asset-light industrial "
     "services (consulting, staffing, facilities services, distribution).",
     "EV / Full-Time Employees", "valuation")
_add("price_to_tangible_book", "Price / Tangible Book",
     "Price vs tangible book value per share.",
     "Useful for asset-heavy rails, airlines, shipping, and heavy "
     "machinery; less relevant for services / IP-rich industrials "
     "dominated by goodwill and intangibles.",
     "P/TBV = Price / (Equity - Intangibles) / Shares", "valuation")
_add("cash_to_market_cap", "Cash-to-Market-Cap Ratio",
     "How much of market cap is backed by cash.",
     "Mostly relevant for emerging industrial operators. >20% can "
     "signal either hidden value or an under-leveraged balance sheet.",
     "Cash / Market Cap = Total Cash / Market Capitalization", "valuation")

# Profitability
_add("roe", "Return on Equity",
     "Profit generated per dollar of equity.",
     "Target ROE > 15% for mature industrial operators. Asset-light "
     "services and IP-rich names often exceed 25-30%.",
     "ROE = Net Income / Equity", "profitability")
_add("roa", "Return on Assets",
     "Profit per dollar of assets.",
     "ROA > 8% is strong for industrials. Asset-heavy rails and airlines "
     "naturally run lower (3-6%).",
     "ROA = Net Income / Total Assets", "profitability")
_add("roic", "Return on Invested Capital",
     "Return on all invested capital.",
     "THE core industrials quality metric. ROIC > 15% through cycle "
     "suggests a durable competitive advantage (installed base, "
     "aftermarket, brand, scale, route density).",
     "ROIC = NOPAT / Invested Capital", "profitability")
_add("gross_margin", "Gross Margin",
     "Revenue remaining after cost of goods sold.",
     "Proxy for pricing power and product differentiation. Aerospace / "
     "aftermarket: >45%. Quality machinery: 30-40%. Diversified "
     "industrials: 25-35%. Transports / distribution: 15-25%.",
     "Gross Margin = Gross Profit / Revenue", "profitability")
_add("operating_margin", "Operating Margin",
     "Revenue remaining after all operating expenses.",
     "Operating-leverage indicator. Best-in-class (ITW, TDG, HEI): >25%. "
     "Quality industrials: 15-22%. Transports (LTL / rails): 20-30%. "
     "Airlines: 5-12% mid-cycle. E&C: 5-10%.",
     "Operating Margin = Operating Income / Revenue", "profitability")
_add("net_margin", "Net Profit Margin",
     "Revenue remaining as net profit.",
     "Bottom-line profitability after interest and tax.",
     "Net Margin = Net Income / Revenue", "profitability")
_add("fcf_margin", "Free Cash Flow Margin",
     "Revenue converted to free cash flow.",
     "Measures actual cash generation that funds dividends, buybacks, "
     "and M&A. >10% is strong for mature industrials; >15% for quality "
     "aerospace / compounders.",
     "FCF Margin = FCF / Revenue", "profitability")
_add("ebitda_margin", "EBITDA Margin",
     "Revenue remaining as EBITDA.",
     "Approximates operating cash flow. >20% is healthy for quality "
     "industrials; >30% for aerospace aftermarket; <12% typical for "
     "trucking and distribution.",
     "EBITDA Margin = EBITDA / Revenue", "profitability")
_add("sga_pct_of_revenue", "SG&A as % of Revenue",
     "Selling, general, and administrative expense as a fraction of revenue.",
     "Overhead-intensity indicator. Industrial conglomerates: 10-15%. "
     "Services / distribution: 15-25%. Rising SG&A% with flat revenue "
     "is a margin-leverage warning.",
     "SG&A% = SG&A / Revenue", "profitability")
_add("segment_operating_margin", "Segment Operating Margin (proxy)",
     "Estimated segment-level operating margin after variable overhead.",
     "Unit-economic indicator for diversified industrials and "
     "multi-segment operators. Healthy segments show 12-20% operating "
     "margin before corporate overhead.",
     "(Gross Profit - Variable SG&A) / Revenue", "profitability")
_add("operating_ratio", "Operating Ratio",
     "Operating expenses as a fraction of revenue (1 - operating margin).",
     "Hallmark metric for railroads and LTL trucking. Best-in-class rails "
     "run 56-62% operating ratio; LTL leaders like ODFL run 72-76%. Lower "
     "is better; every 100 bps of improvement is significant.",
     "Operating Ratio = Operating Expenses / Revenue", "profitability")
_add("fcf_conversion", "FCF Conversion",
     "Free cash flow divided by net income.",
     "Capital-discipline and earnings-quality indicator. Quality industrial "
     "compounders consistently convert >95% of net income to FCF. Heavy "
     "capex cyclicals may run 60-80%; working-capital-intensive E&C can "
     "drop below 50% during growth.",
     "FCF Conversion = Free Cash Flow / Net Income", "profitability")

# Solvency
_add("debt_to_equity", "Debt-to-Equity Ratio",
     "Debt financing vs equity financing.",
     "Industrials can carry meaningful leverage given capital intensity "
     "and asset backing. Mature industrials often run 0.5-1.5x; rails and "
     "airlines can exceed 1.5x while retaining investment grade.",
     "D/E = Total Debt / Equity", "solvency")
_add("debt_to_ebitda", "Debt-to-EBITDA",
     "Leverage ratio relative to operating cash flow.",
     "The primary leverage metric for industrial operators. <2x is "
     "conservative, 2-3.5x is normal for mature industrials, >4.5x is "
     "stressed and risks credit downgrade.",
     "Debt/EBITDA = Total Debt / EBITDA", "solvency")
_add("current_ratio", "Current Ratio",
     "Short-term asset coverage of liabilities.",
     "Capital-goods and distribution inventories skew this metric; >1.2x "
     "is typical for industrials given inventory turns and trade payables.",
     "Current Ratio = Current Assets / Current Liabilities", "solvency")
_add("quick_ratio", "Quick Ratio",
     "Liquidity excluding inventory.",
     "Important sanity check for project-based industrials (E&C) and "
     "inventory-heavy distributors where inventory liquidation may be slow.",
     "Quick Ratio = (Current Assets - Inventory) / Current Liabilities", "solvency")
_add("interest_coverage", "Interest Coverage",
     "Ability to pay interest from operating earnings.",
     "> 6x is comfortable for industrials given dividend-funding needs. "
     "< 3x signals balance-sheet stress — a serious concern for cyclicals "
     "heading into a downturn.",
     "Interest Coverage = Operating Income / Interest Expense", "solvency")
_add("lease_adjusted_debt_ratio", "Lease-Adjusted Leverage",
     "Debt-to-EBITDAR after capitalizing operating leases (8x rent proxy).",
     "Critical for airlines, trucking, and marine shipping where aircraft "
     "and vessel lease commitments are large. Target <4x; >5x is stressed "
     "and signals limited capacity to absorb a downturn.",
     "(Debt + 8 × Rent) / (EBITDA + Rent)", "solvency")
_add("altman_z_score", "Altman Z-Score",
     "Bankruptcy probability predictor.",
     "Z > 2.99: Safe. 1.81-2.99: Grey zone. < 1.81: Distress risk. "
     "Especially useful for cyclical industrials (airlines, shipping, "
     "E&C, heavy machinery) heading into a downturn.",
     "Z = 1.2(WC/TA) + 1.4(RE/TA) + 3.3(EBIT/TA) + 0.6(MV/TL) + 1.0(Sales/TA)",
     "solvency")
_add("cash_burn_rate", "Cash Burn Rate",
     "Annual rate of cash consumption for pre-profit operators.",
     "Relevant only for emerging / early-stage industrial operators.",
     "Cash Burn = Annual Operating Cash Flow (when negative)", "solvency")
_add("cash_runway_years", "Cash Runway",
     "Years of operation at current burn rate.",
     "< 1 year = imminent financing. > 2 years = comfortable. Target for "
     "emerging industrial operators: 18+ months to next program milestone.",
     "Cash Runway = Total Cash / Annual Burn Rate", "solvency")
_add("debt_service_coverage", "Debt Service Coverage",
     "EBITDA coverage of interest expense.",
     "> 6x is comfortable for mature industrials. Levered cyclicals "
     "(airlines, E&C, shipping) should target > 4x through cycle given "
     "swings in operating income.",
     "DSCR = EBITDA / Interest Expense", "solvency")

# Growth
_add("revenue_growth_yoy", "Revenue Growth (YoY)",
     "Annual revenue change.",
     "Core growth driver. For mature industrials, 3-7% is healthy through "
     "cycle; scaling operators should deliver >10%. Watch volume vs. "
     "price-mix vs. M&A contribution.",
     "Growth = (Rev_Current - Rev_Prior) / |Rev_Prior|", "growth")
_add("revenue_cagr_3y", "Revenue CAGR (3-Year)",
     "3-year compound revenue growth.",
     "Smooths near-term cyclicality. > 6% is strong for mature industrials; "
     "> 12% for scaling operators.",
     "CAGR = (End/Start)^(1/3) - 1", "growth")
_add("earnings_growth_yoy", "Earnings Growth (YoY)",
     "Annual net income change.",
     "Should track or exceed revenue growth to validate operating "
     "leverage and pricing-power capture.",
     "Growth = (NI_Current - NI_Prior) / |NI_Prior|", "growth")
_add("capex_intensity", "CAPEX Intensity",
     "CAPEX as % of revenue.",
     "Asset-intensity indicator. Asset-light services / distribution: "
     "< 3%. Quality machinery / aerospace: 3-5%. Rails: 17-20%. Airlines "
     "& shipping: highly variable, 8-15%+ through fleet-renewal cycles.",
     "CAPEX Intensity = CAPEX / Revenue", "growth")
_add("organic_revenue_growth", "Organic Revenue Growth (proxy)",
     "Revenue growth minus total-asset growth.",
     "When companies don't disclose organic growth directly, this proxy "
     "separates underlying volume/price growth from M&A and capacity "
     "additions. Positive values suggest the existing base is generating "
     "more revenue — a key distinction for industrial roll-ups.",
     "Rev Growth - Asset Growth", "growth")
_add("book_to_bill_ratio", "Book-to-Bill Ratio",
     "Orders received divided by revenue shipped in the period.",
     ">1 signals backlog growing; <1 signals backlog shrinking. Core "
     "leading indicator for aerospace, defense, and machinery. Where "
     "orders are not disclosed we approximate from inventory / revenue "
     "trends.",
     "Orders / Revenue (proxy: 1 + inventory delta / revenue)", "growth")
_add("backlog_growth_yoy", "Backlog Growth (YoY)",
     "Change in reported backlog year-over-year.",
     "Forward-revenue-visibility indicator for aerospace & defense primes, "
     "machinery OEMs, and E&C contractors. Where backlog is not disclosed "
     "we proxy with inventory-growth direction.",
     "(Backlog_Current - Backlog_Prior) / Backlog_Prior", "growth")
_add("shares_growth_yoy", "Share Dilution (YoY)",
     "Annual change in shares outstanding.",
     "Mature industrials should run net buybacks. Net dilution > 2%/yr in "
     "a Dividend-Aristocrat-style operator signals capital-allocation "
     "concerns.",
     "Dilution = (Shares_Current - Shares_Prior) / Shares_Prior", "growth")
_add("shares_growth_3y_cagr", "Dilution / Buyback CAGR (3-Year)",
     "3-year compound share dilution rate.",
     "Tracks capital-discipline trend. Best-in-class industrials deliver "
     "-1% to -3% (net buyback) CAGR alongside the dividend.",
     "CAGR = (Shares_End / Shares_Start)^(1/3) - 1", "growth")
_add("operating_leverage", "Operating Leverage",
     "Earnings growth relative to revenue growth.",
     "> 1.5x signals scaling margin expansion; < 1x suggests margin "
     "compression from input-cost or fixed-cost drag.",
     "Op Leverage = Earnings Growth / Revenue Growth", "growth")

# Efficiency
_add("inventory_turnover", "Inventory Turnover",
     "How many times per year inventory is sold.",
     "Machinery / capital goods: 3-6x. Distribution: 5-8x. Building "
     "products: 4-7x. Declining turnover is an early warning of demand "
     "weakness or channel destocking.",
     "Inventory Turnover = COGS / Average Inventory", "efficiency")
_add("days_inventory", "Days Inventory",
     "Average days required to sell inventory.",
     "Machinery: 60-120 days. Distribution: 45-75 days. Building products: "
     "50-90 days. Declining days = healthier; rising days = potential "
     "demand or order-book issues.",
     "Days Inventory = 365 / Inventory Turnover", "efficiency")
_add("working_capital_intensity", "Working-Capital Intensity",
     "Working capital as % of revenue.",
     "Services and distribution often run 5-10% working capital. "
     "Capital-goods OEMs can run 15-25% given longer lead times. E&C "
     "contractors can swing widely with project stage.",
     "WC Intensity = Working Capital / Revenue", "efficiency")
_add("revenue_per_employee", "Revenue per Employee",
     "Top-line revenue divided by headcount.",
     "Labour-productivity proxy. Services: $200-400K. Machinery / "
     "building products: $400-700K. Aerospace: $400-600K. Asset-light "
     "distribution: $500K+.",
     "Revenue / Full-Time Employees", "efficiency")

# Business quality
_add("quality_score", "Industrials Business Quality Score",
     "Composite quality score (0-100).",
     "Evaluates backlog / margin strength, unit economics, financial "
     "position, management alignment, and capital discipline. >70 is "
     "high quality (Dividend-Aristocrat tier), <35 is weak.",
     "Weighted sum of backlog strength, unit economics, financial position, "
     "insider alignment, dilution", "business_quality")
_add("backlog_strength", "Backlog / Margin Strength",
     "Qualitative assessment of pricing power and order-book quality.",
     "Derived primarily from gross margin level and trend. Premium "
     "industrials (A&D aftermarket, specialty machinery) sustain >45% "
     "gross margin with stable / expanding pricing.",
     "Inferred from Gross Margin level + trend", "business_quality")
_add("cyclical_sensitivity", "Cyclical Sensitivity",
     "Exposure to macro and end-market cycles.",
     "Aerospace & defense primes and commercial services are least "
     "cyclical; airlines, shipping, trucking and heavy construction are "
     "highly cyclical. Diversified conglomerates and quality machinery "
     "fall in between.",
     "Inferred from sub-segment classification", "business_quality")
_add("unit_economics_quality", "Unit Economics Quality",
     "Combined ROIC + operating margin assessment.",
     "Strong unit economics through cycle is the single most reliable "
     "long-term performance indicator for industrial operators.",
     "Composite of ROIC and Operating Margin", "business_quality")
_add("aftermarket_mix_quality", "Aftermarket / Services Mix",
     "Qualitative read on asset-light services vs capex-heavy OEM.",
     "Aftermarket and service revenue produces higher and more stable "
     "ROIC than new-equipment sales. Inferred from CAPEX intensity.",
     "Inferred from CAPEX / Revenue", "business_quality")


SECTION_EXPLANATIONS = {
    "profile": {
        "title": "Company Profile",
        "description": (
            "Company identification, market cap tier, operator maturity stage, "
            "primary industrials sub-segment (aerospace & defense, machinery, "
            "building products, rails, airlines, logistics, services, etc.), "
            "and geographic market-exposure tier."
        ),
    },
    "valuation": {
        "title": "Valuation Metrics",
        "description": (
            "Price-based ratios. P/E, P/FCF and EV/EBITDA are the primary "
            "anchors for mature industrial operators; P/B and price-to-"
            "tangible-book matter for asset-heavy cyclicals. For emerging "
            "operators, P/S and cash-to-market-cap are more useful."
        ),
    },
    "profitability": {
        "title": "Profitability Metrics",
        "description": (
            "Margin and return analysis. Gross margin is the proxy for "
            "pricing power; ROIC separates Dividend-Aristocrat-tier "
            "franchises from commodity-like operators. Includes SG&A%, a "
            "segment-margin proxy, and operating ratio for rails / trucking."
        ),
    },
    "solvency": {
        "title": "Solvency & Survival",
        "description": (
            "Balance sheet strength. Debt/EBITDA and lease-adjusted "
            "leverage are the core metrics — lease commitments are large "
            "for airlines, trucking, and marine shipping. Cash runway only "
            "matters for pre-profit emerging operators."
        ),
    },
    "growth": {
        "title": "Growth & Capital Discipline",
        "description": (
            "Revenue / earnings growth, CAPEX intensity, organic-growth "
            "proxy, book-to-bill / backlog growth, and share dilution / "
            "buybacks. Mature industrials should run net buybacks alongside "
            "the dividend; >2% dilution per year is a red flag."
        ),
    },
    "efficiency": {
        "title": "Operating Efficiency",
        "description": (
            "Asset turnover, inventory turnover, days inventory, working-"
            "capital intensity, and revenue per employee. Working-capital "
            "discipline is especially differentiating in capital goods "
            "and E&C where project cash-flow timing can swing widely."
        ),
    },
    "share_structure": {
        "title": "Share Structure",
        "description": (
            "Shares outstanding, fully diluted, insider ownership, and "
            "institutional holdings. Family / founder-controlled industrials "
            "(Illinois Tool Works alumni operators, Dover, etc.) historically "
            "deliver long-term-oriented capital allocation."
        ),
    },
    "business_quality": {
        "title": "Industrials Business Quality Assessment",
        "description": (
            "Industrials-specific quality scoring. Evaluates backlog / "
            "margin strength, unit economics, financial position, management "
            "alignment, and capital discipline. Includes cyclical-sensitivity "
            "tagging."
        ),
    },
    "intrinsic_value": {
        "title": "Intrinsic Value Estimates",
        "description": (
            "Multiple valuation methods adapted by stage. Mature operators: "
            "DCF + EV/EBITDA mid-cycle comps. Scaling operators: EV/EBITDA "
            "peer comps. Emerging: EV/Revenue with margin-ramp. IP "
            "licensors: DCF on royalty stream."
        ),
    },
    "conclusion": {
        "title": "Assessment Conclusion",
        "description": (
            "Weighted scoring across 5 categories with weights adapted by "
            "both tier and operator stage. Includes a 10-point industrials "
            "screening checklist."
        ),
    },
}


CONCLUSION_METHODOLOGY = {
    "overall": {
        "title": "Conclusion Methodology",
        "description": (
            "Score is a weighted average of 5 categories (valuation, "
            "profitability, solvency, growth, business quality). Weights "
            "vary by BOTH company tier AND operator stage. Mature industrial "
            "franchises: profitability and quality weighted at 25% each. "
            "Emerging industrials: solvency and growth weighted at 25-35%. "
            "Verdicts: Strong Buy (>=75), Buy (>=60), Hold (>=45), Caution "
            "(>=30), Avoid (<30)."
        ),
    },
    "valuation": {
        "title": "Valuation Score",
        "description": (
            "Starts at 50. Adjusted by P/E, P/FCF, EV/EBITDA, P/S, and P/B. "
            "Early-stage / emerging industrial operators get a bonus for "
            "low P/B."
        ),
    },
    "profitability": {
        "title": "Profitability Score",
        "description": (
            "Starts at 50. ROIC is weighted most heavily, then gross margin, "
            "operating margin, and FCF conversion. Pre-profit operators "
            "default to 50 since margins are not meaningful yet."
        ),
    },
    "solvency": {
        "title": "Solvency Score",
        "description": (
            "Starts at 50. Debt/equity, debt/EBITDA, current ratio, interest "
            "coverage, and cash runway for pre-profit operators. Emerging "
            "industrials are penalized heavily for any material debt."
        ),
    },
    "growth": {
        "title": "Growth Score",
        "description": (
            "Starts at 50. Revenue growth, 3-year CAGR, earnings growth, "
            "and share dilution. Scaling-stage operators get the highest "
            "growth thresholds; net buybacks earn a bonus."
        ),
    },
    "business_quality": {
        "title": "Industrials Business Quality Score",
        "description": (
            "Composite of backlog / margin strength (25pts), unit economics "
            "/ ROIC (25pts), financial position (20pts), management "
            "alignment (15pts), and capital discipline (15pts). Includes "
            "cyclical-sensitivity tagging."
        ),
    },
}


def get_explanation(key): return METRIC_EXPLANATIONS.get(key)


def get_section_explanation(section): return SECTION_EXPLANATIONS.get(section)


def get_conclusion_explanation(category=None):
    return CONCLUSION_METHODOLOGY.get(category or "overall")


def list_metrics(category=None):
    metrics = list(METRIC_EXPLANATIONS.values())
    return [m for m in metrics if m.category == category] if category else metrics
