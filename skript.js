let isAdmin = false;
const username = prompt("Введите Telegram username:");
const password = prompt("Введите пароль:");

if (username === "@duxcrime" && password === "duxcrime") {
  isAdmin = true;
  document.getElementById("admin-panel").style.display = "block";
}

fetch("/api/juices")
  .then(res => res.json())
  .then(data => {
    const list = document.getElementById("juice-list");
    const admin = document.getElementById("juice-admin");
    list.innerHTML = "";
    admin.innerHTML = "";

    data.forEach(j => {
      const li = document.createElement("li");
      li.innerHTML = \`\${j.name} <span class="\${j.available ? 'available' : 'unavailable'}">\${j.available ? 'в наличии' : 'нет в наличии'}</span>\`;
      list.appendChild(li);

      if (isAdmin) {
        const div = document.createElement("div");
        div.innerHTML = \`
          <label>\${j.name}</label>
          <input type="checkbox" \${j.available ? "checked" : ""} onchange="toggleAvailability('\${j.name}', this.checked)" />
          <button onclick="deleteJuice('\${j.name}')">Удалить</button>
        \`;
        admin.appendChild(div);
      }
    });
  });

function toggleAvailability(name, state) {
  fetch("/api/update", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, available: state, admin_user: username, admin_pass: password })
  }).then(() => location.reload());
}

function addJuice() {
  const name = document.getElementById("new-juice").value;
  fetch("/api/add", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, admin_user: username, admin_pass: password })
  }).then(() => location.reload());
}

function deleteJuice(name) {
  fetch("/api/delete", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, admin_user: username, admin_pass: password })
  }).then(() => location.reload());
}
