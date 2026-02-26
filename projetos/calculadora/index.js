let operacaoAtual = "";

const resultadoEl = document.getElementById("resultado");
const operacaoEl = document.getElementById("operacao");
const historyEl = document.getElementById("historyList");

function atualizarDisplay() {
    operacaoEl.innerHTML = operacaoAtual;
}

function insert(valor) {
    operacaoAtual += valor;
    atualizarDisplay();
}

function clean() {
    operacaoAtual = "";
    resultadoEl.innerHTML = "0";
    atualizarDisplay();
}

function back() {
    operacaoAtual = operacaoAtual.slice(0, -1);
    atualizarDisplay();
}

function calcular() {
    if (!operacaoAtual) return;

    try {
        let resultado = eval(operacaoAtual);

        resultadoEl.innerHTML = resultado;

        adicionarHistorico(operacaoAtual, resultado);

        operacaoAtual = resultado.toString();
        atualizarDisplay();

    } catch {
        resultadoEl.innerHTML = "Erro";
    }
}

/* =========================
   FUNÇÕES CIENTÍFICAS
========================= */

function scientific(tipo) {
    try {
        let valor = eval(operacaoAtual);

        switch (tipo) {
            case "sin":
                valor = Math.sin(valor);
                break;
            case "cos":
                valor = Math.cos(valor);
                break;
            case "tan":
                valor = Math.tan(valor);
                break;
            case "sqrt":
                valor = Math.sqrt(valor);
                break;
            case "log":
                valor = Math.log10(valor);
                break;
        }

        adicionarHistorico(tipo + "(" + operacaoAtual + ")", valor);

        operacaoAtual = valor.toString();
        resultadoEl.innerHTML = valor;
        atualizarDisplay();

    } catch {
        resultadoEl.innerHTML = "Erro";
    }
}

/* =========================
   HISTÓRICO
========================= */

function adicionarHistorico(conta, resultado) {
    const item = document.createElement("p");
    item.textContent = `${conta} = ${resultado}`;
    historyEl.prepend(item);
}
/* =========================
   SUPORTE AO TECLADO
========================= */

document.addEventListener("keydown", (e) => {

    if (!isNaN(e.key) || "+-*/().".includes(e.key)) {
        insert(e.key);
    }

    if (e.key === "Enter") calcular();

    if (e.key === "Backspace") back();

    if (e.key === "Escape") clean();
});