import React, { Component } from 'react';
import Item from './Item'
import './App.css';

class App extends Component {

  constructor(props){
    super(props);
    this.state={
      items: [{id: 0, text: 'Home', color:'white'},
                {id: 1, text: 'About', color:'white'},
                {id: 2, text: 'Contact', color:'white'}]
    }
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick(prevId, id){
    let obj = this.state.items;
    var index = obj.findIndex ((item) => item.id == item.id)
    var indexPrev = obj.findIndex ((item) => item.id == item.prevId)
    console.log(index);
    console.log(indexPrev);
    obj[index].color = 'blue';
    obj[indexPrev].color = 'white';
    this.setState({ items: obj});
  }

  render() {
    return (
      <div>
        <label>Navigation Menu Bar </label>
      <ul>
      {
        this.state.items.map((item) => {
        return <Item item={item} key={item.id} id={item.id} text = {item.text} 
                  isClicked = {item.isClicked}
                  color = {item.color}
                  handleClick = {this.handleClick}/>
        })  
      }
      </ul>
      </div>
    );
  }
}

export default App;
