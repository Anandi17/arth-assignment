async def score_resume_with_ai(resume_text: str, job_description: str):
    prompt = f"""
    Compare the following resume with the job description.
    JD: {job_description}
    Resume: {resume_text}
    
    Provide:
    1. Match percentage (0-100)
    2. Top 3 strengths
    3. Top 2 gaps
    """
    
    # Example using OpenAI (ensure API key is set)
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content