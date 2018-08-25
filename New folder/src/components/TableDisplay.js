import React from 'react';
import classes from './TableDisplay.css';
import TableMain from './DocsControl/TableMain';
import Pagination from './DocsControl/Pagination';

const tabledisplay = (props) => {
    // Logic for displaying todos
    const { response,currentPage, todosPerPage } = props;
    const indexOfLastTodo = currentPage * todosPerPage;
    const indexOfFirstTodo = indexOfLastTodo - todosPerPage;
    const currentTodos = response.slice(indexOfFirstTodo, indexOfLastTodo);
    const colNames = [];
    for (let i = 0; i < props.colsize; i++) {
      colNames.push(props.fields[i]);
    }
    let attachedClasses = [classes.Tabledisplay];
    if (props.open) {
        attachedClasses = [classes.Tabledisplay, classes.Open];
    }

      return (
        <div className={attachedClasses.join(' ')}>
          {/*<h1>ECS JOB STATUS FOR - {props.selecteditem} (dummy)</h1>*/}

  
          <TableMain mdata = {currentTodos} columN = {colNames}/>
          <Pagination 
          value = {props} 
          clickhandle = {props.handleClick} />
      </div>
      );
    }

export default tabledisplay;
