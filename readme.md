<!-- <p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/gabrielvss/recomendation_video_api.svg">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/johnvict0r/tech-news.svg">

  <a href="https://github.com/johnvict0r/tech-news./commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/johnvict0r/tech-news.svg">
  </a>

  <a href="https://github.com/johnvict0r/tech-news./issues">
    <img alt="Repository issues" src="https://img.shields.io/github/issues/johnvict0r/tech-news.svg">
  </a>

  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">
</p>  -->

<p align="center">
  <a href="#rocket-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-layout">Layout</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-contribuir">Como contribuir</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#memo-licença">Licença</a>
</p>

<br>

<!-- <p align="center">
  <img alt="Frontend" src=".github/tech-news.png" width="100%">
</p>
imagem do sistema
-->

## :rocket: Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [youtube-dl](https://youtube-dl.org/)
- [Docker](https://www.docker.com/)
- [LightGBM](https://lightgbm.readthedocs.io/en/latest/)
- [scikit-learn](https://scikit-learn.org/stable/)

## 💻 Projeto

O recomendation_video_api se trata de um serviço web que fornece um ranking de vídeos recomendados de acordo com os gostos do autor :thumbsup:, a lista corresponde as seguintes chaves de pesquisa:

- kaggle
- machine learning
- data science

Esse projeto foi desenvolvido no curso de [Data Science](https://curso.mariofilho.com/) do [Mario Filho](https://www.mariofilho.com/sobre-o-autor/).

## 🤔 Como contribuir

- Faça um fork desse repositório;
- Cria uma branch com a sua feature: `git checkout -b minha-feature`;
- Faça commit das suas alterações: `git commit -m 'feat: Minha nova feature'`;
- Faça push para a sua branch: `git push origin minha-feature`.

Depois que o merge da sua pull request for feito, você pode deletar a sua branch.

## :wrench: Como rodar

- Python

  - `pip install requirements.txt`
  - `python app.py`

- Docker

  - `docker build . -t container_name`
  - `docker run -it -p number_port:5000 container_name`
