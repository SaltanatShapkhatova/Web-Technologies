import React, { Component } from 'react';

class Item extends Component {

  constructor(props){
    super(props);
    this.state={
      prevId: null,
      isToggle: false,
      color: ''
    }
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick(id){
    this.setState({
      isToggle: !this.state.isToggle
    });
    if(this.state.prevId != null){
      if(this.state.prevId != id){
        this.props.handleClick(this.state.prevId, id);
      }
    }
    this.setState({prevId: id});
  }

  render() {

    return (
      <div>
        <button onClick={(e)=> this.handleClick(this.props.id) }
                style={{backgroundColor:this.state.isToggle ? 'blue' : 'white'}}>
                {this.props.text}</button>
      </div>
    );
  }
}

export default Item;
