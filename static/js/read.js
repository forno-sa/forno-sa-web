import React from 'react';
import ReactDOM from 'react-dom';
import customData from './data.json';

class Iread extends React.Component {
  render() {
    $.getJSON("data.json", function(json) {
    console.log(json);
	});
  }
}

ReactDOM.render(<Iread />, document.getElementById('iread'));