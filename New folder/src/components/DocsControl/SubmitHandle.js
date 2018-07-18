import React from 'react';

const submithandle = (props) => {

	const callApi = async () => {
		console.log("sending", JSON.stringify(props.value));
		const response = await fetch('/api/add_message/1234', 
		    	{method: "post", 
		    	headers: {'Accept':'application/json','Content-Type': 'application/json'},
		    	body:JSON.stringify(props.value)});

		const body = await response.json();
		if (response.status !== 200) throw Error(body.message);
		console.log(body)
		return null;
  	};

	return(

			<div>
				<button onClick= {()=> callApi()}>Submit</button>
			</div>
		);
};

export default submithandle;