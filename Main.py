import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_summary(prompt):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "developer", "content": "You are a summarizer which summarize the text that is given to you."},
            {
                "role": "user",
                "content": f"Summarize this text{prompt}"
            }
        ],
        temperature=0.3,
        max_tokens=150
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    prompt = input("Enter the text you want to summarize: \n")
    
    print("\n")
    print(generate_summary(prompt))