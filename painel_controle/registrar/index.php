<!-- Registrar -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Utility Hub API - Registrar</title>

    <!-- Import css -->
    <link rel="stylesheet" href="../../utils/css/default.css">
</head>

<script>
    function validateRegisterForm() {
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
        <h1>Registrar</h1>
        <p>Parar criar uma nova conta, preencha todos os campos a seguir</p>
        <br>

        <!-- TODO: Incluir action -->
        <form method="post" action="" onsubmit="return validateRegistrarForm()">

            <input class="input" type="text" placeholder="Nome completo" name="name" required>
            <input class="input" type="text" placeholder="E-mail" name="email" required>
            <input class="input" type="password" placeholder="Senha" name="password" required>
            <input class="input" type="password" placeholder="Confirmar senha" name="confirm_password" required>
            <button type="submit" class="btn">Registrar</button>
        </form>
    </div>
</body>

</html>