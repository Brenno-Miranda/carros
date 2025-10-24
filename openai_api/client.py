from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_bio_car_ia(model, brand, value, factory_year):
    client = OpenAI()

    prompt = f"""
        Você é um assistente especialista em gerar descrições de carros para consultas futuras. Suas descrições devem ser baseadas nas informações passadas sobre o carro(modelo, marca, valor, ano). Suas respostas devem conter no máximo 200 caracteres. Dados do carro:
        Modelo: {model}
        Marca: {brand}
        Valor: {value}
        Ano: {factory_year}
    """ 

    response = client.chat.completions.create(
        model='gpt-4.1-nano',
        max_tokens=500,
        messages=[
            {'role': 'user', 'content': prompt}
        ]
    )

    return response.choices[0].message.content