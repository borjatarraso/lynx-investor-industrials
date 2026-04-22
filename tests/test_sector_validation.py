"""Tests for the industrials sector validation gate."""

import pytest
from lynx_industrials.core.analyzer import _validate_sector, SectorMismatchError
from lynx_industrials.models import CompanyProfile


class TestSectorValidation:
    """Sector validation blocks non-industrials companies."""

    def _profile(self, ticker="T", sector=None, industry=None, desc=None):
        return CompanyProfile(
            ticker=ticker, name=f"{ticker} Corp",
            sector=sector, industry=industry, description=desc,
        )

    # --- Should ALLOW ---
    def test_industrials_sector(self):
        _validate_sector(self._profile(sector="Industrials", industry="Aerospace & Defense"))

    def test_aerospace_defense_industry(self):
        _validate_sector(self._profile(sector="Industrials", industry="Aerospace & Defense"))

    def test_farm_heavy_construction_machinery_industry(self):
        _validate_sector(self._profile(sector="Industrials", industry="Farm & Heavy Construction Machinery"))

    def test_specialty_industrial_machinery_industry(self):
        _validate_sector(self._profile(sector="Industrials", industry="Specialty Industrial Machinery"))

    def test_conglomerates_industry(self):
        _validate_sector(self._profile(sector="Industrials", industry="Conglomerates"))

    def test_building_products_industry(self):
        _validate_sector(self._profile(sector="Industrials", industry="Building Products & Equipment"))

    def test_electrical_equipment_industry(self):
        _validate_sector(self._profile(sector="Industrials", industry="Electrical Equipment & Parts"))

    def test_engineering_construction_industry(self):
        _validate_sector(self._profile(sector="Industrials", industry="Engineering & Construction"))

    def test_industrial_distribution_industry(self):
        _validate_sector(self._profile(sector="Industrials", industry="Industrial Distribution"))

    def test_rental_leasing_services_industry(self):
        _validate_sector(self._profile(sector="Industrials", industry="Rental & Leasing Services"))

    def test_integrated_freight_logistics_industry(self):
        _validate_sector(self._profile(sector="Industrials", industry="Integrated Freight & Logistics"))

    def test_railroads_industry(self):
        _validate_sector(self._profile(sector="Industrials", industry="Railroads"))

    def test_airlines_industry(self):
        _validate_sector(self._profile(sector="Industrials", industry="Airlines"))

    def test_trucking_industry(self):
        _validate_sector(self._profile(sector="Industrials", industry="Trucking"))

    def test_marine_shipping_industry(self):
        _validate_sector(self._profile(sector="Industrials", industry="Marine Shipping"))

    def test_specialty_business_services_industry(self):
        _validate_sector(self._profile(sector="Industrials", industry="Specialty Business Services"))

    def test_staffing_employment_services_industry(self):
        _validate_sector(self._profile(sector="Industrials", industry="Staffing & Employment Services"))

    def test_waste_management_industry(self):
        _validate_sector(self._profile(sector="Industrials", industry="Waste Management"))

    def test_aerospace_in_description(self):
        _validate_sector(self._profile(
            sector="Other", industry="Other",
            desc="Prime manufacturer of aerospace and defense systems including aircraft and avionics"))

    def test_railroad_in_description(self):
        _validate_sector(self._profile(
            sector="Other", industry="Other",
            desc="Operates a Class I railroad and freight rail network across North America"))

    def test_airline_in_description(self):
        _validate_sector(self._profile(
            sector="Other", industry="Other",
            desc="Commercial airline operating scheduled passenger services as a low-cost carrier"))

    def test_machinery_in_description(self):
        _validate_sector(self._profile(
            sector="Other", industry="Other",
            desc="Global manufacturer of heavy machinery and construction equipment"))

    # --- Should BLOCK ---
    def test_technology_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Technology", industry="Software"))

    def test_financial_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Financial Services", industry="Banks"))

    def test_healthcare_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Healthcare", industry="Drug Manufacturers"))

    def test_basic_materials_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Basic Materials", industry="Gold"))

    def test_energy_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Energy", industry="Oil & Gas E&P"))

    def test_real_estate_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Real Estate", industry="REIT"))

    def test_consumer_defensive_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Consumer Defensive", industry="Packaged Foods"))

    def test_consumer_cyclical_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Consumer Cyclical", industry="Specialty Retail"))

    def test_consumer_discretionary_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="Consumer Discretionary", industry="Apparel Manufacturing"))

    def test_all_none_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile())

    def test_empty_strings_blocked(self):
        with pytest.raises(SectorMismatchError):
            _validate_sector(self._profile(sector="", industry="", desc=""))

    def test_error_message_content(self):
        with pytest.raises(SectorMismatchError, match="outside the scope"):
            _validate_sector(self._profile(sector="Technology", industry="Software"))

    def test_error_suggests_another_agent(self):
        """Wrong-sector warning appends a 'use lynx-investor-*' line."""
        with pytest.raises(SectorMismatchError) as exc:
            _validate_sector(self._profile(
                sector="Healthcare", industry="Biotechnology"))
        message = str(exc.value)
        assert "Suggestion" in message
        assert "lynx-investor-healthcare" in message

    def test_error_never_suggests_self(self):
        """The suggestion never points back to this agent itself."""
        with pytest.raises(SectorMismatchError) as exc:
            _validate_sector(self._profile(
                sector="Technology", industry="Software"))
        message = str(exc.value)
        assert "use 'lynx-investor-industrials'" not in message
