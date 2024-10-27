document.addEventListener("DOMContentLoaded", function () {
  const menuBtn = document.getElementById("menuBtn");
  const mobileMenu = document.getElementById("mobileMenu");
  const backBtn = document.getElementById("backBtn");

  menuBtn.addEventListener("click", (e) => {
    e.stopPropagation(); // Prevent event from bubbling up
    mobileMenu.classList.toggle("-translate-x-full");
  });

  backBtn.addEventListener("click", () => {
    window.history.back();
  });

  // Close menu when clicking outside
  document.addEventListener("click", (e) => {
    if (!mobileMenu.contains(e.target) && e.target !== menuBtn) {
      mobileMenu.classList.add("-translate-x-full");
    }
  });

  // Modal dialogs
  const modalDialog = document.querySelectorAll(".modal-dialog");

  function closeModalDialog() {
    const closeButtons = document.querySelectorAll(".btn-close-dialog");
    closeButtons.forEach((button) => {
      button.addEventListener("click", () => {
        modalDialog.forEach((dialog) => {
          dialog.style.display = "none";
        });
      });
    });
  }

  function openModalDialog() {
    const deleteButtons = document.querySelectorAll(".btn-delete");
    deleteButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const contentId = button.getAttribute("data-content-id");
        const type = button.getAttribute("data-type");
        modalDialog.forEach((dialog) => {
          dialog.style.display = "block";
          dialog.setAttribute("data-content-id", contentId);
          dialog.setAttribute("data-type", type);
        });
      });
    });
  }

  function confirmDeleteContentModalDialog() {
    const deleteContentButtons = document.querySelectorAll(
      ".btn-delete-content"
    );
    deleteContentButtons.forEach((button) => {
      button.addEventListener("click", async () => {
        const dialog = button.closest(".modal-dialog");
        const contentId = dialog.getAttribute("data-content-id");
        const type = dialog.getAttribute("data-type");
        if (!contentId) {
          return;
        }
        try {
          const response = await fetch(`/${type}/delete/${contentId}/`, {
            method: "DELETE",
            headers: {
              "Content-Type": "application/json",
              "X-CSRFToken": getCookie("csrftoken"),
            },
          });

          let data;
          const contentType = response.headers.get("content-type");
          if (contentType && contentType.indexOf("application/json") !== -1) {
            data = await response.json();
          } else {
            data = await response.text();
          }

          if (response.ok) {
            // Encontrar e remover o elemento da DOM após deletar com sucesso
            const contentElement = document.querySelector(
              `[data-content-item-id="${contentId}"]`
            );
            if (contentElement) {
              contentElement.remove();
            } else {
              console.warn(
                `Elemento com data-content-id="${contentId}" não encontrado.`
              );
            }
            // Fechar o modal
            if (dialog) {
              dialog.style.display = "none";
            }
            console.log(data.message || "Conteúdo deletado com sucesso");
          } else {
            throw new Error(
              data.error || data || "Falha ao deletar o conteúdo"
            );
          }
        } catch (error) {
          console.error("Erro ao deletar conteúdo:", error);
          alert(
            error.message ||
              "Ocorreu um erro ao tentar deletar o conteúdo. Por favor, tente novamente."
          );
        }
      });
    });

    const joinWorkshopBtn = document.querySelectorAll(".btn-join-workshop");
    joinWorkshopBtn.forEach((button) => {
      button.addEventListener("click", async () => {
        const workshopId = button.getAttribute("data-content-id");
        try {
          const response = await fetch(`/workshop/join/${workshopId}/`, {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "X-CSRFToken": getCookie("csrftoken"),
            },
          });
          if (response.ok) {
            console.log("Inscrição no workshop realizada com sucesso");
            window.location.reload();
          } else {
            throw new Error("Falha ao inscrever no workshop");
          }
        } catch (error) {
          console.error("Erro ao inscrever no workshop:", error);
          alert(
            error.message ||
              "Ocorreu um erro ao tentar inscrever no workshop. Por favor, tente novamente."
          );
        }
      });
    });
  }

  const favoriteWorkshopBtn = document.querySelectorAll(".btn-favorite");
  favoriteWorkshopBtn.forEach((button) => {
    button.addEventListener("click", async () => {
      const workshopId = button.getAttribute("data-content-id");
      try {
        const response = await fetch(`/favorites/add/${workshopId}/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken"),
          },
        });
        if (response.ok) {
          console.log("Workshop favoritado com sucesso");
          window.location.reload();
        } else {
          throw new Error("Falha ao favoritar workshop");
        }
      } catch (error) {
        console.error("Erro ao favoritar workshop:", error);
        alert(
          error.message ||
            "Ocorreu um erro ao tentar favoritar o workshop. Por favor, tente novamente."
        );
      }
    });
  });

  const completeLessonBtn = document.querySelectorAll(".btn-complete-lesson");
  completeLessonBtn.forEach((button) => {
    button.addEventListener("click", async () => {
      const lessonId = button.getAttribute("data-content-id");
      const workshopId = button.getAttribute("data-workshop-id");
      try {
        const response = await fetch(
          `/lesson/complete/${workshopId}/${lessonId}/`,
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              "X-CSRFToken": getCookie("csrftoken"),
            },
          }
        );
        if (response.ok) {
          console.log("Aula concluída com sucesso");
          window.location.reload();
        } else {
          throw new Error("Falha ao concluir aula");
        }
      } catch (error) {
        console.error("Erro ao concluir aula:", error);
        alert(
          error.message ||
            "Ocorreu um erro ao tentar concluir a aula. Por favor, tente novamente."
        );
      }
    });
  });

  // Função auxiliar para obter o valor do cookie CSRF
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  // Add this new function to hide messages with animation
  function hideMessages() {
    const messagesDiv = document.querySelector(".messages");
    if (messagesDiv) {
      setTimeout(() => {
        messagesDiv.style.transition = "opacity 1s ease-out";
        messagesDiv.style.opacity = "0";
        setTimeout(() => {
          messagesDiv.style.display = "none";
        }, 1000);
      }, 5000);
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    const zipCodeInput = document.getElementById("id_zipcode");
    const streetInput = document.getElementById("id_street");
    const neighborhoodInput = document.getElementById("id_neighborhood");
    const cityInput = document.getElementById("id_city");
    const stateInput = document.getElementById("id_state");

    if (zipCodeInput) {
      zipCodeInput.addEventListener("blur", function () {
        const zipCode = zipCodeInput.value.replace(/\D/g, "");
        if (zipCode.length === 8) {
          fetch(`https://viacep.com.br/ws/${zipCode}/json/`)
            .then((response) => response.json())
            .then((data) => {
              if (!data.erro) {
                if (streetInput) streetInput.value = data.logradouro;
                if (neighborhoodInput) neighborhoodInput.value = data.bairro;
                if (cityInput) cityInput.value = data.localidade;
                if (stateInput) stateInput.value = data.uf;
              }
              id_number.focus();
            })
            .catch((error) => console.error("Erro ao buscar CEP:", error));
        }
      });
    } else {
      console.error("Campo de CEP não encontrado");
    }
  });

  // Call the function to hide messages
  hideMessages();

  openModalDialog();
  closeModalDialog();
  confirmDeleteContentModalDialog();
});
