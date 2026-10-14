"""Gera as páginas do site da Alícia Lemos (HTML estático).

Todos os textos do site estão neste arquivo. Para mudar um texto, edite aqui e rode:

    python3 ferramentas/gerar-site.py

As páginas .html da raiz são recriadas. (Não edite os .html direto: a próxima geração
apagaria a mudança.) O visual fica em assets/css/site.css.
"""
import sys
from html import escape
from urllib.parse import quote

import os

# Por padrão, gera as páginas na pasta acima de "ferramentas/" (a raiz do site).
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# Domínio do site, sem barra no final (ex.: "https://alicialemos.psc.br").
# Com ele preenchido, as páginas ganham endereço oficial (canonical), a imagem de
# compartilhamento funciona no WhatsApp e é gerado o sitemap.xml para o Google.
DOMAIN = ""
WA = "5581997082433"
EMAIL = "alicialemos.psi@gmail.com"
INSTA = "psi.alicialemos"
LINKEDIN = "https://www.linkedin.com/in/alicialemos"
CRP = "CRP 02/34070"
TITLE = "Psicóloga Clínica, Acompanhante Terapêutica e Aplicadora ABA"


def wa(msg):
    return f"https://wa.me/{WA}?text={quote(msg)}"


# Ícones de traço simples (24×24)
ICONS = {
    "broto": '<path d="M12 21v-8"/><path d="M12 13c0-4 3-6.5 7-6.5 0 4-3 6.5-7 6.5Z"/><path d="M12 15.5C12 12 9.5 9.5 5.5 9.5 5.5 13 8 15.5 12 15.5Z"/>',
    "familia": '<circle cx="8" cy="6.5" r="2.5"/><circle cx="16" cy="6.5" r="2.5"/><circle cx="12" cy="13" r="1.8"/><path d="M3.5 20v-3.5A4.5 4.5 0 0 1 8 12"/><path d="M20.5 20v-3.5A4.5 4.5 0 0 0 16 12"/><path d="M9 20v-1.5a3 3 0 0 1 6 0V20"/>',
    "constelacao": '<circle cx="6" cy="7" r="2"/><circle cx="17" cy="5.5" r="2"/><circle cx="12" cy="13" r="2"/><circle cx="18.5" cy="17.5" r="2"/><circle cx="6.5" cy="18" r="2"/><path d="m7.8 8.1 2.6 3.3M15.6 7l-2.4 4.4M13.6 14.3l3.4 2.2M10.3 14l-2.4 2.6"/>',
    "pessoa": '<circle cx="12" cy="7" r="3.2"/><path d="M5 20.5c.6-4 3.4-6.3 7-6.3s6.4 2.3 7 6.3"/>',
    "casal": '<circle cx="9.5" cy="12" r="5.5"/><circle cx="14.5" cy="12" r="5.5"/>',
    "conversa": '<path d="M4 5.5h12a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H9l-4 3.5v-3.5H4a2 2 0 0 1-2-2v-6a2 2 0 0 1 2-2Z"/><path d="M18 9.5h2a2 2 0 0 1 2 2V17a2 2 0 0 1-2 2h-1v2.5L16 19h-4"/>',
    "maos": '<path d="M7 12V6.5a1.5 1.5 0 0 1 3 0V11"/><path d="M10 10V5a1.5 1.5 0 0 1 3 0v5"/><path d="M13 10V6a1.5 1.5 0 0 1 3 0v6.5"/><path d="M16 9.5a1.5 1.5 0 0 1 3 0V14a7 7 0 0 1-7 7h-.5a6.5 6.5 0 0 1-5.4-2.9L4 15a1.6 1.6 0 0 1 2.6-1.8L8 15"/>',
    "casa": '<path d="M3.5 11 12 4l8.5 7"/><path d="M5.5 9.5V20h13V9.5"/><path d="M10 20v-5h4v5"/>',
    "alvo": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>',
    "lupa": '<circle cx="10.5" cy="10.5" r="6"/><path d="m15 15 5.5 5.5"/>',
    "bussola": '<circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5 5-2Z"/>',
    "coracao": '<path d="M12 20s-7.5-4.6-7.5-10.2A4.3 4.3 0 0 1 12 7.2a4.3 4.3 0 0 1 7.5 2.6C19.5 15.4 12 20 12 20Z"/>',
    "capelo": '<path d="m2.5 9 9.5-4.5L21.5 9 12 13.5 2.5 9Z"/><path d="M6.5 11v4.5c1.5 1.6 3.4 2.5 5.5 2.5s4-.9 5.5-2.5V11"/><path d="M21.5 9v5"/>',
    "livro": '<path d="M12 6.5C10 5 7 4.5 3.5 5v13c3.5-.5 6.5 0 8.5 1.5 2-1.5 5-2 8.5-1.5V5C17 4.5 14 5 12 6.5Z"/><path d="M12 6.5v13"/>',
    "escola": '<path d="M3 10.5 12 6l9 4.5-9 4.5-9-4.5Z"/><path d="M7 12.5V17c1.4 1.3 3.1 2 5 2s3.6-.7 5-2v-4.5"/>',
    "estrela": '<path d="m12 3.5 2.4 5.3 5.8.6-4.3 3.9 1.2 5.7L12 16.1 6.9 19l1.2-5.7L3.8 9.4l5.8-.6L12 3.5Z"/>',
    "email": '<rect x="3" y="5.5" width="18" height="13" rx="2"/><path d="m4 7 8 6 8-6"/>',
    "instagram": '<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="0.9" fill="currentColor"/>',
    "linkedin": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10.5V17M8 7.3v.1"/><path d="M11.5 17v-6.5"/><path d="M11.5 13.5c0-1.8 1.1-3 2.6-3s2.4 1 2.4 3V17"/>',
    "local": '<path d="M12 21s-6.5-6.2-6.5-11a6.5 6.5 0 0 1 13 0c0 4.8-6.5 11-6.5 11Z"/><circle cx="12" cy="10" r="2.3"/>',
    "tela": '<rect x="3" y="4.5" width="18" height="12" rx="2"/><path d="M8.5 20h7M12 16.5V20"/>',
}
WA_SVG = '<svg class="ico-wa" viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 2.2A9.7 9.7 0 0 0 3.6 16.8L2.3 21.7l5-1.3A9.7 9.7 0 1 0 12 2.2Zm0 17.7a8 8 0 0 1-4.1-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8 8 0 1 1 12 19.9Zm4.4-6c-.2-.1-1.4-.7-1.7-.8-.2-.1-.4-.1-.5.1l-.8 1c-.1.2-.3.2-.5.1a6.6 6.6 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.5-.4h-.5a.9.9 0 0 0-.7.3 2.8 2.8 0 0 0-.9 2.1 5 5 0 0 0 1 2.6 11.2 11.2 0 0 0 4.3 3.8c1.6.7 2.2.7 3 .6.5-.1 1.4-.6 1.6-1.1.2-.6.2-1 .1-1.1l-.5-.3Z"/></svg>'


def icon(name, cls="icon"):
    return f'<span class="{cls}" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg></span>'


NAV = [  # (endereço, rótulo no computador, rótulo completo no menu do celular)
    ("index.html", "Início", "Início"),
    ("infancia-adolescencia-familia.html", "Infância e família", "Infância, adolescência e família"),
    ("neurodivergencias.html", "Neurodivergências", "Neurodivergências"),
    ("psicoterapia-adultos.html", "Adultos", "Psicoterapia para adultos"),
    ("psicoterapia-casais.html", "Casais", "Psicoterapia para casais"),
    ("sobre-mim.html", "Sobre mim", "Sobre mim"),
    ("index.html#perguntas", "Dúvidas", "Perguntas frequentes"),
    ("index.html#contato", "Contato", "Contato"),
]
AGENDAR = wa("Olá, Alícia! Gostaria de agendar um atendimento.")


def header(current):
    items = []
    for href, short, full in NAV:
        cur = ' aria-current="page"' if href == current else ""
        if short == full:
            items.append(f'<li><a href="{href}"{cur}>{short}</a></li>')
        else:
            items.append(f'<li><a href="{href}"{cur} aria-label="{full}"><span class="lbl-short" aria-hidden="true">{short}</span><span class="lbl-full" aria-hidden="true">{full}</span></a></li>')
    return f'''<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="index.html" aria-label="Alícia Lemos, Psicóloga — página inicial">
      <img src="assets/img/logo-simbolo-160.webp" width="160" height="99" alt="">
      <span class="brand-name">Alícia Lemos<small>Psicóloga</small></span>
    </a>
    <nav class="main-nav" id="menu" aria-label="Menu principal">
      <ul>
        {"".join(items)}
      </ul>
      <div class="nav-cta"><a class="btn btn-primary" href="{AGENDAR}" target="_blank" rel="noopener">{WA_SVG}Agendar atendimento</a></div>
    </nav>
    <a class="btn btn-primary header-cta" href="{AGENDAR}" target="_blank" rel="noopener">Agendar atendimento</a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="menu" aria-label="Abrir menu"><span></span></button>
  </div>
</header>'''


FOOTER = f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <img class="footer-logo" src="assets/img/logo-simbolo-clara.webp" width="132" height="83" alt="">
        <h2>Alícia Lemos</h2>
        <p class="f-title">{TITLE}<br>{CRP}</p>
      </div>
      <div>
        <h3>Atendimentos</h3>
        <ul>
          <li><a href="infancia-adolescencia-familia.html">Infância, adolescência e família</a></li>
          <li><a href="neurodivergencias.html">Neurodivergências</a></li>
          <li><a href="psicoterapia-adultos.html">Psicoterapia para adultos</a></li>
          <li><a href="psicoterapia-casais.html">Psicoterapia para casais</a></li>
          <li><a href="sobre-mim.html">Sobre mim</a></li>
        </ul>
      </div>
      <div>
        <h3>Contato</h3>
        <ul>
          <li><a href="{AGENDAR}" target="_blank" rel="noopener">WhatsApp: (81) 99708-2433</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="https://instagram.com/{INSTA}" target="_blank" rel="noopener">Instagram: @{INSTA}</a></li>
          <li><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn: Alícia Lemos</a></li>
          <li><a href="privacidade.html">Política de privacidade e dados pessoais</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="ano">2026</span> Alícia Lemos · {CRP}. Todos os direitos reservados.</span>
      <span>Este site não oferece atendimento de urgência. Em caso de crise, ligue 188 (CVV) ou 192 (SAMU).</span>
    </div>
  </div>
</footer>
<a class="wa-float" href="{AGENDAR}" target="_blank" rel="noopener" aria-label="Conversar pelo WhatsApp">{WA_SVG}</a>
<script src="assets/js/site.js" defer></script>'''


PAGES = []


def page(filename, title, description, body, extra_head=""):
    url = f"{DOMAIN}/" + ("" if filename == "index.html" else filename.removesuffix(".html"))
    canonical = f'\n<link rel="canonical" href="{url}">\n<meta property="og:url" content="{url}">' if DOMAIN else ""
    if "noindex" not in extra_head and filename != "404.html":
        PAGES.append(url)
    html = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<meta name="theme-color" content="#faf6f0">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Alícia Lemos · Psicóloga">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:image" content="{DOMAIN}/assets/img/compartilhar.jpg">{canonical}
<link rel="icon" href="assets/img/icone-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/img/icone-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..600;1,9..144,400&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="assets/css/site.css">
{extra_head}</head>
<body>
{header(filename)}
<main id="conteudo">
{body}
</main>
{FOOTER}
</body>
</html>
'''
    with open(f"{OUT}/{filename}", "w", encoding="utf-8") as f:
        f.write(html)


def cta_band(title, text, primary_label, primary_msg, secondary=True):
    sec = (
        f'<a class="btn btn-ghost" href="{wa("Olá, Alícia! Tenho algumas dúvidas sobre o atendimento.")}" target="_blank" rel="noopener">Tirar dúvidas pelo WhatsApp</a>'
        if secondary else ""
    )
    return f'''<section class="section">
  <div class="wrap">
    <div class="cta-band">
      <div>
        <h2>{title}</h2>
        <p>{text}</p>
      </div>
      <div class="btn-row">
        <a class="btn btn-light" href="{wa(primary_msg)}" target="_blank" rel="noopener">{primary_label}</a>
        {sec}
      </div>
    </div>
  </div>
</section>'''


STEPS = '''<section class="section alt" id="primeiro-contato">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Como funciona</span>
      <h2>O primeiro passo é compreender o que você precisa.</h2>
    </div>
    <ol class="steps">
      <li><h3>Entre em contato</h3><p>Envie uma mensagem pelo WhatsApp ou pelo formulário de contato.</p></li>
      <li><h3>Conte brevemente o que procura</h3><p>Não é preciso compartilhar detalhes íntimos. Basta dizer se o atendimento é para você, para uma criança, um adolescente, seu casal ou sua família.</p></li>
      <li><h3>Conversamos sobre as possibilidades</h3><p>Esclareço suas dúvidas, entendo a demanda de forma preliminar e vemos se o serviço procurado é adequado.</p></li>
      <li><h3>Receba as informações</h3><p>Modalidade, disponibilidade, valores e demais condições são informados com transparência.</p></li>
    </ol>
  </div>
</section>'''


def topics(items):
    return '<ul class="topics">' + "".join(f"<li>{t}</li>" for t in items) + "</ul>"


# ---------------------------------------------------------------- Início
FAQ = [
    ("Quais são as modalidades de atendimento disponíveis?",
     "Ofereço psicoterapia para crianças, adolescentes e adultos, psicoterapia de casal, orientação parental e familiar, além de acompanhamento terapêutico e aplicação de intervenções baseadas em ABA em contexto escolar ou domiciliar, conforme a necessidade e as condições de cada atendimento."),
    ("Você atende crianças, adolescentes e adultos?",
     "Sim. O atendimento é direcionado a crianças, adolescentes e adultos, de acordo com a demanda apresentada e a modalidade mais adequada."),
    ("Como funciona a psicoterapia infantil?",
     "A psicoterapia infantil utiliza recursos adequados à idade da criança para favorecer a expressão, a compreensão das emoções e o desenvolvimento de novas possibilidades de enfrentamento. Quando necessário, também envolve a participação dos responsáveis."),
    ("Como funciona a orientação parental?",
     "É um espaço para mães, pais e responsáveis compreenderem melhor as necessidades da criança ou do adolescente e refletirem sobre comunicação, manejo e estratégias de cuidado no cotidiano."),
    ("Como funciona a psicoterapia de casal?",
     "A psicoterapia de casal oferece um espaço de escuta e reflexão sobre a dinâmica da relação, a comunicação, os conflitos, os acordos e os impactos da convivência no contexto familiar. O trabalho é construído de acordo com a história e as necessidades de cada casal."),
    ("A psicoterapia de casal é indicada apenas quando o casal deseja permanecer junto?",
     "Não necessariamente. O atendimento pode ajudar o casal a compreender melhor sua dinâmica, tomar decisões com mais consciência, reorganizar a convivência ou lidar com mudanças na relação. A psicoterapia não determina um resultado específico nem substitui a decisão das pessoas envolvidas."),
    ("Qual é a diferença entre psicoterapia, acompanhamento terapêutico e aplicação ABA?",
     "A psicoterapia é um atendimento psicológico voltado à compreensão das experiências e ao cuidado emocional. O acompanhamento terapêutico oferece suporte em contextos cotidianos, como a escola, enquanto a aplicação ABA utiliza estratégias baseadas na Análise do Comportamento Aplicada, conforme objetivos e supervisão definidos."),
    ("Você atende pessoas que suspeitam ser neurodivergentes?",
     "Sim. O atendimento pode ajudar a compreender as experiências vividas, organizar dúvidas e discutir possibilidades de avaliação ou encaminhamento, sem substituir uma avaliação diagnóstica quando ela for necessária."),
    ("Você realiza avaliação psicológica ou neuropsicológica?",
     "Não realizo avaliações psicológicas ou neuropsicológicas ainda, pois estou finalizando minha especialização, mas posso oferecer acompanhamento psicológico e indicar profissionais ou serviços adequados quando necessário."),
    ("Os atendimentos são presenciais ou on-line?",
     "Os atendimentos podem ser on-line ou presenciais em Recife, realizados em domicílio ou na escola, conforme o serviço e a disponibilidade. A modalidade de cada caso é combinada no primeiro contato."),
    ("Qual é o valor da sessão?",
     "Os valores variam conforme a modalidade, a duração e as condições do atendimento. As informações são fornecidas de maneira transparente no primeiro contato."),
    ("Como funciona o primeiro contato?",
     "Você pode enviar uma mensagem pelo WhatsApp ou pelo formulário, informando brevemente qual atendimento procura. A partir disso, conversamos sobre sua necessidade, disponibilidade, valores e próximos passos."),
]

FAQ_LD = (
    '<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
    + ",".join(
        '{"@type":"Question","name":%s,"acceptedAnswer":{"@type":"Answer","text":%s}}'
        % (__import__("json").dumps(q, ensure_ascii=False), __import__("json").dumps(a, ensure_ascii=False))
        for q, a in FAQ
    )
    + "]}</script>\n"
)
PERSON_LD = f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Psychologist","name":"Alícia Lemos","description":"{TITLE}. {CRP}.","telephone":"+55 81 99708-2433","email":"{EMAIL}","image":"{DOMAIN}/assets/img/compartilhar.jpg","address":{{"@type":"PostalAddress","addressLocality":"Recife","addressRegion":"PE","addressCountry":"BR"}},"areaServed":"Recife e atendimento on-line","sameAs":["https://instagram.com/{INSTA}","{LINKEDIN}"]}}</script>
'''

areas = [
    ("infancia-adolescencia-familia.html", "broto", "Infância, adolescência e família",
     "Psicoterapia infantojuvenil, orientação parental e familiar, acompanhamento terapêutico e aplicação ABA."),
    ("neurodivergencias.html", "constelacao", "Neurodivergências",
     "Acolhimento para quem tem uma suspeita, recebeu um diagnóstico ou busca acompanhamento contínuo."),
    ("psicoterapia-adultos.html", "pessoa", "Psicoterapia para adultos",
     "Um espaço para compreender sua história, suas emoções e construir novos caminhos."),
    ("psicoterapia-casais.html", "casal", "Psicoterapia para casais",
     "Escuta e reflexão sobre a dinâmica da relação, a comunicação e o contexto familiar."),
]
area_cards = "".join(
    f'''<a class="card service-link" href="{h}">{icon(i)}<h3>{t}</h3><p>{d}</p><span class="link-arrow">Saiba mais <span aria-hidden="true">→</span></span></a>'''
    for h, i, t, d in areas
)

faq_html = "".join(
    f'<details><summary>{q}</summary><div class="answer"><p>{a}</p></div></details>' for q, a in FAQ
)

OPCOES = [
    "Psicoterapia para adulto",
    "Atendimento para criança ou adolescente",
    "Orientação parental ou familiar",
    "Psicoterapia de casal",
    "Neurodivergências",
    "Acompanhamento terapêutico ou ABA",
    "Ainda não sei",
]

index_body = f'''<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">Psicóloga Clínica · {CRP}</span>
      <h1>Um espaço para compreender a si mesmo, desenvolver possibilidades e construir novos caminhos</h1>
      <p class="lede">Sou Alícia Lemos, Psicóloga Clínica graduada pela Universidade Federal de Pernambuco, com pós-graduação em andamento em Neuropsicologia, Acompanhante Terapêutica e Aplicadora ABA (Análise do Comportamento Aplicada).</p>
      <p class="hero-intro">Acredito em uma Psicologia que acolhe a singularidade de cada pessoa, respeita suas diferenças e considera o contexto em que ela vive. Atendo crianças, adolescentes, adultos, casais e famílias.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="#atendimentos">Conheça meus atendimentos</a>
        <a class="btn btn-ghost" href="{wa("Olá, Alícia! Gostaria de agendar uma conversa.")}" target="_blank" rel="noopener">{WA_SVG}Agende uma conversa</a>
      </div>
      <div class="hero-meta"><span>Recife – PE</span><span>Atendimento on-line, domiciliar e escolar</span><span>Crianças, adolescentes, adultos, casais e famílias</span></div>
    </div>
    <div class="hero-photo">
      <picture>
        <source media="(max-width: 820px)" srcset="assets/img/alicia-retrato-480.webp">
        <img src="assets/img/alicia-retrato-720.webp" width="720" height="957" alt="Alícia Lemos, psicóloga, sorrindo sentada em uma poltrona" fetchpriority="high">
      </picture>
      <div class="hero-badge"><b>Alícia Lemos</b>Psicóloga Clínica · {CRP}</div>
    </div>
  </div>
</section>

<section class="section alt" id="atendimentos">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Atendimentos</span>
      <h2>Propostas de cuidado construídas de acordo com cada pessoa ou relação</h2>
      <p class="lede">Escolha a área mais próxima do que você procura. Se ainda não souber, tudo bem: podemos conversar e entender juntos.</p>
    </div>
    <div class="grid-4">{area_cards}</div>
  </div>
</section>

<section class="section">
  <div class="wrap about-teaser">
    <img src="assets/img/alicia-retrato-480.webp" width="480" height="638" alt="Retrato de Alícia Lemos" loading="lazy">
    <div>
      <span class="eyebrow">Sobre mim</span>
      <h2>Uma Psicologia que acolhe a singularidade de cada pessoa</h2>
      <p class="lede" style="margin-top:16px">Meu trabalho é voltado ao cuidado psicológico, ao desenvolvimento humano e à compreensão das experiências que atravessam nossas vidas, nossas relações e nossas formas de existir.</p>
      <a class="link-arrow" href="sobre-mim.html">Conheça minha trajetória <span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>

{STEPS}

<section class="section" id="perguntas">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Dúvidas</span>
      <h2>Perguntas frequentes</h2>
    </div>
    <div class="faq">{faq_html}</div>
  </div>
</section>

<section class="section alt" id="contato">
  <div class="wrap contact-grid">
    <div>
      <span class="eyebrow">Contato</span>
      <h2>Vamos conversar sobre o atendimento mais adequado para você?</h2>
      <p class="lede" style="margin-top:16px">Se você está buscando acompanhamento psicológico ou quer entender as possibilidades de atendimento para você, seu casal ou sua família, entre em contato. Será um prazer esclarecer suas dúvidas e explicar como funciona o processo.</p>
      <ul class="channels">
        <li><a href="{AGENDAR}" target="_blank" rel="noopener">{icon("conversa")}<span><b>WhatsApp</b><small>(81) 99708-2433</small></span></a></li>
        <li><a href="mailto:{EMAIL}">{icon("email")}<span><b>E-mail</b><small>{EMAIL}</small></span></a></li>
        <li><a href="https://instagram.com/{INSTA}" target="_blank" rel="noopener">{icon("instagram")}<span><b>Instagram</b><small>@{INSTA}</small></span></a></li>
        <li><a href="{LINKEDIN}" target="_blank" rel="noopener">{icon("linkedin")}<span><b>LinkedIn</b><small>Alícia Lemos</small></span></a></li>
        <li><div>{icon("local")}<span><b>Onde atendo</b><small>On-line · Em Recife, em casa ou na escola, conforme o serviço</small></span></div></li>
      </ul>
    </div>
    <div class="form-card">
      <h3>Prefere deixar seus dados?</h3>
      <p>Preencha e o WhatsApp abre com a mensagem pronta. Nada é enviado nem guardado pelo site.</p>
      <form class="form" id="form-contato">
        <div class="form-row">
          <div class="field"><label for="f-nome">Nome</label><input id="f-nome" name="nome" autocomplete="name" required></div>
          <div class="field"><label for="f-contato">E-mail ou telefone</label><input id="f-contato" name="contato" autocomplete="tel"></div>
        </div>
        <div class="field">
          <label for="f-atendimento">Qual atendimento procura?</label>
          <select id="f-atendimento" name="atendimento" required>
            <option value="" disabled selected>Escolha uma opção</option>
            {"".join(f"<option>{o}</option>" for o in OPCOES)}
          </select>
        </div>
        <fieldset class="field">
          <legend>Como prefere ser contatado(a)?</legend>
          <div class="choices">
            <label><input type="radio" name="preferencia" value="WhatsApp" checked> WhatsApp</label>
            <label><input type="radio" name="preferencia" value="ligação"> Ligação</label>
            <label><input type="radio" name="preferencia" value="e-mail"> E-mail</label>
          </div>
        </fieldset>
        <button class="btn btn-primary" type="submit">{WA_SVG}Enviar pelo WhatsApp</button>
        <p class="form-note">Por segurança, não inclua informações de saúde, diagnósticos ou relatos pessoais. Isso pode ser conversado com calma depois. Veja a <a href="privacidade.html">política de privacidade</a>.</p>
      </form>
    </div>
  </div>
</section>'''

page("index.html",
     "Alícia Lemos · Psicóloga Clínica em Recife | " + CRP,
     "Psicoterapia para crianças, adolescentes, adultos e casais, orientação parental, neurodivergências, acompanhamento terapêutico e ABA. Atendimento em Recife e on-line.",
     index_body, PERSON_LD + FAQ_LD)

# ---------------------------------------------------------------- Infância, adolescência e família
inf_body = f'''<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Início</a> · Infância, adolescência e família</p>
    <span class="eyebrow">Infância, adolescência e família</span>
    <h1>Cuidar de quem está crescendo também é cuidar das relações ao seu redor</h1>
    <p class="lede">A infância e a adolescência são etapas marcadas por descobertas, transformações e desafios. As emoções, os comportamentos e as relações fazem parte desse processo e precisam ser compreendidos com atenção à história e à singularidade de cada pessoa.</p>
    <p class="lede">Meu trabalho busca oferecer suporte ao desenvolvimento emocional, à autonomia, à comunicação e à construção de relações mais saudáveis, considerando também o papel da família e dos ambientes em que a criança ou o adolescente está inserido.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <article class="service" id="psicoterapia-infantojuvenil">
      <div class="service-side">{icon("broto")}<h3>Psicoterapia infantojuvenil</h3></div>
      <div class="service-body">
        <p>Atendimento psicológico voltado à compreensão das emoções, dos comportamentos, das dificuldades relacionais e dos desafios do desenvolvimento.</p>
        <p>O acompanhamento é construído de acordo com as necessidades da criança ou do adolescente, considerando sua história, seu contexto e sua maneira particular de se expressar.</p>
        <p>Conforme a necessidade, o trabalho pode envolver conversas com os responsáveis e orientação parental.</p>
        <a class="btn btn-primary" href="{wa("Olá, Alícia! Gostaria de saber mais sobre o atendimento infantojuvenil.")}" target="_blank" rel="noopener">Saiba mais sobre o atendimento infantojuvenil</a>
      </div>
    </article>

    <article class="service" id="orientacao-parental">
      <div class="service-side">{icon("familia")}<h3>Orientação parental e familiar</h3></div>
      <div class="service-body">
        <p>A família também precisa de espaço para compreender o que está acontecendo e encontrar novas possibilidades de cuidado.</p>
        <p>A orientação parental ajuda mães, pais e responsáveis a compreender as necessidades dos filhos, refletir sobre os desafios do dia a dia e desenvolver estratégias de comunicação, manejo e apoio ao desenvolvimento.</p>
        <div class="fineprint"><b>Para não confundir:</b> a orientação parental é voltada aos responsáveis; a psicoterapia infantojuvenil é o atendimento da própria criança ou adolescente; e a <a href="psicoterapia-casais.html">psicoterapia de casal</a> cuida da relação conjugal. No primeiro contato, conversamos sobre qual delas faz sentido para a sua família.</div>
        <a class="btn btn-primary" href="{wa("Olá, Alícia! Gostaria de conhecer o atendimento às famílias (orientação parental e familiar).")}" target="_blank" rel="noopener">Conheça o atendimento às famílias</a>
      </div>
    </article>

    <article class="service" id="acompanhamento-aba">
      <div class="service-side">{icon("maos")}<h3>Acompanhamento terapêutico e aplicação ABA</h3></div>
      <div class="service-body">
        <p>Serviços voltados ao apoio ao desenvolvimento e à participação da criança ou do adolescente em seus contextos do dia a dia. São diferentes da psicoterapia e por isso são apresentados separadamente:</p>
        <div class="sub-services">
          <div class="card">
            <h4>Acompanhamento terapêutico (AT)</h4>
            <p>Apoio à criança ou ao adolescente em ambientes como a escola ou a casa, de acordo com a necessidade e o planejamento do atendimento.</p>
            <p class="note">Onde acontece: escola ou domicílio, conforme o combinado com a família.</p>
          </div>
          <div class="card">
            <h4>Aplicação de intervenções baseadas em ABA</h4>
            <p>Execução de estratégias individualizadas, baseadas na Análise do Comportamento Aplicada, com objetivos definidos.</p>
            <p class="note">Realizada com a orientação e a supervisão profissional pertinentes a cada caso.</p>
          </div>
        </div>
        <div class="fineprint">O acompanhamento terapêutico e a aplicação ABA não substituem a psicoterapia. A finalidade, os objetivos, o local e as condições de cada atendimento são combinados antes do início.</div>
        <a class="btn btn-primary" href="{wa("Olá, Alícia! Gostaria de informações sobre acompanhamento terapêutico e ABA.")}" target="_blank" rel="noopener">Solicitar informações sobre acompanhamento e ABA</a>
      </div>
    </article>
  </div>
</section>

{STEPS}

{cta_band("Vamos conversar sobre o que sua família precisa?", "Conte brevemente para quem é o atendimento e eu explico as possibilidades, a disponibilidade e os valores.", "Buscar atendimento para meu filho ou filha", "Olá, Alícia! Gostaria de buscar atendimento para meu filho ou filha.")}'''

page("infancia-adolescencia-familia.html",
     "Psicoterapia infantojuvenil, orientação parental, AT e ABA | Alícia Lemos · Psicóloga em Recife",
     "Psicoterapia para crianças e adolescentes, orientação parental e familiar, acompanhamento terapêutico na escola ou em casa e aplicação de intervenções baseadas em ABA.",
     inf_body)

# ---------------------------------------------------------------- Neurodivergências
neuro_cards = [
    ("lupa", "Quando existe uma suspeita",
     "Um espaço para compreender as dificuldades percebidas, organizar as dúvidas, conhecer melhor a própria história e discutir possibilidades de avaliação e encaminhamento."),
    ("bussola", "Após um diagnóstico",
     "Acompanhamento para compreender o diagnóstico, reconhecer necessidades individuais e construir estratégias para lidar com emoções, relações, autonomia e desafios do dia a dia."),
    ("coracao", "Acompanhamento contínuo",
     "Um cuidado para crianças, adolescentes e adultos neurodivergentes que respeita as particularidades de cada pessoa, suas potencialidades, necessidades de suporte, contexto social e qualidade de vida."),
]
neuro_body = f'''<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Início</a> · Neurodivergências</p>
    <span class="eyebrow">Neurodivergências</span>
    <h1>Compreender as diferenças é ampliar as possibilidades de cuidado.</h1>
    <p class="lede">Cada pessoa tem uma maneira própria de perceber, sentir, aprender, se comunicar e se relacionar com o mundo.</p>
    <p class="lede">Quando surgem dúvidas sobre o desenvolvimento ou sobre a possibilidade de uma neurodivergência, informações confiáveis e um espaço de escuta ajudam a compreender melhor as próprias necessidades e os próximos passos.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Três momentos em que posso acompanhar você</h2>
      <p class="lede">Atendo crianças, adolescentes e adultos neurodivergentes e também pessoas que estão investigando características ou buscando compreender melhor suas experiências.</p>
    </div>
    <div class="grid-3">{"".join(f'<div class="card">{icon(i)}<h3>{t}</h3><p>{d}</p></div>' for i, t, d in neuro_cards)}</div>
    <div class="fineprint" style="margin-top:28px">A proposta não é reduzir a pessoa a um diagnóstico, mas compreender como ela vive, quais barreiras encontra e que recursos podem favorecer seu bem-estar e sua participação na vida cotidiana.</div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <div class="section-head">
      <h2>O que eu ofereço e o que é encaminhado</h2>
      <p class="lede">Psicoterapia, avaliação psicológica e avaliação neuropsicológica são serviços diferentes. Para você saber exatamente o que esperar:</p>
    </div>
    <div class="scope">
      <div class="card yes">
        <h3>{icon("estrela")} Ofereço</h3>
        <ul>
          <li>Acolhimento e acompanhamento psicológico (psicoterapia) de pessoas neurodivergentes e de quem tem uma suspeita</li>
          <li>Apoio para organizar dúvidas e entender os caminhos de avaliação</li>
          <li><a href="infancia-adolescencia-familia.html#acompanhamento-aba">Acompanhamento terapêutico e aplicação ABA</a> para crianças e adolescentes</li>
          <li><a href="infancia-adolescencia-familia.html#orientacao-parental">Orientação parental e familiar</a></li>
        </ul>
      </div>
      <div class="card no">
        <h3>{icon("bussola")} Encaminho quando necessário</h3>
        <ul>
          <li>Avaliação psicológica e avaliação neuropsicológica: ainda não realizo, pois estou finalizando minha especialização</li>
          <li>Diagnóstico e acompanhamentos com outros profissionais, quando forem necessários</li>
        </ul>
        <p class="topics-note" style="margin-bottom:0">Quando for o caso, indico profissionais ou serviços adequados. O acompanhamento psicológico não substitui uma avaliação diagnóstica.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="cta-band">
      <div>
        <h2>Vamos entender juntos qual é o próximo passo?</h2>
        <p>Conte brevemente se o atendimento é para você ou para seu filho ou filha. Eu explico as possibilidades.</p>
      </div>
      <div class="btn-row">
        <a class="btn btn-light" href="{wa("Olá, Alícia! Quero entender minhas possibilidades de atendimento em neurodivergências.")}" target="_blank" rel="noopener">Quero entender minhas possibilidades de atendimento</a>
        <a class="btn btn-ghost" href="{wa("Olá, Alícia! Gostaria de buscar atendimento em neurodivergências para meu filho ou filha.")}" target="_blank" rel="noopener">Buscar atendimento para meu filho ou filha</a>
      </div>
    </div>
  </div>
</section>'''

page("neurodivergencias.html",
     "Neurodivergências: acolhimento e acompanhamento psicológico | Alícia Lemos · Psicóloga em Recife",
     "Acompanhamento psicológico de crianças, adolescentes e adultos neurodivergentes e de quem tem uma suspeita ou recebeu um diagnóstico. Atendimento em Recife e on-line.",
     neuro_body)

# ---------------------------------------------------------------- Adultos
adultos_body = f'''<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Início</a> · Psicoterapia para adultos</p>
    <span class="eyebrow">Psicoterapia para adultos</span>
    <h1>Um espaço para compreender sua história e construir novas possibilidades de existir.</h1>
    <p class="lede">Nem sempre conseguimos compreender o que sentimos, por que repetimos certos padrões ou como lidar com as mudanças e os conflitos que atravessam nossas vidas.</p>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="prose">
      <h2>O que é a psicoterapia</h2>
      <p style="margin-top:18px">A psicoterapia é um espaço de escuta, reflexão e construção de sentidos. Um lugar para olhar para a própria história, reconhecer emoções, compreender relações e desenvolver novas formas de se posicionar diante de si, dos outros e do mundo.</p>
      <p>Minha atuação é orientada por uma perspectiva humanizada, inclusiva e atenta à experiência singular de cada pessoa, com influência fenomenológica e existencial.</p>
      <p>O processo considera não apenas os sintomas ou as dificuldades apresentadas, mas também os sentidos que cada experiência tem na vida de quem a vive.</p>
    </div>
    <aside class="explain" aria-label="A abordagem em palavras simples">
      <h3>A abordagem, em palavras simples</h3>
      <dl>
        <dt>Fenomenológica</dt>
        <dd>Busca compreender como você vive suas experiências: seus sentimentos, percepções, relações e o contexto em que está.</dd>
        <dt>Existencial</dt>
        <dd>Valoriza a liberdade, as escolhas, a responsabilidade, os valores e os sentidos que cada pessoa constrói ao longo da vida.</dd>
        <dt>Na prática</dt>
        <dd>Olhar para você de forma integral, respeitando sua história e ajudando a refletir sobre o que vive, suas possibilidades e os caminhos que deseja construir.</dd>
      </dl>
    </aside>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <div class="section-head">
      <h2>Temas que podem ser trabalhados</h2>
    </div>
    {topics(["Ansiedade e dificuldades emocionais", "Autoconhecimento e autoestima", "Relacionamentos e conflitos interpessoais", "Mudanças de vida, escolhas e transições", "Sentido da vida e questões existenciais", "Autonomia, identidade e construção de limites", "Experiências de sofrimento e dificuldades de adaptação"])}
    <p class="topics-note">Esses são exemplos de possibilidades de trabalho. Cada processo é único e construído a partir da sua história e das suas necessidades.</p>
  </div>
</section>

{cta_band("Você não precisa ter todas as respostas para começar.", "Se deseja compreender melhor o que está vivendo, podemos conversar sobre suas necessidades e verificar se o atendimento faz sentido para você.", "Tenho interesse em iniciar a psicoterapia", "Olá, Alícia! Tenho interesse em iniciar a psicoterapia.")}

{STEPS}'''

page("psicoterapia-adultos.html",
     "Psicoterapia para adultos | Alícia Lemos · Psicóloga em Recife",
     "Psicoterapia para adultos com abordagem humanizada, de influência fenomenológica e existencial: ansiedade, autoestima, relacionamentos, transições e sentido da vida.",
     adultos_body)

# ---------------------------------------------------------------- Casais
casais_body = f'''<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Início</a> · Psicoterapia para casais</p>
    <span class="eyebrow">Psicoterapia para casais</span>
    <h1>Cuidar da relação também é cuidar das pessoas que fazem parte dela.</h1>
    <p class="lede">As relações passam por diferentes fases, mudanças e desafios. Conflitos recorrentes, dificuldades de comunicação, distanciamento, mudanças na rotina ou acontecimentos importantes podem afetar a forma como o casal se relaciona.</p>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="prose">
      <h2>Como é o trabalho com o casal</h2>
      <p style="margin-top:18px">A psicoterapia de casal oferece um espaço de escuta e reflexão para que as pessoas possam compreender melhor a dinâmica da relação, expressar suas necessidades e construir formas mais conscientes de diálogo e convivência.</p>
      <p>O trabalho considera a história de cada pessoa, os acordos e padrões construídos ao longo da relação e o contexto em que o casal está inserido.</p>
    </div>
    <aside class="explain">
      <h3>O que a psicoterapia de casal não é</h3>
      <dl>
        <dt>Não é um julgamento</dt>
        <dd>A proposta não é definir quem está certo ou errado, mas favorecer a compreensão dos conflitos, das necessidades e das possibilidades daquela relação.</dd>
        <dt>Não promete um resultado</dt>
        <dd>Não há promessa de reconciliação ou de manutenção da relação. As decisões continuam sendo das pessoas envolvidas.</dd>
      </dl>
    </aside>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <div class="section-head">
      <h2>Temas que podem ser trabalhados</h2>
    </div>
    {topics(["Dificuldades de comunicação e escuta", "Conflitos recorrentes e diferenças na forma de lidar com situações", "Distanciamento emocional ou dificuldades na convivência", "Mudanças de vida e transições na relação", "Parentalidade e impactos da relação no contexto familiar", "Construção e revisão de acordos e limites", "Confiança, intimidade e expectativas sobre a relação", "Decisões importantes e momentos de crise", "Reorganização da relação diante de mudanças familiares"])}
    <p class="topics-note">São possibilidades de trabalho. Cada casal tem uma história, uma dinâmica e necessidades próprias.</p>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div class="prose">
      <span class="eyebrow">Relação e família</span>
      <h2>A relação do casal faz parte de um contexto mais amplo</h2>
      <p style="margin-top:18px">Mudanças na comunicação, nos conflitos e na forma de tomar decisões podem repercutir na rotina da família, na parentalidade e na maneira como os filhos vivem o ambiente de casa.</p>
      <p>Por isso, quando pertinente, o processo pode ajudar o casal a refletir sobre como sua dinâmica se relaciona com as demais relações familiares, sempre respeitando os limites, os objetivos e a modalidade do atendimento.</p>
    </div>
    <div class="fineprint" style="margin-top:0">A psicoterapia de casal não substitui a psicoterapia individual, a <a href="infancia-adolescencia-familia.html#orientacao-parental">orientação parental</a> ou a psicoterapia familiar. Quando necessário, conversamos sobre outras possibilidades de cuidado ou encaminhamentos adequados.</div>
  </div>
</section>

{cta_band("Toda relação pode precisar de um espaço para ser compreendida.", "Se vocês desejam compreender melhor o que estão vivendo, podemos conversar sobre a demanda e verificar se a psicoterapia de casal é uma possibilidade adequada.", "Tenho interesse em iniciar a psicoterapia de casal", "Olá, Alícia! Tenho interesse em iniciar a psicoterapia de casal.")}

{STEPS}'''

page("psicoterapia-casais.html",
     "Psicoterapia para casais | Alícia Lemos · Psicóloga em Recife",
     "Psicoterapia de casal: comunicação, conflitos, acordos, parentalidade e momentos de crise, considerando o contexto familiar. Atendimento em Recife e on-line.",
     casais_body)

# ---------------------------------------------------------------- Sobre mim
formacao = [
    ("capelo", "Graduação em Psicologia", "Universidade Federal de Pernambuco (UFPE)"),
    ("livro", "Pós-graduação em Neuropsicologia", "Em andamento"),
    ("estrela", "Educação socioemocional", "Experiência profissional"),
    ("broto", "Acompanhamento de crianças e adolescentes", "Incluindo o trabalho com pessoas neurodivergentes"),
    ("maos", "Acompanhamento terapêutico e práticas baseadas em ABA", "Acompanhante Terapêutica e Aplicadora ABA"),
]
sobre_body = f'''<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Início</a> · Sobre mim</p>
    <span class="eyebrow">Sobre mim</span>
    <h1>Quem sou eu e como compreendo o cuidado psicológico</h1>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap about-grid">
    <div class="about-photo">
      <picture>
        <source media="(max-width: 820px)" srcset="assets/img/alicia-consultorio-768.webp">
        <img src="assets/img/alicia-consultorio-1200.webp" width="1200" height="800" alt="Alícia Lemos sentada à mesa, com a placa Psicóloga Clínica, CRP 02/34070, sobre a mesa">
      </picture>
    </div>
    <div class="prose">
      <p>Sou Alícia Lemos, Psicóloga Clínica formada pela Universidade Federal de Pernambuco, com pós-graduação em andamento em Neuropsicologia. Sou também Acompanhante Terapêutica e Aplicadora ABA.</p>
      <p>Minha trajetória reúne experiências ligadas ao desenvolvimento humano, à educação socioemocional e ao acompanhamento de crianças e adolescentes, incluindo o trabalho com pessoas neurodivergentes.</p>
      <p>Parto do reconhecimento de que cada pessoa tem uma história, um contexto e necessidades próprias. Por isso, procuro compreender não apenas o que alguém apresenta como dificuldade, mas também suas relações, seus recursos, suas experiências e as condições em que vive.</p>
      <p>Na clínica, busco construir um espaço de escuta, acolhimento e reflexão, respeitando a singularidade de cada pessoa, casal, família e processo.</p>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <div class="section-head">
      <h2>Formação e experiência</h2>
    </div>
    <ul class="timeline">
      {"".join(f'<li>{icon(i)}<div><b>{t}</b><span>{d}</span></div></li>' for i, t, d in formacao)}
    </ul>
    <p class="topics-note">{CRP} · Conselho Regional de Psicologia da 2ª Região (Pernambuco).</p>
  </div>
</section>

{cta_band("Vamos conversar?", "Conte brevemente o que você procura e eu explico como funciona o atendimento.", "Agendar atendimento", "Olá, Alícia! Gostaria de agendar um atendimento.")}'''

page("sobre-mim.html",
     "Sobre mim | Alícia Lemos · Psicóloga Clínica, " + CRP,
     "Alícia Lemos é Psicóloga Clínica formada pela UFPE, com pós-graduação em andamento em Neuropsicologia, Acompanhante Terapêutica e Aplicadora ABA, em Recife.",
     sobre_body)

# ---------------------------------------------------------------- Privacidade
priv_body = f'''<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Início</a> · Política de privacidade</p>
    <h1>Política de privacidade e tratamento de dados pessoais</h1>
    <p class="lede">Como este site trata as informações de quem o visita, em conformidade com a Lei Geral de Proteção de Dados (Lei nº 13.709/2018).</p>
  </div>
</section>
<section class="section" style="padding-top:24px">
  <div class="wrap legal">
    <h2>Quem é a responsável</h2>
    <p>Alícia Lemos, {TITLE}, {CRP}. Contato: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

    <h2>Quais dados este site coleta</h2>
    <p>Este site não tem cadastro, não usa cookies de rastreamento nem ferramentas de publicidade, e não guarda os dados digitados no formulário.</p>
    <p>Ao usar o formulário de contato, as informações que você preencher (nome, contato, tipo de atendimento procurado e preferência de contato) são usadas apenas para montar uma mensagem que abre no seu WhatsApp. Ela só é enviada se você confirmar o envio no aplicativo.</p>

    <h2>Para que os dados são usados</h2>
    <p>Os dados recebidos por WhatsApp, e-mail ou Instagram são usados exclusivamente para responder ao seu contato, esclarecer dúvidas e combinar um possível atendimento. Não são vendidos nem compartilhados com terceiros, salvo por obrigação legal.</p>

    <h2>Cuidados com informações de saúde</h2>
    <p>Pedimos que você não envie, no primeiro contato, informações de saúde, diagnósticos, documentos ou relatos íntimos. Essas informações são tratadas com sigilo profissional apenas durante o atendimento, conforme o Código de Ética Profissional do Psicólogo.</p>

    <h2>Serviços de terceiros</h2>
    <ul>
      <li>As conversas pelo WhatsApp e pelo Instagram seguem as políticas de privacidade da Meta.</li>
      <li>As fontes do site são carregadas do Google Fonts, que pode receber dados técnicos de acesso, como o endereço IP.</li>
    </ul>

    <h2>Seus direitos</h2>
    <p>Você pode pedir a qualquer momento acesso, correção ou exclusão dos seus dados de contato, e informações sobre o uso deles, pelo e-mail <a href="mailto:{EMAIL}">{EMAIL}</a>. Os registros de atendimento psicológico seguem os prazos de guarda definidos pelo Conselho Federal de Psicologia.</p>

    <h2>Atualizações</h2>
    <p>Esta política pode ser atualizada para refletir mudanças no site. Última atualização: outubro de 2026.</p>
  </div>
</section>'''

page("privacidade.html",
     "Política de privacidade | Alícia Lemos · Psicóloga",
     "Como o site de Alícia Lemos, Psicóloga, trata dados pessoais conforme a LGPD.",
     priv_body, '<meta name="robots" content="noindex">\n')

print("ok")

# ---------------------------------------------------------------- 404
page("404.html",
     "Página não encontrada | Alícia Lemos · Psicóloga",
     "Esta página não existe.",
     f'''<section class="page-hero" style="min-height:52vh">
  <div class="wrap">
    <span class="eyebrow">Página não encontrada</span>
    <h1>Não encontramos esta página</h1>
    <p class="lede">O endereço pode ter mudado. Você pode voltar ao início ou falar diretamente comigo.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="index.html">Ir para o início</a>
      <a class="btn btn-ghost" href="{AGENDAR}" target="_blank" rel="noopener">Falar pelo WhatsApp</a>
    </div>
  </div>
</section>''', '<meta name="robots" content="noindex">\n')
print("404 ok")

if DOMAIN:
    with open(f"{OUT}/sitemap.xml", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        f.write("".join(f"  <url><loc>{u}</loc></url>\n" for u in PAGES))
        f.write("</urlset>\n")
    print("sitemap ok")

with open(f"{OUT}/robots.txt", "w", encoding="utf-8") as f:
    f.write("User-agent: *\nAllow: /\nDisallow: /privacidade\n" + (f"Sitemap: {DOMAIN}/sitemap.xml\n" if DOMAIN else ""))
