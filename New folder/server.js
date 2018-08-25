const express = require('express');
const mysql = require('mysql');

const app = express();
const port = process.env.PORT || 5000;

var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password: "Manoj@13",
  database : 'sys'
});

app.get('/SST-GX', (req, res) => {
  // res.send({ express: 'Hello From Gokul' });
  connection.query('select * from metrics', (error, results,fields) =>{
      if (error) throw error;
      res.send(JSON.stringify([results,fields]));
  });
});

app.get('/SST', (req, res) => {
  // res.send({ express: 'Hello From Gokul' });
  connection.query('select * from host_summary', (error, results,fields) =>{
      if (error) throw error;
      res.send(JSON.stringify([results,fields]));
  });
});

app.get('/SST-PAM', (req, res) => {
  // res.send({ express: 'Hello From Gokul' });
  connection.query('show tables', (error, results,fields) =>{
      if (error) throw error;
      res.send(JSON.stringify([results,fields]));
  });
});



app.listen(port, () => console.log(`Listening on port ${port}`));
