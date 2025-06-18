import tkinter as tk
from number_entry import IntEntry, FloatEntry


def calculate_monthly_repayment(principal, annual_rate, years):
    """
    Calculate the monthly mortgage repayment amount.
    Args:
        principal (float): The loan amount.
        annual_rate (float): The annual interest rate (as a percentage, e.g. 5 for 5%).
        years (int): The loan term in years.
    Returns:
        float: The monthly repayment amount.
    """
    rate = annual_rate / 100 / 12
    n_payments = years * 12
    payment = (
        principal
        * rate
        * (1 + rate) ** n_payments
        / ((1 + rate) ** n_payments - 1)
    )
    return payment

def calculate_total_payment(monthly_payment, years):
    """
    Calculate the total payment over the entire mortgage period.
    Args:
        monthly_payment (float): The monthly repayment amount.
        years (int): The loan term in years.
    Returns:
        float: The total payment over the loan.
    """
    return monthly_payment * years * 12


def reset_fields(entries, result_labels):
    """
    Reset all input fields and clear result labels.
    Args:
        entries (list): List of entry widgets to clear
        result_labels (list): List of result labels to clear
    """
    for entry in entries:
        entry.delete(0, tk.END)
    for label in result_labels:
        label.config(text="")


def setup_frame(root):
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    # Principal
    principal_label = tk.Label(frame, text="Principal:")
    principal_label.grid(row=0, column=0, sticky="e", padx=8, pady=8)
    principal_entry = FloatEntry(
        frame,
        lower_bound=0.01,
        upper_bound=100_000_000,
        width=15,
    )
    principal_entry.grid(row=0, column=1, padx=8, pady=8)

    # Interest Rate
    rate_label = tk.Label(frame, text="Interest Rate (%):")
    rate_label.grid(row=1, column=0, sticky="e", padx=8, pady=8)
    rate_entry = FloatEntry(frame, lower_bound=0.01, upper_bound=100.0)
    rate_entry.grid(row=1, column=1, padx=8, pady=8)

    # Years
    years_label = tk.Label(frame, text="Years:")
    years_label.grid(row=2, column=0, sticky="e", padx=8, pady=8)
    years_entry = IntEntry(frame, lower_bound=1, upper_bound=99, width=3)
    years_entry.grid(row=2, column=1, padx=8, pady=8)

    # Result labels
    monthly_label = tk.Label(frame, text="Monthly Payment:")
    monthly_label.grid(row=3, column=0, sticky="e", padx=8, pady=(12, 8))
    monthly_result = tk.Label(frame, text="")
    monthly_result.grid(row=3, column=1, sticky="w", padx=8, pady=(12, 8))

    total_label = tk.Label(frame, text="Total Payment:")
    total_label.grid(row=4, column=0, sticky="e", padx=8, pady=8)
    total_result = tk.Label(frame, text="")
    total_result.grid(row=4, column=1, sticky="w", padx=8, pady=8)

    def calculate_mortgage():
        try:
            principal = principal_entry.get()
            annual_rate = rate_entry.get()
            years = years_entry.get()
            payment = calculate_monthly_repayment(principal, annual_rate, years)
            total = calculate_total_payment(payment, years)
            monthly_result.config(text=f"${payment:,.2f}", fg="black")
            total_result.config(text=f"${total:,.2f}", fg="black")
        except Exception as e:
            monthly_result.config(text="Please input all fields", fg="red")
            total_result.config(text="", fg="red")
            return e

    # Create a frame for buttons
    button_frame = tk.Frame(frame)
    button_frame.grid(row=5, column=0, columnspan=2, pady=(12, 0))

    # Calculate button
    calc_button = tk.Button(button_frame, text="Calculate", command=calculate_mortgage, width=10)
    calc_button.pack(side=tk.LEFT, padx=5)
    
    # Reset button
    reset_button = tk.Button(
        button_frame, 
        text="Reset", 
        command=lambda: reset_fields(
            [principal_entry, rate_entry, years_entry],
            [monthly_result, total_result]
        ),
        width=10
    )
    reset_button.pack(side=tk.LEFT, padx=5)


def main():
    root = tk.Tk()
    root.title("Mortgage Calculator")
    setup_frame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
