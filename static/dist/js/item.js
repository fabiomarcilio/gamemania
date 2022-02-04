
$(".capitalizar").blur(function () {
    if (this.value) {
        this.value = Capitalizar(this.value);
    }
});

$(document).on("submit", function () {
    // remove máscaras no submit do form
    $('.mask-data').unmask();
});


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