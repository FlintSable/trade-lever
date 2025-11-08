import sys
from pathlib import Path

# Add parent directory to path for development (allows running without pip install)
sys.path.insert(0, str(Path(__file__).parent.parent))

from trade_lever import calculate_position


def get_positive_float(prompt, field_name):
    """Get a positive float from user input with validation."""
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                print(f"Error: {field_name} cannot be empty")
                continue

            float_value = float(value)
            if float_value <= 0:
                print(f"Error: {field_name} must be positive, got {float_value}")
                continue

            return float_value
        except ValueError:
            print(f"Error: {field_name} must be a valid number")


def get_risk_percentage():
    """Get risk percentage from user with validation (0 < x <= 100)."""
    while True:
        try:
            value = input("Enter risk percentage (0-100): ").strip()
            if not value:
                print("Error: Risk percentage cannot be empty")
                continue

            risk = float(value)
            if risk <= 0 or risk > 100:
                print(f"Error: Risk percentage must be between 0 and 100, got {risk}")
                continue

            return risk
        except ValueError:
            print("Error: Risk percentage must be a valid number")


def get_entries():
    """Get entry prices from user with validation."""
    entries = []
    print("\nEnter up to 10 entry prices (press Enter to finish):")

    for i in range(1, 11):
        while True:
            entry_input = input(f"  Entry {i}: ").strip()

            # Allow skipping after at least one entry
            if not entry_input:
                if entries:
                    return entries
                elif i == 1:
                    print("Error: At least one entry price is required")
                    continue
                else:
                    return entries

            # Validate entry value
            try:
                entry_value = float(entry_input)
                if entry_value <= 0:
                    print(f"Error: Entry price must be positive, got {entry_value}")
                    continue
                entries.append(entry_value)
                break
            except ValueError:
                print("Error: Entry price must be a valid number")

    return entries


def main():
    """Main CLI application for trade calculation."""
    print("=" * 50)
    print("TradeLever - Position Size Calculator")
    print("=" * 50)

    try:
        # Gather inputs with validation
        account_size = get_positive_float("Enter account size: $", "Account size")
        sl = get_positive_float("Enter stop loss: $", "Stop loss")
        leverage = get_positive_float("Enter leverage: ", "Leverage")
        risk_percentage = get_risk_percentage()
        entries = get_entries()

        # Calculate position
        position, avg_entry, change, leveraged_change = calculate_position(
            account_size, entries, sl, leverage, risk_percentage
        )

        # Display results
        print("\n" + "=" * 50)
        print("Trade Calculation Results")
        print("=" * 50)
        print(f"Average Entry: ${avg_entry:.4f}")
        print(f"Percentage Change to SL: {change:.2f}%")
        print(f"Leverage Adjusted % Change: {leveraged_change:.2f}%")
        print(f"-" * 50)
        print(f"Total Margin: ${position:.2f}")
        print(f"Margin Per Entry: ${position / len(entries):.2f}")
        print(f"Position Per Entry: ${position / len(entries) * leverage:.2f}")
        print(f"Total Position: ${position * leverage:.2f}")
        print(f"-" * 50)
        print(f"Total Risked: ${account_size * (risk_percentage / 100):.2f}")
        print(f"Risk Percentage: {risk_percentage:.2f}%")
        print("=" * 50)

    except (ValueError, TypeError) as e:
        print(f"\nCalculation Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()    