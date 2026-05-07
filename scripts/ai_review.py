import os
import subprocess
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def run(cmd):
    result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    return result.stdout + "\n" + result.stderr

errors = ""
errors += "RUFF:\n" + run("ruff check . || true")
errors += "\nPYTEST:\n" + run("pytest || true")
errors += "\nNPM BUILD:\n" + run("npm run build --if-present || true")

response = client.responses.create(
    model="gpt-5.2",
    instructions="""
Eres un agente experto en Python, Flask, MySQL, Astro, JavaScript y PHP.
Explica los errores de forma clara y devuelve código corregido cuando sea posible.
Responde en español.
""",
    input=f"Revisa estos errores del proyecto y dime cómo corregirlos:\n\n{errors}"
)

print(response.output_text)