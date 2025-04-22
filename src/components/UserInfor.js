import React from "react";

class UserInfor extends React.Component {
  state = {
    name: "Tuyen Vu",
    address: "Nam Dinh",
    age: 22,
  };
  handleClick = (event) => {
    console.log("Click me");
    console.log("My name is: ", this.state.name);
    this.setState({
      name: "Tuyen",
      age: Math.floor(Math.random() * 100 + 1),
    });

    //   this.setState({
    //     age: Math.floor(Math.random() * 100 + 1),
    //   });
    // };
  };

  handleOnchangeInput = (event) => {
    this.setState({
      name: event.target.value,
    });
  };

  handleOnchangeAge = (event) => {
    this.setState({
      age: event.target.value,
    });
  };

  handleOnSubmit = (event) => {
    event.preventDefault();
    console.log(this.state);
  };
  render() {
    return (
      <div>
        My Name is:
        {this.state.name} and I'm {this.state.age}
        <form onSubmit={(event) => this.handleOnSubmit(event)}>
          <label>Your name:</label>
          <input
            value={this.state.name}
            type="text"
            onChange={(event) => {
              this.handleOnchangeInput(event);
            }}
          />
          <br></br>
          <label>Your age:</label>
          <input
            value={this.state.age}
            type="text"
            onChange={(event) => {
              this.handleOnchangeAge(event);
            }}
          />
          <button>Submit</button>
        </form>
      </div>
    );
  }
}
export default UserInfor;
