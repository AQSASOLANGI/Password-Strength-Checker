import re
import streamlit as st

# =========================
# PASSWORD CHECK FUNCTION
# =========================
def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Minimum 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter (A-Z)")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter (a-z)")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one number (0-9)")

    if re.search(r"[@#$%!&*]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character (@#$%!&*)")

    return score, suggestions


# =========================
# STREAMLIT UI
# =========================
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

st.title("🔐 Password Strength Checker")
st.markdown("**Beginner Python Project • 2025**")

st.divider()

password = st.text_input(
    "Enter your password",
    type="password",
    placeholder="Type password here..."
)

if password:
    score, suggestions = check_password_strength(password)

    # Progress bar
    st.subheader("Strength Meter")
    st.progress(score / 5)

    # Strength message
    if score <= 2:
        st.error("🔴 WEAK PASSWORD")
    elif score == 3:
        st.warning("🟡 MEDIUM PASSWORD")
    else:
        st.success("🟢 STRONG PASSWORD")

    st.write(f"**Score:** {score}/5")

    # Suggestions
    if suggestions:
        st.subheader("🔧 Suggestions to Improve")
        for s in suggestions:
            st.write("❌", s)
    else:
        st.balloons()
        st.success("🎉 Your password is strong and secure!")

st.divider()
st.caption("Made with ❤️ using Python & Streamlit")
