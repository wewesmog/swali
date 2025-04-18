from openai import OpenAI
from typing import List, Dict, Any, Optional
import os
from dotenv import load_dotenv
from pydantic import BaseModel



load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=OPENAI_API_KEY)

client = OpenAI()

def call_llm_api(messages: List[Dict[str, str]], 
                model: str = "gpt-4o-mini-2024-07-18",
                response_format: Optional[BaseModel] = None,
                max_tokens: int = 2000,
                temperature: float = 0.3) -> Any:
    """
    Make a call to the OpenAI API for chat completions.
    """
    try:
        response = client.beta.chat.completions.parse(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            response_format=response_format
        )
        return response.choices[0].message.parsed
    except Exception as e:
        print(f"Error in OpenAI API call: {e}")
        raise
