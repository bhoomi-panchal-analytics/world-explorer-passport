import streamlit as st
import json

st.title("🧠 World Quiz")

with open("data/quizzes.json") as f:
    quizzes = json.load(f)

question = quizzes["capital_quiz"][0]

st.subheader(question["question"])

answer = st.radio(
    "Choose answer",
    question["options"]
)

if st.button("Submit"):

    if answer == question["answer"]:
        st.success("Correct!")
    else:
        st.error(
            f"Wrong. Correct answer is {question['answer']}"
        )
