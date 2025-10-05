// Datos de juegos (ejemplo)
const juegos = [
  {
    id: 1,
    nombre: "Fantasy Realm",
    imagen: "https://via.placeholder.com/200x180/333/fff?text=Fantasy+Realm",
    categorias: ["Fantasía", "RPGM", "Protagonista masculino"]
  },
  {
    id: 2,
    nombre: "Dark School",
    imagen: "https://via.placeholder.com/200x180/444/fff?text=Dark+School",
    categorias: ["Escolar", "Corrupción", "2D"]
  },
  {
    id: 3,
    nombre: "Alien Desire",
    imagen: "https://via.placeholder.com/200x180/222/ff66aa?text=Alien+Desire",
    categorias: ["Ciencia ficción", "Interracial", "Furry"]
  },
  {
    id: 4,
    nombre: "Queen's Slave",
    imagen: "https://via.placeholder.com/200x180/111/ffcc00?text=Queen%27s+Slave",
    categorias: ["Dominación femenina", "Esclavo", "Bdsm"]
  },
  {
    id: 5,
    nombre: "Family Secrets",
    imagen: "https://via.placeholder.com/200x180/555/ff9999?text=Family+Secrets",
    categorias: ["Incesto", "Romance", "Drama"]
  }
];

let categoriaActual = 'todas';

// Renderizar juegos
function renderJuegos(lista) {
  const container = document.getElementById('gamesContainer');
  container.innerHTML = '';
  lista.forEach(juego => {
    const card = document.createElement('div');
    card.className = 'game-card';
    card.innerHTML = `
      <img src="${juego.imagen}" alt="${juego.nombre}">
      <div class="title">${juego.nombre}</div>
    `;
    card.addEventListener('click', () => {
      window.location.href = `juego.html?id=${juego.id}`;
    });
    container.appendChild(card);
  });
}

// Filtrar por búsqueda y categoría
function filtrarJuegos() {
  const query = document.getElementById('searchInput').value.toLowerCase();
  let filtrados = juegos;

  // Filtrar por categoría
  if (categoriaActual !== 'todas') {
    filtrados = filtrados.filter(juego =>
      juego.categorias.includes(categoriaActual)
    );
  }

  // Filtrar por búsqueda
  filtrados = filtrados.filter(juego =>
    juego.nombre.toLowerCase().includes(query) ||
    juego.categorias.some(cat => cat.toLowerCase().includes(query))
  );

  renderJuegos(filtrados);
}

// Eventos de búsqueda
document.getElementById('searchInput').addEventListener('input', filtrarJuegos);

// Eventos de botones de categoría
document.querySelectorAll('.cat-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    // Quitar clase 'active' de todos
    document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
    // Agregar a este
    btn.classList.add('active');
    // Actualizar filtro
    categoriaActual = btn.dataset.category;
    filtrarJuegos();
  });
});

// Cargar todos los juegos al inicio
renderJuegos(juegos);