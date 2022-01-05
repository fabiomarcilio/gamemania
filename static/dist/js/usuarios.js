var SPMaskBehavior = function (val) {
    return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
},
    spOptions = {
        onKeyPress: function (val, e, field, options) {
            field.mask(SPMaskBehavior.apply({}, arguments), options);
        }
    };
$('.sp_celphones').mask(SPMaskBehavior, spOptions);


$(function () {
    //Adiciona máscaras na criação da tela.
    $('.mask-cpf').mask('000.000.000-00', { reverse: true });
    // $('.mask-data').mask('00/00/0000');
    $('.mask-telefone').mask(SPMaskBehavior, spOptions);
    $('.mask-cep').mask('00000-000');
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
