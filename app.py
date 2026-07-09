import streamlit as st
from dotenv import load_dotenv
import os

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from pydantic import BaseModel
from typing import List, Optional

load_dotenv()

st.set_page_config(page_title="Movie Information Extractor", page_icon="🎬")

st.title("🎬 Movie Information Extractor")
st.write("Paste a movie description below and extract structured information.")

model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.7,
    api_key=os.getenv("MISTRAL_API_KEY"),
)

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
    (
        "human",
        "{paragraph}"
    )
])

paragraph = st.text_area(
    "Movie Paragraph",
    height=250,
    placeholder="Paste a movie description here..."
)

if st.button("Extract Information"):
    if paragraph.strip() == "":
        st.warning("Please enter a movie paragraph.")
    else:
        with st.spinner("Extracting information..."):
            try:
                final_prompt = prompt.invoke({
                    "paragraph": paragraph,
                    "format_instructions": parser.get_format_instructions()
                })

                response = model.invoke(final_prompt)

                movie_data = parser.parse(response.content)

                st.success("Extraction Complete!")

                st.json(movie_data.model_dump())

            except Exception as e:
                st.error(f"Error: {e}")
