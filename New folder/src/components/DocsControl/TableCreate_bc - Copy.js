import React, { Component } from 'react';


class TableCreate extends Component {

  constructor(props) {
      super(props);
      this.state = {
        // ...props,
        clicked: false,
        clickedli:[]
      };
      this.clickmarker = this.clickmarker.bind(this);
    }


   clickmarker(event, index) {
    console.log(index)
    if (this.state.clicked){
      console.log("clicked again");
      // let array = [...this.state.clickedli];
      // let ind = array.indexOf(index);
      // array.splice(ind,1);
      this.props.clickappend("R", index)
      // this.setState({clicked: !this.state.clicked, clickedli: array});
      }
    else{
      console.log("clicked new")
      this.props.clickappend("A", index)
      this.setState({clicked: !this.state.clicked, clickedli:[...this.state.clickedli, index]})
      }
    };

  render(){
      const index = this.props.rid
      // console.log(this.state.clickedli);
      let rowd = null;
      const rowda = this.props.rowdata;
      rowd = this.props.coln.map((number,id) =>{
        if (number!=="index"){
            return(
              <td key={id}>{eval("rowda." + number)}</td>
            );
        }
      
    });

      if (this.state.clicked){
        rowd.push(
        <td
            key={this.props.coln.length}
            id={this.props.coln.length}
            onClick = {(event)=>this.clickmarker(event, this.props.rid)}> &#10004; </td>
          );
      }
      else{
        rowd.push(
        <td
            key={this.props.coln.length}
            id={this.props.coln.length}
            onClick = {(event)=>this.clickmarker(event, this.props.rid)}></td>
    );
      }

    
    return(
      <tr 
        key={this.props.rid}>
        {rowd}</tr>
    );
    }
}

export default TableCreate;
