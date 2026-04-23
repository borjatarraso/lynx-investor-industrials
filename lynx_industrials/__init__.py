"""Lynx Industrials — Fundamental analysis for industrial-sector companies."""

from pathlib import Path

# Suite-level constants come from lynx-investor-core (shared across every agent).
from lynx_investor_core import (
    LICENSE_NAME,
    LICENSE_TEXT,
    LICENSE_URL,
    SUITE_LABEL,
    SUITE_NAME,
    SUITE_VERSION,
    __author__,
    __author_email__,
    __license__,
    __year__,
)
from lynx_investor_core import storage as _core_storage

# Initialize the shared storage layer with this agent's project root so
# data/ and data_test/ live beside *this* package.
_core_storage.set_base_dir(Path(__file__).resolve().parent.parent)

# ---------------------------------------------------------------------------
# Agent-specific identity
# ---------------------------------------------------------------------------

__version__ = "5.1"  # lynx-investor-industrials version (independent of core)

APP_NAME = "Lynx Industrials Analysis"
APP_SHORT_NAME = "Industrials Analysis"
APP_TAGLINE = "Industrials Fundamental Analysis"
APP_SCOPE = "industrial-sector companies"
PROG_NAME = "lynx-industrials"
PACKAGE_NAME = "lynx_industrials"
USER_AGENT_PRODUCT = "LynxIndustrials"
NEWS_SECTOR_KEYWORD = "industrials stock"

TICKER_SUGGESTIONS = (
    "  - For aerospace & defense, try: BA, LMT, RTX, NOC, GD, HEI, TDG, LHX",
    "  - For industrial conglomerates, try: GE, HON, MMM, ITT",
    "  - For machinery & capital goods, try: CAT, DE, ITW, PCAR, CMI, DOV, ETN",
    "  - For building products, try: CARR, JCI, TT, LII, MAS, AOS, ALLE",
    "  - For air freight & logistics, try: UPS, FDX, CHRW, EXPD, ODFL, XPO",
    "  - For railroads, try: UNP, CSX, NSC, CP, CNI",
    "  - For airlines, try: DAL, UAL, LUV, AAL, ALK",
    "  - You can also type the full company name: 'Caterpillar'",
)

DESCRIPTION = (
    "Fundamental analysis specialized for industrial-sector companies — "
    "aerospace & defense, industrial conglomerates, machinery & capital "
    "goods, electrical equipment, building products, construction & "
    "engineering, trading & distribution, railroads, airlines, trucking, "
    "marine shipping, air-freight & logistics, professional services, "
    "and commercial services. Evaluates cyclical industrial operators "
    "across all maturity stages from emerging industrial-tech upstarts "
    "to mature Dividend Aristocrats using industrials-specific metrics: "
    "backlog, book-to-bill ratio, organic revenue growth, operating ratio, "
    "free-cash-flow conversion, ROIC, capex intensity, working-capital "
    "discipline, and end-market cyclicality.\n\n"
    "Part of the Lince Investor Suite."
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _load_logo_ascii() -> str:
    """Load the ASCII logo from img/logo_ascii.txt."""
    from lynx_investor_core.logo import load_logo_ascii
    return load_logo_ascii(Path(__file__).resolve().parent)


def get_about_text() -> dict:
    """Return structured about information (uniform across agents)."""
    from lynx_investor_core.about import AgentMeta, build_about
    meta = AgentMeta(
        app_name=APP_NAME,
        short_name=APP_SHORT_NAME,
        tagline=APP_TAGLINE,
        package_name=PACKAGE_NAME,
        prog_name=PROG_NAME,
        version=__version__,
        description=DESCRIPTION,
        scope_description=APP_SCOPE,
    )
    return build_about(meta, logo_ascii=_load_logo_ascii())
