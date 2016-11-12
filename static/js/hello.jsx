import React from 'react';
import ReactDOM from 'react-dom';
import LineExample from './line';

class Hello extends React.Component {
  render() {
    return <h1>Hello</h1>
  }
}

class App extends React.Component {
	render() {
		return (
				<LineExample />
		);
	}
}

ReactDOM.render(<App />, document.getElementById('app'));

