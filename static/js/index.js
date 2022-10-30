window.onload = () => {
  const UpdateAccount = document.querySelector("#UpdateAccount");
  const UpdateUnsegmented = document.querySelector("#UpdateUnsegmented");
  const UpdateURL = document.querySelector("#UpdateURL");
  const LoadFile = document.querySelector("#LoadFile");
  
  const SearchExistingAccounts = document.querySelector(
    "#SearchExistingAccounts"
  );
  UpdateAccount.classList.remove("active");
  UpdateUnsegmented.classList.remove("active");
  UpdateURL.classList.remove("active");
  LoadFile.classList.remove("active");
  SearchExistingAccounts.classList.remove("active");

  if (
    window.location.href.split("/").at(-2) == "updateaccount"
  ) {
    UpdateAccount.classList.add("active");
  } else if (
    window.location.href.split("/").at(-2) == "updateunsegmented"
  ) {
    UpdateUnsegmented.classList.add("active");
  } else if (
    window.location.href.split("/").at(-2) == "updateurl"
  ) {
    UpdateURL.classList.add("active");
  } else if (
    window.location.href.split("/").at(-2) == "loadfile"
  ) {
    LoadFile.classList.add("active");
  } else if (
    window.location.href.split("/").at(-2) ==
    "searchexisting"
  ) {
    SearchExistingAccounts.classList.add("active");
  }
};

const navbarClose = document.querySelector(".navbar-close");
const navbarOpen = document.querySelector(".navbar-open");
const navbar = document.querySelector(".navbar");
const mainMenu = document.querySelector(".main-menu");
const about = document.querySelector(".about");

navbarClose.addEventListener("click", () => {
  navbar.style.width = "0";
  navbar.style.background = "transparent";
  mainMenu.style.display = "none";
  about.style.display = "none";
  navbarClose.style.display = "none";
  navbarOpen.style.visibility = "visible";
});
navbarOpen.addEventListener("click", () => {
  navbar.style.width = null;
  navbar.style.background = null;
  mainMenu.style.display = null;
  about.style.display = null;
  navbarClose.style.display = null;
  navbarOpen.style.visibility = null;
});

