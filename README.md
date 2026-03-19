# Docker Snippets

![Docker Snippets](https://raw.githubusercontent.com/tuusuario/docker-snippets/main/screenshot.png)
*(Opcional: añade una captura de pantalla de la app)*

Flask web app minimalista para **guardar, buscar y organizar comandos Docker**. Ideal para aprender Docker con una aplicación real y persistente.

## ✨ Características

- 💾 **Persistencia** con volumen Docker (`data/snippets.json`)
- 🔍 **Búsqueda** por comando o descripción
- 🏷️ **Tags** para categorizar (network, volume, compose...)
- 📱 **Responsive** con Bootstrap 5
- ⚙️ **Configurable** (puerto vía `APP_PORT`)

## 🚀 Iniciar rápidamente

### 1. Pull de la imagen
```bash
docker pull tuusuario/docker-snippets:latest
