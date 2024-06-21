import weaviate from 'weaviate-client';
import rlSync from 'readline-sync';


let client;

async function createCollection() {
  const questions = await client.collections.create({
    name: 'Question',
    vectorizers: [
      weaviate.configure.vectorizer.text2VecOllama({
        name: 'title_vector',
        sourceProperties: ['title'],
        apiEndpoint: 'http://host.docker.internal:11434',
        model: "all-minilm",
      })
    ]
  })
  console.log(`Collection ${questions.name} created!`);
}

async function getJsonData() {
  const file = await fetch('https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json');
  return file.json();
}

async function importQuestions() {
  // Get the questions directly from the URL
  const questions = client.collections.get('Question');
  const data = await getJsonData();
  const result = await questions.data.insertMany(data)
  console.log('We just bulk inserted', result);
}

async function nearTextQuery(queryStr) {
  const questions = client.collections.get('Question');

  const result = await questions.query.nearText(queryStr, {
    limit: 3
  });

  for (let object of result.objects) {
    console.log(JSON.stringify(object.properties, null, 2));
  }

  return result;
}
async function main() {
  //   const client = await weaviate.connectToWeaviateCloud(
  //     'http://localhost:8080',
  //   );
  client = await weaviate.connectToLocal();
  // await createCollection();
  // await importQuestions();
  let userInput = '';

  while (userInput !== 'quit') {
    userInput = rlSync.question('Enter a query string:');
    await nearTextQuery(userInput);
  }
};

main();
