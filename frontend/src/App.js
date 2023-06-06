import React, { useEffect, useState } from 'react';

function App() {
  const [nomes, setNomes] = useState([]);

  useEffect(() => {
    fetch('/nomes')
      .then(response => response.json())
      .then(data => setNomes(data));
  }, []);

  const handleSubmit = (event) => {
    event.preventDefault();
    const nome = event.target.nome.value;

    fetch('/nomes', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ nome }),
    })
      .then(response => response.json())
      .then(() => {
        fetch('/nomes')
          .then(response => response.json())
          .then(data => setNomes(data));
      });

    event.target.reset();
  };

  return (
    <div className="container">
      <h1>Inserir Nomes</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" name="nome" placeholder="Digite um nome" required />
        <button type="submit">Adicionar</button>
      </form>
      <ul>
        {nomes.map((nome, index) => (
          <li key={index}>{nome.nome}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;

