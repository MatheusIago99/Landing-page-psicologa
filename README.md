# Alícia Lemos — Site profissional de Psicologia

Site institucional de Alícia Lemos, Psicóloga Clínica, Acompanhante Terapêutica e Aplicadora ABA (CRP 02/34070), feito a partir do briefing da cliente: clareza, acolhimento, acessibilidade e contato fácil pelo WhatsApp.

> Repositório privado: contém dados pessoais da cliente (foto, telefone, CRP).

## Páginas

| Arquivo | Conteúdo |
|---|---|
| `index.html` | Início: apresentação, áreas de atendimento, como funciona o primeiro contato, perguntas frequentes e contato |
| `infancia-adolescencia-familia.html` | Psicoterapia infantojuvenil, orientação parental e familiar, acompanhamento terapêutico e aplicação ABA |
| `neurodivergencias.html` | Suspeita, após o diagnóstico, acompanhamento contínuo e o que é oferecido ou encaminhado |
| `psicoterapia-adultos.html` | Psicoterapia para adultos e a abordagem em palavras simples |
| `psicoterapia-casais.html` | Psicoterapia de casal e a relação com o contexto familiar |
| `sobre-mim.html` | Trajetória, formação e experiência |
| `privacidade.html` | Política de privacidade (LGPD) |
| `404.html` | Página não encontrada |

## Como alterar textos

Todos os textos ficam em **`ferramentas/gerar-site.py`**. Edite lá e rode:

```bash
python3 ferramentas/gerar-site.py
```

As páginas `.html` são recriadas. Não edite os `.html` direto: a próxima geração apagaria a mudança.
O visual (cores, fontes, espaçamentos) fica em `assets/css/site.css`; o menu do celular e o formulário, em `assets/js/site.js`.

**Quando o domínio estiver no ar**, preencha `DOMAIN = "https://seu-dominio"` no início de `ferramentas/gerar-site.py` e gere de novo: as páginas ganham o endereço oficial, a imagem de compartilhamento passa a aparecer no WhatsApp e é criado o `sitemap.xml` para o Google.

## Decisões

- **HTML e CSS puros**, sem framework nem build: carrega rápido e publica direto na Vercel.
- **Formulário sem servidor:** monta a mensagem e abre o WhatsApp; nada é enviado nem guardado pelo site, e ele não pede informações de saúde.
- **Ética profissional:** sem promessas de resultado; avaliação psicológica e neuropsicológica aparecem como não oferecidas no momento (com encaminhamento); acompanhamento terapêutico e ABA apresentados separados da psicoterapia.
- **Acessibilidade:** contraste AA, textos alternativos, navegação por teclado, link "pular para o conteúdo" e menu acessível.
- **SEO:** título e descrição próprios por página, dados estruturados (profissional e perguntas frequentes) e `robots.txt`.
- **Segurança:** `vercel.json` com política de conteúdo (CSP), HSTS e outros cabeçalhos; `.vercelignore` deixa os arquivos internos fora do site publicado.

## Publicação (Vercel)

1. Em vercel.com: **Add New → Project** e importar este repositório do GitHub.
2. Framework Preset: **Other** · Build Command: *(vazio)* · Output Directory: *(vazio, raiz)*.
3. Em **Settings → Domains**, adicionar o domínio `.psc.br` e seguir as instruções de DNS.

O `vercel.json` já ativa endereços sem `.html` (ex.: `/neurodivergencias`) e os cabeçalhos de segurança.

> O plano gratuito da Vercel (Hobby) é só para uso não comercial. Como é o site profissional de uma cliente, o plano adequado é o Pro.
