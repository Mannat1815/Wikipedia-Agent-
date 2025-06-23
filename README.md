# 🧠 Multi-Agent AI Playground

A multi-agent AI application built with the [Phi](https://github.com/phi-tools/phi) framework, leveraging Groq's `llama3-70b-8192` model. Features two agents: one for web searches using DuckDuckGo and another for fetching and summarizing Wikipedia content.

## ✨ Features

- 🌐 **Web Search Agent**: Performs real-time web searches with cited sources via DuckDuckGo.
- 📚 **Wikipedia Agent**: Retrieves and summarizes Wikipedia content, using tables for structured data.
- 📝 **Markdown Output**: Clean, formatted responses with tool call visibility.
- 🔄 **Hot Reloading**: Streamlined development with auto-reload via Uvicorn.

## 🛠️ Tech Stack

- Python 3.8+
- Phi Framework
- Groq API (`llama3-70b-8192`)
- DuckDuckGo Tool
- WikipediaTools
- python-dotenv

## 📁 Project Structure

```
project/
├── main.py            # Main script to initialize agents and serve the app
├── .env              # Environment variables (PHI_API_KEY)
├── requirements.txt  # Python dependencies
└── README.md         # This file
```



## 🧠 Agents Overview

| Agent Name         | Role Description                              | Tools Used       |
|--------------------|-----------------------------------------------|------------------|
| Web Search Agent   | Searches the web for up-to-date information   | DuckDuckGo       |
| Wikipedia Agent    | Fetches and summarizes Wikipedia content      | WikipediaTools   |


## 📄 License

This project is licensed under the MIT License.
