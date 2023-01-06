// import { keyboard } from '@testing-library/user-event/dist/keyboard';
import { tab } from '@testing-library/user-event/dist/tab';
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

class ButtonKey extends React.Component {
  render() {
    return(
      <button className="button-key" /*onClick={this.props.onClick}*/>
        {this.props.content}
      </button>
    )
  }
}

class Screen extends React.Component {
  render() {
    return (
      <div className='content-screen'>
        {this.props.content}
      </div>
    )
  }
}

class Keyboard extends React.Component {
  renderNumberKey(i) {
    return(
      <ButtonKey
        content={i}
        // onClick={() => numberClick()}
      />
    )
  }

  render() {
    let table = [];
    for (let i=1; i<10; i+=3) {
      let row = []
      for (let j=i; j<(i+3); j++){
        row.push(this.renderNumberKey(j));
      }
      table.push(
        <div className='keyboard-row' key={i}>
          {row}
        </div>
      );
    }
    table.reverse();

    let row = []
    row.push(this.renderNumberKey(0))
    row.push(<ButtonKey content={','}/>)
    row.push(<ButtonKey content={'='}/>)
    table.push(<div classname='keyboard-row' key={0}>{row}</div>)

    return(
      <div className='calculator'>
        <Screen content={'Rebooting...'}/>
        <div className='keyboard'>
          <div className='number-pad'>
            {table}
          </div>
          <div className='operation-col'>
            <ButtonKey content={'÷'}/>
            <ButtonKey content={'x'}/>
            <ButtonKey content={'-'}/>
            <ButtonKey content={'+'}/>
          </div>
        </div>
      </div>
    )
  }
}

const test = <Keyboard />

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  test
);
