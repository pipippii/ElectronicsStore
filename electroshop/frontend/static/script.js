fetch('http://localhost:5000/api/products')
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById('products');
    data.forEach(p => {
      const div = document.createElement('div');
      div.innerHTML = `<h2>${p.name}</h2><p>${p.price} ₽</p>`;
      container.appendChild(div);
    });
  });
