#!/bin/sh
# Comando de build da Cloudflare Pages: copia só os arquivos do site para dist/
# (a pasta ferramentas/ e o README ficam de fora do site publicado).
set -e
rm -rf dist
mkdir -p dist
cp ./*.html robots.txt _headers dist/
cp -r assets dist/
[ -f sitemap.xml ] && cp sitemap.xml dist/
echo "Site pronto em dist/"
