from openai import OpenAI
import os

class Agent:
    def __init__(self, name, instructions, model="gpt-4"):
        self.name = name
        self.instructions = instructions
        self.model = model
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def run(self, prompt, history=None):
        # Prepare the messages
        messages = [{"role": "system", "content": self.instructions}]
        
        # Add history if provided
        if history:
            messages.extend(history)
        
        # Add the current prompt
        messages.append({"role": "user", "content": prompt})
        
        # Get completion from OpenAI
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}" 