import React from 'react'
import InputLabel from '@material-ui/core/InputLabel';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemAvatar from '@material-ui/core/ListItemAvatar';
import Avatar from '@material-ui/core/Avatar';
import ListItemText from '@material-ui/core/ListItemText';
import NoteIcon from '@material-ui/icons/Note';
import './Home.css'

class Home extends React.Component {

  servidorA = "http://34.123.224.145"
  servidorB = "http://35.226.94.227"

  constructor(props){
    super(props)
    this.state = { servidor: 1 }
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(e) {
    this.setState({servidor: e.target.value})
    console.log(this.state.servidor)
  }

  generate(element) {
    return [0, 1, 2].map((value) =>
      React.cloneElement(element, {
        key: value,
      }),
    );
  }
  

  render() {
    return (
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
        
        <div style={{paddingLeft: 10+'%', width: 80+'%'}}>
          <div>
            <List>
              {this.generate(
                <ListItem>
                  <ListItemAvatar>
                    <Avatar>
                      <NoteIcon />
                    </Avatar>
                  </ListItemAvatar>
                  <ListItemText
                    primary="Single-line item"
                  />
                </ListItem>,
              )}
            </List>
          </div>
        </div>

      </div>
    )
  }
}

export default Home  