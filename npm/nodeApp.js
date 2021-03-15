const express = require('express')
const app = express();
const http = require('http').createServer(app);

app.use('/ressources', express.static('static'))
app.use('/cluster', express.static('node_modules/leaflet.markercluster/dist'))

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/static/carte.html');
});

http.listen(10042, () => {
    console.log('listening on *:10042');
});
