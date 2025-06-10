import React from "react";
import "./DisplayInfor.scss";
import logo from "./../logo.svg";

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
      <div className="display-infor-container">
        <img src={logo} alt="logo" />
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
            {listUser.map((user) => {
              return (
                <div
                  key={user.id}
                  className={+user.age > 18 ? "green" : "pink"}
                >
                  <div style={{ color: "yellow", paddingTop: "50px" }}>
                    My name is: {user.name}{" "}
                  </div>
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
