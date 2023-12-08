.. Trabalho_LP_A2 documentation master file, created by
   sphinx-quickstart on Wed Dec  6 09:52:49 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bem-vindo à documentação do projeto Space War!
==============================================

Este projeto é referente à avaliação 2 da disciplina de Linguagens de Programação do curso de Ciência de Dados e Inteligência Artificial da Fundação Getúlio Vargas (FGV). \

As pastas presentes nesse trabalho são:

* **images**: Contém as sprites utilizadas.
* **sounds**: Contém os sons utilizados.

Além disso, ele possui os seguintes módulos na pasta raiz:

* **assets.txt**: Contém os links das fontes de todos os assets utilizados.
* **main.py**: Contém a definição da função `game_init`, chamada nele mesmo, e o loop principal do jogo.
* **player.py**: Contém a definição das classes `Ship`, correspondente à nave principal, e `Shot`, correspondente aos seus tiros.
* **screens.py**: Contém a criação da tela do jogo e dos textos utilizados.
* **sounds.py**: Carrega os sons e a música do jogo.
* **space_objects.py**: Contém a definição da classe `SpaceObject` e de suas classes filhas `BigMeteor`, responsável pelos asteroides, e `Comet`, responsável pelos cometas.
* **space_sprites.py**: Contém a definição da classe `SpaceSprites`, correspondente à imagem de fundo do jogo.
* **sprites.py**: Carrega todas as imagens utilizadas.
* **ufo**: Contém a definição das classes `Ufo`, responsável pela nave alienígena, e `Laser`, responsável pelos seus tiros.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   main
   player
   space_sprites
   space_objects
   ufo

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
