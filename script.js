function testarCertificado() {
  const input = document.getElementById('arquivoCertificado');
  const resultado = document.getElementById('resultado');

  if (!input.files.length) {
    resultado.textContent = 'Por favor, selecione um arquivo de certificado.';
    return;
  }

  const arquivo = input.files[0];
  resultado.textContent = `Arquivo selecionado: ${arquivo.name}\nTestando certificado... (lógica futura aqui)`;

  // Aqui depois podemos adicionar a lógica para ler e validar o certificado
}


