import streamlit as st

def main():
    st.title("Basic Math Calculator")

    st.write("Enter two numbers to get their sum:")

    # Input fields for numbers with validation
    num1 = st.number_input("Enter first number", format="%f")
    num2 = st.number_input("Enter second number", format="%f")

    if st.button("Add"):
        result = num1 + num2
        st.success(f"The sum of {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()
