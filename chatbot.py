# chatbot.py
class RAGChatbot:
    def __init__(self):
        self.documents = []

    def load_pdf_content(self, pdf_file):
        content = pdf_file.read()
        self.documents.append(content)
        return f"PDF loaded successfully ({len(content)} bytes)"

    def chat(self, query):
        return f"🤖 Bot response to: {query}"

    def get_document_stats(self):
        return f"Loaded {len(self.documents)} document(s)"
