import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

kernel = sk.Kernel()

api_key, org_id = sk.openai_settings_from_dot_env()
kernel.add_text_completion_service("dv", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))

prompt = input('\nHow can I help you? ')

response = kernel.create_semantic_function(prompt)

print("\n")
print(response())
print("\n\n")

