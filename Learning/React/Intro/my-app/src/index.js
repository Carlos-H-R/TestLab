import React, { createElement } from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

function Square(props){
  return (
    <button className='square' onClick={props.onClick}>
      {props.value}
    </button>
  );
}

class Board extends React.Component {
  renderSquare(i) {
    return (<Square 
      value={this.props.squares[i]} 
      onClick={() => this.props.onClick(i)}
      key = {i}
      />
    );
  }

  render(){
    let f = []

    for (let i=0; i<9; i+=3){
      let c = [];
      
      for (let j=i; j<(i+3); j++){
        c.push(this.renderSquare(j));
      }
      
      let b = [
      <div className='board-row' key={i}>
        {c}
      </div>
      ]

      f.push(b);
    }


    return (
      <div>
        {f}
      </div>
    );
  }
}

class Game extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      history: [{
        squares: Array(9).fill(null),
        lastMove: Array(2).fill(null),
      }],
      stepNumber: 0,
      xIsNext: true,
    };
  }

  historyButton(desc, move, step){
    let buttonstate = { fontWeight: 'normal'};

    if (this.state.stepNumber === move){
      buttonstate = { fontWeight: 'bold'}
    }
  
    return (
      <button 
      onClick={() => {this.jumpTo(move, step)}}
      style = { buttonstate } 
      >
      {desc}
    </button>
    );
  }

  handleClick(i) {
    const history = this.state.history.slice(0,this.state.stepNumber + 1);
    const current = history[history.length - 1];
    const squares = current.squares.slice();
    const row = Number.parseInt(i/3);
    const col = (i%3);
    if (calculatorWinner(squares) || squares[i]) {
      return;
    }

    squares[i] = this.state.xIsNext ? 'X' : 'O';
    this.setState({
      history: history.concat([{
        squares: squares,
        lastMove: [row+1,col+1],
      }]),
      stepNumber: history.length,
      xIsNext: !this.state.xIsNext
    });
  }

  jumpTo(step, last) {
    this.setState({
      currentMove: last.lastMove,
      stepNumber: step,
      xIsNext: (step % 2) === 0,
    })
  }

  render() {
    const history = this.state.history;
    const current = history[this.state.stepNumber];
    const winner  = calculatorWinner(current.squares);
    
    let last = 'Last move: none';
    if (current.lastMove[0]){
      last = 'Last move: (' +  current.lastMove + ')';
    }

    const moves = history.map((step, move) => {
      const desc = move ?
        'Go to move #' + move :
        'Go to the start';
      
      return(
        <li key = {move}
        >
          {this.historyButton(desc, move, step)}
        </li>
      );
    });
    
    let status;
    if (winner) {
      status = 'Winner: ' + winner;
    }
    else {
      status = 'Next player: ' + 
      (this.state.xIsNext ? 'X' : 'O');
    }

    return (
      <div className="game">
        <div className="game-board">
          <Board
            squares = {current.squares}
            onClick = {(i) => this.handleClick(i)}
          />
        </div>
        <div className="game-info">
          <div>{status}</div>
          <div>{last}</div>
          <ol>{moves}</ol>
        </div>
      </div>
    );
  }
}

function calculatorWinner(squares){
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (let i = 0; i < lines.length; i++) {
    if ((squares[lines[i][0]] === squares[lines[i][1]]) && 
        (squares[lines[i][0]] === squares[lines[i][2]])) {
          return (squares[lines[i][0]]);
        }
  }
  return null;
}



// ========================================

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Game />);
