import streamlit as st
from src.summarizer import summarize, get_styles
from src.utils import fetch_url_text, get_stats, compression_ratio

# -- Page config ---------------------------------------------------------------
st.set_page_config(
    page_title="AI Summarizer",
    page_icon="🗂️",
    layout="centered"
)

# -- Custom CSS ----------------------------------------------------------------
st.markdown("""
<style>
    .main { max-width: 780px; }
    .stat-box {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
    }
    .summary-box {
        background: #f0f7ff;
        border-left: 4px solid #4a90e2;
        border-radius: 6px;
        padding: 1.2rem 1.5rem;
        font-size: 1.05rem;
        line-height: 1.7;
    }
    .tag {
        display: inline-block;
        background: #e8f4fd;
        color: #1a73e8;
        border-radius: 20px;
        padding: 2px 12px;
        font-size: 0.8rem;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# -- Header --------------------------------------------------------------------
st.title("🗂️ AI Text Summarizer")
st.caption("Paste text or drop a URL · Powered by Claude Haiku")
st.divider()

# -- Input section -------------------------------------------------------------
input_mode = st.radio(
    "Choose input type",
    ["Paste text", "Enter a URL"],
    horizontal=True
)

text = ""

if input_mode == "Paste text":
    text = st.text_area(
        "Your text",
        height=220,
        placeholder="Paste any article, blog post, or paragraph here..."
    )

else:
    url = st.text_input(
        "Article URL",
        placeholder="https://en.wikipedia.org/wiki/..."
    )
    if url:
        with st.spinner("Fetching article..."):
            try:
                text = fetch_url_text(url)
                st.success("Article fetched successfully!")
                with st.expander("Preview fetched text"):
                    st.write(text[:1200] + "..." if len(text) > 1200 else text)
            except Exception as e:
                st.error(f"Could not fetch article: {e}")

# -- Options -------------------------------------------------------------------
style = st.selectbox("Summary style", get_styles())

# -- Summarize button ----------------------------------------------------------
if st.button("✨ Summarize", type="primary", disabled=not text.strip()):

    orig_stats = get_stats(text)

    # Original text stats
    st.subheader("Original text")
    c1, c2, c3 = st.columns(3)
    c1.metric("Words",     orig_stats["words"])
    c2.metric("Sentences", orig_stats["sentences"])
    c3.metric("Characters", orig_stats["chars"])

    st.divider()

    # Generate summary
    with st.spinner("Generating summary..."):
        result = summarize(text, style)

    # Summary output
    st.subheader("Summary")
    st.markdown(f'<div class="summary-box">{result}</div>', unsafe_allow_html=True)
    st.markdown(f'<br><span class="tag">{style}</span>', unsafe_allow_html=True)

    # Summary stats
    st.subheader("Summary stats")
    summ_stats = get_stats(result)
    ratio      = compression_ratio(text, result)

    s1, s2, s3 = st.columns(3)
    s1.metric("Words",      summ_stats["words"])
    s2.metric("Sentences",  summ_stats["sentences"])
    s3.metric("Compressed", f"{ratio}%", help="How much shorter vs original")

    st.divider()

    # Download
    st.download_button(
        label="⬇️ Download summary",
        data=result,
        file_name="summary.txt",
        mime="text/plain"
    )
