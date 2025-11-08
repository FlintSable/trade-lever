def calculate_position(account_size, entries, sl, leverage, risk_percentage):
    """
    Calculate optimal position size based on risk parameters.

    Args:
        account_size (float): Total account balance (must be > 0)
        entries (list): List of entry prices (must not be empty, all values > 0)
        sl (float): Stop loss price (must be > 0 and != avg_entry)
        leverage (float): Leverage multiplier (must be > 0)
        risk_percentage (float): Risk per trade as percentage (must be 0 < x <= 100)

    Returns:
        tuple: (position_size, avg_entry, percentage_change, leverage_adjusted_change)

    Raises:
        ValueError: If any input validation fails
        TypeError: If inputs are of incorrect type

    Example:
        >>> calculate_position(10000, [45000, 44800], 44500, 3.0, 1.0)
        (500.45, 44900, -0.89, -2.67)
    """
    # Type validation
    if not isinstance(account_size, (int, float)):
        raise TypeError(f"account_size must be a number, got {type(account_size).__name__}")
    if not isinstance(entries, list):
        raise TypeError(f"entries must be a list, got {type(entries).__name__}")
    if not isinstance(sl, (int, float)):
        raise TypeError(f"sl must be a number, got {type(sl).__name__}")
    if not isinstance(leverage, (int, float)):
        raise TypeError(f"leverage must be a number, got {type(leverage).__name__}")
    if not isinstance(risk_percentage, (int, float)):
        raise TypeError(f"risk_percentage must be a number, got {type(risk_percentage).__name__}")

    # Value validation
    if account_size <= 0:
        raise ValueError(f"account_size must be positive, got {account_size}")

    if not entries:
        raise ValueError("entries list cannot be empty")

    for i, entry in enumerate(entries):
        if not isinstance(entry, (int, float)):
            raise TypeError(f"entries[{i}] must be a number, got {type(entry).__name__}")
        if entry <= 0:
            raise ValueError(f"entries[{i}] must be positive, got {entry}")

    if sl <= 0:
        raise ValueError(f"sl must be positive, got {sl}")

    if leverage <= 0:
        raise ValueError(f"leverage must be positive, got {leverage}")

    if risk_percentage <= 0 or risk_percentage > 100:
        raise ValueError(f"risk_percentage must be between 0 and 100, got {risk_percentage}")

    # Calculate average entry
    avg_entry = sum(entries) / len(entries)

    # Check that stop loss is different from average entry
    if sl == avg_entry:
        raise ValueError(f"stop loss ({sl}) cannot equal average entry ({avg_entry})")

    # Perform calculations
    percentage_change = ((sl - avg_entry) / avg_entry) * 100
    leverage_adjusted_change = percentage_change * leverage
    risk_amount = account_size * (risk_percentage / 100)
    position_size = abs(risk_amount / (leverage_adjusted_change / 100))

    return position_size, avg_entry, percentage_change, leverage_adjusted_change