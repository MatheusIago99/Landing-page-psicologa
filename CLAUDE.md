# Site da psicóloga Alícia Lemos

Site institucional de **Alícia Lemos** (Psicóloga Clínica, Acompanhante Terapêutica e Aplicadora ABA, CRP 02/34070, Recife-PE). Desenvolvedor: Matheus Iago (GitHub `matheusiago99`). Toda a comunicação com o usuário é em **português do Brasil**, em linguagem simples (ele segue passo a passo por prints do painel).

## Produção

- **URL atual:** https://alicia-lemos.matheusiago2012.workers.dev (domínio próprio `.psc.br` ainda não configurado).
- **Hospedagem:** Cloudflare Workers com arquivos estáticos (`wrangler.jsonc`, pasta `dist/`). Push na `main` publica sozinho em menos de 1 minuto. Se um push não aparecer em **Deployments**, refazer a conexão em **Settings → Build** (Disconnect/Connect); **Retry build** refaz o commit antigo e não serve.
- Build: `sh ferramentas/preparar-publicacao.sh` (copia só os arquivos do site para `dist/`). Deploy: `npx wrangler deploy`. Preview builds desligados.
- `dist/` e `.wrangler/` não vão para o repositório.

## Como editar

- **Todo o conteúdo está em `ferramentas/gerar-site.py`.** Nunca editar os `.html` direto: eles são gerados. Depois de editar, rodar `python3 ferramentas/gerar-site.py` e commitar os `.html` gerados junto.
- Visual em `assets/css/site.css`; menu e formulário em `assets/js/site.js`. O gerador acrescenta `?v=<hash>` aos links do CSS/JS (os assets ficam 7 dias no cache do navegador), então sempre regenerar depois de mexer neles.
- Contatos nas constantes do início do gerador: WhatsApp `5581997082433`, e-mail `alicialemos.psi@gmail.com`, Instagram `psi.alicialemos`, LinkedIn `https://www.linkedin.com/in/alicialemos`.
- `DOMAIN = ""`: quando o domínio existir, preencher para gerar canonical, `og:url` e `sitemap.xml`.
- O formulário de contato não envia nada: monta a mensagem e abre o WhatsApp.
- `_headers` tem CSP restritiva (só recursos do próprio site e Google Fonts). Recurso externo novo exige ajustar a CSP.

## Decisões de conteúdo

- Páginas: início, infância/adolescência/família, neurodivergências, adultos, casais, sobre mim, privacidade (LGPD) e 404.
- **Alícia ainda não tem consultório próprio.** Não escrever "consultório" nem "atendimento presencial em consultório". Formulação usada: atendimento on-line e presencial em Recife, em domicílio ou na escola, conforme o serviço.
- Ética do CFP: sem promessas de resultado; avaliação psicológica/neuropsicológica aparece como não oferecida no momento; acompanhamento terapêutico e ABA separados da psicoterapia. Rodapé com aviso de urgência (CVV 188 / SAMU 192).

## Testes antes de publicar

Servir a pasta (`python3 -m http.server 8090`) e conferir com Playwright em 1440px e 390px: sem rolagem horizontal, um `h1` por página, imagens com `alt`, sem erros no console.
