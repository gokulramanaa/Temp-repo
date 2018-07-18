import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom';
import Layout from './hoc/Layout/Layout';
// import Tabledisplay from './components/TableDisplay';

class App extends Component {
  render () {
    return (
    	<BrowserRouter>
      <div>
        <Layout>
        </Layout>
      </div>
      </BrowserRouter>
    );
  }
}

export default App;