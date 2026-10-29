document.addEventListener("DOMContentLoaded",function(){
 var b=document.querySelector(".menu"),n=document.querySelector("nav");
 if(b)b.addEventListener("click",function(){var o=n.classList.toggle("open");b.setAttribute("aria-expanded",o)});
 var P=window.GRADIQ_PRODUCTS||{};
 document.querySelectorAll("[data-buy]").forEach(function(a){var u=(P[a.dataset.buy]||{}).BUY_URL;
  if(u){a.href=u;a.textContent="Buy on Etsy";a.classList.remove("disabled");a.classList.add("primary");a.removeAttribute("aria-disabled");a.target="_blank";a.rel="noopener"}});
});
