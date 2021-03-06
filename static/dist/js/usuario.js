var SPMaskBehavior = function (val) {
    return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
},
    spOptions = {
        onKeyPress: function (val, e, field, options) {
            field.mask(SPMaskBehavior.apply({}, arguments), options);
        }
    };
// $('.sp_celphones').mask(SPMaskBehavior, spOptions);

$(".capitalizar").blur(function () {
    if (this.value) {
        this.value = Capitalizar(this.value);
    }
});

$(function () {
    //Adiciona máscaras na criação da tela.
    $('.mask-cpf').mask('000.000.000-00', { reverse: true });
    // $('.mask-data').mask('00/00/0000');
    $('.mask-telefone').mask(SPMaskBehavior, spOptions);
    $('.mask-cep').mask('00000-000');
    $(".cnpj").mask("00.000.000/0000-00", { reverse: true });

});

$(document).on("submit", function () {
    // remove máscaras no submit do form
    $('.mask-cpf').unmask();
    // $('.mask-data').unmask();
    $('.mask-telefone').unmask();
    $('.mask-cep').unmask();
});

// pesquisa o cep pela API do Via Cep e preenche os campos (cep.js)
$(".mask-cep").blur(function () {
    pesquisarCep($(this));
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
