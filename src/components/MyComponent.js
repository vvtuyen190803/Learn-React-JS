import React from "react";
import UserInfor from "./UserInfor";
import DisplayInfor from "./DisplayInfor";

class MyComponent extends React.Component {
  state = {
    listUser: [
      { id: 1, name: "tata", age: "90" },
      { id: 2, name: "Tama", age: "80" },
      { id: 3, name: "TAMA", age: "69" },
    ],
  };
  //JSX
  //dry: don't repeat youseft
  render() {
    return (
      <div>
        <UserInfor />
        <br></br>

        <DisplayInfor listUser={this.state.listUser} />
      </div>
    );
  }
}

export default MyComponent;
