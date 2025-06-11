import React from "react";
import AddUserInfor from "./AddUserInfor";
import DisplayInfor from "./DisplayInfor";

class MyComponent extends React.Component {
  state = {
    listUser: [
      { id: 1, name: "tata", age: "12" },
      { id: 2, name: "Tama", age: "26" },
      { id: 3, name: "TAMA", age: "69" },
    ],
  };

  handleAddNewUser = (userObj) => {
    this.setState({
      listUser: [userObj, ...this.state.listUser],
    });
  };

  handleDeleteUser = (userId) => {
    let listUserClone = this.state.listUser;
    listUserClone = listUserClone.filter((item) => item.id !== userId);
    this.setState({
      listUser: listUserClone,
    });
  };
  //JSX
  //dry: don't repeat youseft
  render() {
    return (
      <>
        <div className="a">
          <AddUserInfor handleAddNewUser={this.handleAddNewUser} />
          <br></br>

          <DisplayInfor
            listUser={this.state.listUser}
            handleDeleteUser={this.handleDeleteUser}
          />
        </div>
        <div className="b"></div>
      </>
    );
  }
}

export default MyComponent;
