import streamlit as st
from openai import OpenAI
import pandas as pd

priority_score_map = {
    "P1": 3,
    "P2": 2,
    "P3": 1
}

severity_score_map = {
    "High": 3,
    "Medium": 2,
    "Low": 1
}

st.write("App started")

st.title("Incident Triage Pipeline")
st.caption("AI-powered incident classification and prioritisation")

incident = st.text_area("Describe the incident")

if "log" not in st.session_state:
    st.session_state["log"] = []


def parse_response(text):
    result = {}

    for field in ["Cause", "Severity", "Priority", "Owner", "Action"]:
        if field + ":" in text:
            value = text.split(field + ":")[1]

            for next_field in ["Cause", "Severity", "Priority", "Owner", "Action"]:
                if next_field != field and next_field + ":" in value:
                    value = value.split(next_field + ":")[0]

            result[field] = value.strip()

    return result


if st.button("Analyse Incident"):
    if not incident.strip():
        st.warning("Please enter an incident description")
    else:
        try:
            api_key = st.secrets["OPENAI_API_KEY"]

            with st.spinner("Analysing..."):
                client = OpenAI(api_key=api_key)

                response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are an engineering triage assistant.\n\n"
                                "Return the output in EXACTLY the following format.\n"
                                "Do not include any extra text or explanation.\n\n"
                                "Cause: <short root cause>\n"
                                "Severity: <Low | Medium | High>\n"
                                "Priority: <P1 | P2 | P3>\n"
                                "Owner: <Team name>\n"
                                "Action: <clear recommended action>\n"
                            )
                        },
                        {"role": "user", "content": incident}
                    ]
                )

            output = response.choices[0].message.content
            parsed = parse_response(output)

            result = {
                "incident": incident,
                **parsed
            }

            # Calculate scores
            result["priority_score"] = priority_score_map.get(parsed.get("Priority"), 0)
            result["severity_score"] = severity_score_map.get(parsed.get("Severity"), 0)

            st.session_state["log"].append(result)

            st.subheader("Latest Analysis")
            st.write(f"**Cause:** {parsed.get('Cause')}")
            st.write(f"**Severity:** {parsed.get('Severity')}")
            st.write(f"**Priority:** {parsed.get('Priority')}")
            st.write(f"**Owner:** {parsed.get('Owner')}")
            st.write(f"**Action:** {parsed.get('Action')}")

        except Exception as e:
            st.error(f"Error: {e}")

st.subheader("Incident Log")

if st.session_state["log"]:
    df = pd.DataFrame(st.session_state["log"])

    df = df.sort_values(by=["priority_score", "severity_score"], ascending=False)

    df = df[[
        "Priority",
        "Severity",
        "Cause",
        "Owner",
        "incident",
        "Action"
    ]]

    df = df.rename(columns={
        "incident": "Incident",
        "Cause": "Cause",
        "Severity": "Severity",
        "Priority": "Priority",
        "Owner": "Owner",
        "Action": "Recommended Action"
    })

    st.dataframe(df)
else:
    st.write("No incidents logged yet")