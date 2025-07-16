<!DOCTYPE html><html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vozol Жижи</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      background: linear-gradient(to bottom, #1a1a1a, #000000);
      color: white;
      font-family: 'Segoe UI', sans-serif;
      text-align: center;
      padding: 20px;
      overflow-x: hidden;
    }
    h1 {
      font-size: 2.5rem;
      margin-bottom: 20px;
      color: #ff4d4d;
      text-shadow: 0 0 10px #ff4d4d;
    }
    .login {
      max-width: 400px;
      margin: 0 auto 40px;
      background: #222;
      padding: 20px;
      border-radius: 12px;
    }
    input {
      width: 80%;
      padding: 10px;
      margin: 10px 0;
      border-radius: 8px;
      border: none;
    }
    button {
      padding: 10px 20px;
      background: #ff4d4d;
      color: white;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      margin-top: 10px;
    }
    .flavor {
      margin: 10px auto;
      padding: 10px;
      width: fit-content;
      background: rgba(255, 255, 255, 0.08);
      border-radius: 12px;
      cursor: pointer;
      transition: 0.3s;
    }
    .flavor:hover {
      background: rgba(255, 255, 255, 0.2);
    }
    .admin-panel {
      margin-top: 30px;
    }
    .snowflake {
      position: fixed;
      top: -10px;
      color: #fff;
      user-select: none;
      pointer-events: none;
      font-size: 16px;
      animation: fall linear infinite;
    }
    @keyframes fall {
      0% { transform: translateY(0); opacity: 1; }
      100% { transform: translateY(100vh); opacity: 0; }
    }
  </style>
</head>
<body>  <h1>🔥 Продажа жижи VOZOL</h1>  <div id="auth" class="login">
    <h2>Введите юзернейм телеграм и придумайте пароль</h2>
    <input id="username" type="text" placeholder="@username" />
    <input id="password" type="password" placeholder="Пароль" />
    <button onclick="login()">Войти</button>
  </div>  <div id="site" style="display:none;">
    <div id="flavors"></div>
    <p>Цена — <strong>10€</strong> за банку</p>
    <p>Контакт: <a href="https://t.me/duxcrime">@duxcrime</a></p>
  </div>  <div id="admin" class="admin-panel" style="display:none;">
    <h2>Админ панель</h2>
    <input id="newFlavor" type="text" placeholder="Добавить вкус (со смайликом)" />
    <button onclick="addFlavor()">Добавить</button>
    <ul id="flavorList"></ul>
  </div><audio id="vapeSound" src="48ae894c5a60281.mp3"></audio>

  <script>
    let users = JSON.parse(localStorage.getItem('users') || '{}');
    let flavors = JSON.parse(localStorage.getItem('flavors') || '[]');
    let currentUser = null;

    function renderFlavors() {
      const flavorDiv = document.getElementById("flavors");
      flavorDiv.innerHTML = '';
      flavors.forEach((flavor, index) => {
        const el = document.createElement("div");
        el.className = 'flavor';
        el.textContent = flavor;
        el.onclick = () => {
          document.getElementById("vapeSound").play();
        };
        flavorDiv.appendChild(el);
      });
    }

    function renderAdminList() {
      const list = document.getElementById("flavorList");
      list.innerHTML = '';
      flavors.forEach((flavor, index) => {
        const li = document.createElement("li");
        li.textContent = flavor;
        const delBtn = document.createElement("button");
        delBtn.textContent = '❌';
        delBtn.onclick = () => {
          flavors.splice(index, 1);
          localStorage.setItem('flavors', JSON.stringify(flavors));
          renderFlavors();
          renderAdminList();
        };
        li.appendChild(delBtn);
        list.appendChild(li);
      });
    }

    function addFlavor() {
      const input = document.getElementById("newFlavor");
      const value = input.value.trim();
      if (value) {
        flavors.push(value);
        localStorage.setItem('flavors', JSON.stringify(flavors));
        input.value = '';
        renderFlavors();
        renderAdminList();
      }
    }

    function login() {
      const u = document.getElementById("username").value;
      const p = document.getElementById("password").value;

      if (!u || !p) return alert("Введите все данные");

      if (u === "@duxcrime" && p === "duxcrime") {
        currentUser = u;
        document.getElementById("auth").style.display = 'none';
        document.getElementById("site").style.display = 'block';
        document.getElementById("admin").style.display = 'block';
        renderFlavors();
        renderAdminList();
      } else {
        if (!users[u]) {
          users[u] = p;
          localStorage.setItem('users', JSON.stringify(users));
        }
        currentUser = u;
        document.getElementById("auth").style.display = 'none';
        document.getElementById("site").style.display = 'block';
        renderFlavors();
      }
    }

    // Snowfall effect
    function createSnowflake() {
      const snowflake = document.createElement('div');
      snowflake.classList.add('snowflake');
      snowflake.textContent = '❄';
      snowflake.style.left = Math.random() * 100 + 'vw';
      snowflake.style.animationDuration = (Math.random() * 3 + 2) + 's';
      snowflake.style.fontSize = (Math.random() * 10 + 10) + 'px';
      document.body.appendChild(snowflake);
      setTimeout(() => snowflake.remove(), 5000);
    }
    setInterval(createSnowflake, 200);
  </script></body>
</html>
