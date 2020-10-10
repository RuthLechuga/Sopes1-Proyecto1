import React from 'react'

class Home extends React.Component {
    render() {
      return (
        <Dropdown>
            <Dropdown.Toggle variant="success" id="dropdown-basic">Servidores</Dropdown.Toggle>
        
            <Dropdown.Menu>
                <Dropdown.Item href="#/action-1">Servidor A</Dropdown.Item>
                <Dropdown.Item href="#/action-2">Servidor B</Dropdown.Item>
            </Dropdown.Menu>
        </Dropdown>
      )
    }
}

export default Home  