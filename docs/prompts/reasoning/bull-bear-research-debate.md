---
category: "reasoning"
title: "Bull-Bear Research Debate (Evidence Adjudication)"
---
[← Back to Reasoning Prompts](../index.md)

# Bull-Bear Research Debate (Evidence Adjudication)

**Category:** reasoning
**Source:** Adapted from https://github.com/TauricResearch/TradingAgents/tree/main/tradingagents/agents/researchers and https://github.com/TauricResearch/TradingAgents/blob/main/tradingagents/graph/conditional_logic.py (Apache-2.0, TauricResearch)

Copyright TauricResearch. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md). This adaptation adds an explicit round cap that is not present in the captured researcher prompt files; the upstream controller uses `count >= 2 * max_debate_rounds`. Modifications: human decision boundary, no-order rule, required per-turn citations, and optional downside checks without inventing missing risk-debate speakers.

## When to Use

Adjudicate competing investment-research theses on a named instrument when a frozen evidence bundle exists and a human must make the decision. Do not use this prompt to place trades or to claim predicted returns.

## The Prompt

```text
Run a bounded bull/bear research debate on [instrument] using [evidence bundle]
under [round cap]. Freeze the evidence date, instrument identifier, source set,
and judge rubric before the first turn. Without separate role invocations or an
executor, label the run as role simulation. This is research debate only: never
place, stage, or recommend market orders, never size a live allocation, and never
assert backtested or expected profit and loss.

1. Admit the case. Confirm the instrument, asset class, evidence cutoff date, and
   which reports are present (market, sentiment, news, fundamentals or explicit
   absence). Missing fundamentals are unavailable, not bearish by default. If the
   bundle cannot support either thesis, return INSUFFICIENT EVIDENCE and stop.

2. Alternate bull and bear turns. The bull argues growth, advantages, and
   positive indicators, and must rebut the latest bear points with citations.
   The bear argues risks, weaknesses, and negative indicators, and must rebut
   the latest bull points with citations. Each turn requires at least one
   evidence citation (source locator in the frozen bundle). Engagement is
   rebuttal, not a data dump. Do not invent quotes, numbers, or filings.

3. Count turns explicitly. Increment the shared debate count once per completed
   speaker turn. The authored hard stop, added because the captured researcher
   files do not contain it, is: stop debate when count >= 2 * [round cap], using
   the supplied cap or default max_debate_rounds = 1 (two speaker turns each
   side). Do not start a turn that would exceed the cap. Do not reset count.

4. Optional downside check (not a third invented speaker): after the capped
   debate, list portfolio-context questions the human should weigh (drawdown,
   liquidity, concentration, correlation). Do not generate missing aggressive,
   conservative, or neutral risk-analyst voices, and do not claim a high-risk
   stance is optimal.

5. The research manager reads the full transcript and adjudicates. Conflict
   alone is not a reason to Hold. Weigh merits independent of speaking order.
   Emit exactly one research recommendation from Buy / Overweight / Hold /
   Underweight / Sell, or ABSTAIN when evidence remains balanced or too thin.
   Follow with Rationale (which cited arguments decided it) and Strategic
   Actions framed as research implications for a human, not executable orders.

6. The human makes the decision. The manager transcript is advisory. Do not
   transmit orders, change positions, or imply that following the rating would
   have produced historical returns. Disclose uncertainty, source age, and
   remaining disagreements.

Return the transcript ledger (turn, speaker, cited sources), terminal count
versus cap, manager recommendation or ABSTAIN, rationale, residual risks, and
the explicit statement that no order was placed. Role simulation must be labeled.
```

## How It Works

TradingAgents alternates bull and bear researchers over shared reports, then a research manager writes a rating and plan. Upstream routing stops the debate after `count >= 2 * max_debate_rounds`; that cap is authored into this prompt because it is not in the captured researcher files. Optional H6 downside questions are checks only; missing risk-debate nodes are not invented. Explicit turn accounting is kept; lexical majority voting is not used as a judge.

Unlike [Debate Coach](../education/debate-coach.md), this is evidence-conditioned investment-research adjudication, not coaching rhetoric. Unlike [Agent Graph With Cycles](../system/agent-graph-cycle.md), routing is a two-speaker rebuttal with a manager transcript, not generic worker/reviewer cycles. Unlike [Self-Consistency](self-consistency.md), the manager weighs cited arguments rather than taking a lexical plurality. Unlike [Financial Analyst](financial-analyst.md), the output is a bounded debate record plus a human-owned decision, not a persona report and not a claim of trading performance.

## Variables

- `[instrument]`: ticker or asset identifier, asset class, and evidence cutoff date.
- `[evidence bundle]`: market, sentiment, news, and fundamentals reports or explicit absences, with locators.
- `[round cap]`: max_debate_rounds; stop when count >= 2 * this value; default 1 if unspecified.

## Tested On

Not model-tested. Curated Apache-2.0 adaptation; no live debate run, investment-return, backtest, or order-routing evaluation is claimed.
