def calculate_position(account_size, entries, sl, leverage, risk_percentage):
    if not entries:
        raise ValueError("Entry list cannot be empty")
    avg_entry = sum(entries) / len(entries)

    percentage_change = ((sl - avg_entry) / avg_entry) * 100
    leverage_adjusted_change = percentage_change * leverage
    risk_amount = account_size * (risk_percentage / 100)

    if leverage_adjusted_change == 0:
        raise ValueError("Leverage-adjusted change results in division by zero.")
    position_size = abs(risk_amount / (leverage_adjusted_change / 100))

    return position_size, avg_entry, percentage_change, leverage_adjusted_change