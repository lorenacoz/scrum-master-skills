# senior-pm

> **Use these instructions for this whole conversation.** Apply them when: Scores portfolio health, risk exposure and resource capacity from a project JSON and frames board-ready status reports. Use when running a portfolio review, writing an executive RAG report, or rebalancing people across projects.

> This skill also ships helper scripts (Python). They are not included here; the instructions work without them.

# Senior Project Management Expert

## Overview

Portfolio-level project management for enterprise software and SaaS: which projects need attention, where the risk sits, whether the people exist to deliver, and how to tell executives. The tools do the arithmetic deterministically; your job is to check their inputs, read the results against the context, and turn them into a decision someone can make.

**Done looks like:** every red or amber project is named with its weakest dimension and a recommended action; every top risk has an owner and a mitigation; capacity gaps are stated in hours per week with the people or dates that close them; the executive ask sits in the first 100 words.

## When to Use

- "Run a portfolio health review", "build an executive status report", "map our stakeholders"
- Several projects compete for the same people and someone has to say which slips
- A board or exec RAG report is due and the current one hides red projects in an average
- A risk register exists but nobody knows which risks matter most or which mitigations are late

Single-team sprint health belongs to `scrum-master/`; cross-team dependency and milestone tracking to `program-manager/`.

## Clarify First

Before generating the report or analysis, settle the inputs below. When one is missing or vague and would change the result, ask about it; when it wouldn't, use a sensible default and say which one you used.

- **Which artifact:** portfolio health review, executive status report, stakeholder map, or risk/capacity analysis (each maps to a different tool and structure).
- **Audience:** board, exec staff, or delivery team (sets the altitude, RAG framing, and level of detail).
- **Portfolio scope and data:** which projects and what timeline/budget/risk data exists (scores and dashboards are only as good as the inputs).
- **Prioritization model:** WSJF, RICE, ICE, or MoSCoW, when ranking projects (each produces a different order).

Ask about the two or three inputs that matter most for this request, not the whole list. If the user wants a result straight away, produce it and state your assumptions at the top.

## Quick Start

Run from the skill folder (``). All four tools print text by default and JSON with `--format json`.

```bash
# Portfolio health: per-project timeline/budget/scope/quality/risk scores and RAG
python3 scripts/project_health_dashboard.py assets/sample_project_data.json

# Risk register: probability x impact matrix, categories, overdue mitigations
python3 scripts/risk_matrix_analyzer.py assets/sample_project_data.json --format json

# Capacity: utilisation per person, weekly demand vs capacity, gaps per project
python3 scripts/resource_capacity_planner.py assets/sample_project_data.json

# Stakeholders: Mendelow quadrant, communication plan, blocker strategies
python3 scripts/stakeholder_mapper.py assets/sample_stakeholders.json
```

`assets/expected_output.json` holds the key numbers these commands produce on the sample, so you can confirm a change did not break the maths.

### Inputs and how the numbers are derived

`sample_project_data.json` is one portfolio file with `portfolio_metadata`, `projects`, `resources` and `risks`. The first three tools read it directly:

| Tool | Reads | Derived values |
|------|-------|----------------|
| `project_health_dashboard.py` | `projects[]`, `risks[]` | Timeline: planned end plus `days_behind_schedule`. Budget: estimate at completion = spent / progress once 20% done, else spent + remaining. Scope: share of milestones due by the as-of date that are complete, less 0.03 per scope change. Quality: 0.7 x test pass rate + 0.3 x coverage, left out (weights renormalised) when both are 0. Risk: sum of probability x impact over the project's open risks. |
| `risk_matrix_analyzer.py` | `risks[]` | Score, level, category concentration, mitigations past `target_resolution` |
| `resource_capacity_planner.py` | `resources[]`, `projects[]` | Weekly demand = remaining budget / blended hourly rate of assigned people, spread over the weeks left; allocation = each person's utilisation split across `current_projects` |
| `stakeholder_mapper.py` | `stakeholders[]` (see `assets/sample_stakeholders.json`) | Quadrant from power and interest (1-10, threshold 5) |

A flat per-project schema (`project_id`, `planned_budget`, `forecasted_total_cost`, ...) is also accepted; see the docstrings. These derivations are heuristics: say so when a number drives a decision, and override with real forecasts when the team has them.

**Dates.** Schedule, milestone and overdue checks use `--as-of YYYY-MM-DD`, defaulting to `portfolio_metadata.generated_on` and otherwise the latest date in the file, so a report is reproducible and the sample does not drift with today's date. Pass `--as-of` with today's date for a live review.

**Exit codes.** `0` report produced · `2` missing or unreadable file, invalid JSON, or the wrong shape (for example no `projects`, a project without `id`, no `stakeholders`). The tools report; they do not gate, so a red project still exits 0.

## Anti-Patterns

### Burying the ask in the executive report
**Mistake:** The 20-slide deck puts the decision the exec must make on slide 14.
**Why it happens:** Decks follow the order the work happened, so the ask lands at the end.
**Instead:** Put the decision or ask on slide 1 or in the first 100 words. Any ask past slide 5 means the report needs restructuring. Executives skim, and a missed ask leads to a decision made on incomplete data.

### Averaging the portfolio into one color
**Mistake:** The dashboard shows portfolio health as a single R/Y/G. Two projects are red, but the aggregate reads yellow.
**Why it happens:** One summary color is what executives asked for, and averaging is the easy way to produce it.
**Instead:** Name each red project next to any aggregate from `project_health_dashboard.py`. Eight greens and two reds is not a yellow portfolio. It has two projects that need attention now.

### A risk matrix with no mitigations
**Mistake:** The risk matrix plots 22 risks by probability and impact, with no mitigation column.
**Why it happens:** Plotting and scoring feel like the analysis, so the plan for each risk gets left for later.
**Instead:** Give every risk a mitigation before the matrix goes to anyone. `risk_matrix_analyzer.py` outputs a mitigation strategy, so carry it into the report instead of showing the plot alone.

Seven more, each with a bad and a good example: `references/red-flags.md`.

## Reference Documentation

Load the reference that matches the task — keep this file lean and pull detail on demand:

- **[references/methodology-and-operations.md](references/methodology-and-operations.md)** — the full three-tier analysis approach, prioritization models, risk framework, stakeholder-mapping detail, asset/template descriptions, weekly/monthly/quarterly workflows, handoff protocols, KPIs, anti-patterns, troubleshooting, success criteria, and Python tool flag reference. Read this for any hands-on portfolio, risk, capacity, or reporting work.
- **[references/portfolio-prioritization-models.md](references/portfolio-prioritization-models.md)** — deep dive on WSJF/RICE/ICE/MoSCoW/MCDA and the model-selection decision tree. Read when choosing or defending a prioritization model.
- **[references/risk-management-framework.md](references/risk-management-framework.md)** — full quantitative risk process: identification, three-point estimation, EMV, portfolio correlation, risk appetite. Read for any non-trivial risk analysis.
- **[references/stakeholder-engagement-guide.md](references/stakeholder-engagement-guide.md)** — Mendelow quadrant playbooks, blocker engagement, communication cadences. Read when building a stakeholder/communication plan.
- **[references/red-flags.md](references/red-flags.md)** — common ways this skill's output goes wrong, with fixes. Read before finalizing a portfolio assessment or executive report.

## Scope & Limitations

**In Scope:** Multi-project portfolio health assessment with weighted composite scoring; probability/impact risk analysis with category weighting (EMV and Monte Carlo by hand, guided by the references); resource capacity planning with utilization optimization and skill-matching; stakeholder mapping with Mendelow's Matrix and targeted communication plans; executive-level reporting with RAG status dashboards and strategic recommendations.

**Out of Scope:** Sprint-level team management (see `scrum-master/`); product backlog management and feature prioritization (see `execution/prioritization-frameworks/`); agile coaching and team maturity (see `agile-coach/`); financial modeling beyond project-level ROI (see `finance/`); contract negotiation and procurement.

**Important Caveats:** Health scores use fixed thresholds (see the script headers); calibrate them to your portfolio. The tools do not compute EMV or Monte Carlo forecasts; `references/risk-management-framework.md` explains how to do that by hand when the decision warrants it. Capacity is a weekly snapshot and assumes the named resources are the whole team, so a project staffed partly by people outside the file shows a large gap; check that before escalating. Inputs are self-reported and the tools check arithmetic, not truth.

## Integration Points

| Integration | Direction | Description |
|------------|-----------|-------------|
| `scrum-master/` | Receives from | Sprint velocity and health metrics feed portfolio-level health dashboards |
| `sprint-retrospective/` | Receives from | Retro insights inform stakeholder reports and process improvement tracking |
| `execution/brainstorm-okrs/` | Feeds into | Portfolio priorities and strategic context shape quarterly OKR themes |
| `execution/outcome-roadmap/` | Feeds into | Portfolio health data influences roadmap commitment levels (Now/Next/Later) |
| `discovery/pre-mortem/` | Receives from | Launch-blocking tigers escalate into portfolio risk register |
| `execution/release-notes/` | Complements | Release notes incorporate stakeholder communication plans from mapper |
| Jira via Atlassian MCP | Bidirectional | Pull project data for health analysis; push status reports to Confluence |
| Financial Systems | Receives from | Real-time budget and spend data for variance analysis |

## Files

| File | Purpose |
|------|---------|
| `scripts/project_health_dashboard.py` | Per-project health scores, RAG, interventions |
| `scripts/risk_matrix_analyzer.py` | Risk matrix, categories, overdue mitigations |
| `scripts/resource_capacity_planner.py` | Utilisation, demand vs capacity, gaps |
| `scripts/stakeholder_mapper.py` | Mendelow quadrants and communication plan |
| `assets/sample_project_data.json` | Four-project portfolio with resources and risks |
| `assets/sample_stakeholders.json` | Ten stakeholders for the mapper |
| `assets/expected_output.json` | Key results of the first three tools on the sample |
| `assets/*_template.md` | Charter, RACI, stakeholder map and executive report templates |

---

# Reference material

Where the instructions above say to read a `references/` file, use the matching section below.

## references/methodology-and-operations.md

# Senior PM — Methodology & Operations

> Read this for the full three-tier analysis approach, prioritization models, risk framework, stakeholder mapping detail, asset/template descriptions, the weekly/monthly/quarterly workflows, handoff protocols, KPIs, anti-patterns, troubleshooting, success criteria, and the Python tool flag reference.

## Methodology & Frameworks

### Three-Tier Analysis Approach

**Tier 1: Portfolio Health Assessment**
Uses `project_health_dashboard.py` to provide comprehensive multi-dimensional scoring:

```bash
python3 scripts/project_health_dashboard.py assets/sample_project_data.json
```

**Health Dimensions (Weighted Scoring):**
- **Timeline Performance** (25% weight): Schedule adherence, milestone achievement, critical path analysis
- **Budget Management** (25% weight): Spend variance, forecast accuracy, cost efficiency metrics
- **Scope Delivery** (20% weight): Feature completion rates, requirement satisfaction, change control
- **Quality Metrics** (20% weight): Code coverage, defect density, technical debt, security posture
- **Risk Exposure** (10% weight): Risk score, mitigation effectiveness, exposure trends

**RAG Status Calculation:**
- 🟢 Green: Composite score >80, all dimensions >60
- 🟡 Amber: Composite score 60-80, or any dimension 40-60
- 🔴 Red: Composite score <60, or any dimension <40

**Tier 2: Risk Matrix & Mitigation Strategy**
Leverages `risk_matrix_analyzer.py` for quantitative risk assessment:

```bash
python3 scripts/risk_matrix_analyzer.py assets/sample_project_data.json
```

**Risk Quantification Process:**
1. **Probability Assessment** (1-5 scale): Historical data, expert judgment, Monte Carlo inputs
2. **Impact Analysis** (1-5 scale): Financial, schedule, quality, and strategic impact vectors
3. **Category Weighting**: Technical (1.2x), Resource (1.1x), Financial (1.4x), Schedule (1.0x)
4. **EMV Calculation**: Risk Score = (Probability × Impact × Category Weight)

**Risk Response Strategies:**
- **Avoid** (>18 score): Eliminate through scope/approach changes
- **Mitigate** (12-18 score): Reduce probability or impact through active intervention
- **Transfer** (8-12 score): Insurance, contracts, partnerships
- **Accept** (<8 score): Monitor with contingency planning

**Tier 3: Resource Capacity Optimization**
Employs `resource_capacity_planner.py` for portfolio resource analysis:

```bash
python3 scripts/resource_capacity_planner.py assets/sample_project_data.json
```

**Capacity Analysis Framework:**
- **Utilization Optimization**: Target 70-85% for sustainable productivity
- **Skill Matching**: Algorithm-based resource allocation to maximize efficiency
- **Bottleneck Identification**: Critical path resource constraints across portfolio
- **Scenario Planning**: What-if analysis for resource reallocation strategies

### Advanced Prioritization Models

**Weighted Shortest Job First (WSJF) - For Agile Portfolios**
```
WSJF Score = (User Value + Time Criticality + Risk Reduction) ÷ Job Size

Application Context:
- Resource-constrained environments
- Fast-moving competitive landscapes  
- Agile/SAFe methodology adoption
- Clear cost-of-delay quantification available
```

**RICE Framework - For Product Development**
```
RICE Score = (Reach × Impact × Confidence) ÷ Effort

Best for:
- Customer-facing initiatives
- Marketing and growth projects
- When reach metrics are quantifiable
- Data-driven product decisions
```

**ICE Scoring - For Rapid Decision Making**
```  
ICE Score = (Impact + Confidence + Ease) ÷ 3

Optimal when:
- Quick prioritization needed
- Brainstorming and ideation phases
- Limited analysis time available
- Cross-functional team alignment required
```

**Decision Tree for Model Selection:**
Reference: `references/portfolio-prioritization-models.md`

- **Resource Constrained?** → WSJF
- **Customer Impact Focus?** → RICE
- **Need Speed?** → ICE
- **Multiple Stakeholder Groups?** → MoSCoW
- **Complex Trade-offs?** → Multi-Criteria Decision Analysis (MCDA)

### Risk Management Framework

**Quantitative Risk Analysis Process:**
Reference: `references/risk-management-framework.md`

**Step 1: Risk Identification & Classification**
- Technical risks: Architecture, integration, performance
- Resource risks: Availability, skills, retention
- Schedule risks: Dependencies, critical path, external factors
- Financial risks: Budget overruns, currency, economic factors
- Business risks: Market changes, competitive pressure, strategic shifts

**Step 2: Probability/Impact Assessment**
Uses three-point estimation for Monte Carlo simulation:
```
Expected Value = (Optimistic + 4×Most Likely + Pessimistic) ÷ 6
Standard Deviation = (Pessimistic - Optimistic) ÷ 6
```

**Step 3: Expected Monetary Value (EMV) Calculation**
```
EMV = Σ(Probability × Financial Impact) for all risk scenarios

Risk-Adjusted Budget = Base Budget × (1 + Risk Premium)
Risk Premium = Portfolio Risk Score × Risk Tolerance Factor
```

**Step 4: Portfolio Risk Correlation Analysis**
```
Portfolio Risk = √(Σ Individual Risks² + 2Σ Correlation×Risk1×Risk2)
```

**Risk Appetite Framework:**
- **Conservative**: Risk scores 0-8, 25-30% contingency reserves
- **Moderate**: Risk scores 8-15, 15-20% contingency reserves  
- **Aggressive**: Risk scores 15+, 10-15% contingency reserves

## Stakeholder Mapping & Engagement

### Power/Interest Grid (Mendelow's Matrix)

Uses `stakeholder_mapper.py` to classify stakeholders and generate communication plans:

```bash
python3 scripts/stakeholder_mapper.py stakeholders.json
python3 scripts/stakeholder_mapper.py --demo --format json
```

**Classification Quadrants (threshold at 5/10):**
- **Manage Closely** (High Power, High Interest): Weekly 1:1s, steering committee, proactive escalation
- **Keep Satisfied** (High Power, Low Interest): Monthly executive summary, milestone invites
- **Keep Informed** (Low Power, High Interest): Bi-weekly newsletter, demo invites, dashboards
- **Monitor** (Low Power, Low Interest): Quarterly updates, organizational newsletter

**Blocker Engagement Strategy:**
The tool identifies stakeholders with `attitude: blocker` and generates targeted engagement strategies based on their power level — high-power blockers require urgent 1:1 engagement and potential executive sponsor escalation; low-power blockers need transparency and involvement.

**Integration with OKR Brainstorming:**
Stakeholder mapping feeds directly into OKR alignment — high-power/high-interest stakeholders shape strategic objectives, while their feedback validates Key Results. Cross-reference with `execution/brainstorm-okrs/` for OKR development workflows.

Reference: `references/stakeholder-engagement-guide.md`
Template: `assets/stakeholder_map_template.md`

## Assets & Templates

### Project Charter Template
Reference: `assets/project_charter_template.md`

**Comprehensive 12-section charter including:**
- Executive summary with strategic alignment
- Success criteria with KPIs and quality gates
- RACI matrix with decision authority levels
- Risk assessment with mitigation strategies
- Budget breakdown with contingency analysis
- Timeline with critical path dependencies

**Key Features:**
- Production-ready for board presentation
- Integrated stakeholder management framework
- Risk-adjusted financial projections
- Change control and governance processes

### Executive Report Template  
Reference: `assets/executive_report_template.md`

**Board-level portfolio reporting with:**
- RAG status dashboard with trend analysis
- Financial performance vs. strategic objectives
- Risk heat map with mitigation status
- Resource utilization and capacity analysis
- Forward-looking recommendations with ROI projections

**Executive Decision Support:**
- Critical issues requiring immediate action
- Investment recommendations with business cases
- Portfolio optimization opportunities
- Market/competitive intelligence integration

### RACI Matrix Template
Reference: `assets/raci_matrix_template.md`

**Enterprise-grade responsibility assignment featuring:**
- Detailed stakeholder roster with decision authority
- Phase-based RACI assignments (initiation through deployment)
- Escalation paths with timeline and authority levels
- Communication protocols and meeting frameworks
- Conflict resolution processes with governance integration

**Advanced Features:**
- Decision-making RACI for strategic vs. operational choices
- Risk and issue management responsibility assignment
- Performance metrics for RACI effectiveness
- Template validation checklist and maintenance procedures

### Sample Portfolio Data
Reference: `assets/sample_project_data.json`

**Realistic multi-project portfolio including:**
- 4 projects across different phases and priorities
- Complete financial data (budgets, actuals, forecasts)
- Resource allocation with utilization metrics
- Risk register with probability/impact scoring
- Quality metrics and stakeholder satisfaction data
- Dependencies and milestone tracking

**Data Completeness:**
- Works with all three analysis scripts
- Demonstrates portfolio balance across strategic priorities
- Includes both successful and at-risk project examples
- Provides historical trend data for analysis

### Expected Output Examples
Reference: `assets/expected_output.json`

**Demonstrates script capabilities with:**
- Portfolio health scores and RAG status
- Risk matrix visualization and mitigation priorities
- Resource capacity analysis with optimization recommendations
- Integration examples showing how outputs complement each other

## Implementation Workflows

### Portfolio Health Review (Weekly)

1. **Data Collection & Validation**
   ```bash
   # Update project data from JIRA, financial systems, team surveys
   python3 scripts/project_health_dashboard.py current_portfolio.json
   ```
   - *Validate:* all 5 health dimensions have current-period data; no project missing more than one dimension
2. **Risk Assessment Update**
   ```bash
   # Refresh risk probabilities and impact assessments
   python3 scripts/risk_matrix_analyzer.py current_portfolio.json
   ```
   - *Validate:* every critical/high risk has an active mitigation owner; no risks aged >30 days without update
3. **Capacity Analysis**
   ```bash  
   # Review resource utilization and bottlenecks
   python3 scripts/resource_capacity_planner.py current_portfolio.json
   ```
   - *Validate:* utilization sits in the 70-85% optimal band; hotspots flagged with a named resolution action
4. **Executive Summary Generation**
   - Synthesize outputs into executive report format
   - Highlight critical issues and recommendations
   - Prepare stakeholder communications
   - *Validate:* one-page RAG summary fits the audience; every red status has a documented intervention plan inside 48 hours

### Monthly Strategic Review

1. **Portfolio Prioritization Review**
   - Apply WSJF/RICE/ICE models to evaluate current priorities
   - Assess strategic alignment with business objectives
   - Identify optimization opportunities

2. **Risk Portfolio Analysis**
   - Update risk appetite and tolerance levels
   - Review portfolio risk correlation and concentration
   - Adjust risk mitigation investments

3. **Resource Optimization Planning**
   - Analyze capacity constraints across upcoming quarter
   - Plan resource reallocation and hiring strategies
   - Identify skill gaps and training needs

4. **Stakeholder Alignment Session**
   - Present portfolio health and strategic recommendations
   - Gather feedback on prioritization and resource allocation
   - Align on upcoming quarter priorities and investments

### Quarterly Portfolio Optimization

1. **Strategic Alignment Assessment**
   - Evaluate portfolio contribution to business objectives
   - Assess market and competitive position changes
   - Update strategic priorities and success criteria

2. **Financial Performance Review**
   - Analyze risk-adjusted ROI across portfolio
   - Review budget performance and forecast accuracy
   - Optimize investment allocation for maximum value

3. **Capability Gap Analysis**
   - Identify emerging technology and skill requirements
   - Plan capability building investments
   - Assess make vs. buy vs. partner decisions

4. **Portfolio Rebalancing**
   - Apply three horizons model for innovation balance
   - Optimize risk-return profile using efficient frontier
   - Plan new initiatives and sunset decisions

## Integration Strategies

### Atlassian Integration
- **Jira**: Portfolio dashboards, cross-project metrics, risk tracking
- **Confluence**: Strategic documentation, executive reports, knowledge management
- Use MCP integrations to automate data collection and report generation

### Financial Systems Integration
- **Budget Tracking**: Real-time spend data for variance analysis
- **Resource Costing**: Hourly rates and utilization for capacity planning
- **ROI Measurement**: Value realization tracking against projections

### Stakeholder Management
- **Executive Dashboards**: Real-time portfolio health visualization
- **Team Scorecards**: Individual project performance metrics
- **Risk Registers**: Collaborative risk management with automated escalation

## Handoff Protocols

### TO Scrum Master
**Context Transfer:**
- Strategic priorities and success criteria
- Resource allocation and team composition
- Risk factors requiring sprint-level attention
- Quality standards and acceptance criteria

**Ongoing Collaboration:**
- Weekly velocity and health metrics review
- Sprint retrospective insights for portfolio learning
- Impediment escalation and resolution support
- Team capacity and utilization feedback

### TO Product Owner
**Strategic Context:**
- Market prioritization and competitive analysis
- User value frameworks and measurement criteria
- Feature prioritization aligned with portfolio objectives
- Resource and timeline constraints

**Decision Support:**
- ROI analysis for feature investments
- Risk assessment for product decisions
- Market intelligence and customer feedback integration
- Strategic roadmap alignment and dependencies

### FROM Executive Team
**Strategic Direction:**
- Business objective updates and priority changes
- Budget allocation and resource approval decisions
- Risk appetite and tolerance level adjustments
- Market strategy and competitive response decisions

**Performance Expectations:**
- Portfolio health and value delivery targets
- Timeline and milestone commitment expectations
- Quality standards and compliance requirements
- Stakeholder satisfaction and communication standards

## Success Metrics & KPIs

### Portfolio Performance Indicators
- **On-time Delivery Rate**: >80% projects delivered within 10% of planned timeline
- **Budget Variance**: <5% average variance across portfolio
- **Quality Score**: >85 composite quality rating across all projects
- **Risk Mitigation Effectiveness**: >90% risks with active mitigation plans
- **Resource Utilization**: 75-85% average utilization across teams

### Strategic Value Indicators  
- **ROI Achievement**: >90% projects meeting ROI projections within 12 months
- **Strategic Alignment**: >95% portfolio investment aligned with business priorities
- **Innovation Balance**: 70% operational, 20% growth, 10% transformational projects
- **Stakeholder Satisfaction**: >8.5/10 average satisfaction across executive stakeholders
- **Value Acceleration**: <6 months average time from completion to value realization

### Risk Management Indicators
- **Risk Exposure Level**: Maintain within approved risk appetite ranges
- **Risk Resolution Time**: <30 days average for medium risks, <7 days for high risks
- **Mitigation Cost Efficiency**: Mitigation spend <20% of total portfolio risk EMV
- **Risk Prediction Accuracy**: >70% accuracy in risk probability assessments

## Continuous Improvement Framework

### Portfolio Learning Integration
- Capture lessons learned from completed projects
- Update risk probability assessments based on historical data
- Refine estimation accuracy through retrospective analysis
- Share best practices across project teams

### Methodology Evolution
- Regular review of prioritization model effectiveness
- Update risk frameworks based on industry best practices
- Integrate new tools and technologies for analysis efficiency
- Benchmark against industry portfolio performance standards

### Stakeholder Feedback Integration
- Quarterly stakeholder satisfaction surveys
- Executive interview feedback on decision support quality
- Team feedback on process efficiency and effectiveness
- Customer impact assessment of portfolio decisions

This skill represents the pinnacle of enterprise project management capability, providing both strategic oversight and tactical execution support for complex digital transformation initiatives. The combination of quantitative analysis, sophisticated prioritization, and executive-level communication enables senior project managers to drive significant business value while managing enterprise-level risks and complexities.

## Anti-patterns

| Anti-pattern | Failure mode | Fix |
|--------------|--------------|-----|
| RAG status assigned by gut feel, not by dimension scoring | Optimism bias; reds surface too late; executives lose trust in the reports | Use `project_health_dashboard.py` thresholds and calibrate dimension weights with sponsors — don't override without documenting why |
| Risk register full of "medium" risks | Team avoiding extreme ratings; no actionable signal | Run a calibration workshop with reference incidents; force a distribution across low/medium/high/critical |
| Portfolio-level decisions made from project-level dashboards | Local optimization; strategic misalignment; hidden dependencies | Aggregate via portfolio view; apply WSJF/RICE across the portfolio, not per project |
| Capacity planner shows zero gaps while teams complain of overload | Utilization excludes meeting overhead, context-switching, unplanned work | Include 15% meeting overhead and 5% context-switching; validate against team self-reports |
| Stakeholder map classifies everyone as "Manage Closely" | Thresholds too low or scores inflated; dilutes engagement plan | Use relative ranking within the group; enforce the 4-quadrant split |
| Executive reports written for the PM, not the executive | Attention drops; decisions delayed; report becomes an artifact not a tool | Lead with RAG + top 3 decisions needed; push dimension detail to an appendix |
| Treating EMV as a point estimate | Planning against a single number; surprise when variance arrives | Present EMV with a confidence range; layer Monte Carlo for schedule-critical projects |
| Ignoring risk correlation across projects | Shared dependency fails and multiple projects go red simultaneously | Run portfolio-level correlation analysis quarterly; flag shared vendors, shared teams, shared infra |
| Rebalancing the portfolio reactively (project-by-project) instead of on a cadence | Whiplash for teams; rebalancing becomes political | Quarterly rebalancing on a fixed cadence using three horizons and efficient-frontier view |

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---------|-------------|------------|
| Portfolio health score does not match stakeholder perception | Dimension weights misaligned with organizational priorities, or data inputs incomplete | Recalibrate HEALTH_DIMENSIONS weights with executive sponsors; ensure all 5 dimensions have data |
| Risk matrix shows all risks clustered in medium zone | Probability/impact scoring lacks granularity or team avoids extreme ratings | Facilitate risk calibration workshop; use three-point estimation and reference past incidents |
| Resource capacity planner shows zero gaps despite team complaints | Utilization data does not account for meeting overhead, context-switching, or unplanned work | Verify CAPACITY_FACTORS config; include 15% meeting overhead and 5% context-switching penalty |
| Stakeholder mapper classifies everyone as "Manage Closely" | Power/interest thresholds too low for your organization, or scores inflated | Adjust POWER_THRESHOLD and INTEREST_THRESHOLD (default: 5); use relative ranking within group |
| RAG status oscillates between green and amber weekly | Thresholds set too tight, or data updates cause noise | Widen amber band (e.g., 55-80 instead of 60-80); use rolling 2-week average instead of point-in-time |
| EMV calculations produce unrealistically high risk exposure | Category weights compounding with high probability/impact scores | Review RISK_CATEGORIES weights; cap financial risk weight at 1.4x; validate probability estimates against historical data |
| Executive reports are too long for stakeholder attention span | Report template includes too many detail sections for the audience | Tailor output to audience using the tone guide; executives need 1-page RAG summary, not full dimension breakdown |

## Success Criteria

- Portfolio average health score maintained above 75/100 across all active projects
- On-time delivery rate exceeds 80% (within 10% of planned timeline)
- Budget variance maintained below 5% average across the portfolio
- Risk mitigation effectiveness above 90% (all critical/high risks have active mitigation plans)
- Resource utilization consistently in the 70-85% optimal range
- Stakeholder satisfaction above 8.5/10 as measured by quarterly surveys
- All projects in red RAG status have documented intervention plans within 48 hours

## Tool Reference

### project_health_dashboard.py

Aggregates project metrics across timeline, budget, scope, quality, and risk dimensions. Produces composite health scores and RAG status.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `data_file` | positional | (required) | Path to JSON file containing project portfolio data |
| `--format` | choice | `text` | Output format: `text` or `json` |
| `--as-of` | date | `portfolio_metadata.generated_on`, else latest date in the data | Evaluation date for schedule, milestone and overdue checks |

### risk_matrix_analyzer.py

Builds probability/impact matrices, calculates weighted risk scores by category, and suggests mitigation strategies.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `data_file` | positional | (required) | Path to JSON file containing risk register data |
| `--format` | choice | `text` | Output format: `text` or `json` |
| `--as-of` | date | `portfolio_metadata.generated_on`, else latest date in the data | Evaluation date for schedule, milestone and overdue checks |

### resource_capacity_planner.py

Models team capacity across projects, identifies utilization imbalances, and provides optimization recommendations.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `data_file` | positional | (required) | Path to JSON file containing resource and project capacity data |
| `--format` | choice | `text` | Output format: `text` or `json` |
| `--as-of` | date | `portfolio_metadata.generated_on`, else latest date in the data | Evaluation date for schedule, milestone and overdue checks |

### stakeholder_mapper.py

Classifies stakeholders into Mendelow's Matrix quadrants and generates tailored communication plans with blocker engagement strategies.

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `data_file` | positional | (optional) | Path to JSON file with stakeholder data |
| `--format` | choice | `text` | Output format: `text` or `json` |
| `--demo` | flag | off | Run with built-in sample data (10 stakeholders) |

## references/portfolio-prioritization-models.md

# Portfolio Prioritization Models & Decision Frameworks

## Executive Overview

This reference guide provides senior project managers with sophisticated prioritization methodologies for managing complex project portfolios. It covers quantitative scoring models (WSJF, ICE, RICE), qualitative frameworks (MoSCoW, Kano), and decision trees for selecting the optimal prioritization approach based on context, stakeholder needs, and strategic objectives.

---

## Model Selection Decision Tree

### Context-Based Framework Selection

```
START: What is your primary prioritization objective?

├── Maximize Business Value & ROI
│   ├── Clear quantitative metrics available? → RICE Model
│   └── Mix of quantitative/qualitative factors? → Weighted Scoring Matrix
│
├── Optimize Resource Utilization  
│   ├── Agile/SAFe environment? → WSJF (Weighted Shortest Job First)
│   └── Traditional PM environment? → Resource-Constraint Optimization
│
├── Stakeholder Alignment & Buy-in
│   ├── Multiple stakeholder groups? → MoSCoW Method
│   └── Customer-focused prioritization? → Kano Analysis
│
├── Speed of Decision Making
│   ├── Need rapid decisions? → ICE Scoring
│   └── Complex trade-offs acceptable? → Multi-Criteria Decision Analysis
│
└── Strategic Portfolio Balance
    ├── Innovation vs. Operations balance? → Three Horizons Model
    └── Risk vs. Return optimization? → Efficient Frontier Analysis
```

---

## Quantitative Prioritization Models

### 1. WSJF (Weighted Shortest Job First)

**Best Used For:** Agile portfolios, resource-constrained environments, when cost of delay is critical

**Formula:** `WSJF Score = (User/Business Value + Time Criticality + Risk Reduction) ÷ Job Size`

#### Detailed Scoring Framework

**User/Business Value (1-20 scale):**
- **1-5:** Nice to have improvements, minimal user impact
- **6-10:** Moderate value, affects subset of users/processes
- **11-15:** Significant value, major user/business impact
- **16-20:** Critical value, transformational business impact

**Time Criticality (1-20 scale):**
- **1-5:** No time pressure, can be delayed 12+ months
- **6-10:** Some urgency, should complete within 6-12 months
- **11-15:** Urgent, needed within 3-6 months
- **16-20:** Critical time pressure, needed within 1-3 months

**Risk Reduction/Opportunity Enablement (1-20 scale):**
- **1-5:** Minimal risk mitigation or future opportunity impact
- **6-10:** Moderate risk reduction or enables some future work
- **11-15:** Significant risk mitigation or enables key capabilities
- **16-20:** Critical risk mitigation or foundational for future strategy

**Job Size (1-20 scale, reverse scored):**
- **1-5:** Very large (>12 months, >$2M, >20 people)
- **6-10:** Large (6-12 months, $1-2M, 10-20 people)
- **11-15:** Medium (3-6 months, $500K-1M, 5-10 people)
- **16-20:** Small (<3 months, <$500K, <5 people)

#### WSJF Implementation Example

```
Project A: Mobile App Enhancement
- User Value: 15 (significant user experience improvement)
- Time Criticality: 12 (competitive pressure, 4-month window)
- Risk Reduction: 8 (moderate technical debt reduction)
- Job Size: 14 (3-month project, $750K, 7 people)
WSJF = (15 + 12 + 8) ÷ 14 = 2.5

Project B: Infrastructure Security Upgrade  
- User Value: 8 (minimal user-facing impact)
- Time Criticality: 18 (regulatory compliance deadline)
- Risk Reduction: 17 (critical security vulnerability mitigation)
- Job Size: 10 (8-month project, $1.5M, 12 people)
WSJF = (8 + 18 + 17) ÷ 10 = 4.3

Result: Project B prioritized despite lower user value due to criticality and risk reduction.
```

### 2. RICE Framework

**Best Used For:** Product development, marketing initiatives, when reach and impact can be quantified

**Formula:** `RICE Score = (Reach × Impact × Confidence) ÷ Effort`

#### RICE Scoring Guidelines

**Reach (Number per time period):**
- **Projects:** Number of users/customers/processes affected per month
- **Internal Initiatives:** Number of employees/systems/workflows impacted
- **Strategic Programs:** Market size or business units affected

**Impact (Multiplier scale):**
- **3.0:** Massive impact - Transforms core business metrics
- **2.0:** High impact - Significantly improves key metrics
- **1.0:** Medium impact - Moderately improves metrics
- **0.5:** Low impact - Slight improvement in metrics
- **0.25:** Minimal impact - Barely measurable improvement

**Confidence (Percentage as decimal):**
- **100% (1.0):** High confidence - Strong data and precedent
- **80% (0.8):** Medium confidence - Some data, reasonable assumptions
- **50% (0.5):** Low confidence - Limited data, high uncertainty

**Effort (Person-months):**
- Total estimated effort across all teams and functions
- Include planning, design, development, testing, deployment, training

#### RICE Application Example

```
Initiative: Customer Self-Service Portal
- Reach: 50,000 customers per month
- Impact: 1.0 (moderate reduction in support calls)
- Confidence: 0.8 (good data from customer surveys)
- Effort: 18 person-months
RICE = (50,000 × 1.0 × 0.8) ÷ 18 = 2,222

Initiative: Sales Process Automation
- Reach: 200 sales reps per month
- Impact: 2.0 (significant productivity improvement)
- Confidence: 0.9 (pilot data available)
- Effort: 12 person-months
RICE = (200 × 2.0 × 0.9) ÷ 12 = 30

Result: Sales automation prioritized despite much smaller reach due to high impact and efficiency.
```

### 3. ICE Scoring

**Best Used For:** Rapid prioritization, brainstorming sessions, when detailed analysis isn't feasible

**Formula:** `ICE Score = (Impact + Confidence + Ease) ÷ 3`

Each dimension scored 1-10:

**Impact (1-10):**
- **10:** Revolutionary change, massive business impact
- **7-9:** Significant improvement in key metrics
- **4-6:** Moderate positive impact
- **1-3:** Minimal or unclear impact

**Confidence (1-10):**
- **10:** Certain of outcome, strong data/precedent
- **7-9:** High confidence, some supporting evidence
- **4-6:** Medium confidence, reasonable assumptions
- **1-3:** Low confidence, uncertain outcome

**Ease (1-10):**
- **10:** Minimal effort, existing resources, low complexity
- **7-9:** Moderate effort, some new resources needed
- **4-6:** Significant effort, substantial resource commitment
- **1-3:** Very difficult, major resource investment

#### ICE Prioritization Matrix

| Initiative | Impact | Confidence | Ease | ICE Score | Priority |
|------------|--------|------------|------|-----------|----------|
| API Documentation Update | 6 | 9 | 9 | 8.0 | High |
| Machine Learning Platform | 9 | 5 | 3 | 5.7 | Medium |
| Mobile App Redesign | 8 | 7 | 5 | 6.7 | Medium-High |
| Data Warehouse Migration | 7 | 8 | 2 | 5.7 | Medium |

---

## Qualitative Prioritization Frameworks

### 1. MoSCoW Method

**Best Used For:** Scope management, stakeholder alignment, requirement prioritization

**Categories:**
- **Must Have:** Non-negotiable requirements, project fails without these
- **Should Have:** Important but not critical, can be delayed if necessary  
- **Could Have:** Nice to have, include if resources permit
- **Won't Have:** Explicitly out of scope for current timeframe

#### MoSCoW Implementation Guidelines

**Must Have Criteria:**
- Legal/regulatory requirement
- Critical business process dependency
- Fundamental system functionality
- Security/compliance necessity

**Should Have Criteria:**
- Significant user value or business benefit
- Competitive advantage requirement
- Important process improvement
- Strong stakeholder demand

**Could Have Criteria:**
- Enhancement to user experience
- Process optimization opportunity
- Future-proofing consideration
- Secondary stakeholder request

**Won't Have Criteria:**
- Feature creep identification
- Future phase consideration
- Out-of-budget items
- Low-value/high-effort items

#### MoSCoW with Quantitative Overlay

```
Priority Distribution Guidelines:
- Must Have: 60% of budget/effort (ensures core delivery)
- Should Have: 20% of budget/effort (key value delivery)  
- Could Have: 20% of budget/effort (buffer for scope adjustment)
- Won't Have: Document for future consideration

Risk Management:
- If Must Haves exceed 60%: Scope too large, requires reduction
- If Should Haves exceed 30%: Risk of scope creep
- If Could Haves exceed 20%: May indicate unclear priorities
```

### 2. Kano Model Analysis

**Best Used For:** Customer-focused prioritization, product development, user experience improvements

#### Kano Categories

**Basic Needs (Must-Be):**
- **Definition:** Expected features, dissatisfaction if absent
- **Customer Response:** "Of course it should do that"
- **Business Impact:** Prevents customer loss but doesn't drive acquisition
- **Examples:** Security, basic functionality, compliance

**Performance Needs (More-Is-Better):**
- **Definition:** Linear satisfaction relationship with performance
- **Customer Response:** "The better it performs, the happier I am"
- **Business Impact:** Competitive differentiation opportunity
- **Examples:** Speed, efficiency, cost, reliability

**Excitement Needs (Delighters):**
- **Definition:** Unexpected features that create delight
- **Customer Response:** "Wow, I didn't expect that!"
- **Business Impact:** Customer acquisition and loyalty driver
- **Examples:** Innovative features, exceptional experiences

**Indifferent Features:**
- **Definition:** Features customers don't care about
- **Customer Response:** "Whatever, doesn't matter to me"
- **Business Impact:** Resource waste if prioritized
- **Action:** Eliminate or deprioritize

**Reverse Features:**
- **Definition:** Features that actually create dissatisfaction
- **Customer Response:** "I wish this wasn't here"
- **Business Impact:** Customer churn risk
- **Action:** Remove immediately

#### Kano Prioritization Matrix

| Feature | Kano Category | Customer Impact | Implementation Cost | Priority Score |
|---------|---------------|-----------------|-------------------|----------------|
| Single Sign-On | Basic | High Dissatisfaction if Missing | Medium | Must Do |
| Load Time <2sec | Performance | Linear Satisfaction | High | High Priority |
| AI-Powered Recommendations | Excitement | High Delight Potential | Very High | Medium Priority |
| Advanced Analytics Dashboard | Indifferent | Low Interest | Medium | Low Priority |

---

## Advanced Prioritization Models

### 1. Multi-Criteria Decision Analysis (MCDA)

**Best Used For:** Complex portfolios with multiple competing objectives and diverse stakeholder interests

#### Weighted Scoring Matrix Setup

**Step 1: Define Evaluation Criteria**
```
Strategic Criteria (40% weight):
- Strategic Alignment (15%)
- Market Opportunity (10%) 
- Competitive Advantage (15%)

Financial Criteria (35% weight):
- ROI/NPV (20%)
- Payback Period (10%)
- Cost Efficiency (5%)

Risk/Feasibility Criteria (25% weight):
- Technical Risk (10%)
- Resource Availability (10%)
- Timeline Feasibility (5%)
```

**Step 2: Score Each Project (1-5 scale)**

**Step 3: Calculate Weighted Scores**
```
Project Score = Σ(Criterion Score × Criterion Weight)

Example:
Project Alpha:
- Strategic Alignment: 4 × 0.15 = 0.60
- Market Opportunity: 5 × 0.10 = 0.50
- Competitive Advantage: 3 × 0.15 = 0.45
- ROI/NPV: 4 × 0.20 = 0.80
- Payback Period: 3 × 0.10 = 0.30
- Cost Efficiency: 5 × 0.05 = 0.25
- Technical Risk: 2 × 0.10 = 0.20
- Resource Availability: 4 × 0.10 = 0.40
- Timeline Feasibility: 4 × 0.05 = 0.20
Total Score: 3.70
```

### 2. Three Horizons Model

**Best Used For:** Balancing innovation with operational excellence, strategic portfolio planning

#### Horizon Definitions

**Horizon 1: Core Business (70% of portfolio)**
- **Focus:** Optimize existing products/services
- **Timeline:** 0-2 years
- **Risk Level:** Low
- **ROI Expectation:** High certainty, moderate returns
- **Examples:** Process improvements, maintenance, incremental features

**Horizon 2: Emerging Opportunities (20% of portfolio)**
- **Focus:** Extend core capabilities into new areas
- **Timeline:** 2-5 years  
- **Risk Level:** Medium
- **ROI Expectation:** Medium certainty, high returns
- **Examples:** New markets, adjacent products, platform extensions

**Horizon 3: Transformational Initiatives (10% of portfolio)**
- **Focus:** Create new capabilities and business models
- **Timeline:** 5+ years
- **Risk Level:** High
- **ROI Expectation:** Low certainty, very high potential returns
- **Examples:** Breakthrough technologies, new business models, moonshots

#### Portfolio Balance Guidelines

```
Balanced Portfolio Allocation:
- Conservative Organization: H1=80%, H2=15%, H3=5%
- Growth-Oriented: H1=60%, H2=25%, H3=15%
- Innovation Leader: H1=50%, H2=30%, H3=20%

Risk Management:
- H1 projects should fund H2 and H3 experiments
- H2 successes should scale to become new H1 businesses
- H3 failures should generate learning for future initiatives
```

### 3. Efficient Frontier Analysis

**Best Used For:** Risk-return optimization, portfolio-level resource allocation

#### Risk-Return Plotting

**Step 1: Quantify Risk and Return for Each Project**
```
Return Metrics:
- Expected NPV or IRR
- Strategic value score
- Market opportunity size

Risk Metrics:
- Probability of failure
- Variance in expected outcomes
- Technical/market uncertainty
```

**Step 2: Plot Projects on Risk-Return Matrix**

**Step 3: Identify Efficient Frontier**
- Projects offering maximum return for each risk level
- Projects below the frontier are suboptimal
- Portfolio optimization involves selecting mix along frontier

**Step 4: Apply Risk Appetite**
- Conservative: Lower risk portion of frontier
- Moderate: Balanced mix across frontier
- Aggressive: Higher risk/return portion

#### Portfolio Optimization Example

```
Efficient Frontier Projects:
- Low Risk/Low Return: Process Automation (Risk=2, Return=15%)
- Medium Risk/Medium Return: Market Expansion (Risk=5, Return=25%)
- High Risk/High Return: New Technology Platform (Risk=8, Return=45%)

Suboptimal Projects:
- High Risk/Low Return: Legacy System Upgrade (Risk=7, Return=12%)
- Reason: Market Expansion offers better return for similar risk level
```

---

## Decision Trees for Model Selection

### Scenario-Based Model Selection

#### Scenario 1: Resource-Constrained Environment
```
Available Resources < Demand?
├── Yes: Use WSJF (maximize value per unit effort)
└── No: Use RICE or Weighted Scoring (optimize for maximum impact)

Time Pressure for Decisions?
├── High: Use ICE Scoring (rapid evaluation)
└── Low: Use MCDA (thorough analysis)

Stakeholder Alignment Issues?
├── Yes: Use MoSCoW (consensus building)
└── No: Proceed with quantitative method
```

#### Scenario 2: Innovation vs. Operations Balance
```
Portfolio Currently Imbalanced?
├── Too Operational: Apply Three Horizons Model (increase H2/H3)
├── Too Innovative: Focus on H1 projects (stabilize revenue)
└── Balanced: Use efficient frontier analysis (optimize mix)

Strategic Direction Clear?
├── Yes: Use strategic alignment scoring
└── No: Use broad stakeholder input (MoSCoW or Kano)
```

#### Scenario 3: Customer vs. Business Value Tension
```
Primary Value Driver?
├── Customer Satisfaction: Use Kano Analysis
├── Business ROI: Use RICE or financial scoring
└── Both Equally Important: Use balanced scorecard approach

Data Availability?
├── Rich Customer Data: Kano → RICE combination
├── Limited Data: ICE scoring → MoSCoW validation
└── Financial Data Only: WSJF or NPV ranking
```

---

## Hybrid Prioritization Approaches

### 1. Two-Stage Prioritization

**Stage 1: Strategic Filtering**
- Apply MoSCoW or Strategic Alignment Filter
- Eliminate projects that don't meet minimum criteria
- Reduce candidate pool by 40-60%

**Stage 2: Detailed Scoring**
- Apply WSJF, RICE, or MCDA to remaining candidates
- Rank order for resource allocation
- Final prioritization with stakeholder review

### 2. Weighted Multi-Model Approach

```
Combined Score = (WSJF Score × 0.4) + (Strategic Score × 0.3) + (Risk Score × 0.3)

Benefits:
- Reduces single-model bias
- Incorporates multiple perspectives
- Provides robustness check

Challenges:
- More complex to calculate
- Requires normalization of scales
- May obscure clear trade-offs
```

### 3. Dynamic Prioritization

**Concept:** Priorities change as conditions change; build flexibility into the system

**Implementation:**
- Monthly priority reviews using lightweight scoring (ICE)
- Quarterly deep-dive analysis using comprehensive model (MCDA)
- Annual strategic realignment using Three Horizons

**Trigger Events for Reprioritization:**
- Significant market changes
- Technology breakthroughs or failures
- Resource availability changes
- Strategic direction shifts
- Competitive moves

---

## Implementation Best Practices

### 1. Model Calibration and Validation

**Historical Validation:**
- Compare model predictions to actual project outcomes
- Identify systematic biases in scoring
- Adjust scoring criteria based on lessons learned

**Cross-Validation:**
- Use multiple models on same project set
- Investigate projects that rank very differently
- Understand root causes of ranking differences

**Stakeholder Validation:**
- Present prioritization results to key stakeholders
- Gather feedback on "surprising" rankings
- Adjust weights or criteria based on strategic input

### 2. Common Implementation Pitfalls

**Over-Engineering the Process:**
- **Problem:** Complex models that take too long to use
- **Solution:** Start simple, add complexity only when needed

**Score Inflation:**
- **Problem:** All projects rated as high importance
- **Solution:** Forced ranking, relative scoring, external calibration

**Gaming the System:**
- **Problem:** Project sponsors inflate scores to get priority
- **Solution:** Independent scoring, historical validation, transparency

**Analysis Paralysis:**
- **Problem:** Endless refinement without decision making
- **Solution:** Set decision deadlines, "good enough" thresholds

### 3. Organizational Change Management

**Building Buy-In:**
- Involve stakeholders in model selection process
- Provide training on chosen methodology
- Start with pilot group before full rollout
- Demonstrate early wins from improved prioritization

**Managing Resistance:**
- Address concerns about "pet projects" being deprioritized
- Show how model supports rather than replaces judgment
- Provide transparency into scoring rationale
- Allow for appeals process with clear criteria

**Continuous Improvement:**
- Regular retrospectives on prioritization effectiveness
- Gather feedback from project teams and stakeholders
- Update models based on changing business context
- Share success stories and lessons learned

---

## Tools and Templates

### 1. Excel-Based Prioritization Templates

**WSJF Calculator:**
- Automated score calculation
- Sensitivity analysis for weight changes
- Portfolio-level aggregation
- Visual ranking dashboard

**RICE Framework Spreadsheet:**
- Reach estimation guidelines
- Impact scoring rubric
- Confidence level definitions
- Effort estimation templates

### 2. Decision Support Dashboards

**Portfolio Overview:**
- Current project distribution across models
- Resource allocation vs. strategic priorities
- Risk-return visualization
- Priority change tracking

**Stakeholder Views:**
- Executive summary of top priorities
- Department-specific project impacts
- Budget allocation by strategic theme
- Timeline and milestone visualization

### 3. Governance Integration

**Portfolio Review Templates:**
- Monthly priority health check
- Quarterly strategic alignment review
- Annual prioritization methodology assessment
- Exception handling procedures

---

## Advanced Topics

### 1. Machine Learning Enhanced Prioritization

**Predictive Scoring:**
- Use historical project data to improve scoring accuracy
- Identify patterns in successful vs. failed initiatives
- Automate routine scoring updates
- Flag projects with unusual risk profiles

**Natural Language Processing:**
- Analyze project descriptions for implicit risk factors
- Extract customer sentiment from feedback data
- Monitor market signals for priority implications
- Automate competitive intelligence gathering

### 2. Real-Time Priority Adjustment

**Market Signal Integration:**
- Customer satisfaction scores
- Competitive intelligence
- Regulatory changes
- Technology disruption indicators

**Internal Signal Monitoring:**
- Resource availability changes
- Budget reforecasts
- Strategic initiative launches
- Organizational restructuring

### 3. Portfolio Scenario Planning

**What-If Analysis:**
- Impact of budget cuts on portfolio balance
- Effect of resource constraints on delivery timelines
- Strategic pivot implications for current priorities
- Market disruption response strategies

---

*This framework should be customized based on organizational maturity, industry context, and strategic objectives. Regular updates should incorporate lessons learned and evolving best practices.*

## references/red-flags.md

# Red Flags: Senior PM

> Common ways this skill's output goes wrong -- concrete examples, why they're bad, and how to fix them.

## How to use this document

Scan every Senior PM artifact (portfolio dashboard, stakeholder map, EMV risk analysis, executive report, resource plan) before publishing. Each red flag has bad and good quoted examples.

---

## Red Flag 1: Stakeholder Mapping as Quarterly Art Project

**Symptom.** Mendelow's matrix drawn at offsite, framed on a wall, never referenced again.
**Why it's bad.** Stakeholder maps are a *coordination* tool. They guide which stakeholders need what cadence, what level of detail, and what level of consultation. Letting the map age means engagement defaults to whoever shouts loudest, not the people actually moving the work.
**Bad example:**
> "Q1 offsite produced a Mendelow's matrix. Q2 in progress: no PM has referenced the map; new stakeholders not added; departing stakeholders still listed."
**Good example:**
> "Stakeholder map updated at the start of each quarter and after major org changes (new exec joining, reorg, M&A). Each high-power-high-interest stakeholder has a documented engagement cadence (weekly 1:1, monthly digest, etc.) and an owner. Map lives in Notion / Confluence, accessible to all PMs."
**How to catch it.** Map's last edit > 90 days ago + org has changed = update.

---

## Red Flag 2: EMV Without Re-Estimation

**Symptom.** EMV (Expected Monetary Value) calculated at project kickoff; never re-computed as new evidence arrives.
**Why it's bad.** EMV combines impact + probability. Both update with new information (a customer commitment increases impact; a failed experiment decreases probability). A static EMV reflects kickoff conditions, which may have shifted dramatically.
**Bad example:**
> "EMV for Project X: $4.2M (calculated Jan 2026). Today: May 2026, EMV still cited as $4.2M, but the competitive launch in March changed the win probability."
**Good example:**
> "EMV re-estimated quarterly. Inputs (impact, probability) sourced from a versioned spreadsheet. Quarterly portfolio review compares current EMV to last quarter's; large swings trigger discussion. Documented in `references/emv-process.md`."
**How to catch it.** EMV figure cited in executive report > 90 days old without re-estimation = recompute.

---

## Red Flag 3: Portfolio Dashboard With No Re-Allocation Decisions

**Symptom.** Portfolio dashboard shows 18 active projects; every quarter the same 18 continue, regardless of changing evidence.
**Why it's bad.** The point of portfolio management is to *reallocate* -- kill projects that are underperforming, double down on projects that are overperforming. Without reallocation decisions, the dashboard is a status report, not management.
**Bad example:**
> "Q1 portfolio: 18 projects. Q2 portfolio: 18 projects. Q3: 18. Same allocations."
**Good example:**
> "Quarterly portfolio review explicitly asks: which projects do we accelerate, which do we slow, which do we kill? Reallocation log captures the decisions. Last 4 quarters: 3 projects killed, 4 accelerated, 2 paused, 11 continued. Investment shifts visible quarter-over-quarter."
**How to catch it.** Portfolio composition unchanged for > 2 quarters = portfolio review is theater.

---

## Red Flag 4: Executive Report That Buries the Important Thing

**Symptom.** 20-slide deck; the critical decision the exec needs to make is slide 14.
**Why it's bad.** Executives skim. The most important thing must be on slide 1 or in the first 100 words. Burying it means the exec misses it, decides on incomplete data, and the PM gets blamed.
**Bad example:**
> "Q2 executive deck: 20 slides. Slide 14: 'Need approval to spend $80k on vendor switch.' Exec did not get past slide 11."
**Good example:**
> "Executive deck structure: (1) headline + R/Y/G; (2) decisions needed; (3) major changes since last report; (4) detail in appendix. Top-of-deck answer to 'what do you need from me?' is never buried."
**How to catch it.** Any 'ask' / decision in an executive report past slide 5 = restructure.

---

## Red Flag 5: Resource Plan With No Re-Baselining

**Symptom.** Resource plan made in Q1; Q2 reality is dramatically different (2 engineers departed, 1 new program added); plan unchanged.
**Why it's bad.** A static resource plan misallocates by definition. Teams operate under the old assumption, programs get short-changed, and the PgM is surprised when work slips.
**Bad example:**
> "Resource plan v1: Q1. Today: Q2. 2 engineers left; 1 new initiative added. Plan still shows 100% on Q1 initiatives."
**Good example:**
> "Resource plan is re-baselined every quarter, and ad-hoc when material changes occur (departure, new hire, new initiative, scope swap). Versioned in git or Notion-history. Decisions to re-allocate are captured in a change log."
**How to catch it.** Resource plan unchanged > 90 days with org changes = re-baseline.

---

## Red Flag 6: Risk Matrix Without Mitigations

**Symptom.** Risk matrix shows 22 risks, plotted by probability x impact. No mitigation column.
**Why it's bad.** Plotting risks is interesting; mitigating them is the actual work. A matrix without mitigations is awareness without action; the risks fire and the team is no more prepared than if no analysis had been done.
**Bad example:**
> "Risk matrix: 22 risks in the high-high quadrant. (No mitigation column, no owner column.)"
**Good example:**
> "Every risk in the matrix has: Probability, Impact, EMV, Mitigation (what we do now), Tripwire (when we know it has fired), Contingency (what we do if it fires), Owner, Next Review. Top 5 by EMV are tracked in the weekly PgM sync."
**How to catch it.** Risk matrix with no mitigation column = re-do with mitigations.

---

## Red Flag 7: Stakeholder Engagement Defaulting to Highest-Power

**Symptom.** Every decision is escalated to the CEO. Low-power stakeholders (e.g. customer-success, support) are never consulted.
**Why it's bad.** Over-relying on high-power stakeholders alienates the people closest to the customer and centralizes decisions inappropriately. Quality suffers (CS / support have the operational reality CEO does not see) and the org becomes brittle.
**Bad example:**
> "All scoping decisions: escalated to CEO. CS team not consulted. Result: ship features that customers can't be onboarded onto because CS process is missing."
**Good example:**
> "Stakeholder map drives engagement: high-power-high-interest get weekly; high-power-low-interest get monthly digest; low-power-high-interest (CS, support) get deep consultation on operational implications. Decisions stay at the lowest level that has the information."
**How to catch it.** Decisions escalated > 80% of the time to a single exec = re-distribute via the stakeholder map.

---

## Red Flag 8: Portfolio Health Dashboard With Aggregated R/Y/G Only

**Symptom.** Dashboard shows portfolio health as a single R/Y/G summary. Underneath, two projects are red but the aggregate shows yellow.
**Why it's bad.** Aggregation hides the signal. A portfolio of 8 green + 2 red projects is *not* yellow -- it has 2 red projects that need attention now. Aggregation lets the worst items hide in the average.
**Bad example:**
> "Portfolio health: YELLOW. (Underneath: 6 green, 2 yellow, 2 red. Reds not flagged separately.)"
**Good example:**
> "Portfolio dashboard shows: (1) count and list of red projects (always visible); (2) count of yellow with the reason; (3) the aggregate (computed automatically). Red items always surface, regardless of how many greens there are."
**How to catch it.** Dashboard reports only the aggregate = expose the reds explicitly.

---

## Red Flag 9: Senior PM Doing Junior PM Work

**Symptom.** Senior PM writing 14 PRDs / quarter, attending every sprint planning, grooming backlogs across 4 teams.
**Why it's bad.** A Senior PM's leverage is in *cross-team coordination, strategic bets, and unblocking*, not in producing artifacts. Doing junior PM work means the senior strategic work is missed and the junior PMs do not grow.
**Bad example:**
> "Senior PM week: 14h refinement meetings, 12h writing PRDs, 6h sprint planning. 0h on portfolio strategy or stakeholder mapping."
**Good example:**
> "Senior PM week: 6h portfolio strategy + stakeholder engagement, 6h cross-team coordination, 4h coaching junior PMs (their PRDs, not the SPM's), 4h on a single high-leverage strategic bet, 4h overhead. Junior PMs own their team's artifacts."
**How to catch it.** Senior PM time-tracking shows > 50% on per-team artifacts = re-scope role.

---

## Red Flag 10: No Quarterly Portfolio Retro

**Symptom.** Portfolio shifts quarter to quarter; nobody analyzes what allocations worked.
**Why it's bad.** The org cannot improve its portfolio decisions if it does not look at past portfolio decisions in retrospect. Same biases recur; same losers get continued; same winners get under-funded.
**Bad example:**
> "Q1 portfolio retro: not held. Q2 portfolio decisions made on the same heuristics as Q1, which were the same as Q4 last year."
**Good example:**
> "Quarterly portfolio retro: which projects beat plan, which missed, what does it say about our scoring and selection? Outputs feed the next quarter's portfolio decisions. Documented in `references/portfolio-retro-template.md`."
**How to catch it.** No portfolio retro on the calendar = schedule.

---

## Red Flag Quick Reference

| # | Anti-pattern | One-line check |
|---|---|---|
| 1 | Stakeholder map as art project | Last edit < 90 days + after org changes? |
| 2 | EMV without re-estimation | EMV refreshed in last quarter? |
| 3 | Portfolio unchanged | Composition shifts QoQ? |
| 4 | Exec report buries the ask | Decision needed in first 5 slides? |
| 5 | Static resource plan | Re-baselined after material changes? |
| 6 | Risk matrix without mitigations | Every risk has mitigation + tripwire + owner? |
| 7 | Engagement defaults to highest-power | Stakeholder map drives cadence? |
| 8 | Aggregated R/Y/G hides reds | Reds always surface explicitly? |
| 9 | Senior PM doing junior work | > 50% time on per-team artifacts? |
| 10 | No portfolio retro | Quarterly retro scheduled? |

## Related Reading

- `SKILL.md` -- Senior PM patterns
- `scripts/project_health_dashboard.py --help` -- the portfolio dashboard
- `scripts/risk_matrix_analyzer.py --help` -- EMV + mitigation tracking
- `scripts/stakeholder_mapper.py --help` -- Mendelow's matrix tool
- `scripts/resource_capacity_planner.py --help` -- portfolio resource allocation
- Sibling skill: `program-manager/` -- coordination across programs
- Sibling skill: `execution/quarterly-planning/` -- the planning cycle the portfolio reflects
- Sibling skill: `c-level-advisor/` -- the executive-context advisory

## references/risk-management-framework.md

# Risk Management Framework for Senior Project Managers

## Executive Summary

This framework provides senior project managers with quantitative risk analysis methodologies, decision frameworks, and portfolio-level risk management strategies. It goes beyond basic risk identification to provide sophisticated tools for risk quantification, Monte Carlo simulation, expected monetary value (EMV) analysis, and enterprise risk appetite frameworks.

---

## Risk Classification & Quantification

### Risk Categories with Quantitative Weightings

#### 1. Technical Risk (Weight: 1.2x)
**Definition:** Technology implementation, integration, and performance risks

**Quantification Approach:**
- **Technology Maturity Score (TMS):** 1-5 scale based on technology adoption curve
- **Integration Complexity Index (ICI):** Number of integration points × complexity factor
- **Performance Risk Factor (PRF):** Historical performance variance in similar projects

**Formula:** `Technical Risk Score = (TMS × 0.3 + ICI × 0.4 + PRF × 0.3) × 1.2`

**Typical Sub-Risks:**
- Architecture scalability limitations (Impact: Schedule +15-30%, Cost +10-25%)
- Third-party integration failures (Impact: Schedule +20-40%, Cost +15-30%)
- Performance bottlenecks (Impact: Quality -20-40%, Cost +5-15%)
- Technology obsolescence (Impact: Long-term maintenance +50-100%)

#### 2. Resource Risk (Weight: 1.1x)  
**Definition:** Human capital availability, skills, and retention risks

**Quantification Approach:**
- **Skill Availability Index (SAI):** Market availability of required skills (1-5)
- **Team Stability Factor (TSF):** Historical turnover rate in similar roles
- **Capacity Utilization Ratio (CUR):** Team utilization vs. sustainable capacity

**Formula:** `Resource Risk Score = (SAI × 0.4 + TSF × 0.3 + CUR × 0.3) × 1.1`

**Financial Impact Models:**
- Key person departure: 3-6 months replacement + 2-4 weeks knowledge transfer
- Skill gap: 15-30% productivity reduction + training/hiring costs
- Over-utilization: 20-40% quality degradation + burnout-related delays

#### 3. Schedule Risk (Weight: 1.0x)
**Definition:** Timeline compression, dependencies, and critical path risks

**Quantification Method: Monte Carlo Simulation**
```
Three-Point Estimation:
- Optimistic (O): Best case scenario (10% probability)
- Most Likely (M): Realistic estimate (50% probability)  
- Pessimistic (P): Worst case scenario (90% probability)

Expected Duration = (O + 4M + P) / 6
Standard Deviation = (P - O) / 6

Monte Carlo Variables:
- Task duration uncertainty
- Resource availability variations
- Dependency delay impacts
- External factor disruptions
```

#### 4. Financial Risk (Weight: 1.4x)
**Definition:** Budget overruns, funding availability, and cost variability risks

**Expected Monetary Value (EMV) Analysis:**
```
EMV = Σ(Probability × Impact) for all financial risk scenarios

Cost Escalation Model:
- Labor cost inflation: Historical rate ± standard deviation
- Technology cost changes: Market volatility analysis
- Scope creep financial impact: Historical data from similar projects
- Currency/economic factors: Economic indicators correlation

Risk-Adjusted Budget = Base Budget × (1 + Risk Premium)
Risk Premium = Portfolio Risk Score × Risk Tolerance Factor
```

---

## Quantitative Risk Analysis Methodologies

### 1. Expected Monetary Value (EMV) Analysis

**Purpose:** Quantify financial impact of risks to inform investment decisions

**Process:**
1. **Risk Event Identification:** Catalog all potential financial impact events
2. **Probability Assessment:** Use historical data, expert judgment, and statistical models
3. **Impact Quantification:** Model financial consequences across multiple scenarios
4. **EMV Calculation:** Probability × Financial Impact for each risk
5. **Portfolio EMV:** Sum of all individual risk EMVs

**Example EMV Calculation:**
```
Risk: Third-party API failure requiring alternative implementation

Probability Scenarios:
- Minor disruption (60% chance): $50K additional cost
- Major redesign (30% chance): $200K additional cost  
- Complete platform change (10% chance): $500K additional cost

EMV = (0.6 × $50K) + (0.3 × $200K) + (0.1 × $500K)
EMV = $30K + $60K + $50K = $140K

Risk-adjusted budget should include $140K contingency for this risk.
```

### 2. Monte Carlo Simulation for Schedule Risk

**Purpose:** Model schedule uncertainty using probabilistic analysis

**Implementation Process:**
1. **Task Duration Modeling:** Define probability distributions for each task
2. **Dependency Mapping:** Model task dependencies and their uncertainty
3. **Resource Constraint Integration:** Include resource availability variations
4. **External Factor Variables:** Weather, regulatory approvals, vendor delays
5. **Simulation Execution:** Run 10,000+ iterations to generate probability curves

**Key Outputs:**
- **P50 Schedule:** 50% confidence completion date
- **P80 Schedule:** 80% confidence completion date (recommended for commitments)
- **P95 Schedule:** 95% confidence completion date (worst-case planning)
- **Critical Path Sensitivity:** Which tasks most impact overall schedule

**Schedule Risk Interpretation:**
```
If P50 = 6 months, P80 = 7.5 months:
- Schedule Buffer Required: 1.5 months (25% buffer)
- Risk Level: Medium (broad distribution indicates uncertainty)
- Mitigation Priority: Focus on tasks with highest variance contribution
```

### 3. Risk Appetite & Tolerance Frameworks

#### Enterprise Risk Appetite Levels

**Conservative (Risk Score Target: 0-8)**
- **Philosophy:** Minimize risk exposure, accept lower returns for certainty
- **Suitable Projects:** Core business operations, regulatory compliance, customer-facing systems
- **Contingency Reserves:** 20-30% of project budget
- **Decision Criteria:** Require 90%+ confidence levels for major decisions

**Moderate (Risk Score Target: 8-15)**
- **Philosophy:** Balanced risk-return approach, selective risk taking
- **Suitable Projects:** Process improvements, technology upgrades, market expansion
- **Contingency Reserves:** 15-20% of project budget  
- **Decision Criteria:** 70-80% confidence levels acceptable

**Aggressive (Risk Score Target: 15+)**
- **Philosophy:** High risk tolerance for high strategic returns
- **Suitable Projects:** Innovation initiatives, emerging technology adoption, new market entry
- **Contingency Reserves:** 10-15% of project budget (accept higher failure rates)
- **Decision Criteria:** 60-70% confidence levels acceptable

#### Risk Tolerance Thresholds

**Financial Tolerance Levels:**
- **Level 1:** <$100K potential loss - Team/PM authority
- **Level 2:** $100K-$500K potential loss - Business unit approval required
- **Level 3:** $500K-$2M potential loss - Executive committee approval
- **Level 4:** >$2M potential loss - Board approval required

**Schedule Tolerance Levels:**
- **Green:** <5% schedule impact - Monitor and mitigate
- **Amber:** 5-15% schedule impact - Active mitigation required
- **Red:** >15% schedule impact - Escalation and replanning required

---

## Advanced Risk Modeling Techniques

### 1. Correlation Analysis for Portfolio Risk

**Purpose:** Understand how risks interact across projects and compound at portfolio level

**Correlation Types:**
- **Positive Correlation:** Risks that tend to occur together (e.g., economic downturn affecting multiple projects)
- **Negative Correlation:** Risks that are mutually exclusive (e.g., resource conflicts between projects)
- **No Correlation:** Independent risks

**Portfolio Risk Calculation:**
```
Portfolio Variance = Σ(Individual Project Variance) + 2Σ(Correlation × StdDev1 × StdDev2)

Where correlation coefficients range from -1.0 to +1.0:
- +1.0: Perfect positive correlation (risks always occur together)
- 0.0: No correlation (risks are independent)
- -1.0: Perfect negative correlation (risks never occur together)
```

### 2. Value at Risk (VaR) for Project Portfolios

**Definition:** Maximum expected loss over a specific time period at a given confidence level

**Calculation Example:**
```
For a portfolio with expected value of $10M and monthly VaR of $500K at 95% confidence:
"There is a 95% chance that portfolio losses will not exceed $500K in any given month"

VaR Calculation Methods:
1. Historical Simulation: Use past project performance data
2. Parametric Method: Assume normal distribution of returns
3. Monte Carlo Simulation: Model complex risk interactions
```

### 3. Real Options Analysis for Project Flexibility

**Purpose:** Value the flexibility to modify project approach based on new information

**Common Real Options in Projects:**
- **Expansion Option:** Scale up successful projects
- **Abandonment Option:** Exit failing projects early
- **Timing Option:** Delay project start for better conditions
- **Switching Option:** Change technology/approach mid-project

**Black-Scholes Adaptation for Projects:**
```
Project Option Value = S₀ × N(d₁) - K × e^(-r×T) × N(d₂)

Where:
S₀ = Current project value estimate
K = Required investment (strike price)
r = Risk-free rate
T = Time to decision point
N(d) = Cumulative standard normal distribution
```

---

## Risk Response Strategies with Decision Trees

### Strategy Selection Framework

#### 1. Avoid (Eliminate Risk)
**Decision Criteria:**
- High impact + High probability risks
- Cost of avoidance < Expected risk cost
- Alternative approaches available

**Examples:**
- Choose proven technology over cutting-edge solutions
- Eliminate high-risk features from scope
- Change project approach entirely

#### 2. Mitigate (Reduce Probability or Impact)
**Decision Tree for Mitigation Investment:**
```
If (Risk EMV > Mitigation Cost × 1.5):
    Implement mitigation
Else if (Risk Impact > Risk Tolerance Threshold):
    Consider partial mitigation
Else:
    Accept risk
```

**Mitigation Effectiveness Factors:**
- Cost efficiency: Mitigation cost ÷ Risk EMV reduction
- Implementation feasibility: Resource availability and timeline
- Residual risk: Remaining risk after mitigation

#### 3. Transfer (Share Risk with Others)
**Transfer Mechanisms:**
- Insurance: For predictable, quantifiable risks
- Contracts: Fixed-price contracts transfer cost risk to vendors
- Partnerships: Share both risks and rewards
- Outsourcing: Transfer operational risks to specialists

**Transfer Decision Matrix:**
| Risk Type | Transfer Mechanism | Cost Efficiency | Risk Retention |
|-----------|-------------------|-----------------|----------------|
| Technical | Fixed-price contract | High | Low |
| Schedule | Penalty clauses | Medium | Medium |
| Market | Revenue sharing | Low | High |
| Operational | Insurance/SLA | High | Low |

#### 4. Accept (Acknowledge and Monitor)
**Acceptance Criteria:**
- Low impact × Low probability risks
- Mitigation cost > Risk EMV
- Risk within established tolerance thresholds

**Active Acceptance:** Establish contingency reserves and response plans
**Passive Acceptance:** Monitor but take no proactive action

---

## Risk Monitoring & Key Performance Indicators

### Risk Health Metrics

#### 1. Portfolio Risk Exposure Trends
```
Risk Velocity = (New Risks Added - Risks Resolved) / Time Period
Risk Burn Rate = Total Risk EMV Reduction / Time Period
Risk Coverage Ratio = Mitigation Budget / Total Risk EMV
```

#### 2. Risk Response Effectiveness
```
Mitigation Success Rate = Risks Successfully Mitigated / Total Mitigation Attempts
Average Resolution Time = Σ(Risk Resolution Days) / Number of Resolved Risks
Cost of Risk Management = Total Risk Management Spend / Project Budget
```

#### 3. Leading vs. Lagging Indicators

**Leading Indicators (Predictive):**
- Resource utilization trends
- Stakeholder satisfaction scores  
- Technical debt accumulation
- Team velocity variance
- Budget burn rate vs. planned

**Lagging Indicators (Confirmatory):**
- Actual schedule delays
- Budget overruns
- Quality defect rates
- Stakeholder complaints
- Team turnover events

### Risk Dashboard Design

**Executive Level (Strategic View):**
- Portfolio risk heat map
- Top 10 risks by EMV
- Risk appetite vs. actual exposure
- Risk-adjusted project ROI

**Program Level (Tactical View):**
- Risk trend analysis
- Mitigation plan status
- Resource allocation for risk management
- Cross-project risk correlations

**Project Level (Operational View):**
- Individual risk register
- Risk response action items
- Risk probability/impact changes
- Mitigation cost tracking

---

## Integration with Portfolio Management

### Strategic Risk Alignment

**Risk-Adjusted Portfolio Optimization:**
1. **Risk-Return Analysis:** Plot projects on risk vs. return matrix
2. **Portfolio Diversification:** Balance high-risk/high-reward with stable projects
3. **Resource Allocation:** Allocate risk management resources based on EMV
4. **Strategic Fit:** Ensure risk appetite aligns with strategic objectives

**Capital Allocation Models:**
```
Risk-Adjusted NPV = Standard NPV × Risk Adjustment Factor

Risk Adjustment Factor = 1 - (Project Risk Score × Risk Penalty Rate)

Where Risk Penalty Rate reflects organization's risk aversion:
- Conservative: 0.8% per risk score point
- Moderate: 0.5% per risk score point  
- Aggressive: 0.2% per risk score point
```

### Governance Integration

**Risk Committee Structure:**
- **Executive Risk Committee:** Monthly, strategic risks >$1M impact
- **Portfolio Risk Board:** Bi-weekly, cross-project risks
- **Project Risk Teams:** Weekly, operational risk management

**Escalation Triggers:**
- Risk EMV exceeds defined thresholds
- Risk probability or impact significantly changes
- Mitigation plans fail or become ineffective
- New risk categories emerge

**Decision Authority Matrix:**
| Risk EMV Level | Authority Level | Response Time | Required Documentation |
|----------------|-----------------|---------------|------------------------|
| <$50K | Project Manager | 24 hours | Risk register update |
| $50K-$250K | Program Manager | 48 hours | Risk assessment report |
| $250K-$1M | Business Owner | 72 hours | Executive summary + options |
| >$1M | Executive Committee | 1 week | Full risk analysis + recommendation |

---

## Advanced Topics

### Behavioral Risk Factors

**Cognitive Biases in Risk Assessment:**
- **Optimism Bias:** Tendency to underestimate risk probability
- **Anchoring Bias:** Over-reliance on first information received
- **Availability Heuristic:** Overweighting easily recalled risks
- **Confirmation Bias:** Seeking information that confirms existing beliefs

**Bias Mitigation Techniques:**
- Independent risk assessments from multiple sources
- Devil's advocate roles in risk sessions
- Historical data analysis vs. expert judgment
- Pre-mortem analysis: "How could this project fail?"

### Emerging Risk Categories

**Digital Transformation Risks:**
- Data privacy and cybersecurity (GDPR, CCPA compliance)
- Legacy system integration complexity
- Change management and user adoption
- Cloud migration and vendor lock-in

**Regulatory and Compliance Risks:**
- Changing regulatory landscape
- Cross-border data transfer restrictions
- Industry-specific compliance requirements
- Audit and documentation requirements

**Sustainability and ESG Risks:**
- Environmental impact assessments
- Social responsibility requirements
- Governance and ethical considerations
- Long-term sustainability of solutions

---

## Implementation Guidelines

### Risk Framework Maturity Model

**Level 1 - Basic (Ad Hoc):**
- Qualitative risk identification
- Simple probability/impact matrices
- Reactive risk response
- Project-level focus only

**Level 2 - Managed (Repeatable):**
- Standardized risk processes
- Quantitative risk analysis
- Proactive mitigation planning
- Portfolio-level risk aggregation

**Level 3 - Defined (Systematic):**
- Enterprise risk integration
- Monte Carlo simulation
- Risk-adjusted decision making
- Cross-functional risk management

**Level 4 - Advanced (Quantitative):**
- Real-time risk monitoring
- Predictive risk analytics
- Automated risk reporting
- Strategic risk optimization

**Level 5 - Optimizing (Continuous Improvement):**
- AI-enhanced risk prediction
- Dynamic risk response
- Industry benchmark integration
- Continuous framework evolution

### Getting Started: 90-Day Implementation Plan

**Days 1-30: Foundation**
- Assess current risk management maturity
- Define risk appetite and tolerance levels
- Establish risk governance structure
- Train core team on quantitative methods

**Days 31-60: Tools & Processes**
- Implement EMV and Monte Carlo tools
- Create risk dashboard templates
- Establish risk register standards
- Begin historical data collection

**Days 61-90: Integration & Optimization**
- Integrate with portfolio management
- Establish reporting rhythms
- Conduct first portfolio risk review
- Plan continuous improvement initiatives

---

*This framework should be adapted to organizational context, industry requirements, and project complexity. Regular updates should incorporate lessons learned and emerging best practices.*

## references/stakeholder-engagement-guide.md

# Stakeholder Engagement Guide for Senior Project Managers

## Executive Summary

This guide provides senior project managers with a structured approach to stakeholder identification, classification, engagement, and communication. It centers on Mendelow's Power/Interest Grid as the primary classification framework, with practical engagement tactics, communication templates, influence mapping techniques, and strategies for handling resistance.

---

## Power/Interest Grid Framework (Mendelow's Matrix)

### Overview

Mendelow's Matrix is a two-dimensional model that classifies stakeholders based on two axes:

- **Power** (vertical axis): The stakeholder's ability to influence project decisions, resources, and outcomes
- **Interest** (horizontal axis): The stakeholder's level of concern or engagement with the project

This creates four quadrants, each requiring a distinct engagement strategy.

### The Four Quadrants

```
  Power
  HIGH  | Keep Satisfied      | Manage Closely      |
        | (low interest)      | (high interest)     |
  ------+---------------------+---------------------+
  LOW   | Monitor             | Keep Informed       |
        | (low interest)      | (high interest)     |
        +---------------------+---------------------+
               LOW                   HIGH
                       Interest
```

### Quadrant 1: Manage Closely (High Power / High Interest)

**Who they are:** Executive sponsors, key decision-makers, product owners, and senior leaders with direct project involvement.

**Why they matter:** These stakeholders can make or break your project. They have both the authority to influence outcomes and the motivation to do so.

**Engagement approach:**
- Treat as partners, not just recipients of information
- Involve in decision-making and trade-off discussions
- Provide advance notice of issues before they escalate
- Seek their input on strategy and direction

### Quadrant 2: Keep Satisfied (High Power / Low Interest)

**Who they are:** C-suite executives, board members, regulatory bodies, and senior leaders with oversight but not daily involvement.

**Why they matter:** While they may not be engaged day-to-day, they can intervene and redirect the project at any time. Dissatisfaction can trigger sudden, disruptive involvement.

**Engagement approach:**
- Respect their time with concise, outcome-focused updates
- Escalate only significant issues that require their authority
- Ensure they feel confident the project is under control
- Avoid unnecessary detail or frequent meetings

### Quadrant 3: Keep Informed (Low Power / High Interest)

**Who they are:** End users, team members, subject matter experts, and community stakeholders who care about outcomes but lack decision authority.

**Why they matter:** They provide valuable feedback, influence organizational sentiment, and can become advocates or detractors. Their collective voice can shift stakeholder power dynamics.

**Engagement approach:**
- Provide regular updates through accessible channels
- Create opportunities for input and feedback
- Acknowledge their interest and contributions
- Use them as project champions and early adopters

### Quadrant 4: Monitor (Low Power / Low Interest)

**Who they are:** Tangentially affected departments, external observers, and stakeholders with minimal connection to the project.

**Why they matter:** While low priority, their position can change. A compliance issue might suddenly give a regulatory observer high power, or organizational changes might shift interest levels.

**Engagement approach:**
- Light-touch communication via existing channels
- Make information available on-demand
- Periodically re-assess their classification
- Watch for signals that power or interest is increasing

---

## Stakeholder Classification Strategies

### Initial Identification Techniques

1. **Organizational chart analysis:** Map reporting lines and identify formal authority
2. **Process mapping:** Identify who is affected by project inputs and outputs
3. **Budget trail:** Follow funding sources to uncover financial stakeholders
4. **Regulatory scan:** Identify compliance and governance stakeholders
5. **Historical review:** Look at who was involved in similar past projects
6. **Snowball method:** Ask known stakeholders "Who else should be involved?"

### Assessing Power

Power comes from multiple sources. Evaluate each stakeholder across these dimensions:

| Power Source | Description | Assessment Question |
|---|---|---|
| **Positional** | Authority from organizational role | Can they approve, block, or redirect the project? |
| **Resource** | Control over budget, people, or tools | Do they control resources the project needs? |
| **Expert** | Specialized knowledge or skills | Does the project depend on their expertise? |
| **Political** | Relationships and organizational influence | Can they mobilize support or opposition? |
| **Informational** | Access to critical data or communication channels | Do they control information flow? |

### Assessing Interest

Interest is driven by how much the project affects the stakeholder:

| Interest Driver | Indicators |
|---|---|
| **Direct impact** | Their work processes, tools, or team will change |
| **Performance link** | Their KPIs or OKRs are affected by project outcomes |
| **Strategic alignment** | The project advances or threatens their strategic goals |
| **Career implications** | Project success/failure affects their professional standing |
| **Personal values** | The project aligns with or conflicts with their beliefs |

### Dynamic Reclassification

Stakeholder positions are not static. Reassess classifications when:

- Project scope changes significantly
- Organizational restructuring occurs
- A major risk materializes
- Budget or timeline shifts substantially
- New regulatory requirements emerge
- A stakeholder changes roles or responsibilities

---

## Communication Plan Templates per Quadrant

### Manage Closely - Communication Plan

| Element | Detail |
|---|---|
| **Frequency** | Weekly (minimum) |
| **Format** | 1:1 meetings, steering committee, ad-hoc calls |
| **Content** | Detailed status, risks, decisions needed, financial health |
| **Preparation** | Tailored agenda, pre-read materials, decision frameworks |
| **Follow-up** | Meeting minutes within 24 hours, action items tracked |
| **Escalation** | Immediate for blockers; same-day for emerging risks |

**Sample weekly update structure:**
1. Key accomplishments this week (3-5 bullets)
2. Upcoming milestones and dependencies
3. Risks and issues requiring attention
4. Decisions needed (with recommendations)
5. Resource or budget concerns
6. Next week priorities

### Keep Satisfied - Communication Plan

| Element | Detail |
|---|---|
| **Frequency** | Monthly (or at major milestones) |
| **Format** | Executive summary email, quarterly review presentation |
| **Content** | High-level status, budget vs. actual, strategic impact |
| **Preparation** | One-page dashboard, RAG status, executive talking points |
| **Follow-up** | Action items only if their input was requested |
| **Escalation** | Only for issues requiring their authority or budget approval |

**Sample monthly executive summary structure:**
1. Overall status (RAG: Red/Amber/Green)
2. Budget health (% spent vs. % complete)
3. Key milestone progress
4. Strategic alignment update
5. Items requiring executive attention (if any)

### Keep Informed - Communication Plan

| Element | Detail |
|---|---|
| **Frequency** | Bi-weekly |
| **Format** | Newsletter, demo invites, shared dashboard, team channel |
| **Content** | Progress updates, upcoming changes, how they are affected |
| **Preparation** | Standardized template, accessible language |
| **Follow-up** | Feedback mechanism (survey, comment thread) |
| **Escalation** | Channel for them to raise concerns that get routed appropriately |

**Sample bi-weekly newsletter structure:**
1. What happened since last update
2. What is coming next
3. How this affects your area
4. Ways to get involved or provide feedback
5. FAQ or myth-busting section

### Monitor - Communication Plan

| Element | Detail |
|---|---|
| **Frequency** | Quarterly |
| **Format** | Organizational newsletter, all-hands mention, intranet page |
| **Content** | Major milestones, organizational impact, general awareness |
| **Preparation** | Brief paragraph or slide for existing communication channels |
| **Follow-up** | None unless they initiate contact |
| **Escalation** | N/A - they should know how to reach the project team if needed |

---

## Engagement Tactics by Quadrant

### Manage Closely - Tactical Playbook

| Tactic | Frequency | Purpose |
|---|---|---|
| Weekly 1:1 meeting | Weekly | Personalized status, relationship building |
| Steering committee seat | Bi-weekly/Monthly | Governance, decision authority |
| Pre-read distribution | Before key meetings | Informed participation, faster decisions |
| Draft review invitations | As needed | Early feedback, ownership |
| Informal check-ins | Ad-hoc | Relationship maintenance, early warning |
| Joint problem-solving sessions | As issues arise | Collaborative resolution, trust building |

### Keep Satisfied - Tactical Playbook

| Tactic | Frequency | Purpose |
|---|---|---|
| Executive summary email | Monthly | Awareness without time burden |
| Milestone demo invitation | At milestones | Visibility into progress |
| Quarterly business review | Quarterly | Strategic alignment check |
| Budget/timeline alert | As needed | No surprises on financials |
| Annual strategic briefing | Annually | Long-term alignment |

### Keep Informed - Tactical Playbook

| Tactic | Frequency | Purpose |
|---|---|---|
| Project newsletter | Bi-weekly | Regular, structured updates |
| Sprint demo invitation | Per sprint | Tangible progress visibility |
| Feedback survey | Monthly | Input channel, engagement |
| FAQ document updates | As needed | Self-service information |
| Champion/ambassador program | Ongoing | Leverage their enthusiasm |

### Monitor - Tactical Playbook

| Tactic | Frequency | Purpose |
|---|---|---|
| All-hands project slide | Quarterly | General awareness |
| Intranet/wiki page | Kept current | On-demand information |
| Organizational newsletter blurb | Quarterly | Passive communication |
| Reclassification check | Quarterly | Catch shifting dynamics |

---

## Influence Mapping Techniques

### Beyond Power and Interest

While the Power/Interest Grid is the primary framework, influence mapping adds a third dimension: the ability of stakeholders to affect the attitudes and decisions of other stakeholders.

### Influence Network Mapping

1. **Identify influence relationships:** For each stakeholder, ask "Who do they influence?" and "Who influences them?"
2. **Map connections:** Draw lines between stakeholders who influence each other
3. **Identify hubs:** Stakeholders with many influence connections are network hubs
4. **Find bridges:** Stakeholders who connect otherwise disconnected groups

### Influence Assessment Criteria

| Factor | Description | Weight |
|---|---|---|
| **Network centrality** | How connected they are to other stakeholders | High |
| **Trust level** | How much others trust their judgment | High |
| **Communication reach** | Size of their communication network | Medium |
| **Track record** | History of successful influence in the organization | Medium |
| **Domain expertise** | Recognized authority in relevant areas | Medium |

### Using Influence Data

- **Identify influencer paths:** To reach a hard-to-engage stakeholder, find who influences them
- **Amplify supporters:** High-influence supporters can be project champions
- **Neutralize blockers:** Engage influencers who can address blocker concerns
- **Build coalitions:** Connect supporters to create a unified voice of support

---

## Dealing with Blockers and Resistance

### Understanding Resistance

Resistance is not inherently negative. It often signals legitimate concerns that, if addressed, improve the project. Common sources of resistance:

| Source | Example | Typical Response |
|---|---|---|
| **Fear of change** | "This will disrupt our proven processes" | Acknowledge concern, show transition plan |
| **Loss of control** | "I won't have oversight anymore" | Define their role in the new state |
| **Past experience** | "We tried this before and it failed" | Explain what is different this time |
| **Competing priorities** | "My team is already at capacity" | Address resource concerns concretely |
| **Lack of trust** | "I don't believe the timeline is realistic" | Provide evidence, invite scrutiny |
| **Political concerns** | "This project benefits their department, not mine" | Find mutual wins, reframe benefits |

### Blocker Engagement Framework

**Step 1: Diagnose**
- Schedule a 1:1 to understand their concerns (listen first)
- Identify whether resistance is rational, emotional, or political
- Determine if their concerns are about the "what" or the "how"

**Step 2: Acknowledge**
- Validate their concerns without necessarily agreeing
- Demonstrate that you have heard and understood their position
- Share where you agree and where you see things differently

**Step 3: Address**
- For rational concerns: provide data, evidence, and risk mitigation plans
- For emotional concerns: build relationship, demonstrate empathy, provide reassurance
- For political concerns: find mutual benefits, involve neutral mediators, align with organizational goals

**Step 4: Involve**
- Give them a role that addresses their concerns (review board, advisory, testing)
- Create structured opportunities for input
- Report back on how their input influenced decisions

**Step 5: Escalate (if necessary)**
- Document the concern and your attempts to address it
- Engage the executive sponsor or a trusted mutual contact
- Frame the escalation around project risk, not personality conflict

### Blocker Priority Matrix

| Power Level | Recommended Urgency |
|---|---|
| High power blocker | Address within 48 hours; escalate if unresolved in 2 weeks |
| Medium power blocker | Address within 1 week; monitor for influence spread |
| Low power blocker | Address within 2 weeks; watch for coalition building |

---

## RACI Integration with Stakeholder Mapping

### Connecting the Frameworks

The Power/Interest Grid tells you **how to communicate** with stakeholders. RACI tells you **what role they play** in specific activities. Together, they create a complete engagement model.

### Mapping Quadrants to RACI Roles

| Quadrant | Typical RACI Roles | Rationale |
|---|---|---|
| **Manage Closely** | A (Accountable), R (Responsible) | High power + high interest = active decision-making roles |
| **Keep Satisfied** | A (Accountable), I (Informed) | High power = accountability; low interest = inform only |
| **Keep Informed** | C (Consulted), I (Informed) | High interest = want input; low power = consultative role |
| **Monitor** | I (Informed) | Low power + low interest = minimal involvement |

### Integration Best Practices

1. **Start with stakeholder mapping** to understand the landscape before assigning RACI roles
2. **Validate RACI with quadrant:** If a "Monitor" stakeholder is assigned "Accountable," either the RACI or the classification needs revision
3. **Use RACI to operationalize the communication plan:** The communication plan defines the cadence; RACI defines the specific activities
4. **Review both together:** When stakeholder classifications shift, review and update RACI assignments

### Warning Signs of Misalignment

| Signal | Problem | Fix |
|---|---|---|
| "Manage Closely" stakeholder has no R or A roles | They are disengaged despite high power/interest | Assign meaningful governance or decision roles |
| "Monitor" stakeholder is Accountable for activities | Over-assignment; creates bottlenecks | Reassess classification or reduce RACI scope |
| Too many C's on one activity | Decision paralysis | Reduce to only essential consultees |
| No A assigned for critical activities | Accountability gap | Assign based on power/interest classification |

---

## Stakeholder Review Cadence

| Review Type | Frequency | Purpose |
|---|---|---|
| **Classification review** | Monthly | Reassess power/interest changes |
| **Communication effectiveness** | Bi-weekly | Check if engagement approach is working |
| **Blocker status check** | Weekly | Track progress on resistance resolution |
| **Full stakeholder audit** | Quarterly | Comprehensive reassessment of all stakeholders |
| **Post-milestone review** | At milestones | Adjust engagement for next project phase |

---

## Key Metrics for Stakeholder Engagement

| Metric | Target | Measurement |
|---|---|---|
| Stakeholder satisfaction score | > 4/5 | Periodic pulse survey |
| Communication plan adherence | > 90% | Track planned vs. actual touchpoints |
| Blocker resolution rate | 100% within 30 days | Track blocker status over time |
| Decision turnaround time | < 5 business days | Measure from request to decision |
| Escalation frequency | Decreasing trend | Count escalations per month |
| Stakeholder NPS | > 30 | Quarterly net promoter score survey |

---

**Last Updated:** March 2026
**Framework Version:** 1.0
**Companion Tool:** `scripts/stakeholder_mapper.py`

---
Skill by Amin Borghei (borghei/Claude-Skills) · License: MIT + Commons Clause · Source: https://github.com/borghei/Claude-Skills/tree/25bf86b89c6c1e63f433a5b65e8cfcb6cf0b7ad3/project-management/senior-pm
