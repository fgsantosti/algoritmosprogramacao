# 🚗 Trabalho Final — Sistemas de Gestão

**Instituto Federal de Educação, Ciência e Tecnologia do Piauí — IFPI / Campus Corrente**

**Disciplina:** Algoritmos e Lógica de Programação

**Curso:** Análise e Desenvolvimento de Sistemas (ADS)

---

## 🎯 Objetivo

Desenvolver um **sistema de gestão** completo, aplicando os conceitos estudados ao longo da disciplina: variáveis e tipos de dados, estruturas de decisão e repetição, listas e dicionários, funções, validação de dados e organização do código.

Cada equipe escolherá **um** dos temas disponíveis abaixo e deverá implementar o sistema atendendo aos requisitos descritos para aquele tema, além dos **requisitos mínimos comuns** a todos os projetos.

> 💡 Todos os temas têm o **mesmo grau de complexidade**. Não há tema "mais fácil" — a nota depende da qualidade da implementação, não do tema escolhido.

---

## 📋 Orientações Gerais

- **Equipes:** de 2 integrantes _(você e Deus)_.
- **Tema:** cada equipe escolhe **um** tema.
- **Linguagem:** Python 3.
- **Entrega:** repositório/pasta com o código-fonte + este README preenchido com os nomes da equipe.
- **Apresentação:** demonstração do sistema funcionando + explicação do código.
- **Prazo de entrega:** `15/07/2026`

---

## ✅ Requisitos Mínimos (comuns a todos os temas)

Independentemente do tema escolhido, o sistema **deve** conter:

1. **Menu principal** com navegação (laço de repetição até o usuário escolher sair).
2. **Cadastro completo (CRUD)** das principais entidades:
   - **C**riar (incluir novo registro)
   - **R**ecuperar (listar / consultar)
   - **U**pdate (alterar dados de um registro)
   - **D**elete (remover registro)
3. **Pelo menos 4 entidades** relacionadas entre si.
4. **Validação de dados de entrada** (não aceitar valores inválidos, campos vazios, opção inexistente no menu etc.).
5. **Regras de negócio** específicas do tema (cálculos, multas, descontos, verificação de disponibilidade etc.).
6. **Manipulação de datas/horas** quando o tema exigir (uso do módulo `datetime`).
7. **Pelo menos 2 relatórios/consultas** com filtro (ex.: listar todos os registros de um período, calcular um total etc.).
8. **Uso de funções** para organizar o código (evitar todo o programa em um único bloco).

### ⭐ Diferenciais (pontuação extra)
- Persistência de dados em arquivo (`.json`, `.csv` ou `.txt`).
- Tratamento de exceções (`try / except`).
- Interface organizada e amigável no terminal.
- Código comentado e bem identado.

---

## 🗂️ Temas Disponíveis

### 1. 🚗 Sistema de Locação de Veículos

A empresa possui uma grande frota de carros de passeio, de diferentes marcas e modelos. Eventualmente um carro é retirado da frota (por acidente grave ou por ser velho demais para o padrão da empresa) e vendido, assim como a frota é renovada — sendo necessário manter sempre o cadastro de veículos atualizado.

Os clientes vão até a empresa e solicitam o aluguel de carros. Primeiro é necessário cadastrá-los, caso ainda não possuam cadastro ou seus dados tenham mudado. Depois de identificado, o cliente escolhe o carro que deseja alugar — **o valor da locação varia conforme o ano, a marca e o modelo**. Durante a locação, o cliente informa por **quanto tempo** usará o carro, **para qual finalidade** e **por onde** trafegará, pois isso também influencia o preço. Antes de liberar o veículo, a empresa exige uma **caução** (valor superior ao estimado); o que não for utilizado é devolvido ao cliente.

Na devolução, define-se o carro como devolvido, registra-se data, hora e quilometragem e verifica-se se ele está nas mesmas condições da locação. Se o cliente passou do tempo combinado, paga pelo **tempo extra**; se causou **danos**, paga pelo reparo; se o custo final foi menor que a caução, recebe a **diferença de volta**.

---

### 2. 🅿️ Sistema de Estacionamento

O estacionamento dispõe de um número limitado de vagas, distintas por tipo (cobertas/descobertas) e por destinação (comuns, preferenciais e para motos). Eventualmente uma vaga é interditada por manutenção ou obras, e a área pode ser ampliada — sendo necessário manter o cadastro de vagas e de sua situação sempre atualizado.

Os clientes chegam para guardar seus veículos. Há dois perfis: o **avulso**, que paga pelo tempo de permanência, e o **mensalista**, com vínculo fixo. O mensalista precisa estar cadastrado; o avulso é identificado a cada entrada pela placa.

Na entrada, registra-se o veículo, seu tipo, a data/hora de chegada e atribui-se uma vaga compatível. **O valor cobrado do avulso varia conforme o tipo de vaga, o tipo de veículo e o período do dia (diurno/noturno).** O mensalista não paga por permanência, mas deve estar com a mensalidade em dia.

Na saída, registra-se data/hora e libera-se a vaga. Para o avulso, calcula-se o valor pelo tempo de permanência, respeitando a **tolerância de cortesia** e a cobrança por hora cheia/fração. Em caso de **perda do ticket**, aplica-se taxa adicional. Para o mensalista, verifica-se se a mensalidade está quitada.

---

### 3. 🏥 Sistema de Clínica Médica/Odontológica

A clínica conta com diversos profissionais de saúde, de diferentes especialidades, que atuam em consultórios próprios. Eventualmente um profissional é afastado, desligado ou tem a agenda suspensa, e novos profissionais são contratados — sendo necessário manter o cadastro de profissionais, especialidades e horários sempre atualizado.

Os pacientes procuram a clínica para marcar consultas. Primeiro é necessário cadastrá-los, registrando se o atendimento será **particular** ou por **convênio**. Depois de identificado, o paciente escolhe a especialidade, o profissional e o horário disponível na agenda — **o valor da consulta varia conforme a especialidade, o tipo de atendimento e se é primeira consulta ou retorno**. O sistema deve **impedir conflito de horário** (dois pacientes no mesmo slot do mesmo profissional).

Realizada a consulta, define-se como concluída, registra-se data/hora e anotam-se no **prontuário** os procedimentos efetuados (cada procedimento extra tem valor próprio e soma ao total). **Retornos dentro do prazo** não são cobrados. Em caso de **falta sem aviso** ou remarcação fora do prazo, registra-se a ocorrência e aplicam-se as penalidades previstas.

---

### 4. 🔧 Sistema de Oficina Mecânica

A oficina mantém um **estoque de peças** de diferentes marcas, valores e quantidades. Eventualmente uma peça esgota e atinge o ponto de reposição, ou é descontinuada; novos itens são adquiridos e há diversos **serviços** oferecidos, cada um com seu valor de mão de obra — sendo necessário manter o cadastro de peças e serviços sempre atualizado.

Os clientes trazem seus veículos para reparo. Primeiro é necessário cadastrá-los e registrar os veículos vinculados. Depois, o veículo é avaliado e abre-se uma **Ordem de Serviço (OS)** com o diagnóstico inicial — **o valor varia conforme as peças necessárias e as horas de mão de obra**. Antes de iniciar, a oficina apresenta o **orçamento**, que o cliente precisa **aprovar**; apenas as peças aprovadas e disponíveis em estoque são reservadas.

Ao finalizar, define-se a OS como concluída, registra-se data/hora de entrega e dá-se **baixa no estoque** das peças usadas, somando peças + mão de obra. Se durante a execução surgirem **problemas adicionais**, eles vão para nova aprovação e somam ao total; se um serviço orçado não for necessário, seu valor é **descontado** do total final.

---

### 5. 📚 Sistema de Biblioteca

A biblioteca possui um acervo de diversos **títulos**, cada um com vários **exemplares** físicos. Eventualmente um exemplar é baixado do acervo (extravio, dano irreparável ou desatualização), e novas obras são adquiridas — sendo necessário manter o cadastro de títulos e a quantidade de exemplares disponíveis sempre atualizado.

Os usuários procuram a biblioteca para fazer empréstimos. Primeiro é necessário cadastrá-los, registrando o **tipo de vínculo** (aluno, professor ou comunidade externa), pois isso define limites e prazos diferentes. Depois, o usuário escolhe a obra — **o prazo e a quantidade de exemplares permitidos variam conforme o tipo de usuário e a natureza da obra**. O sistema verifica se há exemplar disponível e se o usuário não excedeu o limite nem possui pendências; se a obra estiver indisponível, é possível fazer uma **reserva**.

Na devolução, define-se o exemplar como devolvido, registra-se a data e atualiza-se a disponibilidade. Se a devolução for após o prazo, o usuário paga **multa proporcional aos dias de atraso** (valor varia conforme o tipo de obra) e fica **bloqueado** enquanto houver pendência. Em caso de **dano ou perda**, o usuário deve ressarcir a biblioteca.

---

### 6. 🏋️ Sistema de Academia

A academia oferece diferentes **planos** (mensal, trimestral e anual), além de diversas **modalidades/aulas**, ministradas por instrutores em horários determinados. Eventualmente uma modalidade é suspensa ou um instrutor é afastado, e novos planos e modalidades são criados — sendo necessário manter o cadastro de planos, modalidades e instrutores sempre atualizado.

Os clientes procuram a academia para se matricular. Primeiro é necessário cadastrá-los, registrando dados pessoais e (quando houver) a avaliação física. Depois, o aluno escolhe o plano e as modalidades — **a mensalidade varia conforme o plano, a quantidade de modalidades e o horário (comercial/reduzido)**. Na matrícula, registra-se a data de adesão e calcula-se a **data de vencimento** conforme o plano.

A cada acesso do aluno, registra-se data/hora de entrada e verifica-se a situação do pagamento. Se a mensalidade estiver **vencida**, o acesso é bloqueado e a inadimplência é sinalizada. Na **renovação**, recalcula-se o vencimento; no **cancelamento** antes do fim do período, aplicam-se as regras de rescisão (cobrança ou devolução proporcional).

---

## 📊 Critérios de Avaliação

| Critério | Descrição | Pontos |
|---|---|---|
| Funcionamento do menu e CRUD | Menu navegável e cadastro completo das entidades | 2,0 |
| Regras de negócio | Cálculos, multas, descontos e verificações corretas | 2,5 |
| Validação de dados | Tratamento de entradas inválidas | 1,5 |
| Relatórios/consultas | Consultas com filtro funcionando | 1,5 |
| Organização do código | Uso de funções, identação e clareza | 1,5 |
| Apresentação | Demonstração e domínio do código pela equipe | 1,0 |
| **Total** | | **10,0** |

> ⭐ Os diferenciais (persistência, tratamento de exceções, interface caprichada) podem render **pontuação extra** a critério do professor.

---

## 👥 Identificação da Equipe

| Nome | Sistema |
|---|---|
| Ailson dos Santos Sousa | 1 |
| Arthur Nunes Barreto | 2 |
| Ayde Marques Lopes | 3 |
| Bleidson Pereira Nunes | 4 |
| Breno da Silva Moreira | 5 |
| Clara Raimunda Nogueira de Carvalho | 6 |
| Cleiton Junio Ferreira Lustosa Filho | 1 |
| Daniel Soares Rocha | 2 |
| Gabriel Barbosa Rodrigues | 3 |
| Gessy Kelly Pereira de Oliveira | 4 |
| Grazielle Rodrigues de Sena | 5 |
| Gustavo Alves de Souza | 6 |
| Helder Alves de Sousa | 1 |
| Henrique Benning Guimarães | 2 |
| Iandra Cordeiro Ribeiro | 3 |
| Ian Souza Lisboa | 4 |
| Igor Castro de Carvalho Silva | 5 |
| Jefferson Lopes Guedes | 6 |
| Jeiel Alves Gomes | 1 |
| Juliano Pereira da Rocha | 2 |
| Kaian Carvalho de Souza | 3 |
| Kaled Moura Duarte | 4 |
| Karina da Silva Souza | 5 |
| Karine Rodrigues Fialho | 6 |
| Karine Rodrigues Lopes | 1 |
| Kayky Yryell Dias de Assis | 2 |
| Lademir Inácio Strieder Junior | 3 |
| Larissa Santos Guimarães | 4 |
| Lucas Baião de Sousa | 5 |
| Lucas Lustosa Santos | 6 |
| Ludmila de Oliveira Correia | 1 |
| Luiza Batista Sirqueira | 2 |
| Marcílio Ferreira de Souza Junior | 3 |
| Marcos André Rodrigues Oliveira | 4 |
| Marcos Vinicius da Silva Lopes | 5 |
| Maria Luiza Alves Vieira | 6 |
| Marisa de Almeida Cordeiro | 1 |
| Maurícia Lustosa de Carvalho | 2 |
| Moisés da Silva Louzeiro | 3 |
| Moisés Viana de Souza | 4 |
| Natanael de Medeiros Aires | 5 |
| Ney Wanderson Aguiar Alves | 6 |
| Pablo Gama Pereira de Figueiredo | 1 |
| Pietro de Carvalho Rodrigues | 2 |
| Rafael Barreira de Sousa | 3 |
| Rafael da Silva Ribeiro | 4 |
| Raquel Gomes Pinheiro | 5 |
| Renan Alves de Oliveira | 6 |
| Riquelme Ribeiro Pinheiro de Souza | 1 |
| Rodrigo Carvalho Oliveira | 2 |
| Samuel Nunes Lemos | 3 |
| Sérgio Clemente Araújo da Silva | 4 |
| Sérgio de Souza Cruz | 5 |
| Shayara Pereira Natanael | 6 |
| Teéo Henrique Soares | 1 |
| Victor Gabriel Gomes da Silva | 2 |
| Werike Rodrigues Alves | 3 |

São 57 alunos, com os sistemas distribuídos ciclicamente de 1 a 6.

## 🚀 Como Executar

```bash
python main.py
```

> _Descreva aqui quaisquer instruções adicionais para rodar o seu sistema (bibliotecas necessárias, arquivos de dados etc.)._

---

_Bons estudos e mãos à obra! 💻_
