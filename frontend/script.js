const nm_operacional = document.getElementById("num_operacional");
const nm_alerta = document.getElementById("num_alerta");
const nm_manutencao = document.getElementById("num_manutencao");


fetch("http://127.0.0.1:8000/api/fleet")
    .then(resposta => resposta.json())
    .then(data => {
        atualizar_dados(data)
    })
    .catch(error => console.error("Erro na API:", error))

function atualizar_dados(data){
    nm_operacional.innerText = data.operacional;
    nm_alerta.innerText = data.alerta
    nm_manutencao.innerText = data.manutencao
}
