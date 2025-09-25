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

// 🔹 Atualizar dados na tela (saldo e transações)
function atualizarDados() {
  carregaSaldo();
  // Verifica em qual página estamos para recarregar a lista correta
  if (document.getElementById("lista-transacoes")) {
    carregarTransacoes("lista-transacoes");
  }
  // Se houver uma função para carregar relatórios, chame-a também
  if (typeof carregarRelatorios === 'function') carregarRelatorios();
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

/**
 * Formata uma string de data 'YYYY-MM-DD' para o formato 'DD/MM/YYYY'.
 * @param {string} dataString A data no formato 'YYYY-MM-DD'..
 * @returns {string} A data formatada.
 */
function formatarData(dataString) {
  // A data vem como "YYYY-MM-DD HH:MM:SS", separamos a data da hora.
  const [datePart, timePart] = dataString.split(' ');
  const [ano, mes, dia] = datePart.split('-');
  
  // Retorna um objeto com a data e a hora (sem os segundos)
  const hora = timePart ? timePart.substring(0, 5) : ''; // Pega apenas HH:MM
  return { data: `${dia}/${mes}/${ano}`, hora: hora };
}

// 🔹 Carregar transações
async function carregarTransacoes(elementId) {
  const lista = document.getElementById(elementId);
  if (!lista) {
    // console.warn(`Elemento com ID "${elementId}" não encontrado.`);
    return;
  }
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
      btnExcluir.className = "btn-excluir"; // Adiciona uma classe para estilização
      btnExcluir.addEventListener("click", () => excluir(t.id));
      // Adiciona o botão diretamente ao item da transação
      item.appendChild(btnExcluir);

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
    const quickSaldoElement = document.getElementById("quick-saldo"); // Para a página inicial
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
    document.getElementById("exibe-saldo").textContent = "Erro";
  }
}

document.addEventListener('DOMContentLoaded', () => {
  // Carrega o saldo em todas as páginas que incluem este script
  carregaSaldo();
  
  // Carrega a lista de transações recentes apenas se o elemento existir na página (inputs.html)
  if (document.getElementById("lista-transacoes")) {
    carregarTransacoes("lista-transacoes");
  }

  // Carrega o resumo da página inicial se os elementos existirem
  if (document.getElementById("transacoes-hoje")) {
    carregarResumoIndexPage();
  }
});

/**
 * Carrega os dados específicos da página inicial (index.html).
 */
async function carregarResumoIndexPage() {
  try {
    const { transacoes } = await api("transacoes");
    const hoje = new Date().toISOString().split('T')[0]; // Formato YYYY-MM-DD

    // Compara apenas a parte da data (YYYY-MM-DD), ignorando a hora.
    const transacoesHoje = transacoes.filter(t => t.data.startsWith(hoje)).length;
    document.getElementById("transacoes-hoje").textContent = transacoesHoje;
  } catch (error) {
    console.error("Erro ao carregar resumo do dia:", error);
    document.getElementById("transacoes-hoje").textContent = "N/A";
  }
}
