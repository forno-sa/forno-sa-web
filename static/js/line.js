import React from 'react';
import {Line} from 'react-chartjs-2';

// var chartdata = JSON.parse("data.json");
var data;

var oReq = new XMLHttpRequest();
oReq.onload = reqListener;
oReq.open("get", "data.json", true);
oReq.send();

function reqListener(e) {
    data = JSON.parse(this.responseText);
    console.log(data);
}


const datav = {
  datasets: [
    {
      label: 'My First dataset',
      datav: [data
      ]
    }
  ]
};

// $.getJSON("data.json", function(json) {
//     console.log(json);
// });

const option = {
    scales: {
        xAxes: [{
            type: 'linear',
            position: 'bottom'
        }]
    }
};

export default React.createClass({
    displayName: 'LineExample',

    render() {
        return (
        <Line data={data} options={option} />
    );
  }
});
