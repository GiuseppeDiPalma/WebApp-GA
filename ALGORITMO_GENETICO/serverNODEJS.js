var express = require("express");
var bodyParser = require("body-parser");

var app = express();
var jsonParser = bodyParser.json();
var urlencodedParser = bodyParser.urlencoded({ extended: false });

const fs = require('fs');
var obj = {
	table: []
};
let prova;
let nomeFileJson = 'dati.json'
console.log("Server in esecuzione");
app.post("/", urlencodedParser, function(request, response) {	
	console.log(request.body); //This prints the JSON document received (if it is a JSON document)
	// prova = JSON.stringify(request.body);
	fs.writeFile(nomeFileJson, JSON.stringify(request.body));
	
////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////
	const exec = require('child_process').exec;
	var yourscript = exec('sh eseguiCodice.sh',
        (error, stdout, stderr) => {
            console.log(`${stdout}`);
            console.log(`${stderr}`);
            if (error !== null) {
                console.log(`exec error: ${error}`);
            }
		});
////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////		
});

//Start the server and make it listen for connections on port 8080
app.listen(8081);


//come aggiungere questi dati ad un file .json
//impostare algoritmo da file json
// inviare risultati all'applicazione