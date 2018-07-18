import React from 'react';

const tablecreate =(props)=> {

const rowd = props.coln.map((number,indi) => {
  return (<td
      key={indi}
      id={indi}>{eval("props.rowdata."+(number))}</td>
  );
});

rowd.push(
  <td
      key={props.coln.length}
      id={props.coln.length}
      onDoubleClick={(event) => props.clicki(event, props.rid)}>{props.tickval}</td>
    );

  return(
    <tr key={props.rid}>
      {rowd}
    </tr>);
};

export default tablecreate;
