# Como usar esses arquivos:

## Instalar uma distribuição conda 

- [Ananconda](https://www.anaconda.com/products/individual)
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html)


## Instalando o Python ifc open shell

    conda install -c conda-forge ifcopenshell

## instalando pacotes auxiliares:

    conda install -c anaconda pandas
    conda install -c conda-forge matplotlib
    conda install -c anaconda ipywidgets
    conda install -c conda-forge jupyter_contrib_nbextensions
    conda install -c conda-forge k3d
    conda install -c conda-forge pythreejs
    conda install -c conda-forge pythonocc-core
    conda install -c conda-forge lark-parser


## Comandos auxiliares para gerenciar ambientes conda

### Salvando ambientes conda

    conda env export > environment.yml
    conda list -e > requirements.txt

### instalando ambientes conda

    conda create --name pyifc --file requirements.txt
    conda env create --file environment.yml

### Reinstalando jupyter

    conda remove ipykernel ipython jupyter_client jupyter_core traitlets ipython_genutils ipywidgets pandas ifcopenshell matplotlib k3d pythreejs pythonocc-core  jupyter_contrib_nbextensions lark-parsers

    conda clean -tipsy
    conda install ipykernel ipython jupyter_client jupyter_core traitlets ipython_genutils ipywidgets pandas matplotlib
    conda install -c conda-forge ifcopenshell k3d pythreejs pythonocc-core jupyter_contrib_nbextensions