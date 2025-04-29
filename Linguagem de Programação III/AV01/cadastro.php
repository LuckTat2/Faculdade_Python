<?php
$conn = new mysqli('localhost', 'root', 'admin121', 'sistema_cobranca', 3306);

if ($conn->connect_error) {
    die("Erro de conexão: " . $conn->connect_error);
}

$nome = $_POST['nome'];
$email = $_POST['email'];
$telefone = $_POST['telefone'];
$valor = $_POST['valor'];
$vencimento = $_POST['vencimento'];
$status = $_POST['status']; // Captura o status da fatura

// Insere os dados do cliente
$conn->query("INSERT INTO clientes (nome, email, telefone) VALUES ('$nome', '$email', '$telefone')");
$cliente_id = $conn->insert_id;

// Insere a fatura com o status correto
$conn->query("INSERT INTO faturas (cliente_id, valor, vencimento, status) VALUES ($cliente_id, $valor, '$vencimento', '$status')");

// Exibe mensagem de sucesso com HTML e CSS
?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Cadastro Realizado com Sucesso</title>
    <link rel="stylesheet" href="estilo2.css">
</head>
<body>
    <div class="sucesso-container">
        <h2>Cadastro realizado com sucesso!</h2>
        <p>Os dados foram gravados no banco com sucesso.</p>
        <a href="formulario.html" class="voltar-btn">Voltar ao formulário</a>
    </div>
</body>
</html>
<?php
$conn->close();
exit();
?>
