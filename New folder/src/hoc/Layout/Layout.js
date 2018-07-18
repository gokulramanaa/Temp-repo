import React, { Component } from 'react';
import Aux from '../Auxi';
import classes from './Layout.css';
import Toolbar from '../../components/Navigation/Toolbar/Toolbar';
import SideDrawer from '../../components/Navigation/SideDrawer/SideDrawer';
import Dropdown from '../../components/Navigation/DropDown/DropDown';
import Tabledisplay from '../../components/TableDisplay';
import {Route} from 'react-router-dom';
import Loading from '../../components/Navigation/Loading/Loading';
// import Time from 'react-time';


class Layout extends Component {

  constructor (props) {
    super(props)
    this.state = {
        showSideDrawer: false,
        selectedClient: 'SST-PAM',
        selectedview: 'All',
        response:[],
        tempresponse: [],
        fields:[],
        colsize: 0,
        rowsize: 0,
        currentPage: 1,
        todosPerPage: 40,
        filterdisplay: false,
        activepage:1,
        loading: true,
        clients: [
                    {id: 0,
                     title: 'SST'},
                    {id: 1,
                     title: 'SST-GX'},
                    {id: 2,
                     title: 'SST-SHARE'},
                    {id: 3,
                     title: 'SST-PAM'}
                  ],
        viewlist: [
                    {id: 0,
                     title: 'All'},
                    {id: 1,
                     title: 'Last Day'},
                    {id: 2,
                     title: 'Last Week'},
                    {id: 3,
                     title: 'Last Month'}
                  ]
      }; 
    this.handleClientChange = this.handleClientChange.bind(this);
    this.sideDrawerClosedHandler = this.sideDrawerClosedHandler.bind(this);
    this.sideDrawerToggleHandler = this.sideDrawerToggleHandler.bind(this);
    this.handlePageNumberClick = this.handlePageNumberClick.bind(this);
    this.handleFilterViewChange = this.handleFilterViewChange.bind(this);
  };
    

  componentDidMount() {
    this.callApi(this.state.selectedClient)
      .then(res => this.setState({
        response: res[0],fields:res[1], rowsize: res[0].length, 
        colsize:Object.keys(res[0][0]).length, loading: false
       }))
      .catch(err => console.log(err));
  }

    sideDrawerClosedHandler = () => {
        this.setState( { showSideDrawer: false } );
    }

    sideDrawerToggleHandler = () => {
        this.setState( ( prevState ) => {
            return { showSideDrawer: !prevState.showSideDrawer };
        } );
    }

    handleClientChange(event){
        let temp = event.target.value;
        this.setState({selectedClient:temp, loading:true})
        this.callApi(temp)
        .then(res => this.setState({
        response: res[0],fields:res[1], rowsize: res[0].length, 
        colsize:Object.keys(res[0][0]).length, selectedClient: temp,
        currentPage:1, loading: false, filterdisplay: false, selectedview: 'All'
       }))
      .catch(err => console.log(err));
      };

    handleFilterViewChange(event){
      let {response} = this.state;
      let temp = [];
      let view = event.target.value
      if (this.state.selectedClient === "SST-PAM" && view === "Last Day"){
        response.map((item, id) => {
          if(item.Create_time === "2018-07-05 17:25:19"){
              temp.push(item)
            }});
      } else if (this.state.selectedClient === "SST-PAM" && view === "Last Week"){
        response.map((item,id) => {
          if(item.Create_time === "2018-07-05 17:25:20"){
            temp.push(item)
          }});
      } else if (this.state.selectedClient === "SST-PAM" && view === "Last Month"){
        response.map((item,id) => {
          if(item.Create_time === "2018-07-05 17:25:21") {
            temp.push(item)
          }})
      } else { temp = response}
      this.setState({filterdisplay: true, 
                    tempresponse:temp,
                    selectedview: view, 
                    rowsize: temp.length})
    }

    handlePageNumberClick(event) {
        this.setState({
          currentPage: Number(event.target.id)
        });
      }

    callApi = async (one) => {
        const response = await fetch('/' + one);
        const body = await response.json();
        if (response.status !== 200) throw Error(body.message);
        // console.log(body[0])
        return body;
      };


    render () {
      // let today = new Date();
      // let date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
      // console.log("render inside", date, today.getTime(), "----", today)

        if (this.state.loading){
          return (
            <Loading />
            );
        };

        let cresponse = !this.state.filterdisplay? this.state.response: this.state.tempresponse;
        // console.log(cresponse.length);
                        
        return (
            <Aux className= {classes.Content}> 
                <Toolbar drawerToggleClicked={this.sideDrawerToggleHandler} 
                        open = {this.state.showSideDrawer}
                        title={this.state.selectedClient}
                        list={this.state.clients} 
                        selected = {this.handleClientChange}/>
                <SideDrawer
                    open={this.state.showSideDrawer}
                    closed={this.sideDrawerClosedHandler} />
                <main >
{/*                <Dropdown
                      title={this.state.selectedClient}
                      list={this.state.clients} selected = {this.handleClientChange}/> */}
                <Dropdown 
                      title = {this.state.selectedview}
                      list = {this.state.viewlist} selected = {this.handleFilterViewChange} />

                
                <Route path = '/' exact render = {()=> <h1 className = {classes.UnderCons}>Under Construction </h1>} />
                <Route path = '/trend-graph' exact render = {()=> <h1 className = {classes.UnderCons}>Under Construction </h1>} />
                
                <Route 
                                    path = "/status-report" exact 
                                    render = {(props) => (<Tabledisplay {...props} 
                                    open = {this.state.showSideDrawer}
                                    comp = {this.state.selectedClient}
                                    response = {cresponse}
                                    fields = {this.state.fields}
                                    rowsize = {this.state.rowsize}
                                    colsize = {this.state.colsize}
                                    currentPage = {this.state.currentPage}
                                    todosPerPage = {this.state.todosPerPage}
                                    activepage = {this.state.activepage}
                                    handleClick = {this.handlePageNumberClick}
                                    selecteditem = {this.state.selectedClient}/>
                                    )}/>
                
                </main>
            </Aux>
        )
    }
}

export default Layout;