Medical Chatbot
Welcome to the Medical Chatbot repository! This project is an AI-powered chatbot designed to provide context-aware medical assistance using Retrieval-Augmented Generation (RAG). Built with modern AI tools and cloud-ready architecture, it’s a fun and helpful solution for basic healthcare queries when you’re feeling "bimar" (sick) and a doctor isn’t around!
About the Project
This Medical Chatbot leverages cutting-edge technologies to deliver real-time, accurate responses. Whether you’re asking about symptoms or seeking first-aid tips, it remembers your conversation to offer personalized advice. The project was developed over 2 weeks and showcases skills in Python, AI/ML, and cloud integration.
Features

Conversational Memory: Maintains context across questions (e.g., "I’m getting a fever" followed by "What do I do now?").
RAG with Pinecone: Retrieves relevant medical knowledge from a vector database.
Powered by Groq API: Utilizes advanced language models for natural responses.
Streamlit Interface: Offers an interactive and user-friendly frontend.
Cloud-Ready: Designed for deployment on platforms like Azure.

Tech Stack

Frontend: Streamlit
Backend/AI: LangChain, Groq API
Vector Storage: Pinecone
Language: Python
Deployment Target: Azure App Service (in progress)

Getting Started
Prerequisites

Python 3.9 or 3.10
Git
Azure CLI (for deployment)
Environment variables for API keys

Installation

Clone the repository:
bashgit clone https://github.com/Sibghatullah-pk/MEDICALCHATBOT.git
cd MEDICALCHATBOT

Create a virtual environment and activate it:
bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:
bashpip install -r requirements.txt

Set up environment variables:

Create a .env file in the root directory.
Add your API keys:
textGROQ_API_KEY=your_groq_api_key_here
PINECONE_API_KEY=your_pinecone_api_key_here




Running Locally

Run the Streamlit app:
bashstreamlit run app.py

Open your browser at http://localhost:8501 and start chatting!

Usage

Enter a medical question in the input box (e.g., "I’m feeling bimar with a fever").
Follow up with related questions to test the conversational memory.
Note: This is for informational purposes only—consult a healthcare professional for real medical advice!

Deployment
This project is slated for deployment on Azure App Service. Stay tuned for updates on the DevOps pipeline, including CI/CD and containerization steps. Check back for a detailed deployment guide soon!
Contributing
Contributions are welcome! Please fork the repository and submit pull requests. For major changes, please open an issue first to discuss your ideas.

Fork the repo.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m "Add new feature").
Push to the branch (git push origin feature-branch).
Open a pull request.

License
This project is currently unlicensed. Feel free to add a license (e.g., MIT) based on your preference.
Acknowledgments

Inspired by the xAI community and resources.
Thanks to the open-source tools: Streamlit, LangChain, Groq, and Pinecone.

Future Plans

Deploy on Azure with a full CI/CD pipeline.
Add multilingual support for broader reach.
Integrate voice input for hands-free use.

Stay connected for more updates! 🚀
