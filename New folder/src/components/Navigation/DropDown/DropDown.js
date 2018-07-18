import React from 'react';
import classes from './DropDown.css';

const dropdown = (props) => {
		let lishow = null;
		lishow = (props.list.map((item) => <option 
			key = {item.id}
			value = {item.title}>{item.title}</option>));

		  return(
		    <div className= {classes.DropDown}>
		    <select value = {props.title} onChange= {(event)=>props.selected(event)}>
		    	{lishow}
		    </select>
		    </div>
		  )
	};


export default dropdown;