import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

def chatgpt(prompt):
    kernel = sk.Kernel()
    api_key, org_id = sk.openai_settings_from_dot_env()
    kernel.add_text_completion_service("dv", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))
    with open('resume.txt', encoding='utf-8') as f:
        lines = f.readlines()
    user_input = ' '.join(lines) + ' ' + prompt
    semantic_function = kernel.create_semantic_function(user_input)
    response = semantic_function()
    return response

