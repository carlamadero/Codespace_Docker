FROM continuumio/miniconda3

WORKDIR /app

# Crear el entorno virtual y activar
RUN conda create -n data-env python=3.11 -y \
    && echo "source activate data-env" > ~/.bashrc \
    && /bin/bash -c "source activate data-env && conda install numpy pandas matplotlib seaborn scikit-learn -y"

COPY analysis_docker.py /app/

CMD ["/bin/bash", "-c", "source activate data-env && python /app/analysis_docker.py"]
