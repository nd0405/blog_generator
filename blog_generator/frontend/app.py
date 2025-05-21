import streamlit as st
import importlib.util
import sys
import os

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Main container */
    .stApp {
        background-color: #f0f2f6;
        color: #333333;
    }
    /* Sidebar */
    .css-1d391kg {
        background-color: #4a90e2;
        color: white;
    }
    /* Title */
    h1 {
        color: #4a90e2;
        text-align: center;
    }
    /* Input box */
    .stTextInput input {
        background-color: #ffffff;
        color: #333333;
        border-radius: 5px;
        border: 1px solid #4a90e2;
    }
    /* Button */
    .stButton button {
        background-color: #4a90e2;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #357abd;
    }
    /* Generated blog section */
    .stMarkdown {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Ensure the backend script is accessible
backend_path = "D:/blog_generator/test.py"

if os.path.exists(backend_path):
    spec = importlib.util.spec_from_file_location("test", backend_path)
    test = importlib.util.module_from_spec(spec)
    sys.modules["test"] = test
    spec.loader.exec_module(test)
else:
    st.error("Backend file `test.py` not found!")

# Sidebar for additional options
with st.sidebar:
    st.title("⚙️ Settings")
    st.write("Customize your blog generation experience!")
    blog_length = st.slider("Blog Length (Words)", 100, 500, 200)
    tone = st.selectbox("Tone", ["Professional", "Casual", "Informative", "Persuasive"])

# Main content
st.title("📝 AI Blog Generator")
st.write("Generate high-quality blog posts in seconds with LLaMA 2!")

# User input
topic = st.text_input("Enter Blog Topic:", "")

if st.button("Generate Blog", key="generate_blog"):
    if topic.strip():
        # Display a spinner while generating the blog
        with st.spinner("Generating blog... Please wait ⏳"):
            blog_content = test.generate_blog(topic)  # Call backend function
        
        # Display the generated blog
        st.subheader("Generated Blog:")
        st.markdown(
            f"""
            <div style="background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                {blog_content}
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.warning("⚠️ Please enter a topic!")