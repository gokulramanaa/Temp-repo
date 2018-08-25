import React from 'react';
import classes from './Toolbar.css';
import Logo from '../../Logo/Logo';
// import NavigationItems from '../NavigationItems/NavigationItems';
import DrawerToggle from '../SideDrawer/DrawerToggle/DrawerToggle';
import Dropdown from '../DropDown/DropDown';

const toolbar = ( props ) => {
	let attachedClasses = [classes.Toolbar];
    if (props.open) {
        attachedClasses = [classes.Toolbar, classes.Open];
    }
    
    
	return (
		<header className={attachedClasses.join(' ')}>
            <DrawerToggle  clicked={props.drawerToggleClicked} />
            <div className={classes.Logo}>
                <Logo />
            </div>
            <h1 className={classes.Title}> ECS JOB STATUS PORTAL </h1>
            
            <div className={classes.Client}>
            <p className = {classes.Left}>Select Client:</p>
            <Dropdown className={classes.Left}
                      title={props.title}
                      list={props.list} selected = {props.selected}/>
            </div>
        </header>
		);
};


export default toolbar;