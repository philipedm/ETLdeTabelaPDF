# ETLdeTabelaPDF
 ETL de Tabelas em PDF utilizando Pandas e Tabula
 
-

A biblioteca Tabula é utilizada para reconhecer e extrair as tabelas existentes no arquivo pdf.

A biblioteca Pandas é utilizada para manipular, transformar e carregar os dados.

Obs.: O arquivo pdf precisa estar na mesma pasta do código. Se não estiver será necessário informar o caminho.

-

A função tabula.read_pdf precisa de 2 argumentos. O primeiro é o 'local/nome do arquivo' e o segundo as páginas que vamos buscar as tabelas.

Obs.: Para uma melhor confirmação das tabelas extraídas, recomenda-se utilizar a função len para receber a quantidade de tabelas e comparar.
Em alguns casos, a depender do pdf, esse método não terá 100% de acerto. Logo, a extração precisa ser analisada e tratada com o Pandas.

-

Com a biblioteca Pandas, foi feita a transformação/tratamento dos dados.

Nesse mesmo código vemos:

- Criação de um novo Dataframe;
- Busca condicional em tabela;
- Armazenamento de dados em variáveis;
- Inserção de dados em tabela;
- Alteração de nome de colunas;
- Filtragem condicional de dados;
- Conversão de tipo de dados de colunas;
- Criação de arquivo excel com os dados finais tratados.

- 

Todo o código está comentado e explicado para um melhor entendimento.

É importante salientar que existem outros modos de ETL de dados em PDF ou outros arquivos.

O intuito é mostrar o que podemos fazer com as bibliotecas e de modo simples, podendo também ser adicionados outros tratamentos de dados.

-

Philipe Dias Mattos