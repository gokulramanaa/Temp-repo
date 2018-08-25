<<<<<<< HEAD
import React from 'react';
import classes from './Login.css'

const login = (props) => {

	return (
		<form className = {classes.Formdata} onSumbit = {props.something}>
			<label className={classes.FormLable}>
				Username:
				<input className = {classes.Submit} type="text" value="one" onChange={props.changed} />
        	</label>
        	<label className={classes.FormLable}>
        		Password:
        		<input className = {classes.Submit} 	type="Password" />
        	</label>
        	 <input className = {classes.Submit} type="submit" value="Login" />
		</form>
		);
}

=======
import React from 'react';
import classes from './Login.css'

const login = (props) => {

	return (
		<form className = {classes.Formdata} onSumbit = {props.something}>
			<label className={classes.FormLable}>
				Username:
				<input className = {classes.Submit} type="text" value="one" onChange={props.changed} />
        	</label>
        	<label className={classes.FormLable}>
        		Password:
        		<input className = {classes.Submit} 	type="Password" />
        	</label>
        	 <input className = {classes.Submit} type="submit" value="Login" />
		</form>
		);
}

>>>>>>> 24b39daf60f9793a65df2352f5f951f9944d7d7f
export default login;