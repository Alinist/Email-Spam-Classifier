document.addEventListener("DOMContentLoaded", function () {
  const mailsContainer = document.getElementById("mails");
  const contentContainer = document.getElementById("content");
  const predictionResult = document.getElementById("predictionResult");
  const validOption = document.getElementById("valid");
  const spamOption = document.getElementById("spam");
  const writeOption = document.getElementById("write");
  const spamcontainer = document.getElementById("spammails");
  const validContainers = document.getElementById("validmails");
  const options = document.querySelectorAll("#modelsSelect > option");
  const usedModelSpan = document.getElementById("usedModel");
  const predictionContainer = document.getElementById("predictContainer");

  options.forEach((option) => {
    if (option.value == usedModelSpan.innerHTML) {
      option.selected = true;
    }
  });
  if (predictionResult.textContent === "0") {
    predictionResult.innerHTML = "VAILD ✅";
    predictionContainer.style.backgroundColor = "#02864A";
  } else if (predictionResult.textContent === "1") {
    predictionResult.innerHTML = "SPAM ❌";
    predictionContainer.style.backgroundColor = "#E8083E";
  }

  validOption.addEventListener("click", () => {
    validContainers.style.display = "flex";
    spamcontainer.style.display = "none";
    contentContainer.style.display = "none";
    mailsContainer.style.display = "flex";
    spamOption.classList.remove("active");
    writeOption.classList.remove("active");
    validOption.classList.add("active");
    if (document.querySelectorAll("#validmails .mail").length === 0) {
      document.querySelector("#validmails h3").style.display = "initial";
    } else {
      document.querySelector("#validmails h3").style.display = "none";
    }
  });

  spamOption.addEventListener("click", () => {
    validContainers.style.display = "none";
    spamcontainer.style.display = "flex";
    contentContainer.style.display = "none";
    mailsContainer.style.display = "flex";
    writeOption.classList.remove("active");
    validOption.classList.remove("active");
    spamOption.classList.add("active");
    if (document.querySelectorAll("#spammails .mail").length === 0) {
      document.querySelector("#spammails h3").style.display = "initial";
    } else {
      document.querySelector("#spammails h3").style.display = "none";
    }
  });

  writeOption.addEventListener("click", () => {
    contentContainer.style.display = "flex";
    mailsContainer.style.display = "none";
    spamOption.classList.remove("active");
    validOption.classList.remove("active");
    writeOption.classList.add("active");
  });

  window.addEventListener("scroll", function () {
    document.getElementById("options").style.height = `${document.documentElement.scrollTop + 680}px`;
  });

  const vaildMails = document.querySelectorAll("#validmails span");
  for (let i = 0; i < vaildMails.length; i++) {
    vaildMails[i].innerHTML = i + 1;
  }

  const spamMails = document.querySelectorAll("#spammails span");
  for (let i = 0; i < spamMails.length; i++) {
    spamMails[i].innerHTML = i + 1;
  }

});
