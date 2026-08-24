# Alícia Lemos Melo — Landing Page para Psicóloga Clínica

Landing page institucional desenvolvida para uma psicóloga clínica (Gestalt-terapia), com foco em conversão via WhatsApp, identidade visual autoral e conformidade com a LGPD.

> 🔗 **Case de portfólio** — projeto real, entregue para uma cliente. Repositório mantido **privado** por conter dados pessoais dela (foto, telefone, CRP); acesso disponível sob solicitação.

## ✨ Visão geral

O objetivo do projeto foi criar uma presença digital simples, elegante e com identidade própria para uma psicóloga clínica, priorizando:

- **Confiança e credibilidade** — CRP, formação e abordagem terapêutica em destaque
- **Conversão direta** — botões de agendamento levam direto ao WhatsApp com mensagem pré-preenchida
- **Performance** — HTML/CSS puro, sem frameworks ou dependências de build
- **Conformidade** — página dedicada de Política de Privacidade (LGPD)

## 🧠 Contexto e decisões

O briefing era simples: uma página única que passasse acolhimento e credibilidade profissional, sem parecer um site "institucional genérico" de clínica. Algumas decisões de projeto:

- **Tipografia serifada (Fraunces) nos títulos** para trazer um tom mais humano e editorial, fugindo do padrão "corporativo" de sites de saúde
- **Paleta terrosa/neutra** em vez de azul/verde clínico tradicional, reforçando a sensação de acolhimento
- **CTA único e repetido** (WhatsApp) em vez de múltiplos canais, para reduzir fricção na conversão
- **Formulário sem backend**, propositalmente — evita custo de infraestrutura e mantém o fluxo 100% dentro do WhatsApp, canal que a cliente já usa para atendimento

## 🖼️ Preview

![Alícia Lemos Melo — Psicóloga Clínica](assets/alicia-foto.jpeg)

## 🧩 Funcionalidades

- **Hero com CTA duplo** — agendamento direto pelo WhatsApp ou navegação para conhecer a abordagem
- **Faixa animada (marquee)** com palavras-chave do trabalho terapêutico
- **Seção "Sobre"** com citação em destaque e formação/credenciais
- **Cards de público-atendido** (infantil, adultos, casais)
- **Linha do tempo "Como funciona"** em 3 passos até a primeira sessão
- **Formulário de contato** que monta e abre uma mensagem pronta no WhatsApp (sem backend)
- **Animações de scroll reveal** via `IntersectionObserver`
- **SEO on-page** completo: meta description, Open Graph e Twitter Cards
- **Página de Política de Privacidade** separada, com `noindex` e conteúdo alinhado à LGPD
- Totalmente **responsivo** (mobile-first em breakpoints principais)

## 🛠️ Stack

- **HTML5** semântico
- **CSS3** puro (custom properties, grid, flexbox, animações)
- **JavaScript vanilla** (sem dependências)
- **Google Fonts** — [Fraunces](https://fonts.google.com/specimen/Fraunces) (títulos) + [Inter](https://fonts.google.com/specimen/Inter) (corpo de texto)

Sem build step, sem bundler, sem frameworks — o projeto roda apenas abrindo o `index.html`.

## 📁 Estrutura do projeto

```
alicia-psicologia-landing/
├── index.html          # Página principal
├── privacidade.html     # Política de Privacidade (LGPD)
├── assets/
│   ├── alicia-foto.jpeg # Foto de perfil da profissional
│   └── favicon.svg      # Favicon (símbolo Ψ)
└── README.md
```

## 🚀 Como rodar localmente

Por ser um site 100% estático, basta abrir o arquivo diretamente no navegador:

```bash
git clone https://github.com/<seu-usuario>/alicia-psicologia-landing.git
cd alicia-psicologia-landing
open index.html   # ou "start index.html" no Windows
```

Ou sirva com um servidor local simples:

```bash
python3 -m http.server 8000
```

E acesse `http://localhost:8000`.

## 🎨 Identidade visual

Paleta inspirada em tons terrosos e acolhedores, remetendo a um consultório de psicologia:

| Cor | Uso |
|---|---|
| `#F5EFE3` | Fundo principal (cream) |
| `#2B2119` | Texto principal (espresso) |
| `#B87D50` / `#9C6640` | Acentos (clay) |
| `#6E7A5A` | Detalhes (sage) |

## 📌 Notas

- O formulário de contato **não possui backend** — ele monta a mensagem e abre o WhatsApp Web/App com o texto pronto, sem envio automático.
- As imagens e informações pessoais (foto, nome, CRP, telefone) pertencem à cliente do projeto e são usadas aqui como parte do case real de entrega.

## 👤 Autor

Desenvolvido por **Matheus Iago** como projeto de portfólio em desenvolvimento web / landing pages.
