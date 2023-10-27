<!-- LOGIN -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Utility Hub API - Login</title>

    <!-- Import css -->
    <link rel="stylesheet" href="../../utils/css/default.css">
</head>

<script>
    function validateLoginForm() {
        var nome = document.getElementById("name").value;
        var email = document.getElementById("email").value;
        var password = document.getElementById("password").value;
        var confirm_password = document.getElementById("confirm_password").value;

        if (nome == "" || email == "" || password == "" || confirm_password == "") {
            alert("Preencha todos os campos!");
            return false;
        }

        if (password != confirm_password) {
            alert("As senhas não coincidem!");
            return false;
        }

        return true;
    }
</script>

<body>
    <div class="container">
        <h1>Login</h1>
        <p>Para acessar o painel de controle, faça login.</p>
        <p>Se você não tem uma conta, <a href="../registrar/">clique aqui</a> para criar uma.</p>
        <br>

        <!-- TODO: Incluir action -->
        <form method="post" action="" onsubmit="return validateLoginForm()">
            <input class="input" type="text" placeholder="E-mail" name="email" required>
            <input class="input" type="password" placeholder="Senha" name="password" required>
            <button type="submit" class="btn">Entrar</button>
        </form>
    </div>
</body>

</html>