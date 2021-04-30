const express = require('express');
const app = express();
const fs = require('fs');
const http = require('http').createServer(app);

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use('/ressources', express.static('static'))
app.use('/cluster', express.static('node_modules/leaflet.markercluster/dist'))
app.use('/leafletui', express.static('node_modules/ui-leaflet/dist'))
app.use('/angular', express.static('node_modules/angular-simple-logger/dist'))
app.use('/angular-md', express.static('node_modules/angular-material'))
app.use('/angular-an', express.static('node_modules/angular-animate'))
app.use('/angular-ar', express.static('node_modules/angular-aria'))
app.use('/angular-sa', express.static('node_modules/angular-sanitize'))
app.use('/angular-ro', express.static('node_modules/angular-ui-router/release'))

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/static/carte.html');
});

app.post('/',function (req, res){
    fs.writeFileSync('static/review.json', JSON.stringify(req.body));
});

http.listen(10042, () => {
    console.log('listening on *:10042');
});
