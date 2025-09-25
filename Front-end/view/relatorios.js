// Mapeamento de meses para seus nomes
const NOME_MES = {
  "01": "Janeiro", "02": "Fevereiro", "03": "Março", "04": "Abril",
  "05": "Maio", "06": "Junho", "07": "Julho", "08": "Agosto",
  "09": "Setembro", "10": "Outubro", "11": "Novembro", "12": "Dezembro"
};

/**
 * Função principal para carregar todos os dados dos relatórios.
 */
async function carregarRelatorios() {
  const mesSelecionado = document.getElementById('filtro-mes').value;
  const params = mesSelecionado ? `?mes=${mesSelecionado}` : '';

  // Atualiza o título do resumo
  const tituloMes = document.getElementById('titulo-mes');
  tituloMes.textContent = mesSelecionado ? `Resumo de ${NOME_MES[mesSelecionado]}` : 'Resumo Geral';

  // Carrega todos os componentes do dashboard em paralelo
  await Promise.all([
    carregarResumo(params),
    carregarGraficoCategorias(params),
    carregarEvolucaoMensal(),
    carregarTransacoesDoMes(params)
  ]);
}

/**
 * Formata um valor numérico para o formato de moeda BRL.
 */
function formatarMoeda(valor) {
  return `R$ ${parseFloat(valor || 0).toFixed(2).replace('.', ',')}`;
}

/**
 * Carrega os cards de resumo (Receitas, Despesas, Saldo do Mês).
 */
async function carregarResumo(params) {
  try {
    const resumo = await api(`relatorio/resumo${params}`);
    document.getElementById('receitas-mes').textContent = formatarMoeda(resumo.receitas);
    document.getElementById('despesas-mes').textContent = formatarMoeda(resumo.despesas);
    document.getElementById('saldo-mes').textContent = formatarMoeda(resumo.saldo);
  } catch (error) {
    console.error('Erro ao carregar resumo:', error);
  }
}

/**
 * Carrega e renderiza os gráficos de categorias (receitas e despesas).
 */
async function carregarGraficoCategorias(params) {
  const containerReceitas = document.getElementById('grafico-receitas');
  const containerDespesas = document.getElementById('grafico-categorias');

  try {
    const data = await api(`relatorio/categorias${params}`);
    
    // Renderiza gráfico de receitas
    renderizarItensCategoria(containerReceitas, data.receitas, 'receita');
    
    // Renderiza gráfico de despesas
    renderizarItensCategoria(containerDespesas, data.despesas, 'despesa');

  } catch (error) {
    console.error('Erro ao carregar gráficos de categoria:', error);
    containerReceitas.innerHTML = '<p class="error">Erro ao carregar dados.</p>';
    containerDespesas.innerHTML = '<p class="error">Erro ao carregar dados.</p>';
  }
}

/**
 * Função auxiliar para renderizar os itens de um gráfico de categoria.
 */
function renderizarItensCategoria(container, categorias, tipo) {
  container.innerHTML = '';
  const total = Object.values(categorias).reduce((soma, v) => soma + v, 0);

  if (Object.keys(categorias).length === 0) {
    container.innerHTML = `<p class="empty-state">Nenhuma ${tipo} registrada.</p>`;
    return;
  }

  for (const [nome, valor] of Object.entries(categorias)) {
    const percentual = total > 0 ? (valor / total) * 100 : 0;
    const itemHTML = `
      <div class="item-categoria ${tipo}">
        <div class="info-categoria">
          <span class="nome-categoria">${nome}</span>
          <div class="barra-container">
            <div class="barra-progresso ${tipo}" style="width: ${percentual}%;"></div>
          </div>
        </div>
        <span class="valor-categoria">${formatarMoeda(valor)}</span>
      </div>
    `;
    container.innerHTML += itemHTML;
  }
}

/**
 * Carrega e renderiza o gráfico de evolução mensal.
 */
async function carregarEvolucaoMensal() {
  const container = document.getElementById('evolucao-mensal');
  try {
    const data = await api('relatorio/evolucao');
    container.innerHTML = '';

    if (data.length === 0) {
      container.innerHTML = '<p class="empty-state">Dados insuficientes para exibir evolução.</p>';
      return;
    }

    const maxReceita = Math.max(...data.map(d => d.valores.receitas));
    const maxDespesa = Math.max(...data.map(d => d.valores.despesas));
    const maxValor = Math.max(maxReceita, maxDespesa);

    data.forEach(({ mes, valores }) => {
      const percentReceita = maxValor > 0 ? (valores.receitas / maxValor) * 100 : 0;
      const percentDespesa = maxValor > 0 ? (valores.despesas / maxValor) * 100 : 0;

      const itemHTML = `
        <div class="barra-mensal">
          <span class="mes-label">${NOME_MES[mes]}</span>
          <div class="barra-mes-container">
            <div class="barra-receitas" style="width: ${percentReceita}%;"></div>
          </div>
          <div class="valores-mes">
            <span class="valor-mes receita">${formatarMoeda(valores.receitas)}</span>
            <span class="valor-mes despesa">${formatarMoeda(valores.despesas)}</span>
          </div>
        </div>
      `;
      container.innerHTML += itemHTML;
    });

  } catch (error) {
    console.error('Erro ao carregar evolução mensal:', error);
    container.innerHTML = '<p class="error">Erro ao carregar dados.</p>';
  }
}

/**
 * Carrega a lista de transações para o mês selecionado.
 */
async function carregarTransacoesDoMes(params) {
  const lista = document.getElementById('lista-transacoes-mes');
  // A função carregarTransacoes já existe em script.js, vamos reutilizá-la
  // mas precisamos de um endpoint que filtre por mês.
  // O endpoint /transacoes retorna tudo. Vamos criar um novo ou adaptar.
  // Usaremos o novo endpoint: /relatorio/transacoes_mes
  
  lista.innerHTML = '<p>Carregando transações...</p>';
  try {
    const endpoint = params ? `relatorio/transacoes_mes${params}` : 'transacoes';
    const data = await api(endpoint);
    
    // A resposta de /transacoes é {transacoes: [...]}, a de /relatorio/transacoes_mes é [...]
    const transacoes = data.transacoes || data;

    lista.innerHTML = '';
    if (!transacoes || transacoes.length === 0) {
      lista.innerHTML = '<p class="empty-state">Nenhuma transação neste período.</p>';
      return;
    }

    transacoes.forEach(t => {
      const tipo = t.tipo === 'r' ? 'receita' : 'despesa';
      const dataFormatada = new Date(t.data + 'T00:00:00').toLocaleDateString('pt-BR');
      const itemHTML = `
        <div class="transacao ${tipo}">
          <div class="info-container">
            <span class="categoria">${t.categoria}</span>
            <span class="descricao">${t.descricao}</span>
            <span class="data">${dataFormatada}</span>
          </div>
          <span class="valor">${formatarMoeda(t.valor)}</span>
        </div>
      `;
      lista.innerHTML += itemHTML;
    });
  } catch (error) {
    console.error('Erro ao carregar transações do mês:', error);
    lista.innerHTML = '<p class="error">Erro ao carregar transações.</p>';
  }
}