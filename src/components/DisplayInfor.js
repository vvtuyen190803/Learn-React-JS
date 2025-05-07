import React from "react";

class DisplayInfor extends React.Component {
  state = {
    isShowListUser: true,
  };
  handleShowHide = () => {
    this.setState({
      isShowListUser: !this.state.isShowListUser,
    });
  };
  render() {
    const { listUser } = this.props;
    console.log(listUser);

    //props => properties
    return (
      <div>
        <div>
          <span
            onClick={() => {
              this.handleShowHide();
            }}
          >
             {this.state.isShowListUser === true
              ? "Hide List User"
              : "Show List User"}
          </span>
        </div>
        {this.state.isShowListUser && (
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
                <div key={user.id} className={+user.age > 18 ? "green" : "red"}>
                  <div>My name is: {user.name} </div>
                  <div>My age is: {user.age}</div>
                  <hr />
                </div>
              );
            })}
          </div>
        )}
      </div>
    );
  }
}

export default DisplayInfor;
