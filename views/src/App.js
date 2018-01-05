import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';


function enviarInfo() {
  let data = {
    title: 'Desde react',
    text: 'probando',
    time_expiration: 'Un mes'
  }
  let datajson = JSON.stringify(data)
  fetch('http://localhost:8000/', {
  method: 'POST',
  body: datajson
  })
  .then(res => res.json())
  .then(res => console.log(res));
}




class App extends Component {
  constructor(props){
    super(props)
    this.state = { items: {} };
  }

  componentDidMount() {
    var root = 'http://localhost:8000';
    fetch(root + '/5a4feb6fb0a2dd217e669497', {method:'POST'})
    .then(response => response.json())
    .then(function(data){
      this.setState({items:data["paste"]});
    }.bind(this));
  }


  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">sws</h1>
            {enviarInfo()}
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.

        </p>
      </div>
    );
  }
}

export default App;
