import streamlit as st
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from src.prompt import system_prompt
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

# Validate API keys
if not GROQ_API_KEY or not PINECONE_API_KEY:
    st.error("Error: Missing GROQ_API_KEY or PINECONE_API_KEY in .env file. Please configure them.")
    st.stop()

# Title and layout
st.set_page_config(page_title="Medical Chatbot", layout="wide")
st.title("Medical Chatbot")

# Sidebar for settings
with st.sidebar:
    st.header("Settings")
    model_option = st.selectbox("Select Model", ["llama3-8b-8192", "mixtral-8x7b-32768", "grok-beta", "grok-4-0709"])
    export_chat = st.button("Export Chat History")
    clear_chat = st.button("Clear Chat")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Initialize embeddings with error handling
try:
    embeddings = download_hugging_face_embeddings()
except Exception as e:
    st.error(f"Error loading embeddings: {str(e)}. Check your helper module.")
    st.stop()

# Initialize Pinecone vector store
try:
    index_name = "medical-chatbot"
    docsearch = PineconeVectorStore.from_existing_index(index_name=index_name, embedding=embeddings)
except Exception as e:
    st.error(f"Error connecting to Pinecone index: {str(e)}. Check PINECONE_API_KEY and index name.")
    st.stop()

# Initialize retriever
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Initialize LLM
chatModel = ChatGroq(model=model_option, api_key=GROQ_API_KEY)

# Define prompt with memory
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
])

# Initialize memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
for user_msg, bot_msg in st.session_state.chat_history:
    memory.chat_memory.add_user_message(user_msg)
    memory.chat_memory.add_ai_message(bot_msg)

# Create chains
question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Chat input and response handling
user_input = st.text_input("Ask a medical question:", key="user_input")

if user_input:
    try:
        # Update memory with current input
        memory.chat_memory.add_user_message(user_input)
        response = rag_chain.invoke({"input": user_input, "chat_history": memory.load_memory_variables({})["chat_history"]})
        memory.chat_memory.add_ai_message(response["answer"])
        st.session_state.chat_history.append(("User", user_input))
        st.session_state.chat_history.append(("Bot", response["answer"]))
        st.write("**Bot:**", response["answer"])
    except Exception as e:
        st.error(f"Error processing query: {str(e)}")

# Display chat history
st.subheader("Conversation")
for role, message in st.session_state.chat_history:
    st.write(f"**{role}:** {message}")

# Export chat history
if export_chat and st.session_state.chat_history:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"chat_history_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(st.session_state.chat_history, f, indent=4)
    st.sidebar.success(f"Chat history exported to {filename}")

# Clear chat history
if clear_chat:
    st.session_state.chat_history = []
    memory.clear()
    st.experimental_rerun()

# Footer
st.markdown("---")
st.markdown("Powered by Streamlit | Consult a healthcare professional for medical advice.")


