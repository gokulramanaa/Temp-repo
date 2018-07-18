import React from 'react';

const tablecreate =(props)=> {

const rowd = props.coln.map((number,indi) => {
	// console.log("check",props.rowdata[number]);
  return (<td
      key={indi}
      id={indi}>{props.rowdata[number]}</td>
  );
});
  return(
    <tr key={props.rid}>
      {rowd}
    </tr>);
};

export default tablecreate;



// import React from 'react';


// const tablecreate =(props) => {
//       let rowd = null;
//       const rowda = props.rowdata;
//       rowd = props.coln.map((number,id) =>{
//           if (number!=="index"){
//               return(
//                 <td key={id}>{rowda[number]}</td>
//               );
//             }
//           return null;
//       });

//       if (props.index[props.rid]){
//             rowd.push(
//               <td
//                 key={props.coln.length}
//                 id={props.coln.length}
//                 onClick = {(event)=>props.clickappend(event, props.rid)}  > &#10004; </td>
//           );}
//       else{
//             rowd.push(
//               <td
//                   key={props.coln.length}
//                   id={props.coln.length}
//                   onClick = {(event)=>props.clickappend(event, props.rid)}  > </td>
//           );}

//       return(
//           <tr 
//             key={props.rid}>
//             {rowd}</tr>
//       );
// };

// export default tablecreate;
