// URL do backend no Render
const BACKEND_URL = "https://financas-j3ri.onrender.com";

// 🔹 Função central de API
async function api(endpoint, options = {}) {
  try {
    const res = await fetch(`${BACKEND_URL}/${endpoint}`, {
      headers: { "Content-Type": "application/json" },
      ...options,
    });
    if (!res.ok) throw new Error(`Erro: ${res.status}`);
    return await res.json();
  } catch (error) {
    console.error("Erro API:", error);
    throw error;
  }
}

// 🔹 Processar transação (receita ou despesa)
async function processarTransacao(form, tipo, elementoMensagem) {
  const formData = new FormData(form);
  const payload = {
    valor: parseFloat(formData.get("valor")),
    categoria: formData.get("categoria"),
    descricao: formData.get("descricao"),
  };

  if (!payload.valor || payload.valor <= 0) {
    return exibirMensagem(elementoMensagem, "Valor inválido!", "error");
  }

  try {
    const result = await api(tipo, {
      method: "POST",
      body: JSON.stringify(payload),
    });

    exibirMensagem(elementoMensagem, result.mensagem, "success");
    form.reset();
    atualizarDados(); // Atualiza tudo (saldo, transações e relatórios)
  } catch {
    exibirMensagem(elementoMensagem, `Erro ao adicionar ${tipo}.`, "error");
  }
}

// 🔹 Exibir mensagens temporárias
function exibirMensagem(elemento, mensagem, tipo) {
  const div = document.getElementById(elemento);
  div.textContent = mensagem;
  div.className = tipo;

  setTimeout(() => {
    div.textContent = "";
    div.className = "";
  }, 3000);
}

// 🔹 Excluir transação
async function excluir(id) {
  try {
    await api(`deleta/${id}`, { method: "DELETE" });
    atualizarDados();
  } catch {
    exibirMensagem("mensagem-despesa", "Erro ao excluir transação.", "error");
  }
}

// 🔹 Carregar transações
async function carregarTransacoes() {
  const lista = document.getElementById("lista-transacoes");
  lista.innerHTML = "<p>Carregando...</p>";

  try {
    const data = await api("transacoes");
    lista.innerHTML = "";

    if (!data?.transacoes?.length) {
      lista.innerHTML = `
        <div class="empty-state">
          <p>Nenhuma transação registrada.</p>
          <small>Adicione receitas ou despesas para começar</small>
        </div>`;
      return;
    }

    data.transacoes.forEach((t) => {
      const item = document.createElement("div");
      item.className = `transacao ${t.tipo === "r" ? "receita" : "despesa"}`;

      const dataFormatada = formatarData(t.data);

      item.innerHTML = `
        <div class="info-container">
          <span class="categoria">${t.categoria}</span>
          <span class="descricao">${t.descricao || "Sem descrição"}</span>
          <span class="data">${dataFormatada}</span>
        </div>
        <span class="valor">R$ ${parseFloat(t.valor).toFixed(2)}</span>
      `;

      const btnExcluir = document.createElement("button");
      btnExcluir.textContent = "Excluir";
      btnExcluir.addEventListener("click", () => excluir(t.id));
      item.querySelector(".info-container").appendChild(btnExcluir);

      lista.appendChild(item);
    });
  } catch {
    lista.innerHTML = `<div class="error">Erro ao carregar transações.</div>`;
  }
}

// 🔹 Carregar saldo
async function carregaSaldo() {
  try {
    const extrato = await api("saldo");
    const saldoElement = document.getElementById("exibe-saldo");
    const saldo = parseFloat(extrato.saldo) || 0;

    saldoElement.textContent = `R$ ${saldo.toFixed(2)}`;
    saldoElement.style.color = saldo >= 0 ? "#22c55e" : "#ef4444";
  } catch {
    document.getElementById("exibe-saldo").textContent = "Erro";
  }
}

document.addEventListener('DOMContentLoaded', () => {
  // Carrega o saldo em todas as páginas que incluem este script
  carregaSaldo();
  
  // Carrega a lista de transações recentes apenas se o elemento existir na página (inputs.html)
  if (document.getElementById("lista-transacoes")) {
    carregarTransacoes();
  }
});
