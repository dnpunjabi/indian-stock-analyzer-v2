import re

with open('backend/static/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. business-summary-card (Summary)
html = html.replace(
    '<div class="card col-span-4 no-print" id="business-summary-card" style="margin-bottom: 0px;">',
    '<div class="card col-span-4 no-print" id="business-summary-card" data-subtab="summary" style="margin-bottom: 0px;">'
)

# 2. primary-card (Summary)
html = html.replace(
    '<div class="card col-span-2 primary-card">',
    '<div class="card col-span-2 primary-card" data-subtab="summary">'
)

# 3. Technical Timing card (Technical)
html = html.replace(
    '<!-- Technical & Momentum Indicators Card -->\n                        <div class="card">',
    '<!-- Technical & Momentum Indicators Card -->\n                        <div class="card card-hidden" id="tech-timing-card" data-subtab="technical">'
)

# 4. tech-fib-card (Technical)
html = html.replace(
    '<div class="card" id="tech-fib-card">',
    '<div class="card card-hidden" id="tech-fib-card" data-subtab="technical">'
)

# 5. interactive-capture-card (Technical)
html = html.replace(
    '<div class="card" id="interactive-capture-card">',
    '<div class="card card-hidden" id="interactive-capture-card" data-subtab="technical">'
)

# 6. sandbox-card (Valuation)
html = html.replace(
    '<div class="card col-span-2 sandbox-card no-print" id="sandbox-card">',
    '<div class="card col-span-2 sandbox-card no-print card-hidden" id="sandbox-card" data-subtab="valuation">'
)

# 7. dcf-sensitivity-card (Valuation)
html = html.replace(
    '<div class="card col-span-2" id="dcf-sensitivity-card">',
    '<div class="card col-span-2 card-hidden" id="dcf-sensitivity-card" data-subtab="valuation">'
)

# 8. HISTORICAL P/E BANDS (3-5Y) (Valuation)
html = html.replace(
    '<!-- Historical Valuation Bands Card (Recommendation 2) -->\n                        <div class="card col-span-2">',
    '<!-- Historical Valuation Bands Card (Recommendation 2) -->\n                        <div class="card col-span-2 card-hidden" data-subtab="valuation">'
)

# 9. consensus-comparator-card (Valuation)
html = html.replace(
    '<div class="card col-span-2" id="consensus-comparator-card">',
    '<div class="card col-span-2 card-hidden" id="consensus-comparator-card" data-subtab="valuation">'
)

# 10. earnings-quality-card (Fundamental)
html = html.replace(
    '<div class="card col-span-4" id="earnings-quality-card">',
    '<div class="card col-span-4 card-hidden" id="earnings-quality-card" data-subtab="fundamental">'
)

# 11. HISTORICAL PRICE & TREND ANALYSIS (Technical)
html = html.replace(
    '<!-- Relative Valuation PE Bands & Price Chart (Recommendation 2) -->\n                        <div class="card col-span-4 chart-card">',
    '<!-- Relative Valuation PE Bands & Price Chart (Recommendation 2) -->\n                        <div class="card col-span-4 chart-card card-hidden" data-subtab="technical">'
)

# 12. peers-card (Peers)
html = html.replace(
    '<div class="card col-span-2" id="peers-card">',
    '<div class="card col-span-2 card-hidden" id="peers-card" data-subtab="peers">'
)

# 13. peer-chart-card (Peers)
html = html.replace(
    '<div class="card col-span-4 chart-card no-print" id="peer-chart-card">',
    '<div class="card col-span-4 chart-card no-print card-hidden" id="peer-chart-card" data-subtab="peers">'
)

# 14. shareholding-card (Peers)
html = html.replace(
    '<div class="card" id="shareholding-card">',
    '<div class="card card-hidden" id="shareholding-card" data-subtab="peers">'
)

# 15. tech-volatility-card (Technical)
html = html.replace(
    '<div class="card" id="tech-volatility-card">',
    '<div class="card card-hidden" id="tech-volatility-card" data-subtab="technical">'
)

# 16. return-calculator-card (Fundamental)
html = html.replace(
    '<div class="card col-span-2" id="return-calculator-card">',
    '<div class="card col-span-2 card-hidden" id="return-calculator-card" data-subtab="fundamental">'
)

# 17. drawdown-card (Technical)
html = html.replace(
    '<div class="card col-span-4" id="drawdown-card">',
    '<div class="card col-span-4 card-hidden" id="drawdown-card" data-subtab="technical">'
)

# 18. AI STRATEGIC GROWTH CATALYSTS (Summary)
html = html.replace(
    '<!-- Growth Drivers & Major Risk Factors -->\n                        <div class="card col-span-2">',
    '<!-- Growth Drivers & Major Risk Factors -->\n                        <div class="card col-span-2" data-subtab="summary">'
)

# 19. AI INVESTOR RISK ASSESSMENT (Summary)
# Note: The first col-span-2 card is growth drivers, the second is risk assessment.
# Let's replace the risk assessment card uniquely by matching its structure.
html = html.replace(
    '</h3>\n                        </div>\n\n                        <div class="card col-span-2">',
    '</h3>\n                        </div>\n\n                        <div class="card col-span-2" data-subtab="summary">'
)

# 20. strategical-audit-card (Audit)
html = html.replace(
    '<div class="card col-span-4 no-print" id="strategical-audit-card">',
    '<div class="card col-span-4 no-print card-hidden" id="strategical-audit-card" data-subtab="audit">'
)

# 21. CORPORATE CATALYSTS & NEWS FEED (Summary)
html = html.replace(
    '<!-- Governance & News Feed -->\n                        <div class="card col-span-4 no-print">',
    '<!-- Governance & News Feed -->\n                        <div class="card col-span-4 no-print" data-subtab="summary">'
)

with open('backend/static/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done! Card attributes updated successfully.")
