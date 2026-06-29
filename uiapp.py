import os
from dotenv import load_dotenv

import streamlit as st

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from pydantic import BaseModel
from typing import List, Optional

# -----------------------------
# Load Environment
# -----------------------------
load_dotenv()

model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.7,
    api_key=os.getenv("MISTRAL_API_KEY"),
)

# -----------------------------
# Pydantic Model
# -----------------------------
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
Extract movie information from the paragraph.

{format_instructions}
"""
    ),
    ("human", "{paragraph}")
])

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#1e293b,#111827);
}

.main-title{
font-size:52px;
font-weight:800;
text-align:center;
color:white;
}

.subtitle{
text-align:center;
font-size:18px;
color:#cbd5e1;
margin-bottom:30px;
}

.card{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 8px 25px rgba(0,0,0,.15);
margin-bottom:20px;
}

.genre{
display:inline-block;
padding:7px 16px;
margin:5px;
border-radius:30px;
background:#2563eb;
color:white;
font-weight:bold;
}

.cast{
display:inline-block;
padding:7px 15px;
margin:5px;
border-radius:30px;
background:#10b981;
color:white;
font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown("<div class='main-title'>🎬 Movie Information Extractor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Powered by LangChain + Mistral AI + Pydantic</div>", unsafe_allow_html=True)

# -----------------------------
# Input
# -----------------------------
paragraph = st.text_area(
    "Paste a movie description",
    height=220,
    placeholder="Example:\nInception is a 2010 science fiction film directed by Christopher Nolan..."
)

if st.button("🚀 Extract Information", use_container_width=True):

    if paragraph.strip() == "":
        st.warning("Please enter a movie paragraph.")
        st.stop()

    with st.spinner("Analyzing movie..."):

        final_prompt = prompt.invoke({
            "paragraph": paragraph,
            "format_instructions": parser.get_format_instructions()
        })

        response = model.invoke(final_prompt)

        movie = parser.parse(response.content)

    st.success("Movie information extracted successfully!")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("🎥 Title")
        st.write(movie.title)

        st.subheader("📅 Release Year")
        st.write(movie.release_year)

        st.subheader("🎬 Director")
        st.write(movie.director)

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("⭐ Rating")

        if movie.rating:
            st.progress(movie.rating / 10)
            st.metric("IMDb Rating", f"{movie.rating}/10")
        else:
            st.write("Not Available")

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("🎭 Genres")

    genre_html = ""

    for g in movie.genre:
        genre_html += f"<span class='genre'>{g}</span>"

    st.markdown(genre_html, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("👥 Cast")

    cast_html = ""

    for actor in movie.cast:
        cast_html += f"<span class='cast'>{actor}</span>"

    st.markdown(cast_html, unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("📝 Summary")

    st.info(movie.summary)

    st.markdown("---")

    with st.expander("📄 Extracted JSON"):

        st.json(movie.model_dump())