## Restaurante CONN: uma proposta de CRUD básica

Bem-vindo ao **Sistema CONN**, esse projeto busca facilitar e modernizar a logística de pedidos para restaurantes, nessa prática e simulado um restaurante que fornece pratos feito(PF), pizzas e salgados em geral.

---

## Missão 
Diminuir frustração constante no resgistro de pedidos.  

---

## Funcionamento do Sistema (CRUD)

O sistema do restaurante CONN permite:
- **Cadastrar pedidos**: Nome do cliente, prato/massas, quantidade e valor total.    
- **Listar pedidos**: Visualizar todos os pedidos feitos.  
- **Buscar pedidos**: Identificar pedidos pelo número identificador.
- **Atualizar pedidos**: Alterar informações de pratos ou quantidade.  
- **Excluir pedidos**: Remover pedidos do banco de dados.  

Banco de dados utilizado: `SQLite`  
Tabela principal: `pedidos (cliente, prato, quantidade, valor_total)`

---

## Cenário de Uso
Imagine o cliente **Ronaldo Fernandes** chegando a um Restaurante chamado CONN:
1. Ele pede uma **Pizza CONN: Tradicional** tamanho médio.  
2. O atendente registra no sistema:  
   - Cliente: Ronaldo Fernandes  
   - Prato: Pizza CONN  
   - Quantidade: 1  
   - Valor Total: R$ 45,00  
3. O pedido é salvo no banco de dados e aparece na lista de pedidos ativos.  
4. Após o preparo, o cliente recebe sua pizza e o pedido é concluído.  

---