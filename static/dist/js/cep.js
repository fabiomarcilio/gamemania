function limparFormularioCep() {
    //Limpa valores do formulário de cep.
    document.getElementById('id_logradouro').value = ("");
    document.getElementById('id_bairro').value = ("");
    document.getElementById('id_cidade').value = ("");
    document.getElementById('id_uf').value = ("");
    // document.getElementById('id_ibge').value = ("");
};

function viaCepCallback(conteudo) {
    if (!("erro" in conteudo)) {
        document.getElementById('id_logradouro').value = (conteudo.logradouro);
        document.getElementById('id_bairro').value = (conteudo.bairro);
        document.getElementById('id_cidade').value = (conteudo.localidade);
        document.getElementById('id_uf').value = (conteudo.uf);
        // document.getElementById('id_ibge').value = (conteudo.ibge);
    } else {
        limparFormularioCep();
        toastr.error('CEP não encontrado.');
    };
};

function pesquisarCep(obj) {

    const valor = obj.val();
    const id = obj.attr('id');
    const cep = valor.replace(/\D/g, '');

    if (cep !== '' && cep !== '99999999') {

        //Expressão regular para validar o CEP.
        const validacep = /^[0-9]{8}$/;

        //Valida o formato do CEP.
        if (validacep.test(cep)) {

            //Preenche os campos com "..." enquanto consulta webservice.
            document.getElementById('id_logradouro').value = "...";
            document.getElementById('id_bairro').value = "...";
            document.getElementById('id_cidade').value = "...";
            document.getElementById('id_uf').value = "...";
            // document.getElementById('id_ibge').value = "...";

            $.getJSON('https://viacep.com.br/ws/' + cep + '/json/?callback=', (dados) => {
                viaCepCallback(dados);
            });

        } else {
            limparFormularioCep();
            toastr.error('Formato de CEP inválido.');
        };
    } else {
        limparFormularioCep();
    };
};