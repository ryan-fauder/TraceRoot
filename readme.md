# TraceRoot

- Nome do Projeto: TraceRoot

- Desenvolvedores:
  - Nickolas Carlos Carvalho Silva,
  - Matheus Queiroz Rocha Barbosa,
  - Pedro Augusto Serafim Belo,
  - Ryan Fernandes Auder Lopes

## Sobre o projeto

É um programa implementado na linguagem Python que busca raízes de uma função com os métodos de Newton-Raphson e Bisseção.

## Como utilizar?

Em seu terminal, faça um clone do repositório:

```bash
  git clone https://github.com/ryan-fauder/TraceRoot
```

Em seguida, execute o seguinte comando para entrar no diretório criado e iniciar o programa:

```bash
  cd traceroot
  python main.py
```

## Ferramentas

- Python
- Sympy
- Numpy

## Método

O método aplicado pelo programa para a procura de todas as raízes foi definido como:

- Captura a função;
- Verifica se a função é polinomial. Caso não seja, o programa é encerrado;
- Em seguida, verifica quantas vezes a função possui 0 como raiz e realiza a simplificação da expressão;
- Então, outra validação é feita: se a função ainda possui variáveis. Caso não possua, o programa é encerrado;
- Aplica o método de Lagrange para obter possíveis intervalos onde estão contidas as raízes;
- Aplica o método de Descartes para descartar os intervalos retornados pela função de Lagrange que não podem conter raízes reais. Caso todos os intervalos sejam descartados, então o programa é encerrado;
- Assim, inicia a etapa de validação de intervalos: aplica-se o teorema do valor intermediário no intervalo. Logo:
  - Caso seja válido, o intervalo será utilizado;
  - Caso não seja, procura-se um intervalo válido que esteja contido nesse intervalo com o método da bisseção:
    - Se o método encontrar um intervalo válido, então esse será utilizado. Senão, o intervalo é desconsiderado;
- Uma vez que os intervalos foram filtrados, as raízes serão procuradas em cada intervalo:
  - Aplica-se um pré-refinamento no intervalo com o método da bisseção. Nesse sentido, a tolerância é maior (1e-2);
  - Logo, tenta-se realizar um refinamento no intervalo com o método de Newton:
    - Se encontrar uma raiz, então é iniciada uma busca de raízes no próximo intervalo. 
    - Caso o método de Newton falhe, então o refinamento é realizado pelo método da bisseção;
  - Assim, uma raiz é obtida nesse intervalo
- Ao final da busca em todos os intervalos, um conjunto de raízes será obtido. Em seguida, divide-se o polinômio por cada uma dessas raízes. Ou seja, é aplicado o método de deflação de polinômios.
- Após esse método ser aplicado, o programa inicia a busca das raízes nesse polinômio obtido.
- Assim que todas as raízes reais e não multíplas forem obtidas, o programa imprime essas raízes e é encerrado.

## Tasks

- [X] Organizar a main
- [X] Padronizar entrada de intervalos
- [X] Alterar nomes de funções e variaveis
- [X] Arrumar o deflate;
- [X] bissection_table;
- [X] filter_intervals;
- [X] has_degree;
- [X] Escrever a readme.md
- [X] Organizar a controller
