# 🐳 Introducción a Docker

Este repositorio contiene una guía y ejercicios básicos para aprender Docker desde cero. Docker permite desarrollar, enviar y ejecutar aplicaciones dentro de contenedores, lo que facilita la portabilidad y la consistencia en diferentes entornos.

---

## 📘 ¿Qué es Docker?

Docker es una plataforma para desarrollar, enviar y ejecutar aplicaciones usando contenedores. Un contenedor es una unidad estándar de software que empaqueta el código y todas sus dependencias, de modo que la aplicación se ejecuta rápida y confiablemente en cualquier entorno.

---

## 🎯 Objetivos del Proyecto

- Comprender los conceptos fundamentales de Docker.
- Aprender a construir imágenes y ejecutar contenedores.
- Crear entornos de desarrollo portables y replicables.
- Ejecutar una aplicación simple dentro de un contenedor.

---

## ✅ Requisitos Previos

- Tener instalado [Docker Desktop](https://www.docker.com/products/docker-desktop)
- Conocimientos básicos de línea de comandos

---

## 🚀 Comandos Básicos

```bash
# Verificar versión de Docker
docker --version

# Listar imágenes instaladas
docker images

# Listar contenedores en ejecución
docker ps

# Construir una imagen desde un Dockerfile
docker build -t nombre-de-la-imagen .

# Ejecutar un contenedor
docker run -p 8080:80 nombre-de-la-imagen

# Ver logs del contenedor
docker logs id-del-contenedor
