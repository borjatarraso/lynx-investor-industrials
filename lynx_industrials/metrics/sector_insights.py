"""Industrials-focused sector and industry insights."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SectorInsight:
    sector: str
    overview: str
    critical_metrics: list[str] = field(default_factory=list)
    key_risks: list[str] = field(default_factory=list)
    what_to_watch: list[str] = field(default_factory=list)
    typical_valuation: str = ""


@dataclass
class IndustryInsight:
    industry: str
    sector: str
    overview: str
    critical_metrics: list[str] = field(default_factory=list)
    key_risks: list[str] = field(default_factory=list)
    what_to_watch: list[str] = field(default_factory=list)
    typical_valuation: str = ""


_SECTORS: dict[str, SectorInsight] = {}
_INDUSTRIES: dict[str, IndustryInsight] = {}


def _add_sector(sector, overview, cm, kr, wtw, tv):
    _SECTORS[sector.lower()] = SectorInsight(
        sector=sector, overview=overview, critical_metrics=cm,
        key_risks=kr, what_to_watch=wtw, typical_valuation=tv,
    )


def _add_industry(industry, sector, overview, cm, kr, wtw, tv):
    _INDUSTRIES[industry.lower()] = IndustryInsight(
        industry=industry, sector=sector, overview=overview,
        critical_metrics=cm, key_risks=kr, what_to_watch=wtw,
        typical_valuation=tv,
    )


_add_sector(
    "Industrials",
    "Industrial-sector companies design, build, move, and service the "
    "physical economy — aerospace & defense systems, machinery, building "
    "products, electrical equipment, construction & engineering, and the "
    "transportation infrastructure (rail, air freight, trucking, airlines, "
    "shipping) that links them. Earnings are cyclical: revenue, margin, "
    "and order book track ISM PMI, industrial production, and end-market "
    "capex. The best operators compound through cycles by combining an "
    "installed-base / aftermarket moat with disciplined capital allocation; "
    "commoditized peers oscillate with orders and freight rates.",
    ["Organic revenue growth",
     "Book-to-bill ratio & backlog growth",
     "Operating margin (and operating ratio for rails / trucking)",
     "FCF conversion (FCF / Net Income)",
     "ROIC through a full cycle",
     "Debt/EBITDA and lease-adjusted leverage"],
    ["End-market capex downcycles (construction, mining, oil & gas)",
     "Input-cost inflation (steel, aluminium, copper, semiconductors, fuel)",
     "Supply-chain disruption and labour shortages",
     "Freight-rate volatility and over-capacity",
     "Government budget risk for defense primes and E&C",
     "Tariffs, export controls, and geopolitical trade frictions"],
    ["ISM Manufacturing & Services PMI",
     "Industrial production and capacity utilization",
     "Class I rail carloadings and trucking tonnage",
     "Air cargo volumes and airline load factors",
     "Defense budget appropriations and book-to-bill",
     "Non-residential construction starts and backlog"],
    "Quality compounders (aerospace primes, industrial conglomerates): "
    "P/E 20-28x, EV/EBITDA 14-18x. Cyclical machinery / trucking: P/E "
    "12-20x through cycle, EV/EBITDA 7-11x. Airlines / shipping: trough "
    "P/E <8x, peak >20x — trailing multiples are misleading. Dividend "
    "yield 1.5-3% for mature industrials, with Dividend Aristocrats "
    "(CAT, DE, ITW, DOV, EMR) delivering 5-10% dividend growth.",
)


_add_industry(
    "Aerospace & Defense", "Industrials",
    "Aerospace & defense primes (BA, LMT, RTX, NOC, GD, LHX, HEI, TDG) "
    "earn long-cycle, multi-year program economics. Defense primes trade "
    "on orderly US / NATO budget growth; commercial aerospace OEMs on "
    "airline capex and global passenger traffic. Aftermarket / services "
    "(HEI, TDG) earn premium 30%+ operating margins on installed-base "
    "economics. Program execution, cost-plus vs fixed-price mix, and "
    "foreign military sales (FMS) are key differentiators.",
    ["Backlog coverage (backlog / revenue, target >2x)",
     "Book-to-bill ratio (target ≥1)",
     "Segment operating margin (services vs primes)",
     "R&D intensity (4-6% of revenue)",
     "Pension underfunded ratio",
     "FCF conversion"],
    ["Defense budget risk (continuing resolutions, sequestration)",
     "Fixed-price development program cost overruns (e.g. KC-46, Sentinel)",
     "Commercial aerospace order-book cyclicality",
     "Quality / certification crises (e.g. 737 MAX)",
     "Supply-chain bottlenecks (engines, semiconductors)",
     "Export control and ITAR compliance risk"],
    ["DoD appropriations and FY budget",
     "Boeing / Airbus order book and delivery cadence",
     "Revenue passenger kilometres (RPK) recovery",
     "Classified / black budget share of sales",
     "FMS approvals (Poland, Japan, Middle East)",
     "Aftermarket revenue growth vs new-equipment"],
    "Defense primes: P/E 18-22x, EV/EBITDA 13-16x. Aftermarket specialists "
    "(HEI, TDG): P/E 30-45x on durable recurring economics. Commercial "
    "OEMs swing widely. Dividend yield 2-3%.",
)

_add_industry(
    "Industrial Conglomerates", "Industrials",
    "Diversified industrial conglomerates (GE, HON, MMM, ITT) operate "
    "multiple business platforms spanning aerospace, automation, building "
    "technologies, and energy. Simplified GE has reorganized into pure-"
    "plays (GE Aerospace, GE Vernova). Honeywell remains diversified with "
    "a strong automation and aerospace mix. 3M has been disrupted by "
    "litigation overhangs (PFAS, Combat Arms earplugs). Margin quality "
    "varies widely by business mix.",
    ["Organic revenue growth by segment",
     "Segment operating margins and mix",
     "FCF conversion (target >95%)",
     "ROIC through cycle",
     "Debt/EBITDA",
     "Capital deployment (M&A, buybacks, dividend)"],
    ["End-market exposure concentration",
     "Portfolio complexity and hidden subsidies",
     "Litigation overhangs (especially 3M)",
     "Execution risk on strategic spin-offs",
     "China industrial slowdown",
     "Currency translation on large international mix"],
    ["Organic revenue trends by platform",
     "Margin differential vs peers in each segment",
     "FCF conversion trends",
     "Capital-return cadence",
     "Portfolio-reshaping announcements"],
    "Conglomerates: P/E 18-24x, EV/EBITDA 12-16x. Dividend yield 2-3% with "
    "mid-single-digit dividend growth. Pure-play spin-offs often re-rate "
    "higher than the diversified parent.",
)

_add_industry(
    "Machinery", "Industrials",
    "Heavy-machinery companies (CAT, DE, PCAR, CMI, ITW, DOV, OTIS) build "
    "the equipment that moves materials, plants crops, hauls freight, and "
    "runs factories. Earnings are cyclical but Caterpillar and Deere have "
    "compounded aftermarket services / financing into more stable cash "
    "flows. Illinois Tool Works runs a 80/20 operational playbook yielding "
    "25%+ operating margins — the benchmark for the group.",
    ["Organic revenue growth (volume + price)",
     "Operating margin (target >15%, >20% best-in-class)",
     "FCF conversion",
     "Aftermarket / services % of revenue (target >40%)",
     "ROIC", "Dealer inventory levels"],
    ["Construction, mining, and farm capex cycles",
     "Tariff and trade policy (US-China)",
     "Fuel / commodity-price pass-through lag",
     "Off-highway emissions regulation compliance cost",
     "Dealer channel destocking"],
    ["Dealer statistics (retail sales vs shipments)",
     "Mining & construction end-market capex",
     "Precision agriculture adoption",
     "Aftermarket / services growth",
     "Backlog coverage and order trends"],
    "Quality machinery (CAT, DE, ITW): P/E 15-22x through cycle, EV/EBITDA "
    "10-14x. Truck OEMs (PCAR, CMI): P/E 10-16x on sharper cyclicality. "
    "Dividend yield 1.5-2.5% with strong dividend growth records.",
)

_add_industry(
    "Electrical Equipment", "Industrials",
    "Electrical-equipment companies (ETN, ROK, EMR, PH, AME, ROP) sell "
    "power management, industrial automation, motion control, and process "
    "control into long-duration infrastructure, data-center, and factory-"
    "automation end markets. Data-center capex and grid modernization have "
    "powered a mid-cycle rerating. Operating margins have expanded above "
    "20% on automation volume and pricing.",
    ["Organic revenue growth", "Operating margin (target >20%)",
     "Book-to-bill ratio", "FCF conversion",
     "ROIC", "Aftermarket / services mix"],
    ["Data-center capex digestion after current build-out",
     "Component / semi shortages",
     "Competition from Asian automation peers (Siemens, ABB, Keyence)",
     "Cyclicality of industrial automation end markets",
     "Energy-transition policy swings"],
    ["Data-center / AI-driven power-equipment demand",
     "Industrial automation orders",
     "Grid modernization spending",
     "Electrification / EV infrastructure",
     "Price-cost spread"],
    "Quality electrical (ETN, ROK, EMR, AME, ROP): P/E 22-30x, EV/EBITDA "
    "15-20x reflecting margin expansion and data-center tailwinds. "
    "Dividend yield 1-2% with high dividend growth.",
)

_add_industry(
    "Building Products", "Industrials",
    "Building-products companies (CARR, JCI, TT, LII, MAS, AOS, ALLE) make "
    "HVAC, fire & security, insulation, fittings, and residential / "
    "commercial building systems. HVAC names (CARR, TT, LII) have rerated "
    "sharply on decarbonization, data-center cooling, and refrigerant "
    "transition (A2L / R-454B). Residential exposure is tied to housing "
    "starts; non-res to commercial construction put-in-place.",
    ["Organic revenue growth",
     "Operating margin (target >15-20%)",
     "New-construction vs replacement mix",
     "Backlog growth",
     "FCF conversion",
     "Price realization"],
    ["Housing-start cycles",
     "Non-residential construction slowdown",
     "Refrigerant regulation (A2L transition execution)",
     "Copper and steel input costs",
     "Data-center cooling backlog digestion"],
    ["Housing starts (single-family + multifamily)",
     "Non-res construction put-in-place",
     "ABI (Architecture Billings Index) leading indicator",
     "HVAC replacement cycle",
     "Data-center cooling orders"],
    "Quality HVAC (CARR, TT, LII): P/E 22-32x on secular tailwinds. "
    "Building-product roll-ups (AOS, ALLE): P/E 18-24x. Dividend yield "
    "1-2% with strong dividend growth.",
)

_add_industry(
    "Construction & Engineering", "Industrials",
    "Engineering & construction contractors (PWR, ACM, FIX, FLR, DY, MTZ, "
    "EMCOR) build and maintain power grids, telecom networks, water "
    "systems, and large industrial facilities. Earnings are lumpy and "
    "project-driven. Utility-T&D specialists (PWR) enjoy multi-year "
    "visibility from grid-modernization and renewables build-out. "
    "EPC contractors are more cyclical and working-capital intensive.",
    ["Backlog coverage (target >1.5x revenue)",
     "Book-to-bill ratio",
     "Operating margin (thin — 5-10%)",
     "FCF conversion",
     "Working-capital intensity",
     "Project-execution history (cost overruns)"],
    ["Fixed-price project cost overruns",
     "Labour shortages (craft, engineering)",
     "Permitting and interconnection queue delays",
     "Commodity cost pass-through lag",
     "Customer concentration on mega-projects"],
    ["Grid modernization / T&D capex announcements",
     "Renewable power capex pipeline",
     "Data-center site awards",
     "IRA / infrastructure-bill flow-through",
     "Backlog book-to-bill trajectory"],
    "Utility T&D (PWR): P/E 20-30x, EV/EBITDA 13-17x on secular tailwinds. "
    "Diversified E&C (ACM, MTZ): P/E 18-25x. Low-quality fixed-price "
    "EPC earns much lower multiples. Dividend yield typically <1%.",
)

_add_industry(
    "Trading Companies & Distributors", "Industrials",
    "Industrial distributors (FAST, GWW, URI, WSO, MSM, HDS) earn steady "
    "mid-cycle returns on scale, private-label penetration, and e-commerce "
    "capability. Fastenal and Grainger lead in MRO distribution; Watsco "
    "in HVAC distribution; United Rentals in equipment rental. The group "
    "compounds through disciplined M&A roll-ups and share buybacks.",
    ["Organic revenue growth",
     "Gross margin (target >38% for MRO, >30% for rental)",
     "Operating margin (target >15%)",
     "Inventory turnover",
     "ROIC (high on asset-light models)",
     "Same-store sales growth"],
    ["Industrial-production slowdowns",
     "Amazon Business competitive pressure",
     "Non-residential construction downturns (URI)",
     "Rental-fleet utilization / pricing",
     "Small-ticket e-commerce margin compression"],
    ["Daily sales rate / same-store sales",
     "Private-label / exclusive-brand penetration",
     "Onsite and vending-machine program growth",
     "Rental time utilization and rates (URI)",
     "Acquisition pipeline and pricing discipline"],
    "Quality distributors (FAST, GWW): P/E 28-36x on compounding track "
    "record. Rental (URI): P/E 12-18x reflecting cyclicality. Watsco (WSO): "
    "P/E 22-28x with secular HVAC exposure. Yield 1-2%.",
)

_add_industry(
    "Air Freight & Logistics", "Industrials",
    "Air-freight and logistics carriers (UPS, FDX, CHRW, EXPD, ODFL, XPO) "
    "move parcels, LTL freight, and brokered freight between businesses "
    "and consumers. Parcel integrators (UPS, FDX) face e-commerce volume "
    "digestion and cost inflation; LTL (ODFL) is a structurally profitable "
    "oligopoly. Asset-light brokers (CHRW, EXPD) rely on truck-rate "
    "volatility for margin.",
    ["Revenue per shipment / piece",
     "Operating margin (parcel: 8-15%; LTL: 25-30% best-in-class)",
     "Operating ratio (LTL — target <80%)",
     "Capex intensity (parcel vs asset-light)",
     "Volume growth", "Pricing (yield) trends"],
    ["E-commerce volume digestion at UPS / FedEx",
     "Teamsters labour negotiations (UPS)",
     "Trucking capacity cycles",
     "Amazon insourcing of logistics",
     "Fuel-surcharge pass-through lag",
     "International trade / tariff policy"],
    ["Parcel daily volume and yields",
     "LTL shipments and weight per shipment",
     "Truckload spot vs contract spread",
     "International airfreight yields",
     "E-commerce penetration of US retail"],
    "LTL leader (ODFL): P/E 28-38x reflecting pricing discipline. Parcel "
    "(UPS, FDX): P/E 14-20x. Freight brokers (CHRW, EXPD): P/E 18-25x. "
    "Yield 2-3% for parcel.",
)

_add_industry(
    "Railroads", "Industrials",
    "Class I railroads (UNP, CSX, NSC, CP, CNI) operate natural duopolies "
    "or oligopolies on long-haul freight. Operating ratio (opex / revenue) "
    "is the industry's headline metric — the lower the better. Precision "
    "Scheduled Railroading (PSR) drove a decade of margin expansion. "
    "Service-quality recovery post-PSR and volume re-growth are the "
    "current focus. Intermodal volume correlates tightly with import "
    "activity.",
    ["Operating ratio (target <62%; best-in-class <58%)",
     "Revenue per carload",
     "Carload volumes by commodity group",
     "FCF conversion",
     "ROIC", "Service metrics (train speed, dwell)"],
    ["Volume cyclicality (coal decline, intermodal swings)",
     "Service / precision-scheduled-railroading overreach",
     "Labour relations and STB regulation",
     "Rail-safety legislation post East Palestine",
     "Shippers' diversion to trucking during tight service"],
    ["Weekly carload and intermodal volumes (AAR)",
     "Operating ratio trend by carrier",
     "Intermodal pricing vs truck spot",
     "Fuel surcharge and fuel efficiency",
     "Capex as % of revenue (target 17-20%)"],
    "Rails: P/E 18-24x, EV/EBITDA 12-15x. Yield 1.5-2.5% with mid-single-"
    "digit dividend growth. Margin structure varies widely; UNP and CP "
    "typically earn premium multiples.",
)

_add_industry(
    "Passenger Airlines", "Industrials",
    "Passenger airlines (DAL, UAL, AAL, LUV, ALK, JBLU) are capital-"
    "intensive, highly cyclical operators with fuel and labour as largest "
    "cost buckets. Premium-cabin mix, loyalty-program economics, and "
    "international hubs distinguish legacy network carriers (DAL, UAL) "
    "from low-cost carriers. Trailing P/Es are misleading — airlines are "
    "best analysed through trough / peak frameworks and on-balance-sheet "
    "net debt.",
    ["Load factor (target >85%)",
     "RASM (revenue per available seat mile)",
     "CASM ex-fuel (cost per ASM, ex-fuel)",
     "Operating margin through cycle",
     "Net debt / EBITDAR",
     "Unit revenue vs unit cost spread"],
    ["Fuel-price spikes and hedging losses",
     "Labour contract step-ups (pilots, flight attendants)",
     "Demand shocks (pandemics, geopolitics)",
     "Capacity adds compressing yields",
     "Engine / aircraft groundings (GTF, MAX)",
     "Pension and lease-liability overhangs"],
    ["Domestic and international unit revenue",
     "Fuel cost per gallon",
     "Premium cabin revenue growth",
     "Loyalty-program partner spending",
     "Industry capacity (ASM) growth",
     "Net debt trajectory"],
    "Airlines: trough P/E <7x, peak P/E >20x. EV/EBITDAR 5-9x mid-cycle. "
    "Balance-sheet leverage and lease obligations are typically higher "
    "than reported. Yield often 0-1% (low-cost carriers pay no dividend).",
)

_add_industry(
    "Ground Freight & Trucking", "Industrials",
    "Trucking operators (ODFL, SAIA, XPO, KNX, JBHT, LSTR, WERN, SNDR) "
    "haul truckload, LTL, and specialized freight. LTL pricing discipline "
    "is structural; truckload is highly cyclical and capacity-driven. "
    "Dedicated / contract carriers earn steadier returns than spot-exposed "
    "players. Owner-operator vs company-driver mix and terminal density "
    "are key differentiators.",
    ["Operating ratio (LTL: <80%; TL: 85-95%)",
     "Revenue per truck",
     "Tonnage / shipment growth",
     "Fuel-surcharge revenue mix",
     "Driver turnover",
     "Capex intensity"],
    ["Truckload capacity over-build then destocking",
     "Driver shortages and labour inflation",
     "Fuel-price volatility",
     "E-commerce / Amazon in-house freight growth",
     "Weather and natural-disaster disruption"],
    ["Cass Freight Index and ATA tonnage",
     "Spot vs contract rate spread",
     "Load-to-truck ratio",
     "Broker net revenue margin",
     "Fuel surcharge as % of revenue"],
    "LTL leaders (ODFL, SAIA): P/E 25-35x on pricing power. Truckload "
    "and brokers: P/E 12-20x through cycle. Yield typically <1-2%.",
)

_add_industry(
    "Marine Shipping", "Industrials",
    "Marine shipping operators (KEX, MATX, ZIM, DAC, GSL, STNG) carry "
    "container, dry-bulk, tanker, and specialty cargo. Earnings are "
    "extremely cyclical — charter rates can move 3-5x through a cycle "
    "on small changes in supply/demand. Dividend policy often reflects "
    "through-cycle rather than current earnings. Fleet age, scrapping, "
    "and order book are critical supply drivers.",
    ["Utilization / day rates",
     "Time-charter equivalent (TCE)",
     "Operating margin",
     "Orderbook as % of fleet",
     "Net debt / EBITDA",
     "Fleet age and specification"],
    ["Freight rate collapses during capacity over-build",
     "Fuel (bunker) price spikes",
     "Geopolitical choke-point disruption (Suez, Red Sea, Panama)",
     "Environmental regulation (IMO 2030, EEXI)",
     "Second-hand vessel price volatility"],
    ["Container, tanker, and dry-bulk spot rates",
     "Orderbook-to-fleet ratio",
     "Suez / Panama transit volumes",
     "Fuel spread vs heavy fuel oil",
     "Scrapping activity"],
    "Shipping: trough P/E <4x, peak P/E >15x. Trailing multiples highly "
    "misleading. Net asset value and replacement-cost frameworks often "
    "more useful than earnings multiples. Yield often very high at peaks.",
)

_add_industry(
    "Commercial Services & Supplies", "Industrials",
    "Commercial services operators (CTAS, RSG, WM, VRSK, ROL, CPRT, RBA) "
    "provide uniforms, waste collection, pest control, environmental "
    "services, vehicle auctions, and data-analytics services under "
    "multi-year contracts. Revenue visibility is high — CTAS and WM "
    "compound at 8-10% with 20%+ operating margins. Consolidation and "
    "route density drive margin expansion.",
    ["Organic revenue growth",
     "Operating margin (target >20%)",
     "FCF conversion (target >100%)",
     "Customer retention (>90%)",
     "ROIC", "M&A roll-up cadence"],
    ["Labour inflation (drivers, technicians, uniform service)",
     "Fuel-price pass-through lag",
     "Volume sensitivity to industrial production",
     "Regulatory costs (landfill, PFAS)",
     "M&A integration risk"],
    ["Organic revenue trends",
     "Pricing realization vs cost inflation",
     "Tuck-in acquisition cadence",
     "Customer retention / attrition",
     "Capex intensity and fleet age"],
    "Quality services roll-ups (CTAS, WM, RSG, VRSK): P/E 30-40x on "
    "durable growth and FCF. Dividend yield 1-2% with double-digit "
    "dividend growth.",
)

_add_industry(
    "Professional Services", "Industrials",
    "Professional-services firms (BAH, LDOS, CACI, FCN, RHI, MAN, KFY) "
    "provide government IT consulting, management advisory, and staffing. "
    "Government-services leaders (LDOS, BAH, CACI) have secular tailwinds "
    "from defense IT and cybersecurity spending. Staffing names (MAN, "
    "RHI, KFY) are highly cyclical; billable-hour demand closely tracks "
    "corporate confidence.",
    ["Organic revenue growth",
     "Book-to-bill ratio (gov-IT primes)",
     "Operating margin (gov IT: 8-12%; staffing: 5-8%)",
     "Revenue per employee",
     "Utilization rate",
     "Billable-hour growth"],
    ["Government budget continuing resolutions (gov IT)",
     "Hiring freezes compressing staffing demand",
     "Wage inflation squeezing bill-rate spreads",
     "AI disruption of low-end consulting / staffing",
     "Large-contract recompete losses"],
    ["DoD / federal IT outlays",
     "Staffing temp-labour index",
     "Billable hours by practice",
     "Backlog coverage (gov IT)",
     "Pricing vs cost inflation"],
    "Gov-IT primes (LDOS, BAH, CACI): P/E 17-24x. Staffing (MAN, RHI): P/E "
    "10-18x through cycle. Yield 1-2%.",
)


def get_sector_insight(sector: str | None) -> SectorInsight | None:
    return _SECTORS.get(sector.lower()) if sector else None


def get_industry_insight(industry: str | None) -> IndustryInsight | None:
    return _INDUSTRIES.get(industry.lower()) if industry else None


def list_sectors() -> list[str]:
    return sorted(s.sector for s in _SECTORS.values())


def list_industries() -> list[str]:
    return sorted(i.industry for i in _INDUSTRIES.values())
