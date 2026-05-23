document.getElementById("submit").addEventListener("click", validaFormulario);

function validaFormulario() {
    if (document.getElementById("name").value != "" && 
        document.getElementById("email").value != "") {
    alert("Formulário enviado com sucesso!");
} else {
    alert("Por favor, preencha todos os campos obrigatórios.");
}
}

