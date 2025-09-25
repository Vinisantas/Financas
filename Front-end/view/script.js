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
    atualizarDados();
  } catch {
    exibirMensagem(elementoMensagem, `Erro ao adicionar ${tipo}.`, "error");
  }
}

// 🔹 Atualizar dados na tela (saldo e transações)
function atualizarDados() {
  carregaSaldo();
  if (document.getElementById("lista-transacoes")) {
    carregarTransacoes("lista-transacoes");
  }
  if (typeof carregarRelatorios === 'function') carregarRelatorios();
}

// 🔹 Exibir mensagens temporárias
function exibirMensagem(elemento, mensagem, tipo) {
  const div = document.getElementById(elemento);
  if (!div) return;
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

// 🔹 Formatar data
function formatarData(dataString) {
  const [datePart, timePart] = dataString.split(' ');
  const [ano, mes, dia] = datePart.split('-');
  const hora = timePart ? timePart.substring(0, 5) : '';
  return { data: `${dia}/${mes}/${ano}`, hora };
}

// 🔹 Carregar transações
async function carregarTransacoes(elementId) {
  const lista = document.getElementById(elementId);
  if (!lista) return;
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
      const { data, hora } = formatarData(t.data);

      item.innerHTML = `
        <div class="info-container">
          <strong class="categoria">${t.categoria}</strong>
          <span class="descricao">${t.descricao || "Sem descrição"}</span>
          <small class="data">${data} às ${hora}</small>
        </div>
        <span class="valor">R$ ${parseFloat(t.valor).toFixed(2)}</span>
      `;

      const btnExcluir = document.createElement("button");
      btnExcluir.textContent = "Excluir";
      btnExcluir.className = "btn-excluir";
      btnExcluir.addEventListener("click", () => excluir(t.id));
      item.appendChild(btnExcluir);

      lista.appendChild(item);
    });
  } catch {
    lista.innerHTML = `<div class="error">Erro ao carregar transações.</div>`;
  }
}

// 🔹 Carregar saldo
async function carregaSaldo() {
  const saldoElement = document.getElementById("exibe-saldo");
  const quickSaldoElement = document.getElementById("quick-saldo");

  try {
    const extrato = await api("saldo");
    const saldo = parseFloat(extrato.saldo) || 0;
    const saldoFormatado = `R$ ${saldo.toFixed(2).replace('.', ',')}`;
    const corSaldo = saldo >= 0 ? "#22c55e" : "#ef4444";

    if (saldoElement) {
      saldoElement.textContent = saldoFormatado;
      saldoElement.style.color = corSaldo;
    }
    if (quickSaldoElement) {
      quickSaldoElement.textContent = saldoFormatado;
    }
  } catch {
    if (saldoElement) saldoElement.textContent = "Erro";
  }
}

// 🔹 Carregar resumo da página inicial
async function carregarResumoIndexPage() {
  try {
    const { transacoes } = await api("transacoes");
    const hoje = new Date().toISOString().split('T')[0];
    const transacoesHoje = transacoes.filter(t => t.data.startsWith(hoje)).length;
    const el = document.getElementById("transacoes-hoje");
    if (el) el.textContent = transacoesHoje;
  } catch {
    const el = document.getElementById("transacoes-hoje");
    if (el) el.textContent = "N/A";
  }
}

// 🔹 Inicialização
document.addEventListener('DOMContentLoaded', () => {
  carregaSaldo();
  if (document.getElementById("lista-transacoes")) {
    carregarTransacoes("lista-transacoes");
  }
  if (document.getElementById("transacoes-hoje")) {
    carregarResumoIndexPage();
  }

  // Adicionar listeners dos formulários
  const formReceita = document.getElementById("form-receita");
  const formDespesa = document.getElementById("form-despesa");

  if (formReceita) {
    formReceita.addEventListener("submit", async (e) => {
      e.preventDefault();
      await processarTransacao(formReceita, "receita", "mensagem-receita");
    });
  }

  if (formDespesa) {
    formDespesa.addEventListener("submit", async (e) => {
      e.preventDefault();
      await processarTransacao(formDespesa, "despesa", "mensagem-despesa");
    });
  }
});
