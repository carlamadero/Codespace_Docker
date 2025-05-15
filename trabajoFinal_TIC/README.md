**ANALISIS DE DATOS Y CIENCIA DE DATOS**

CARLA MADERO SAN JUAN

GitHub: Codespace_Docker/trabajoFinal_TIC at main · carlamadero/Codespace_Docker

**1. Introducción**

En el campo del análisis de datos y la ciencia de datos, seleccionar el entorno adecuado para ejecutar experimentos y modelos es fundamental para garantizar eficiencia, precisión y escalabilidad. Los científicos de datos manejan grandes volúmenes de información, ejecutan algoritmos intensivos en cálculo y requieren ambientes que permitan la rápida iteración y despliegue de modelos. Esto hace que la elección entre máquinas virtuales (VM) y contenedores Docker sea especialmente relevante.
Las VM y Docker ofrecen soluciones diferentes para aislar aplicaciones y entornos de ejecución, pero tienen diferencias clave que impactan directamente en el desempeño y flexibilidad de los proyectos de ciencia de datos. Este informe se enfoca en evaluar estas dos tecnologías desde la perspectiva de su uso en análisis de datos, considerando métricas como uso de CPU, memoria, almacenamiento, tiempo de arranque y eficiencia en el manejo de grandes volúmenes de datos. Dos de las tecnologías más populares para aislar aplicaciones y sus dependencias son las máquinas virtuales (VM) y los contenedores Docker. Aunque ambos cumplen funciones similares, tienen diferencias fundamentales en términos de rendimiento, uso de recursos y escalabilidad.

¿Qué son las máquinas virtuales?

Las máquinas virtuales son entornos completos que emulan hardware físico, permitiendo ejecutar sistemas operativos completos en un entorno aislado. Cada VM incluye su propio kernel y sistema operativo, proporcionando un alto nivel de aislamiento y seguridad a costa de mayores requisitos de recursos.

Ventajas:

* Mejor aislamiento y seguridad (kernel separado)

* Compatibilidad con herramientas de simulación de hardware

* Entornos completamente independientes

Desventajas:

* Uso intensivo de recursos

* Arranque lento

* Mayor espacio en disco

¿Qué son los contenedores Docker?

Los contenedores Docker son entornos más ligeros que comparten el kernel del sistema operativo host, pero mantienen sus propias dependencias y configuraciones. Esto permite un arranque rápido y un uso más eficiente de los recursos, aunque con menor aislamiento que una VM tradicional.

Ventajas:

* Arranque rápido y menor uso de recursos

* Mejor portabilidad entre entornos

* Facilidad de integración con herramientas DevOps y CI/CD

Desventajas:

* Menor aislamiento, depende del kernel del host

* Menos adecuado para aplicaciones con requisitos de kernel específicos

Objetivo del proyecto

El objetivo de este proyecto es comparar el rendimiento y uso de recursos de un análisis de datos y ciencia de datos en VM y Docker, evaluando métricas clave como uso de CPU, memoria, almacenamiento, tiempo de arranque y rendimiento en operaciones de datos.

**2. Configuración del Entorno de Prueba**

Máquina Host

* CPU: 4 núcleos virtuales

* RAM: 16 GB

* Disco: 512 GB SSD

* Sistema Operativo Host: Ubuntu 22.04 LTS

Máquina Virtual

* Hipervisor: VirtualBox 7.x

* Sistema Operativo: Ubuntu Server 22.04

* Recursos Asignados: 4 vCPU, 8 GB RAM, 40 GB disco

Contenedor Docker

* Imagen Base: continuumio/miniconda3

* Red: Mapeo de puertos (8888:8888 para Jupyter)

* Scripts Utilizados: analysis_vm.py, analysis_docker.py

**3. Métricas y Herramientas Utilizadas**

Uso de Recursos

* Uso de la CPU: Medido con htop, top, docker stats, VBoxManage metrics, vmstat.

* Consumo de memoria: RAM utilizada durante la ejecución de aplicaciones intensivas.

* Espacio en disco requerido: Tamaño de instalación base, aplicaciones y dependencias.

Tiempo de Arranque / Tiempo de Inicio

* Medido usando systemd-analyze, scripts simples o diferencias de fechas para medir tiempos de inicio.

Pruebas de Rendimiento

* CPU: Utiliza herramientas como sysbench, stress-ng o Geekbench para pruebas de esfuerzo.

* E/S de disco: Evaluado con fio o dd if=/dev/zero of=testfile bs=1G count=1 oflag=dsync para medir velocidad de escritura.

* Velocidad de red: Medido con iperf3 para evaluar la latencia y ancho de banda.

Caso de Prueba de Aplicación
   
* Tiempo de implementación: Medición del tiempo para desplegar aplicaciones como servidores MySQL o aplicaciones Node.js.

* Rendimiento: Solicitudes por segundo y latencia en aplicaciones bajo carga.

* Consumo de recursos bajo carga: Monitoreo de uso de CPU, memoria y disco durante operaciones intensivas.

Aislamiento y Seguridad
   
* Separación del kernel: Las VM son más seguras al usar un kernel separado.

* Contenedores: Docker comparte el kernel, lo que es más eficiente pero menos aislado.

* Capas de seguridad: Incluye herramientas como AppArmor, SELinux para mejorar la seguridad en contenedores.

Portabilidad y Flexibilidad

* Facilidad de exportación/importación: Comparación de la simplicidad para mover imágenes de VM vs contenedores.

* Soporte multiplataforma: Compatibilidad en diferentes sistemas operativos como Windows, macOS y Linux.

* Compatibilidad con DevOps: Evaluación de integración en pipelines CI/CD.

**4. Resultados**

Tabla Comparativa de Uso de Recursos

Gráfico de Importancia de Características (Random Forest): Incluido en los scripts (analysis_vm.py y analysis_docker.py).

Ejemplo de Matriz de Confusión: Generada para evaluar precisión del modelo en ambos entornos.

Análisis de Tiempo de Respuesta

**5. Análisis**

Fortalezas de las Máquinas Virtuales

* Mejor aislamiento y seguridad (kernel separado)

* Ideal para aplicaciones que requieren un sistema operativo completo

* Mayor compatibilidad con herramientas de simulación de hardware

Fortalezas de los Contenedores Docker

* Arranque rápido y menor uso de recursos

* Mejor portabilidad entre entornos

* Facilidad de integración con herramientas DevOps y CI/CD

Debilidades

* VM: Uso intensivo de recursos, arranque lento

* Docker: Menor aislamiento, depende del kernel del host

**6. Conclusión**

Para proyectos de ciencia de datos que requieren escalabilidad, rapidez y menor consumo de recursos, Docker es la opción ideal. Sin embargo, para aplicaciones que requieren aislamiento completo, como sistemas financieros o aplicaciones críticas, las máquinas virtuales siguen siendo más apropiadas. La elección depende en gran medida del balance entre rendimiento, seguridad y facilidad de mantenimiento.
