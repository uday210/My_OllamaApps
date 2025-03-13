# Ollama-Gemma Chat Integration

## Overview
This repository contains Python scripts for interacting with the Gemma model through Ollama, implemented in two different ways:
1. A command-line interface
2. An interactive chat interface using Chainlit

## Files Description

### 1. `Ollama_Gemma3.py`
A simple command-line script that sends a single message to the Gemma model through Ollama.

### 2. `ChainLit_Ollama_Gemma.py`
An interactive chat interface built with Chainlit that allows continuous conversation with the Gemma model.

## Prerequisites
- Python 3.x
- Ollama installed with Gemma model
- Required Python packages:
  ```bash
  pip install ollama-python chainlit
  ```
- Gemma model pulled in Ollama:
  ```bash
  ollama pull gemma
  ```

## Running the Applications

### Command Line Version
To run the simple command-line version:
```bash
python Ollama_Gemma3.py
```
This will send a predefined message to Gemma and print the response.

### Interactive Chat Version
To run the Chainlit chat interface:
```bash
chainlit run ChainLit_Ollama_Gemma.py
```
This will start a web interface where you can:
1. Interact with Gemma through a chat interface
2. See the welcome message automatically
3. Send messages and receive responses in real-time

## Features
- Direct integration with Ollama's Gemma model
- Two different interfaces for different use cases
- Asynchronous processing in the Chainlit version
- User-friendly web interface for the Chainlit version

## Note
Make sure Ollama is running in the background before executing either script.