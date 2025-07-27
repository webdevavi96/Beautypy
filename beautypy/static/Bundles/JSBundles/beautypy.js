document.addEventListener("DOMContentLoaded", () => {
  
  //Navigation Mneu toggle
  const menuBtn = document.getElementById("hamburgerBtn");
  menuBtn.addEventListener("click", () => {
    document.getElementById("nav-menu").classList.toggle("hidden");
  });

  // Existing close buttons
  document.querySelectorAll("#closeBtn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const container = btn.closest(
        "div[role='alert'], .bg-blue-500, .bg-green-500, .bg-yellow-500, .bg-red-500"
      );
      if (container) container.remove();
    });
  });

  // Accordion toggle
  document.querySelectorAll("[id^='accordion-btn']").forEach((button) => {
    const panel = button.nextElementSibling;
    if (panel && panel.tagName.toLowerCase() === "div") {
      panel.style.display = "none";
      button.addEventListener("click", () => {
        panel.style.display = panel.style.display === "none" ? "block" : "none";
      });
    }
  });
});
