# Conceptual logic for Module 5 [cite: 97, 102]
def get_onboarding_answer(user_query, document_context):
    prompt = f"""
    Answer the user's question ONLY using the provided documents.
    If the answer is not in the text, say 'Please contact HR at [email]'.
    
    Documents: {document_context}
    Question: {user_query}
    """
    # Call LLM here.../