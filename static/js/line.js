import React from 'react';
import {Line} from 'react-chartjs-2';

const data = {
  datasets: [
    {
      label: 'My First dataset',
      data: [{
          'x': -10,
          'y': 0
      }, {
          'x': 0,
          'y': 10
      }, {
          'x': 10,
          'y': 5
      },
      ]
    }
  ]
};

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
