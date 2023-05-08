console.log("cargado");
let url = window.location.href;
if (url.includes("contact")) {
  console.log(url);
  let footer = document.getElementsByClassName("footer")[0];
  footer.classList.add("fixed-bottom");
}
