# 🎬 AI Movie Information Extractor

A modern AI-powered web application that extracts structured movie information from natural language descriptions using **LangChain**, **Mistral AI**, **Pydantic**, and **Streamlit**.

Simply paste a movie paragraph, click **Extract Information**, and the application automatically identifies important movie details such as the title, release year, genres, director, cast, rating, and summary.

---


## ✨ Features

- 🎬 Extract movie title
- 📅 Detect release year
- 🎭 Identify genres
- 🎥 Detect director
- 👥 Extract cast members
- ⭐ Extract IMDb/movie rating
- 📝 Generate concise movie summary
- 📋 Display structured output using Pydantic
- 🚀 Beautiful and responsive Streamlit UI
- ⚡ Fast AI inference using Mistral AI
- 📄 JSON output for developers

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Interface |
| LangChain | Prompt Engineering & LLM Integration |
| Mistral AI | Large Language Model |
| Pydantic | Structured Output Validation |
| python-dotenv | Environment Variables |

---

## 📂 Project Structure

```text
AI-Movie-Information-Extractor/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── assets/
│   ├── home.png
│   └── result.png
│
└── screenshots/
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/AI-Movie-Information-Extractor.git

cd AI-Movie-Information-Extractor
```

---

### 2️⃣ Create a virtual environment

Using **uv**

```bash
uv venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

### 3️⃣ Install dependencies

Using **uv**

```bash
uv sync
```

or

```bash
uv pip install -r requirements.txt
```

---

### 4️⃣ Create `.env`

```env
MISTRAL_API_KEY=your_api_key_here
```

---

### 5️⃣ Run the application

```bash
streamlit run app.py
```

---

## 💡 Example Input

```text
Inception is a 2010 science fiction action thriller directed by Christopher Nolan. The film stars Leonardo DiCaprio as Dom Cobb, a skilled thief who enters people's dreams to steal secrets. The movie also features Joseph Gordon-Levitt, Elliot Page, Tom Hardy, Ken Watanabe, Cillian Murphy, and Marion Cotillard. It has an IMDb rating of 8.8/10.
```

---

## 📤 Example Output

```json
{
  "title": "Inception",
  "release_year": 2010,
  "genre": [
    "Science Fiction",
    "Action",
    "Thriller"
  ],
  "director": "Christopher Nolan",
  "cast": [
    "Leonardo DiCaprio",
    "Joseph Gordon-Levitt",
    "Elliot Page",
    "Tom Hardy",
    "Ken Watanabe",
    "Cillian Murphy",
    "Marion Cotillard"
  ],
  "rating": 8.8,
  "summary": "A skilled thief enters dreams to steal secrets and performs inception to plant an idea into a target's subconscious."
}
```

---

## 🔮 Future Improvements

- 🎥 Movie poster integration
- 🌐 TMDB API support
- 🎬 Trailer search
- 📊 IMDb rating visualization
- 🎭 Actor profile cards
- 📄 Export to PDF
- 📁 Batch movie extraction
- 🤖 Multi-model support (Gemini, OpenAI, Ollama)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Swapnil**

Engineering Student | AI & ML Enthusiast | GenAI Developer

If you like this project, consider giving it a ⭐ on GitHub!
