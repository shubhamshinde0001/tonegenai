from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

message = input("Enter a message: ")

prompt = f"""
You are a communication analyzer.

Analyze the following message:

"{message}"

Return:

Tone:
Emotion:
Intent:
Urgency:
Politeness:
Possible hidden meaning:

Explain in simple words.
"""

response = llm.invoke(prompt)

print("\n===== LLM UNDERSTANDING =====")
print(response.content)

# Message 1:
# "Okay, fine. I'll do it."

# Message 2:
# "Okay! Fine! I'll do it! 😄"

# Message 3:
# "Okay... fine. I'll do it."

# Message 4:
# "OKAY!!! FINE!!! I'LL DO IT!!!"

# Message 5:
# "Sure, I'll do it. No problem."