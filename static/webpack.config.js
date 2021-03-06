const webpack = require('webpack');
const config = {
    entry:  __dirname + '/js/index.jsx',
    output: {
        path: __dirname + '/dist',
        filename: 'bundle.js',
    },
    resolve: {
        extensions: [".js", ".jsx", ".css"],
        modules: [__dirname + '/node_modules'],
    },
    module: {
      rules: [
        {
          test:/\.js(x)$/,
          exclude: /node_modules/,
          use: [ 'babel-loader'],
        },
      ],
   }
};
module.exports = config;
