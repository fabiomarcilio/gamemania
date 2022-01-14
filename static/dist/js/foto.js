$(document).ready(function (e) {
    $("#img-foto-usuario").on("click", imgFotoClickHandler);
    $('#foto-usuario-input').on("change", fotoUsuarioChangeHandler);
});

function imgFotoClickHandler() {
    $("#foto-usuario-input").click();
}

function fotoUsuarioChangeHandler() {
    const reader = new FileReader();
    reader.onload = function (event) {
        // troca a imagem no frontend
        $('#img-foto-usuario').attr("src", event.target.result);
    };
    // lê o arquivo de imagem como data URL
    reader.readAsDataURL(this.files[0]);
    $('#remover_foto').attr("checked", false);
};