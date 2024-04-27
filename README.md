**phi-3**

https://github.com/microsoft/onnxruntime-genai/blob/main/examples/python/phi-3-tutorial.md?WT.mc_id=aiml-134281-kinfeylo

**Deploy using Ollama:**

pip install huggingface-hub>=0.17.1

huggingface-cli login

huggingface-cli download microsoft/Phi-3-mini-4k-instruct-gguf Phi-3-mini-4k-instruct-q4.gguf --local-dir . --local-dir-use-symlinks False

curl -fsSL https://ollama.com/install.sh | sh

ollama run phi3


**Testing cURL:**

curl -X POST -H "Content-Type: application/json" -d '{"data": "Your prompt here"}' http://localhost:6000/run_phi3



curl -X POST -H "Content-Type: application/json" -d '{"data": "Your prompt here"}' http://34.136.204.188:6000/run_phi3


