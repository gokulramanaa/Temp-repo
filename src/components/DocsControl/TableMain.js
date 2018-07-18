import React from 'react';
import TabelCreate from './TableCreate';
import classes from './TableMain.css';

const tablemain =(props)=> {

  const tableheader = props.columN.map((number,indi) => {
    return (<th 
        key={indi}
        id={indi}>{number}</th>
    );
  });

  return(
    <table className={classes.TableMain} border="1">
      <tbody>
        <tr className = {classes.Header}>
          {tableheader}
        </tr>
        {/* {console.log(props.mdata)} */}
        {props.mdata.map((member,id) =>
          <TabelCreate rowdata = {member} key = {id} rid = {id} coln = {props.columN}/>
        )}
      </tbody>
    </table>
  );
};

export default tablemain;


// import React from 'react';
// import TabelCreate from './TableCreate';
// import './UserInput.css';

// const tablemain =(props) => {
//     let tableheader = null;
//     tableheader = props.columN.map((number,indi) =>{
//         if (number!=="index"){
//             return(
//               <th key={indi}>{number}</th>
//         );}
//             return null
//           })

//     tableheader.push(
//           <td
//           key={props.columN.length}
//           id={props.columN.length} > Correct Rows 
//           </td>
//         );

//     let tablerow = null;
//     tablerow = props.mdata.map((member,id) => {
//               return (
//                           <TabelCreate
//                           rowdata = {member}
//                           key = {id} rid = {member.index}
//                           coln = {props.columN}
//                           clickappend = {(event,id) => props.click(event,id)} 
//                           index = {props.index}  /> );
//           })

//     return(
//           <table className="TableMain" border="1">
//           <tbody>
//           <tr>
//           {tableheader}
//           </tr>
//           {tablerow}
//           </tbody>
//           </table>
//     );
// };

// export default tablemain;