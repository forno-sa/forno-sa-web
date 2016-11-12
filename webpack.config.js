var path = require('path');
var webpack = require('webpack');
 
module.exports = {
    entry: './static/main.js',
    output: { path: './static/js/', filename: 'bundle.js' },
  module: {
    loaders: [
      {
        test: /.jsx?$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        query: {
          presets: ['es2015', 'react']
        }
      }
    ]
  },
};
