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
Os contatos (WhatsApp, e-mail, Instagram e LinkedIn) ficam nas constantes do início do arquivo.
O visual (cores, fontes, espaçamentos) fica em `assets/css/site.css`; o menu do celular e o formulário, em `assets/js/site.js`.
Depois de mudar o CSS ou o JS, gere as páginas de novo: os links ganham `?v=<código>` novo e os navegadores baixam a versão atualizada (sem isso, guardariam a antiga por até 7 dias).

**Quando o domínio estiver no ar**, preencha `DOMAIN = "https://seu-dominio"` no início de `ferramentas/gerar-site.py` e gere de novo: as páginas ganham o endereço oficial, a imagem de compartilhamento passa a aparecer no WhatsApp e é criado o `sitemap.xml` para o Google.

## Decisões

- **HTML e CSS puros**, sem framework: carrega rápido e hospeda de graça na Cloudflare Pages (plano gratuito permite uso comercial).
- **Formulário sem servidor:** monta a mensagem e abre o WhatsApp; nada é enviado nem guardado pelo site, e ele não pede informações de saúde.
- **Ética profissional:** sem promessas de resultado; avaliação psicológica e neuropsicológica aparecem como não oferecidas no momento (com encaminhamento); acompanhamento terapêutico e ABA apresentados separados da psicoterapia.
- **Acessibilidade:** contraste AA, textos alternativos, navegação por teclado, link "pular para o conteúdo" e menu acessível.
- **SEO:** título e descrição próprios por página, dados estruturados (profissional e perguntas frequentes) e `robots.txt`.
- **Segurança:** `_headers` com política de conteúdo (CSP), HSTS e outros cabeçalhos. A publicação copia só os arquivos do site para `dist/`, então `ferramentas/` e o README não ficam públicos.

## Publicação (Cloudflare)

No painel da Cloudflare: **Workers & Pages → Create → Import a repository** e escolher este repositório.

- **Project name:** `alicia-lemos` (o mesmo `name` do `wrangler.jsonc`)
- **Build command:** `sh ferramentas/preparar-publicacao.sh`
- **Deploy command:** `npx wrangler deploy`

O build copia só os arquivos do site para `dist/` (ferramentas/ e README ficam de fora), e o `wrangler.jsonc` publica essa pasta: páginas sem `.html` (ex.: `/neurodivergencias`), página 404 própria e os cabeçalhos de segurança do `_headers`. A cada push na `main`, a Cloudflare publica sozinha. Atenção: só commits feitos pela conta dona do repositório disparam a build; se um push não publicar, faça qualquer commit pelo próprio GitHub (o **Retry build** não serve: ele refaz o commit antigo).

Também funciona como **Pages** (Create → Pages → Connect to Git), com o mesmo build command e **Build output directory** `dist`.

Domínio: em **Settings → Domains & Routes** (Workers) ou **Custom domains** (Pages), adicionar o `.psc.br`.
