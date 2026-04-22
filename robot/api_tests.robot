*** Settings ***
Documentation    Python API tests for lynx-industrials
Library          Process

*** Variables ***
${PYTHON}        python3

*** Keywords ***
When I Run Python Code "${code}"
    ${result}=    Run Process    ${PYTHON}    -c    ${code}    timeout=120s
    Set Test Variable    ${OUTPUT}    ${result.stdout}${result.stderr}
    Set Test Variable    ${RC}    ${result.rc}

Then The Exit Code Should Be ${expected}
    Should Be Equal As Integers    ${RC}    ${expected}

Then The Output Should Contain "${text}"
    Should Contain    ${OUTPUT}    ${text}

*** Test Cases ***
Import All Models
    [Documentation]    GIVEN the package WHEN I import models THEN all classes are available
    When I Run Python Code "from lynx_industrials.models import AnalysisReport, CompanyProfile, CompanyStage, CompanyTier, Segment, JurisdictionTier, Relevance, MarketIntelligence, InsiderTransaction; print('OK')"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "OK"

Import All Calculators
    [Documentation]    GIVEN the package WHEN I import calculators THEN all functions exist
    When I Run Python Code "from lynx_industrials.metrics.calculator import calc_valuation, calc_profitability, calc_solvency, calc_growth, calc_efficiency, calc_share_structure, calc_business_quality, calc_intrinsic_value, calc_market_intelligence; print('OK')"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "OK"

Classify Company Tier Mega Cap
    [Documentation]    GIVEN a large market cap WHEN I classify THEN it returns Mega Cap
    When I Run Python Code "from lynx_industrials.models import classify_tier; print(classify_tier(500_000_000_000).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Mega Cap"

Classify Company Tier Micro Cap
    [Documentation]    GIVEN a small market cap WHEN I classify THEN it returns Micro Cap
    When I Run Python Code "from lynx_industrials.models import classify_tier; print(classify_tier(100_000_000).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Micro Cap"

Classify Company Tier None
    [Documentation]    GIVEN None market cap WHEN I classify THEN it returns Nano Cap
    When I Run Python Code "from lynx_industrials.models import classify_tier; print(classify_tier(None).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Nano Cap"

Classify Operator Stage Mature
    [Documentation]    GIVEN a global industrial WHEN I classify THEN Mature Industrial Franchise
    When I Run Python Code "from lynx_industrials.models import classify_stage; print(classify_stage('global industrial leader and dividend aristocrat', 25000000000, {'operatingMargins': 0.22}).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Mature Industrial Franchise"

Classify Operator Stage IP Licensor
    [Documentation]    GIVEN an asset-light licensor description WHEN I classify THEN IP Licensor
    When I Run Python Code "from lynx_industrials.models import classify_stage; print(classify_stage('asset-light industrial design licensing', 8000000000, {}).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Licensor"

Classify Operator Stage Scaling
    [Documentation]    GIVEN a scaling industrial operator WHEN I classify THEN Scaling Industrial Operator
    When I Run Python Code "from lynx_industrials.models import classify_stage; print(classify_stage('expanding building-products operator with national rollout', 1500000000, {'operatingMargins': 0.06}).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Scaling Industrial Operator"

Classify Operator Stage Emerging
    [Documentation]    GIVEN a small emerging industrial WHEN I classify THEN Emerging Industrial Operator
    When I Run Python Code "from lynx_industrials.models import classify_stage; print(classify_stage('emerging industrial-automation challenger at commercialization stage', 80000000, {'operatingMargins': -0.02}).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Emerging"

Classify Segment Aerospace Defense
    [Documentation]    GIVEN aerospace text WHEN I classify THEN Aerospace & Defense detected
    When I Run Python Code "from lynx_industrials.models import classify_segment; print(classify_segment('leading aerospace and defense prime manufacturer of aircraft and missile systems', 'Aerospace & Defense').value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Aerospace & Defense"

Classify Segment Machinery
    [Documentation]    GIVEN machinery text WHEN I classify THEN Machinery detected
    When I Run Python Code "from lynx_industrials.models import classify_segment; print(classify_segment('global manufacturer of heavy machinery construction equipment and mining equipment', 'Farm & Heavy Construction Machinery').value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Machinery"

Classify Segment Railroads
    [Documentation]    GIVEN railroad text WHEN I classify THEN Railroads detected
    When I Run Python Code "from lynx_industrials.models import classify_segment; print(classify_segment('class i railroad operating freight rail and intermodal rail services', 'Railroads').value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Railroads"

Classify Segment Airlines
    [Documentation]    GIVEN airline text WHEN I classify THEN Airlines detected
    When I Run Python Code "from lynx_industrials.models import classify_segment; print(classify_segment('commercial airline operating scheduled passenger services as a low-cost carrier', 'Airlines').value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Airlines"

Classify Market Exposure Tier 1
    [Documentation]    GIVEN United States WHEN I classify THEN Tier 1
    When I Run Python Code "from lynx_industrials.models import classify_jurisdiction; print(classify_jurisdiction('United States').value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Tier 1"

Classify Market Exposure Tier 2
    [Documentation]    GIVEN Mexico WHEN I classify THEN Tier 2
    When I Run Python Code "from lynx_industrials.models import classify_jurisdiction; print(classify_jurisdiction('Mexico').value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Tier 2"

Relevance Emerging Cash Runway Critical
    [Documentation]    GIVEN emerging operator WHEN I check cash runway THEN critical
    When I Run Python Code "from lynx_industrials.metrics.relevance import get_relevance; from lynx_industrials.models import CompanyTier, CompanyStage; print(get_relevance('cash_runway_years', CompanyTier.MICRO, 'solvency', CompanyStage.EXPLORER).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "critical"

Relevance Mature EV EBITDA Critical
    [Documentation]    GIVEN mature operator WHEN I check EV/EBITDA THEN critical
    When I Run Python Code "from lynx_industrials.metrics.relevance import get_relevance; from lynx_industrials.models import CompanyTier, CompanyStage; print(get_relevance('ev_ebitda', CompanyTier.MID, 'valuation', CompanyStage.PRODUCER).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "critical"

Relevance Mature ROIC Critical
    [Documentation]    GIVEN mature operator WHEN I check ROIC THEN critical
    When I Run Python Code "from lynx_industrials.metrics.relevance import get_relevance; from lynx_industrials.models import CompanyTier, CompanyStage; print(get_relevance('roic', CompanyTier.MID, 'profitability', CompanyStage.PRODUCER).value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "critical"

Get Metric Explanation
    [Documentation]    GIVEN metric key WHEN I get explanation THEN details returned
    When I Run Python Code "from lynx_industrials.metrics.explanations import get_explanation; e = get_explanation('gross_margin'); print(e.full_name)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "Gross Margin"

Get Unknown Metric Returns None
    [Documentation]    GIVEN bad key WHEN I get explanation THEN None
    When I Run Python Code "from lynx_industrials.metrics.explanations import get_explanation; print(get_explanation('nonexistent'))"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "None"

Get Sector Insight
    [Documentation]    GIVEN Industrials WHEN I get insight THEN data returned
    When I Run Python Code "from lynx_industrials.metrics.sector_insights import get_sector_insight; s = get_sector_insight('Industrials'); print('OK' if s else 'FAIL')"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "OK"

Get Industry Insight Aerospace
    [Documentation]    GIVEN Aerospace & Defense WHEN I get insight THEN data returned
    When I Run Python Code "from lynx_industrials.metrics.sector_insights import get_industry_insight; i = get_industry_insight('Aerospace & Defense'); print('OK' if i else 'FAIL')"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "OK"

Get Industry Insight Railroads
    [Documentation]    GIVEN Railroads WHEN I get insight THEN data returned
    When I Run Python Code "from lynx_industrials.metrics.sector_insights import get_industry_insight; i = get_industry_insight('Railroads'); print('OK' if i else 'FAIL')"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "OK"

Storage Mode Switching
    [Documentation]    GIVEN storage WHEN I switch modes THEN it works
    When I Run Python Code "from lynx_industrials.core.storage import set_mode, get_mode, is_testing; set_mode('testing'); assert is_testing(); set_mode('production'); assert not is_testing(); print('OK')"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "OK"

Storage Invalid Mode Raises Error
    [Documentation]    GIVEN storage WHEN I set invalid mode THEN error
    When I Run Python Code "from lynx_industrials.core.storage import set_mode; set_mode('invalid')"
    Then The Exit Code Should Be 1
    Then The Output Should Contain "ValueError"

Export Formats Available
    [Documentation]    GIVEN export module WHEN I check formats THEN all exist
    When I Run Python Code "from lynx_industrials.export import ExportFormat; print(ExportFormat.TXT.value, ExportFormat.HTML.value, ExportFormat.PDF.value)"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "txt html pdf"

About Text Has All Fields
    [Documentation]    GIVEN package WHEN I get about THEN all fields present
    When I Run Python Code "from lynx_industrials import get_about_text; a = get_about_text(); assert all(k in a for k in ['name','suite','version','author','license','description']); print('OK')"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "OK"

Conclusion Generation
    [Documentation]    GIVEN minimal report WHEN I generate conclusion THEN a verdict is produced
    When I Run Python Code "from lynx_industrials.models import AnalysisReport, CompanyProfile; from lynx_industrials.core.conclusion import generate_conclusion; r = AnalysisReport(profile=CompanyProfile(ticker='TEST', name='Test')); c = generate_conclusion(r); assert c.verdict in ['Strong Buy','Buy','Hold','Caution','Avoid']; print('OK')"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "OK"

Industrials Metrics In Explanations
    [Documentation]    GIVEN explanations WHEN I list THEN industrials metrics present
    When I Run Python Code "from lynx_industrials.metrics.explanations import list_metrics; keys = [m.key for m in list_metrics()]; assert 'gross_margin' in keys; assert 'quality_score' in keys; assert 'lease_adjusted_debt_ratio' in keys; assert 'backlog_strength' in keys; assert 'operating_ratio' in keys; assert 'book_to_bill_ratio' in keys; print('OK')"
    Then The Exit Code Should Be 0
    Then The Output Should Contain "OK"
