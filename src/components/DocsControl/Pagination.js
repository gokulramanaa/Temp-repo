import React from 'react';
import classes from './Pagination.css';

const pagination = (props) => {
  // Logic for displaying todos
  // const { response, currentPage, todosPerPage } = props.value;
  // const indexOfLastTodo = currentPage * todosPerPage;
  // const indexOfFirstTodo = indexOfLastTodo - todosPerPage;
  // const currentTodos = response.slice(indexOfFirstTodo, indexOfLastTodo);

  // Logic for displaying page numbers
  const pageNumbers = [];
  for (let i = 1; i <= Math.ceil(props.value.rowsize / props.value.todosPerPage); i++) {
    pageNumbers.push(i);
  }

  const renderPageNumbers = pageNumbers.map(number => {
    return (<li
        key={number}
        id={number}
        onClick={props.clickhandle}>{number}</li>
    );
  });

  return(<ul className = {classes.Pagination}id="page-numbers">{renderPageNumbers}</ul>)
}

export default pagination;
