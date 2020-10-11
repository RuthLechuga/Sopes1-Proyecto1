import React from 'react'
import InputLabel from '@material-ui/core/InputLabel';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemAvatar from '@material-ui/core/ListItemAvatar';
import Avatar from '@material-ui/core/Avatar';
import ListItemText from '@material-ui/core/ListItemText';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import axios from 'axios';

class Home extends React.Component {

  servidorA = "http://34.123.224.145:5000"
  servidorB = "http://35.226.94.227:5000"

  constructor(props){
    super(props)
    this.state = { servidor: 1, notas: [] }
    this.handleChange = this.handleChange.bind(this);
  }

  componentDidMount() {
    this.cargarNotas()
  }

  handleChange(e) {
    this.setState({servidor: e.target.value})
    console.log(this.state.servidor)
    this.cargarNotas()
  }

  cargarNotas = () => {
    let url = this.state.servidor == 2? this.servidorA : this.servidorB

    axios.get(url)  
    .then(res => {
      const notas = res.data;
      this.setState({ notas });
    })
    .catch(error =>{
      console.log(error)
    })
  }

  render() {
    return (
        <div style={{paddingLeft: 10+'%', width: 80+'%'}}>
          <br></br>
          <h1>Publicaciones</h1>
          <Button variant="contained" color="primary" onClick={event =>  window.location.href='/Graficos'}>
            Graficas
          </Button>
          <br></br><br></br>
          <div style={{width:100+'%'}}>
                <FormControl variant="filled" style={{width:100+'%'}}>
                  <InputLabel htmlFor="filled-age-native-simple">Servidor</InputLabel>
                  <Select
                    native
                    value={this.state.servidor}
                    onChange={this.handleChange}
                    style={{width:100+'%'}}
                    inputProps={{
                      name: 'age',
                      id: 'filled-age-native-simple',
                    }}
                  >
                    <option value={1}>Servidor A</option>
                    <option value={2}>Servidor B</option>
                  </Select>
                </FormControl>
              </div>
              <div>
                <List>
                  {this.state.notas.map( value =>{
                    return(
                      <ListItem key={value._id}>
                        <ListItemAvatar><Avatar style={{backgroundColor: "blue"}} /></ListItemAvatar>
                        <ListItemText 
                          primary={value.nota} 
                          secondary={
                            <React.Fragment>
                              <Typography component="span" variant="body2" color="textPrimary">
                                {value.autor  }
                              </Typography>
                            </React.Fragment>}
                        />
                      </ListItem>
                    )
                  })}
                </List>
            </div>
        </div>
    )
  }
}

export default Home  