def calculate_average_entry(entries):
    """
    Calculate the average entry price from a list of entry prices.
    
    Parameters:
    - entries (list of float): Entry prices.
    
    Returns:
    - float: The average entry price.
    """
    if not entries:
        raise ValueError("Entry list cannot be empty.")
    return sum(entries) / len(entries)

def calculate_percentage_change(entry_price, stop_loss):
    """
    Calculate the percentage change between the entry price and stop loss.
    
    Parameters:
    - entry_price (float): The average entry price.
    - stop_loss (float): The stop loss price.
    
    Returns:
    - float: Percentage change to stop loss.
    """
    return ((stop_loss - entry_price) / entry_price) * 100

def calculate_leverage_adjusted_change(percentage_change, leverage):
    """
    Adjust the percentage change by the leverage factor.
    
    Parameters:
    - percentage_change (float): Original percentage change.
    - leverage (float): Leverage factor.
    
    Returns:
    - float: Leverage-adjusted percentage change.
    """
    return percentage_change * leverage

def calculate_position_size(account_size, average_entry, stop_loss, risk_percentage, leverage):
    """
    Calculate the position size based on account size, average entry, stop loss, risk percentage, and leverage.
    
    Parameters:
    - account_size (float): Total capital in the account.
    - average_entry (float): Calculated average entry price.
    - stop_loss (float): Stop loss price.
    - risk_percentage (float): Risk percentage per trade.
    - leverage (float): Leverage factor.
    
    Returns:
    - float: Calculated position size.
    """
    percentage_change = calculate_percentage_change(average_entry, stop_loss)
    leverage_adjusted_change = calculate_leverage_adjusted_change(percentage_change, leverage)
    risk_amount = account_size * (risk_percentage / 100)
    if leverage_adjusted_change == 0:
        raise ValueError("Leverage-adjusted change results in division by zero.")
    return abs(risk_amount / (leverage_adjusted_change / 100))
