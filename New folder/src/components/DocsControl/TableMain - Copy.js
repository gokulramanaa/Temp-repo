import React, { Component } from 'react';
import TabelCreate from './TableCreate_bc';

import './UserInput.css';


class TableMain extends Component {

  constructor(){
    super();
    this.state = {
      ...this.props,
      test:false
      // indexcol = this.props.mdata.
    };
  }

  clickappend (event, index){
    // this.setState({test:!test, clickli:[...this.state.clickli, index]})
    // this.setState({clickedli:[...this.state.clickedli, index]})
    console.log("calling back", index);
  }

  render(){
    console.log("test", this.state.mdata);
    let tableheader = null;
      tableheader = this.props.columN.map((number,indi) =>{
        if (number!=="index"){
            return(
              <th key={indi}>{number}</th>
            );
        }
      
    });

    console.log(tableheader);

    tableheader.push(
          <td
              key={this.props.columN.length}
              id={this.props.columN.length} > Correct Rows 
          </td>
        );

    let tablerow = null;
    tablerow = this.props.mdata.map((member,id) => {
              return (
                          <TabelCreate
                          rowdata = {member}
                          key = {id} rid = {member.index}
                          coln = {this.props.columN}
                          clickappend = {(event,id) => this.props.click(event,id)} 
                          index = {this.props.index}  /> );
          })

      return(
          <table className="TableMain" border="1">
            <tbody>
              <tr>
                {tableheader}
              </tr>
              {tablerow}
            </tbody>
          </table>
    );

    }

  

}

export default TableMain;
