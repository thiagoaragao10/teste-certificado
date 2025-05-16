from fastapi import FastAPI, Request, Form, UploadFile
from fastapi.responses import HTMLResponse
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.hazmat.backends import default_backend
from fastapi.staticfiles import StaticFiles  # Pode manter para uso futuro

app = FastAPI()

# Comentado pois a pasta "static" ainda não existe
# app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <html>
        <head>
            <title>Certipe - Teste de Certificado</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                }
                h1 {
                    color: #2e7d32;
                    margin-bottom: 30px;
                }
                form {
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
                }
                input[type=file] {
                    margin-bottom: 20px;
                }
                input[type=submit] {
                    background-color: #2e7d32;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 5px;
                    cursor: pointer;
                }
                input[type=submit]:hover {
                    background-color: #1b5e20;
                }
                .mensagem {
                    margin-top: 20px;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <h1>Certipe</h1>
            <form action="/verificar_certificado" enctype="multipart/form-data" method="post">
                <input type="file" name="certificado" required>
                <br>
                <input type="submit" value="Verificar Certificado">
            </form>
        </body>
    </html>
    """


@app.post("/verificar_certificado", response_class=HTMLResponse)
async def verificar_certificado(certificado: UploadFile):
    try:
        conteudo = await certificado.read()

        # Aqui tentamos carregar o certificado usando senha vazia, se necessário, pode ajustar
        pkcs12.load_key_and_certificates(conteudo, password=b"", backend=default_backend())

        mensagem = "<p class='mensagem' style='color:green;'>✅ Certificado carregado com sucesso



