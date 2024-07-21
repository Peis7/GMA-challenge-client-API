print("Running mongo-init.js script");
db.createCollection("clients");

const data = cat('/test-data/clients.json');

// Parse the JSON data
const jsonData = JSON.parse(data);

// Insert the JSON data into the collection
db.clients.insertMany(jsonData);
