import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import {TweetsComponent} from './tweets'
import * as serviceWorker from './serviceWorker';

const appEl = document.getElementById('root')
if (appEl) {
  ReactDOM.render(<App />, appEl
  );
}

const TweetsEl = document.getElementById('news')
if (TweetsEl) {
  ReactDOM.render(<TweetsComponent />, TweetsEl
  );
}

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
