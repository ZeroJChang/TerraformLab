# Usa la imagen base de NGINX
FROM nginx

# Elimina cualquier configuración existente
RUN rm -rf /etc/nginx/conf.d/*

# Copia tu configuración personalizada
COPY nginx.conf /etc/nginx/conf.d/

# Copia tu página HTML
COPY index.html /usr/share/nginx/html/
