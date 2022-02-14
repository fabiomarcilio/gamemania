$(document).ready(function (e) {
    $("#id_valor_estimado").each(function (index, element) {
        decimalMask(element);
    });
});

$(".capitalizar").blur(function () {
    if (this.value) {
        this.value = Capitalizar(this.value);
    }
});


function decimalMask(element) {
    const decimalPlaces = parseInt($(element).data("decimalPlaces"));
    $(element).mask("000.000.000,00" + "9".repeat(decimalPlaces), { reverse: true });
};

$(document).on("submit", function () {
    // remove máscaras no submit do form
    $('.mask-data').unmask();
});


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