# 🦜🔗 LangChain Learning Journey

Welcome to my personal journey of learning [LangChain](w) — a powerful framework for developing applications with [language models](w) as part of my Generative AI (GenAI) journey from a user perspective. This repository documents my understanding, experimentation, and progress across core LangChain concepts and tools, eventually leading to building **end-to-end AI agents**.

---

## 🔗About LangChain🦜

[LangChain](w) is an open-source framework for building applications powered by large language models (LLMs). It offers a suite of tools and abstractions to streamline building chains, agents, and retrieval systems.

Learn more at the [official documentation](https://docs.langchain.com/).

---

---
## 📚 why i am learning?
LangChain is an open source framework that helps in building LLM based application. 
It
provides modular components and end-to-end tools that help developers build complex AI
applications, such as chatbots, question-answering systems, retrieval-augmented generation
(RAG), autonomous agents, and more.
1. Supports all the major LLMs
2. Simplifies developing LLM based applications
3. Integrations available for all major tools moreover can connect LLMs to our own data sources, so you can build AI solutions that use up-to-date or private information, not just what the model was trained on
4. Open source/Free/Actively developed
5. Supports all major GenAI use cases
6. Memory: allows AI applications to remember previous conversations or user inputs,
7. Prompt Management:  organize and reuse prompts to get consistent and high-quality outputs from the LLM
8. Chains : Connecting multiple LLM calls and steps into pipelines


---
---
## How does LangChain work?

Chains and Links: In LangChain, a chain is a sequence of steps (called links) that process user input, interact with LLMs, retrieve data, and format the output. Each link performs a specific task, and you can arrange them to create custom workflows.

Example Workflow: For instance, a chain might:

Take a user's question.

Retrieve relevant data from a database.

Send the data to an LLM for processing.

Format and translate the output for the user.

---

## 📚 What I'm Learning
I am learmimg fundaental of langchain , RAG,  Agents

This repo includes  LangChain concepts:

- ✅ **Models** – How to use LLMs, chat models, embedding models like OpenAI ,antrophic, gemini, Hugging Face in LangChain
- 💬 **Prompts** – Creating prompt templates, chat prompt templates,messages,message placeholder
- 🧱 **Structured Output & Output Parsers** – Converting LLM responses into structured data
- 🔗 **Chains** – Connecting multiple LLM calls and steps into pipelines
- ⚙️ **Runnable Interfaces** – The unified API for chaining steps
- 📄 **Document Loaders** – Loading data from PDFs, web pages, etc.
- ✂️ **Text Splitters** – Splitting large documents into smaller chunks
- 🧠 **Vector Stores & Retrievers** – Storing and searching document embeddings
- 📥 **Retrieval-Augmented Generation (RAG)** – Combining LLMs with context from your own data . RAG — a powerful technique that combines retrieval and generation to improve the performance of large language models.     simply training llms by sending query + context in prompt
- 🛠️ **Tool Calling** – Using LLMs to invoke external tools/functions
- 🚧 **Mini Projects** – Hands-on tasks to reinforce concepts
- 🧠 **End-to-End AI Agents** – Building autonomous agents using LangChain




---

## ✅ Progress Tracker

| Topic                          | Status     | Notes                              |
|-------------------------------|------------|------------------------------------|
| LangChain Introduction        | ✅ Done     | Overview         |
| Models                        | ✅ Done     | LLMs,chat models,Embedding models [OpenAI, Anthropic, Gemini,Hugging face]            |
| Prompts                       | ✅ Done     | static vs dynamic prompt , Prompt Templates, chat prompt templates, messages, messages placeholder              |
| Structured Output             | ✅ Done  |  Structured Output  , typeddict , pydantic , jsonschema  for  LLMs finetuned for  giving Structured Output  if we tell |
| Output Parsers                | ✅ Done| string Output Parsers , json Output Parsers , pydantic Output Parsers, structured Output Parsers for  LLMs  not finetuned for giving Structured Output if we tell specially  but can also use for LLMs giving default structured output    |
| Chains                        | ✅ Done | simple chain , sequential chain , conditional chain , parellel chain  |
| Runnables                     | ✅ Done | why needed , what is it , how it is made , task specific runnables ,runnable premitive   |
| Document Loaders              | ✅ Done | starting of rag  |
| Text Splitters                | ✅ Done | different types       |
| Vector Stores                 | ✅ Done | chroma db      |
| Retrievers                    | ✅ Done | different types   |
| Retrieval-Augmented Generation| ✅ Done |What RAG is? ,Why it matters?, How it works step by step? , building YouTube Chatbot : a RAG system in LangChain  |
| Tools                         | ✅ Done | built in tool , custom , toolkit    |
| Tool Calling                  | ⬜ Not Started | Coming soon         |
| Small Projects                | ✅ Started | Ongoing                     | 
| End-to-End AI Agent           | ⬜ Not Started | Final capstone goal              |





