# flightvoice-ai: Real-Time Speech Transcription & Translation

&#x20;

## 📌 Overview

flightvoice is a real-time speech processing system designed for **aviation and military communication**. It transcribes radio speech using **Whisper**, refines content with **DeepSeek**, and translates it using **open-source models**. The system is optimized for low-latency operation with a **Dockerized front-end** and a scalable backend.

## 🎯 Features

- **Live Speech Transcription** using **Whisper**
- **Content Correction & Awareness** via **DeepSeek**
- **Translation** to multiple languages with a locally running model
- **Real-Time Audio Streaming** from a client-server architecture
- **Modular Pipeline** for seamless integration
- **Dockerized Deployment** for scalability

## 🛠️ Tech Stack

- **Programming Languages:** Python
- **Deep Learning Models:** OpenAI Whisper, DeepSeek R1, Custom Translation Model
- **Frameworks & Libraries:** PyTorch, Hugging Face Transformers, WebSockets
- **Deployment:** Docker, FastAPI

## 🚀 Installation & Setup

### Prerequisites

- Python 3.10+
- PyTorch (CUDA if available)
- Docker (for containerized deployment)

### Clone the Repository

```bash
git clone https://github.com/yourusername/flightvoice-ai.git
cd flightvoice-ai
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Server

```bash
python server.py
```

### Start the Client (for Streaming Audio)

```bash
python client.py
```

## 📦 Docker Deployment

### Build and Run

```bash
docker-compose up --build
```

## 📌 Usage

1. Start the server to host the live audio stream.
2. The client captures and transmits speech.
3. The processing pipeline transcribes, corrects, and translates in real-time.
4. The output is displayed in the front-end interface.

## 📝 Roadmap

-

## 🤝 Contribution

Contributions are welcome! Fork the repo, create a branch, and submit a PR.

## 📜 License

MIT License © 2025 flightvoice-ai Team

