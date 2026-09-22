from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# Estado do jogo (reinicia a cada acesso)
numero_secreto = 79
tentativas = []

@app.get("/")
def home():
    html = """
    <html>
      <body style="font-family: sans-serif; max-width: 500px; margin: 50px auto; text-align: center;">
        <h1> Adivinhe o Número</h1>
        <p>Estou pensando em um número entre 1 e 100.</p>
        <form action="/chutar" method="get">
          <input type="number" name="palpite" min="1" max="100" required
                 style="padding: 8px; font-size: 16px;">
          <button type="submit" style="padding: 8px 16px; font-size: 16px;">Chutar</button>
        </form>
      </body>
    </html>
    """
    return HTMLResponse(html)

@app.get("/chutar")
def chutar(palpite: int):
    global tentativas
    if palpite == numero_secreto:
        resultado = f" Acertou! O número era {numero_secreto}."
        tentativas = []
    elif palpite < numero_secreto:
        resultado = f" O número é MAIOR que {palpite}."
        tentativas.append(palpite)
    else:
        resultado = f" O número é MENOR que {palpite}."
        tentativas.append(palpite)

    html = f"""
    <html>
      <body style="font-family: sans-serif; max-width: 500px; margin: 50px auto; text-align: center;">
        <h1> Adivinhe o Número</h1>
        <p style="font-size: 20px;">{resultado}</p>
        <form action="/chutar" method="get">
          <input type="number" name="palpite" min="1" max="100" required
                 style="padding: 8px; font-size: 16px;">
          <button type="submit" style="padding: 8px 16px; font-size: 16px;">Chutar</button>
        </form>
        <p>Tentativas: {tentativas}</p>
        <a href="/">Reiniciar</a>
      </body>
    </html>
    """
    return HTMLResponse(html)
