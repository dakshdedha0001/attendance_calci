import streamlit as st


def calculate_attendance(num, den, classes_left):
    attendance = (num / den) * 100
    message = ""

    if attendance >= 75:
        message = f"You already have {attendance:.2f}% attendance!!"

        for i in range(1, classes_left + 1):
            new_attendance = ((num) / (den + i)) * 100
            if new_attendance < 75:
                message += f"\nYou can skip up to {i} classes out of the {classes_left} remaining and still maintain at least 75% attendance."
                break
        else:
            message += f"\nYou can skip all {classes_left} remaining classes and still maintain at least 75% attendance."

    else:
        message = f"You have {attendance:.2f}% attendance!!"

        for i in range(1, classes_left + 1):
            new_attendance = ((num + i) / (den + i)) * 100
            if new_attendance >= 75:
                message += f"\nYou’ll need to attend {i} more classes out of the remaining {classes_left} to reach 75% attendance."
                break
        else:
            message += f"\nEven if you attend all {classes_left} remaining classes, you won't reach 75% attendance."

    return message


st.title("Attendance Calculator")

num = st.number_input("Enter the number of classes attended:", min_value=0, value=0)
den = st.number_input("Enter the total number of classes:", min_value=1, value=1)
classes_left = st.number_input("Enter the number of classes left:", min_value=0, value=0)

if st.button("Calculate Attendance"):
    if num > den:
        st.error("Please enter valid numbers: attended classes cannot exceed total classes.")
    else:
        result = calculate_attendance(num, den, classes_left)
        st.success(result)
