import "./App.scss";
import React from "react";
import MyComponent from "./components/MyComponent";

class App extends React.Component {
  render() {
    return (
      <div className="app-container">
        Hello World
        <MyComponent />
      </div>
    );
  }
}

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>Hello World! This is a simple React application.</p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

export default App;
