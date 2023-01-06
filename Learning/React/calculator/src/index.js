import { keyboard } from '@testing-library/user-event/dist/keyboard';
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

function sum(x,y) {
  return (x+y);
}

function sub(x,y) {
  return (x-y);
}

function mlt(x,y) {
  return (x*y);
}

function div(x,y) {
  if (y !== 0){
    return (x/y);
  }
}

class NumberKey extends React.Component {
  render() {
    return(
      <button className='number-key' onClick={this.props.onClick}>
        {this.props.content}
      </button>
    )
  }
}

class OperationKey extends React.Component {
  render () {
    return (
      <button className='operation-key' onClick={this.props.onClick}>
        {this.props.content}
      </button>
    )
  }
}

class Keyboard extends React.Component {
  renderNumberKeys(i) {
    return (
      <NumberKey 
        content={i}
        onClick={() => this.props.numberClick(i)}
        key={i}
      />
    );
  }

  renderOperationKey(i) {
    return (
      <OperationKey
        content={i}
        onClick={() => this.props.operationClick(i)}
      />
    )
  }
  
  render(){
    return(
      <div className='keyboard'>
        <div className='keyboard-row'>
          {this.renderNumberKeys(7)}
          {this.renderNumberKeys(8)}
          {this.renderNumberKeys(9)}
          {this.renderOperationKey('÷')}
        </div>
        <div className='keyboard-row'>
          {this.renderNumberKeys(4)}
          {this.renderNumberKeys(5)}
          {this.renderNumberKeys(6)}
          {this.renderOperationKey('x')}
        </div>
        <div className='keyboard-row'>
          {this.renderNumberKeys(1)}
          {this.renderNumberKeys(2)}
          {this.renderNumberKeys(3)}
          {this.renderOperationKey('-')}
        </div>
        <div className='keyboard-row'>
          {this.renderNumberKeys(0)}
          {this.renderOperationKey(',')}
          <OperationKey
            content={'='}
            onClick={this.props.equalClick('=')}
          />
          {this.renderOperationKey('+')}
        </div>
      </div>
    )
  }
}

class Calculator extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      x: '',
      y: '',
      op: '',
    };
  }

  numberClick(i){
    if (this.state.op === '') {
        const aux = this.state.x;
        this.setState({
          x: (aux+i.toString()),
        })
    }

    else{
      const aux = this.state.y;
      this.setState({
        y: (aux + i.toString()),
      })
    }
  }

  operationClick(i){
    this.setState({
      op: (' '+i+' '),
    })
  }

  equalClick(i){
    let result = '';
    if ((this.state.y !== '')){
      const a = Number.parseFloat(this.state.x);
      const b = Number.parseFloat(this.state.y);

      if (this.state.op === ' + '){
        result = sum(a,b);
      }

      else if (this.state.op === ' - '){
        result = sub(a,b);
      }

      else if (this.state.op === ' x '){
        result = mlt(a,b);
      }

      else if (this.state.op === ' ÷ '){
        result = div(a,b);
      }
    }
    // this.changeState(result);
  }
  
  changeState(value){
    this.setState({
      x: value.toString(),
      op: '',
      y: ''
    })
  }

  render() {
    console.log(this.state);
    const show = [this.state.x, this.state.op, this.state.y];

    return (
      <div>
        <div className='screen'>
          {show}
        </div>
        <Keyboard
          numberClick={i => this.numberClick(i)}
          operationClick={i => this.operationClick(i)}
          equalClick={i => this.equalClick()}
        />
      </div>
    );
  }
}

const test = <Calculator />

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  test
);
