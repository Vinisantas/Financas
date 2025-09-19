 // Funções JavaScript com melhorias para o novo layout
    const formReceita = document.getElementById("form-receita");
    const formDespesa = document.getElementById("form-despesa");

    formReceita.addEventListener("submit", async function (e) {
      e.preventDefault();
      await processarTransacao(this, "receita", "mensagem-receita");
    });

    formDespesa.addEventListener("submit", async function (e) {
      e.preventDefault();
      await processarTransacao(this, "despesa", "mensagem-despesa");
    });

    async function processarTransacao(form, tipo, elementoMensagem) {
      const formData = new FormData(form);
      const payload = {
        valor: parseFloat(formData.get("valor")),
        categoria: formData.get("categoria"),
        descricao: formData.get("descricao"),
      };

      try {
        const response = await fetch(`http://localhost:8000/${tipo}`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload)
        });

        const result = await response.json();
        exibirMensagem(elementoMensagem, result.mensagem, "success");

        form.reset();
        carregarTransacoes();
        carregaSaldo();
      } catch (error) {
        console.error(`Erro ao adicionar ${tipo}:`, error);
        exibirMensagem(elementoMensagem, `Erro ao adicionar ${tipo}.`, "error");
      }
    }

    function exibirMensagem(elemento, mensagem, tipo) {
      const div = document.getElementById(elemento);
      div.textContent = mensagem;
      div.className = tipo;

      // Limpar mensagem após 3 segundos
      setTimeout(() => {
        div.textContent = '';
        div.className = '';
      }, 3000);
    }

  async function excluir(id) {
    try {
      const res = await fetch(`http://localhost:8000/deleta/${id}`, {
        method: 'DELETE'
      });
    if (!res.ok) {
      throw new Error(`Erro ao excluir transação: ${res.status}`);
    }

    await carregarTransacoes(); // recarrega a lista
  } catch (err) {
    console.error(err);
  }
}

    async function carregarTransacoes() {
      try {
        const res = await fetch("http://localhost:8000/transacoes");
        if (!res.ok) {
          throw new Error(`Erro ao carregar transações: ${res.status}`);
        }
        const data = await res.json();

        const lista = document.getElementById("lista-transacoes");
        lista.innerHTML = "";

        if (!data || !data.transacoes || data.transacoes.length === 0) {
          lista.innerHTML = `
            <div class="empty-state">
              <p>Nenhuma transação registrada.</p>
              <small>Adicione receitas ou despesas para começar</small>
            </div>`;
          return;
        }

        data.transacoes.forEach((t) => {
          const item = document.createElement("div");
          item.className = `transacao ${t.tipo === 'r' ? 'receita' : 'despesa'}`;

          const dataFormatada = formatarData(t.data);

          item.innerHTML = `
            <div class="info-container">
              <span class="categoria">${t.categoria}</span>
              <span class="descricao">${t.descricao || 'Sem descrição'}</span>
              <span class="data">${dataFormatada}</span>
              <button onclick="excluir(${t.id})">excluir</button>
            </div>
            <span class="valor">R$ ${parseFloat(t.valor).toFixed(2)}</span>
          `;

          lista.appendChild(item);
        });
      } catch (error) {
        console.error("Erro ao carregar transações:", error);
        document.getElementById("lista-transacoes").innerHTML = `
          <div class="error">Erro ao carregar transações. Verifique sua conexão.</div>`;
      }
    }

    function formatarData(dataString) {
      const data = new Date(dataString);
      return new Intl.DateTimeFormat('pt-BR', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      }).format(data);
    }

    async function carregaSaldo() {
      try {
        const res = await fetch("http://localhost:8000/saldo");
        const extrato = await res.json();

        const saldoElement = document.getElementById("exibe-saldo");

        if (extrato.saldo === undefined || extrato.saldo === null) {
          saldoElement.textContent = "R$ 0,00";
          return;
        }

        const saldo = parseFloat(extrato.saldo);
        saldoElement.textContent = `R$ ${saldo.toFixed(2)}`;

        // Adicionar cor baseada no saldo (verde para positivo, vermelho para negativo)
        saldoElement.style.color = saldo >= 0 ? '#22c55e' : '#ef4444';
      } catch (error) {
        console.error("Erro ao carregar saldo:", error);
        document.getElementById("exibe-saldo").textContent = "Erro";
      }
    }
    
    // Carregar ao abrir a página
// --- INICIALIZAÇÃO ---
  document.addEventListener('DOMContentLoaded', () => {
    carregaSaldo();
    if (document.getElementById("lista-transacoes")) {
      carregarTransacoes();
    }
  });
