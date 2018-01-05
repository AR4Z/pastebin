import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';


function json_pastebin(){
  const url = 'http://127.0.0.1:8000/';

  let data = {
    title: 'prueba desde react',
    text: 'esto es una prueba',
    time_expiration: '10 Minutos'
  }
  let my_headers = new Headers();
  let fetchData = {
    method: 'POST',
    body: data,
    headers: my_headers,
    mode:'no-cors'
  }
  console.log("mi fetch", fetchData);

  fetch(url, fetchData)
  .then(function(data_get){
    return data_get;
  })
  .catch(function(error){
    console.log(error);
  })
}


class App extends Component {
  constructor(props){
    super(props)
  }
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
          {console.log("peticion", json_pastebin())}
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
      </div>
    );
  }
}

export default App;
