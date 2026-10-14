/* Menu do celular, cabeçalho ao rolar e formulário que abre o WhatsApp. */
(function () {
  var WHATSAPP = "5581997082433";

  // Menu (celular e tablet)
  var toggle = document.querySelector(".menu-toggle");
  var nav = document.getElementById("menu");
  function setMenu(open) {
    if (!toggle || !nav) return;
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    toggle.setAttribute("aria-label", open ? "Fechar menu" : "Abrir menu");
    nav.classList.toggle("open", open);
    document.body.classList.toggle("menu-open", open);
  }
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      setMenu(toggle.getAttribute("aria-expanded") !== "true");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) setMenu(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") setMenu(false);
    });
  }

  // Sombra no cabeçalho depois de rolar
  var header = document.querySelector(".site-header");
  function onScroll() {
    if (header) header.classList.toggle("scrolled", window.scrollY > 8);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Ano no rodapé
  var year = document.getElementById("ano");
  if (year) year.textContent = new Date().getFullYear();

  // Formulário: monta a mensagem e abre o WhatsApp (nada é enviado ou guardado pelo site)
  var form = document.getElementById("form-contato");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var nome = form.nome.value.trim();
      var contato = form.contato.value.trim();
      var atendimento = form.atendimento.value;
      var pref = form.querySelector("input[name=preferencia]:checked");
      var texto = "Olá, Alícia! Meu nome é " + nome + ".";
      if (atendimento) texto += " Procuro: " + atendimento + ".";
      if (contato) texto += " Meu contato: " + contato + ".";
      if (pref) texto += " Prefiro ser contatado(a) por " + pref.value + ".";
      texto += " Gostaria de mais informações sobre o atendimento.";
      window.open("https://wa.me/" + WHATSAPP + "?text=" + encodeURIComponent(texto), "_blank", "noopener");
    });
  }
})();
