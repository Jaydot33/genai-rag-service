
---

## ⚡️ Quick Start

1. **Clone & Install**
    ```
    git clone https://github.com/Jaydot33/genai-rag-service.git
    cd genai-rag-service
    pip install -r requirements.txt
    ```

2. **Configure Your API Key**
    - Copy `.env.example` to `.env` and add your [Hugging Face or OpenAI token](https://huggingface.co/settings/tokens):
      ```
      OPENAI_API_KEY=your_token_here
      ```

3. **Run the API**
    ```
    uvicorn app.main:app --reload
    ```
    Navigate to [http://localhost:8000/docs](http://localhost:8000/docs) for interactive API docs.

---

## 🧩 Example: Query Endpoint

- **POST** `/query`
    ```
    {
      "question": "What is Retrieval-Augmented Generation?",
      "document_id": "doc-001"
    }
    ```

- **Sample Response**
    ```
    {
      "answer": "Retrieval-Augmented Generation (RAG) combines information retrieval with generative AI to produce context-grounded answers.",
      "context": [
        "RAG enables large language models to use external document stores.",
        "Improves answer reliability and grounding with up-to-date information."
      ]
    }
    ```

---

## 🔒 Security

- All secret API keys and credentials are loaded from `.env` (never hard-coded or committed)
- Add your real key to `.env` (do not share this file!)

---

## 🛠️ LLM Plug-and-Play Integration

- Swap between Hugging Face or OpenAI models by changing the `OPENAI_API_KEY` (and base URL, if needed)
- Supports API-inference with `openai` package’s standardized interface
- Ready for extension with other providers or OSS models

---

## 🏗️ Next Steps

- Expand to include vector DB and document ingestion
- Add automated CI tests and more RAG pipeline options
- Optionally deploy with Docker (see commented Dockerfile)

---

## 📚 References & Useful Links

- [FastAPI](https://fastapi.tiangolo.com/)
- [Hugging Face Inference API](https://huggingface.co/inference-api)
- [OpenAI API](https://platform.openai.com/docs/api-reference)
- [ChromaDB](https://www.trychroma.com/), [Pinecone](https://www.pinecone.io/), [FAISS](https://faiss.ai/)

---

## 🤝 Contributing

Open to issues, pull requests, and feedback—let’s build GenAI workflows together!

---

**Author:** Jimmie Williams (jaydot3) | [LinkedIn](https://www.linkedin.com/in/jimmie-williams33/)
