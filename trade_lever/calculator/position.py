def calculate_position(account_size, entries, sl, leverage, risk_percentage):
    """
    """
    avg_entry = sum(entries) / len(entries)
    percentage_change = ((sl - avg_entry) / avg_entry) * 100
    leverage_adjusted_change = percentage_change * leverage
    risk_amount = account_size * (risk_percentage / 100)
    position_size = abs(risk_amount / (leverage_adjusted_change / 100))
    return position_size, avg_entry, percentage_change, leverage_adjusted_change