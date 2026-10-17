# LangChain Models

Small Python examples for working with large language models, chat models, and
text embeddings through LangChain and the Hugging Face Inference API.

## What is included

```text
langchain-models/
├── 1. LLMs/
│   └── 1_llm_demo.py
├── 2. Chat Models/
│   ├── 1_chatmodel_openai.py
│   ├── 2_chatmodel_anthropic.py
│   ├── 3_chatmodel_gemini.py
│   └── 4_chatmodel_hf.py
└── 3. Embedded Models/
    ├── 1_embeddings_gemini.py
    └── 2_document_similarity.py
```

### Examples

- **LLM**: Sends a prompt to an OpenAI completion model.
- **Chat models**: Demonstrates OpenAI, Anthropic, Google Gemini, and Hugging
  Face chat interfaces.
- **Embeddings**: Creates a Gemini embedding vector and prints its dimensions.
- **Document similarity**: Embeds a list of documents, compares them with a
  query using cosine similarity, and prints the closest document.

## Requirements

- Python 3.10 or newer
- API access to the provider used by the example
- The Python packages used by the examples:

```text
python-dotenv
langchain-openai
langchain-anthropic
langchain-google-genai
huggingface-hub
scikit-learn
numpy
```

Install them with:

```bash
python -m pip install python-dotenv langchain-openai langchain-anthropic langchain-google-genai huggingface-hub scikit-learn numpy
```

## Environment variables

Create a `.env` file in this directory. Add only the credentials for the
provider you intend to use:

```dotenv
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GOOGLE_API_KEY=your_google_api_key
HF_TOKEN=your_hugging_face_token
```

Do not commit `.env` or expose API keys in source control.

## Running an example

Run a script from the project directory, for example:

```bash
python "2. Chat Models/3_chatmodel_gemini.py"
python "3. Embedded Models/2_document_similarity.py"
```

The scripts load environment variables with `python-dotenv` and print the
provider response or similarity result to the console.

## Notes

- Provider model names and LangChain constructor signatures can change over
  time. If an example fails after installing the latest packages, check the
  provider integration documentation and update the model name or constructor
  arguments accordingly.
- The embedding similarity example requests 300-dimensional embeddings and
  uses scikit-learn's cosine similarity implementation.
- These examples are intended for experimentation and learning; they do not
  include retries, persistence, web serving, or production secret management.