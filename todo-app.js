const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let todos = [];

rl.question("What would you like to do? (add/list/quit)", answer => {
  if (answer === "add") {
    rl.question("Enter a todo:", todo => {
      todos.push(todo);
      console.log(`Added "${todo}" to your todo list`);
      rl.close();
    });
  } else if (answer === "list") {
    console.log("Your todos:");
    todos.forEach((todo, index) => {
      console.log(`${index + 1}. ${todo}`);
    });
    rl.close();
  } else if (answer === "quit") {
    console.log("Goodbye!");
    rl.close();
  } else {
    console.log("Invalid command, try again");
    rl.close();
  }
});
