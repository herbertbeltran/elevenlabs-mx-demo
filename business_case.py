"""Simple cost comparison: traditional voiceover production vs. AI voice.

All numbers below are ASSUMPTIONS. Edit them to match real quotes.
"""

# --- Assumptions (edit these) ---
SPOTS_PER_MONTH = 20          # voiceovers an agency produces per month
LANGUAGES = 2                 # versions per spot (e.g., es-MX + en)
TRADITIONAL_COST_MXN = 3500   # voice talent + studio, per spot per language
TRADITIONAL_DAYS = 3          # turnaround per spot (booking, recording, edits)
AI_MONTHLY_PLAN_MXN = 2000    # AI voice subscription per month
AI_REVIEW_COST_MXN = 150      # staff time to review/edit each AI voiceover
AI_HOURS = 1                  # turnaround per spot, in hours


def main() -> None:
    units = SPOTS_PER_MONTH * LANGUAGES
    traditional = units * TRADITIONAL_COST_MXN
    ai = AI_MONTHLY_PLAN_MXN + units * AI_REVIEW_COST_MXN
    savings = traditional - ai

    print(f"Voiceovers per month:     {units}")
    print(f"Traditional cost:         ${traditional:,.0f} MXN  (~{TRADITIONAL_DAYS} days each)")
    print(f"AI voice cost:            ${ai:,.0f} MXN  (~{AI_HOURS} hour each)")
    print(f"Monthly savings:          ${savings:,.0f} MXN ({savings / traditional:.0%})")
    print(f"Annual savings:           ${savings * 12:,.0f} MXN")


if __name__ == "__main__":
    main()
