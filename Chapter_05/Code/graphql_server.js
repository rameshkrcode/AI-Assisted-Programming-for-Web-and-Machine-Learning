
const { ApolloServer, gql } = require('apollo-server');
// Sample book data
const books = [
  { title: "The AI Revolution", author: "John Doe" },
  { title: "Machine Learning 101", author: "Jane Smith" }
];
// Define GraphQL Schema
const typeDefs = gql`
  type Book {
    title: String
    author: String
  }
  type Query {
    books: [Book]
  }
`;
// Resolver Functions
const resolvers = {
  Query: {
    books: () => books
  }
};
// Create GraphQL Server
const server = new ApolloServer({ typeDefs, resolvers });
server.listen().then(({ url }) => {
  console.log(`Server is running at ${url}`);
});
