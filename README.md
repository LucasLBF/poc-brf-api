<p align="center">
  <img src="https://user-images.githubusercontent.com/76190126/153410701-aff85a12-78c5-44cd-a5c9-292894434f31.png" />
</p>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto">Sobre o projeto</a>
      <ul>
        <li><a href="#tecnologias-utilizadas">Tecnologias utilizadas</a></li>
      </ul>
    </li>
    <li>
      <a href="#primeiros-passos">Primeiros passos</a>
      <ul>
        <li><a href="#pré-requisitos"</a>Pré-requisitos</li>
      </ul>
    </li>
    <li>
      <a href="#instalação">Instalação</a>
    </li>
    <li><a href="#uso">Uso</a></li>
    <li><a href="#considerações"</a>Considerações</li>
    <li><a href="#contato">Contato</a></li>
  </ol>
</details>

## Sobre o projeto

Repositório da API para a prova de conceito da solução proposta pela equipe BRF no [CESAR SUMMER JOB 2022.1](https://www.summerjob.cesar.org.br/). A API tem um endpoint que recebe palavras-chave, realiza a varredura de PDFs contidos em um diretório e faz uma extração de trechos e imagens nas quais as palavras-chave aparecem, contendo a fonte onde foi encontrada a informação e a respectiva página, com o intuito de deixar a visualização de relatórios em texto corrido mais dinâmica e sumarizada. 

## Tecnologias Utilizadas

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [pdfminer.six](https://github.com/pdfminer/pdfminer.six)
* [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)

## Primeiros passos

### Pré-requisitos

* [Python 3](https://www.python.org/)
* [PIP - gerenciador de pacotes do Python](https://pypi.org/project/pip/)

## Instalação

1. Clonar o repositório

```sh
  git clone https://github.com/LucasLBF/poc-brf-api.git
```


2. Criar uma venv
```sh
  python -m venv venv
```


3. Ativar a venv

* Windows PowerShell
```sh
.\venv\Scripts\Activate.ps1
```

* Git bash/Terminais Unix
```sh
source ./venv/bin/activate
```


4. Instalar todas as dependências do projeto com o PIP
```sh
pip install -r requirements.txt
```


5. Subir o servidor na máquina local
```sh
  flask run
```


## Uso

A API é consumida pelo frontend da prova de conceito, localizado neste [repositório](https://github.com/LucasLBF/poc-brf-front), por isso também é necessário instalá-lo para que a prova de conceito rode normalmente.


## Considerações

* Alguns PDFs de teste foram deixados no diretório "dataset" no repositório, onde o código irá procurar pelos arquivos em PDF para varrê-los e extrair as informações. Por isso, caso seja de interesse, é recomendável adicionar mais arquivos em PDF nesse diretório para testar o código. 


## Contato

**Contribuidores**
* [Lucas Fernandes](https://github.com/LucasLBF)
* [Bernardo Hoffmann](https://github.com/BerHoffmann)
* [Antônio Fernando](https://github.com/antoniofernandocst)
