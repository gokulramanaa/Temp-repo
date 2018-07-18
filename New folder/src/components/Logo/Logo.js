import React from 'react';

import sstlogo from '../../assets/images/sst.png';
import classes from './Logo.css';

const logo = (props) => (
    <div className={classes.Logo} style={{height: props.height}}>
        <img src={sstlogo} alt="MyBurger" />
    </div>
);

export default logo;