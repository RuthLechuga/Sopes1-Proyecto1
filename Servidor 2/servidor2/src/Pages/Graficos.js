import React from 'react'
import axios from 'axios';
import {
  Chart,
  Series,
  ArgumentAxis,
  CommonSeriesSettings,
  Export,
  Legend,
  Margin
} from 'devextreme-react/chart';
import Button from '@material-ui/core/Button';

class Graficos extends React.Component {

  servidorA = "http://34.123.224.145:5000"
  servidorB = "http://35.226.94.227:5000"

  constructor(props){
    super(props)
    this.state = { 
      servidor: 1,
      notas: [],
      porcentajesA: [],
      porcentajesB:[],
      tiempo: 0
    }
  }

  componentDidMount() {
    this.intervalId = setInterval(() => this.cargarPorcentajes(), 5000);
    this.cargarPorcentajes()
  }

  componentWillUnmount() {
    clearInterval(this.intervalId);
  }

  cargarPorcentajes(){
    //Servidor A
    axios.get(this.servidorA+'/getPorcentajes')  
    .then(res => {
      let ramA = res.data.RAM
      let cpuA = res.data.CPU
      this.setState({ porcentajesA: [...this.state.porcentajesA, 
        {
          'Tiempo': this.state.tiempo,
          'CPU': cpuA*10,
          'RAM': ramA
        }
      ]})
    })
    .catch(error =>{
      console.log(error)
    })

    //Servidor B
    axios.get(this.servidorB+'/getPorcentajes')  
    .then(res => {
      let ramB = res.data.RAM
      let cpuB = res.data.CPU
      this.setState({ porcentajesB: [...this.state.porcentajesB, 
        {
          'Tiempo': this.state.tiempo,
          'CPU': cpuB*10,
          'RAM': ramB
        }
      ]})
    })
    .catch(error =>{
      console.log(error)
    })
    this.setState({tiempo: this.state.tiempo+5})
  }
 
  render() {
    return (
        <div style={{paddingLeft: 10+'%', width: 80+'%'}}>
          <br></br>
          <h1>Graficos</h1>
          <Button variant="contained" color="primary" onClick={event =>  window.location.href='/Graficos'}>
            Publicaciones
          </Button>
          <br></br><br></br>
          <div id="chart-demo">
            <Chart
              palette="Harmony Light"
              title="Servidor A"
              dataSource={this.state.porcentajesA}
            >
              <CommonSeriesSettings
                argumentField="Tiempo"
                type={"area"}
              />
              <Series valueField="RAM" name="RAM"></Series>
              <Series valueField="CPU" name="CPU"></Series>
              <Margin bottom={20} />
              <ArgumentAxis valueMarginsEnabled={false} />
              <Legend
                verticalAlignment="bottom"
                horizontalAlignment="center"
              />
              <Export enabled={true} />
            </Chart>
          </div>
          
          <div id="chart-demo">
            <Chart
              palette="Harmony Light"
              title="Servidor B"
              dataSource={this.state.porcentajesB}
            >
              <CommonSeriesSettings
                argumentField="Tiempo"
                type={"area"}
              />
              <Series valueField="RAM" name="RAM"></Series>
              <Series valueField="CPU" name="CPU"></Series>
              <Margin bottom={20} />
              <ArgumentAxis valueMarginsEnabled={false} />
              <Legend
                verticalAlignment="bottom"
                horizontalAlignment="center"
              />
              <Export enabled={true} />
            </Chart>
          </div>
        </div>
    )
  }
}

export default Graficos  