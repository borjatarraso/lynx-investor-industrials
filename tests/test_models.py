"""Unit tests for data models and classification functions."""

import pytest
from lynx_industrials.models import (
    CompanyProfile, CompanyStage, CompanyTier, Segment,
    JurisdictionTier, Relevance, AnalysisReport,
    ValuationMetrics, SolvencyMetrics, GrowthMetrics,
    BusinessQualityIndicators, ShareStructure, MarketIntelligence,
    FinancialStatement, AnalysisConclusion,
    classify_tier, classify_stage, classify_segment, classify_jurisdiction,
)


class TestClassifyTier:
    def test_mega_cap(self):
        assert classify_tier(300_000_000_000) == CompanyTier.MEGA

    def test_large_cap(self):
        assert classify_tier(50_000_000_000) == CompanyTier.LARGE

    def test_mid_cap(self):
        assert classify_tier(5_000_000_000) == CompanyTier.MID

    def test_small_cap(self):
        assert classify_tier(1_000_000_000) == CompanyTier.SMALL

    def test_micro_cap(self):
        assert classify_tier(100_000_000) == CompanyTier.MICRO

    def test_nano_cap(self):
        assert classify_tier(10_000_000) == CompanyTier.NANO

    def test_none_returns_nano(self):
        assert classify_tier(None) == CompanyTier.NANO

    def test_zero_returns_nano(self):
        assert classify_tier(0) == CompanyTier.NANO

    def test_negative_returns_nano(self):
        assert classify_tier(-100) == CompanyTier.NANO


class TestClassifyStage:
    def test_producer_large_operator(self):
        # >$5B revenue + Dividend Aristocrat language → PRODUCER (Mature Industrial Franchise)
        assert classify_stage(
            "global industrial leader and dividend aristocrat",
            25_000_000_000,
            {"operatingMargins": 0.22},
        ) == CompanyStage.PRODUCER

    def test_producer_without_keyword(self):
        # Just >$5B revenue falls to PRODUCER even without keyword
        assert classify_stage(
            "global machinery manufacturer",
            15_000_000_000,
            {},
        ) == CompanyStage.PRODUCER

    def test_developer_scaling(self):
        # $500M–$5B revenue range with expansion language → DEVELOPER
        assert classify_stage(
            "expanding building-products operator with national rollout",
            1_500_000_000,
            {"operatingMargins": 0.06},
        ) == CompanyStage.DEVELOPER

    def test_explorer_emerging(self):
        # $20M–$500M revenue → EXPLORER (Emerging Industrial Operator)
        assert classify_stage(
            "emerging industrial-automation challenger at commercialization stage",
            80_000_000,
            {"operatingMargins": -0.02},
        ) == CompanyStage.EXPLORER

    def test_grassroots_early_stage(self):
        # Pre-revenue / heavy losses → GRASSROOTS
        assert classify_stage(
            "early stage startup",
            500_000,
            {"profitMargins": -0.50},
        ) == CompanyStage.GRASSROOTS

    def test_royalty_ip_licensor(self):
        # IP-licensor / asset-light language dominates regardless of revenue
        assert classify_stage(
            "asset-light industrial design licensing company",
            8_000_000_000,
            {"operatingMargins": 0.30},
        ) == CompanyStage.ROYALTY

    def test_none_description_default(self):
        # No description and no revenue falls through to EXPLORER default
        assert classify_stage(None, None) == CompanyStage.EXPLORER

    def test_empty_description(self):
        assert classify_stage("", 0, {}) == CompanyStage.EXPLORER


class TestClassifySegment:
    def test_aerospace_defense(self):
        assert classify_segment(
            "leading aerospace and defense prime manufacturer of aircraft, missile and radar systems",
            "Aerospace & Defense",
        ) == Segment.AEROSPACE_DEFENSE

    def test_industrial_conglomerates(self):
        assert classify_segment(
            "diversified industrial conglomerate operating across multi-industry segments",
            "Conglomerates",
        ) == Segment.INDUSTRIAL_CONGLOMERATES

    def test_machinery(self):
        assert classify_segment(
            "global manufacturer of heavy machinery, construction equipment and mining equipment including bulldozer and excavator",
            "Farm & Heavy Construction Machinery",
        ) == Segment.MACHINERY

    def test_electrical_equipment(self):
        assert classify_segment(
            "electrical equipment and industrial automation provider with power management, switchgear and transformer products",
            "Electrical Equipment & Parts",
        ) == Segment.ELECTRICAL_EQUIPMENT

    def test_building_products(self):
        assert classify_segment(
            "building products manufacturer specializing in HVAC, insulation, roofing and windows",
            "Building Products & Equipment",
        ) == Segment.BUILDING_PRODUCTS

    def test_construction_engineering(self):
        assert classify_segment(
            "engineering procurement and construction contractor with EPC contractor experience in heavy civil construction",
            "Engineering & Construction",
        ) == Segment.CONSTRUCTION_ENGINEERING

    def test_air_freight_logistics(self):
        assert classify_segment(
            "integrated air freight and air cargo logistics provider offering parcel delivery and freight forwarding",
            "Integrated Freight & Logistics",
        ) == Segment.AIR_FREIGHT_LOGISTICS

    def test_railroads(self):
        assert classify_segment(
            "class i railroad operating freight rail and intermodal rail services",
            "Railroads",
        ) == Segment.RAILROADS

    def test_airlines(self):
        assert classify_segment(
            "commercial airline operating scheduled passenger services as a low-cost carrier",
            "Airlines",
        ) == Segment.AIRLINES

    def test_trucking(self):
        assert classify_segment(
            "less-than-truckload motor carrier providing over-the-road trucking and freight trucking",
            "Trucking",
        ) == Segment.TRUCKING

    def test_marine_shipping(self):
        assert classify_segment(
            "marine shipping operator with tanker shipping, dry bulk shipping and container shipping fleets",
            "Marine Shipping",
        ) == Segment.MARINE_SHIPPING

    def test_commercial_services(self):
        assert classify_segment(
            "commercial services provider offering waste management, facilities services and pest control",
            "Specialty Business Services",
        ) == Segment.COMMERCIAL_SERVICES

    def test_professional_services(self):
        assert classify_segment(
            "professional services firm providing management consulting and staffing services",
            "Staffing & Employment Services",
        ) == Segment.PROFESSIONAL_SERVICES

    def test_trading_distribution(self):
        assert classify_segment(
            "industrial distributor operating MRO distributor and fastener distributor network with equipment rental",
            "Industrial Distribution",
        ) == Segment.TRADING_DISTRIBUTION

    def test_other_when_no_match(self):
        assert classify_segment("generic company", None) == Segment.OTHER

    def test_none_inputs(self):
        assert classify_segment(None, None) == Segment.OTHER


class TestClassifyJurisdiction:
    def test_us_tier1(self):
        assert classify_jurisdiction("United States") == JurisdictionTier.TIER_1

    def test_uk_tier1(self):
        assert classify_jurisdiction("United Kingdom") == JurisdictionTier.TIER_1

    def test_australia_tier1(self):
        assert classify_jurisdiction("Australia") == JurisdictionTier.TIER_1

    def test_japan_tier1(self):
        assert classify_jurisdiction("Japan") == JurisdictionTier.TIER_1

    def test_mexico_tier2(self):
        assert classify_jurisdiction("Mexico") == JurisdictionTier.TIER_2

    def test_south_korea_tier2(self):
        assert classify_jurisdiction("South Korea") == JurisdictionTier.TIER_2

    def test_unknown_tier3(self):
        assert classify_jurisdiction("SomeCountry") == JurisdictionTier.TIER_3

    def test_none_unknown(self):
        assert classify_jurisdiction(None) == JurisdictionTier.UNKNOWN


class TestDataModels:
    def test_analysis_report_defaults(self):
        r = AnalysisReport(profile=CompanyProfile(ticker="TEST", name="Test"))
        assert r.valuation is None
        assert r.market_intelligence is None
        assert r.financials == []
        assert r.fetched_at != ""

    def test_company_profile_defaults(self):
        p = CompanyProfile(ticker="X", name="X Corp")
        assert p.tier == CompanyTier.NANO
        assert p.stage == CompanyStage.GRASSROOTS
        assert p.primary_segment == Segment.OTHER
        assert p.jurisdiction_tier == JurisdictionTier.UNKNOWN

    def test_solvency_metrics_defaults(self):
        s = SolvencyMetrics()
        assert s.cash_runway_years is None
        assert s.burn_as_pct_of_market_cap is None
        assert s.lease_adjusted_debt_ratio is None

    def test_market_intelligence_defaults(self):
        mi = MarketIntelligence()
        assert mi.insider_transactions == []
        assert mi.risk_warnings == []
        assert mi.disclaimers == []

    def test_business_quality_defaults(self):
        bq = BusinessQualityIndicators()
        assert bq.quality_score is None
        assert bq.backlog_strength is None
        assert bq.cyclical_sensitivity is None
