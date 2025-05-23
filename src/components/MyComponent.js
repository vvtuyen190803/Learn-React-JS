import React from "react";
import AddUserInfor from "./AddUserInfor";
import DisplayInfor from "./DisplayInfor";

class MyComponent extends React.Component {
  state = {
    listUser: [
      { id: 1, name: "tata", age: "16" },
      { id: 2, name: "Tama", age: "26" },
      { id: 3, name: "TAMA", age: "69" },
    ],
  };

  handleAddNewUser = (userObj) => {
    this.setState({
      listUser: [...this.state.listUser, userObj],
    });
  };
  //JSX
  //dry: don't repeat youseft
  render() {
    return (
      <div>
        <AddUserInfor handleAddNewUser={this.handleAddNewUser} />
        <br></br>

        <DisplayInfor listUser={this.state.listUser} />
      </div>
    );
  }
}

export default MyComponent;
