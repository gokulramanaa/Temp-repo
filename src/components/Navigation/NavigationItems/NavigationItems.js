import React from 'react';

import classes from './NavigationItems.css';
import NavigationItem from './NavigationItem/NavigationItem';

const navigationItems = (props) => (
    <ul className={classes.NavigationItems}>
    	<NavigationItem link="/" clicked={props.clicked}>Dashboard</NavigationItem>
        <NavigationItem link="/status-report" clicked={props.clicked}>Status Report</NavigationItem>
        <NavigationItem link="/trend-graph" clicked={props.clicked}>Trend Graph</NavigationItem>

    </ul>
);

export default navigationItems;