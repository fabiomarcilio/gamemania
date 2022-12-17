$(document).ready(function (e) {
    $('.money1').mask('000.000.000.000.000,00', {reverse: true});
    $('.money2').mask('000.000.000.000.000,00', {reverse: true});
});

$(".capitalizar").blur(function () {
    if (this.value) {
        this.value = Capitalizar(this.value);
    }
});

$(document).on("submit", function () {
    // remove máscaras no submit do form
    $('.mask-data').unmask();
    $('.money1').val(BRLParaFloat($('.money1').val()));
    $('.money2').val(BRLParaFloat($('.money2').val()));
});

function BRLParaFloat(strBRL) {
    // recebe uma string representando um valor em reais e converte em Float
    // preenche com 0,00 caso receba vazia (ex: usuário limpou o campo)
    retorno = parseFloat(strBRL.replace(".", "").replace(",", "."));
    if (typeof retorno !== "number" || isNaN(retorno) || retorno < 0 || !isFinite(retorno)) {
        return 0.00
    };
    return retorno
};


function Capitalizar(nome) {
    // remove espaços duplicados e divide o nome
    let nomes = nome.toLowerCase().replace("  ", " ").split(" ");
    // preposições para não capitalizar
    let preps = ["e", "da", "das", "de", "di", "do", "dos", "du", "para", "com"];

    // capitaliza a primeira letra de cada palavra
    return nomes
        .map((nome) => {
            if (!nome) {
                return;
            }
            // se encontrar o nome em uma das preposições, não capitaliza
            if (preps.indexOf(nome) >= 0) {
                return nome;
            }
            return nome[0].toUpperCase() + nome.substr(1);
        })
        .join(" ");
}


// Confirmação Sweet Alert chamada pelo htmx para exclusão de registros.
function showDeleteConfirmationWindow(event) {
    event.preventDefault();  // evita a rolagem da tela ao clicar no link
    return Swal.fire({
        title: "Atenção!",
        text: "Deseja realmente apagar este registro?",
        showCancelButton: true,
        reverseButtons: true,
        confirmButtonText: "Sim, apagar!",
        confirmButtonColor: "#dc3545",
        cancelButtonText: "Cancelar",
        cancelButtonColor: "#17a2b8",
    });
};