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
          const response = await fetch(`/api/${type}/${contentId}/`, {
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
          const response = await fetch(`/api/join-workshop/${workshopId}/`, {
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

  openModalDialog();
  closeModalDialog();
  confirmDeleteContentModalDialog();
});
