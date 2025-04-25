import streamlit as st


# Set page configuration
st.set_page_config(
    page_title="My Streamlit App ✨",
    page_icon="✨",
    layout="wide"
)

# Add a title and description
st.title("Welcome to My Streamlit App ✨")

# Create a sidebar
st.sidebar.header("Navigation 🧭")
page = st.sidebar.radio("Go to", ["Home 🏠", "About ℹ️" , "Contact 📞"])

if page == "Home 🏠":
    st.header("Home Page 🏠")
    st.write("""
    Welcome to my awesome Streamlit website. 🎉
             
    Enjoy exploring, and feel free to reach out with any questions! 💬
""")
    
elif page == "Contact 📞":
    st.header("Contact Us 📩")

    name = st.text_input("Your Name 📝")
    email = st.text_input("Your Email 📧")
    message = st.text_area("Your Message 💬")

    if st.button("Send ✉️"):

        if name and email and message:
            st.success("Message sent successfully! ✅")
        else:
            st.warning("Please fill all fields before sending. ⚠️")
    
else:  # About page
    st.header("About Me ℹ️")

    st.markdown("""
    This is a simple about page created using Streamlit. 📚
    Streamlit is a powerful tool for building interactive web apps with Python. 🐍

    ## Skills 🛠️
    I am a beginner in programming with skills in:
    - HTML 🌐
    - CSS 🎨
    - TypeScript 💻
    - Next.js ⚡

    ## Goal 🎯
    My goal is to continue learning programming and build more complex web applications with Python and Streamlit. 🚀

    Feel free to explore my app and connect with me for any questions or feedback! 💬
    """)
