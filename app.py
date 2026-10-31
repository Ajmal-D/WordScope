
import streamlit as st
import pandas as pd
import plotly.express as px
from pypdf import PdfReader
from processor import clean_and_count
from collections import Counter
import io

# Page configuration
st.set_page_config(
    page_title="WordScope",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 WordScope")
st.subheader("Interactive Multi-Document Word Frequency Analyzer")
st.write(
    "Upload multiple text or PDF documents to analyze, "
    "visualize, and compare word frequencies."
)

# Extract text from uploaded files
def extract_text(file):
    if file.name.lower().endswith(".txt"):
        return file.getvalue().decode("utf-8", errors="ignore")

    elif file.name.lower().endswith(".pdf"):
        reader = PdfReader(io.BytesIO(file.getvalue()))
        return " ".join(
            page.extract_text() or "" for page in reader.pages
        )

    return ""

# File uploader
uploaded_files = st.file_uploader(
    "Upload your documents (TXT or PDF)",
    type=["txt", "pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    document_counts = {}
    combined_counts = Counter()

    # Process every document
    for file in uploaded_files:
        text = extract_text(file)
        word_counts = clean_and_count(text)

        if word_counts:
            document_counts[file.name] = word_counts
            combined_counts.update(word_counts)

    if combined_counts:

        st.success(
            f"Successfully processed {len(document_counts)} documents!"
        )

        # Summary metrics
        col1, col2, col3 = st.columns(3)

        col1.metric("Documents Processed", len(document_counts))
        col2.metric("Unique Words", len(combined_counts))
        col3.metric("Total Words", sum(combined_counts.values()))

        # Combined visualization
        st.header("🌍 Combined Word Frequency")

        top_n = st.slider(
            "Select number of top words",
            min_value=5,
            max_value=30,
            value=10
        )

        combined_df = pd.DataFrame(
            combined_counts.most_common(top_n),
            columns=["Word", "Frequency"]
        )

        fig = px.bar(
            combined_df,
            x="Word",
            y="Frequency",
            color="Frequency",
            title="Most Frequent Words Across All Documents",
            text="Frequency"
        )

        st.plotly_chart(fig, use_container_width=True)

        # Individual document visualizations
        st.header("📄 Individual Document Analysis")

        for filename, counts in document_counts.items():

            with st.expander(f"View analysis: {filename}"):

                individual_df = pd.DataFrame(
                    counts.most_common(top_n),
                    columns=["Word", "Frequency"]
                )

                fig = px.bar(
                    individual_df,
                    x="Word",
                    y="Frequency",
                    title=f"Word Frequency in {filename}",
                    text="Frequency"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

        # Document comparison
        st.header("📊 Document Comparison")

        all_words = set(combined_counts.keys())
        comparison_data = []

        for word in all_words:
            row = {"Word": word}

            for filename, counts in document_counts.items():
                row[filename] = counts.get(word, 0)

            comparison_data.append(row)

        comparison_df = pd.DataFrame(comparison_data)

        top_words = [
            word for word, count
            in combined_counts.most_common(top_n)
        ]

        comparison_df = comparison_df[
            comparison_df["Word"].isin(top_words)
        ]

        comparison_long = comparison_df.melt(
            id_vars="Word",
            var_name="Document",
            value_name="Frequency"
        )

        comparison_fig = px.bar(
            comparison_long,
            x="Word",
            y="Frequency",
            color="Document",
            barmode="group",
            title="Word Frequency Comparison Across Documents"
        )

        st.plotly_chart(
            comparison_fig,
            use_container_width=True
        )

        # Download combined results
        st.header("⬇️ Download Results")

        csv = combined_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "Download Combined Word Frequencies",
            data=csv,
            file_name="word_frequency_results.csv",
            mime="text/csv"
        )

    else:
        st.warning(
            "No meaningful words found. Please upload documents with readable text."
        )

else:
    st.info("👆 Upload at least one TXT or PDF document to get started.")

st.divider()
st.caption("WordScope | Information Visualization | 21CSE481T")
