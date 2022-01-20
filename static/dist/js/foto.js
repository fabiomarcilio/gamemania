$(document).ready(function (e) {
    $("#img-foto").on("click", imgFotoClickHandler);
    $('#foto-input').on("change", fotoChangeHandler);
});

function imgFotoClickHandler() {
    $("#foto-input").click();
}

function fotoChangeHandler() {
    const reader = new FileReader();
    reader.onload = function (event) {
        // troca a imagem no frontend
        $('#img-foto').attr("src", event.target.result);
    };
    // lê o arquivo de imagem como data URL
    reader.readAsDataURL(this.files[0]);
    $('#remover_foto').attr("checked", false);
};