const express = require('express');
const routes = require('./routes');
const { handleError } = require('./Helpers/error')

require('./database');

const app = express();

app.use(express.json());
app.use(routes);

app.use((err, req, res, next) => {
    handleError(err, res);
});

app.listen(3333);