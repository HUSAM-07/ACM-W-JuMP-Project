import streamlit as st

# Function to perform arithmetic operations
def calculate(num1, num2, operation):
    if operation == "Addition":
        return num1 + num2
    elif operation == "Subtraction":
        return num1 - num2
    elif operation == "Multiplication":
        return num1 * num2
    elif operation == "Division":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

# Streamlit app layout
def main():
    st.title("Nirenjana's Simple Calculator")

    # Previous results storage
    previous_results = []

    # Input fields
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")

    # Select operation
    operation = st.selectbox("Select operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

    # Calculate and display result
    if st.button("Calculate"):
        result = calculate(num1, num2, operation)
        previous_results.append(f"{num1} {operation} {num2} = {result}")
        st.success(f"Result: {result}")

    # Display previous results
    st.subheader("Previous Results")
    if previous_results:
        for i, res in enumerate(previous_results):
            st.write(f"{i + 1}. {res}")
    else:
        st.write("No previous results")

if __name__ == "__main__":
    main()
