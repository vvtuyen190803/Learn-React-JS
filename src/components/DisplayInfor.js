import React from "react";

class DisplayInfor extends React.Component {
  render() {
    const { listUser } = this.props;
    console.log(listUser);
    //props => properties
    return (
      <div>
        {/* <div>My name is: {name}</div>
        <div>My age is: {age} </div>
        <hr></hr>
        <div>My name is: {name}</div>
        <div>My age is: {age} </div>
        <hr></hr>
        <div>My name is: {name}</div>
        <div>My age is: {age} </div> */}

        {listUser.map((user) => {
          return (
            <div key={user.id}>
              <div>My name is: {user.name} </div>
              <div>My age is: {user.age}</div>
              <hr />
            </div>
          );
        })}
      </div>
    );
  }
}

export default DisplayInfor;
