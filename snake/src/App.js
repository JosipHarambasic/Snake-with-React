import React, {Component} from 'react';
import './App.css';
import Snake from "./components/Snake";
import Food from "./components/Food";


const getRandomLocation = () => {
    let min = 1;
    let max = 98;
    let x = Math.floor((Math.random()*(max-min+1)+min)/2)*2;
    let y = Math.floor((Math.random()*(max-min+1)+min)/2)*2;
    return [x,y]
}


class App extends Component{

    state = {
        highScore: 0,
        points: 0,
        food: getRandomLocation(),
        speed: 100,
        direction: 'RIGHT',
        snakeDots: [
            [0,0],
            [2,0],
            [4,0]
        ]
    }

    componentDidMount() {
        setInterval(this.moveSnake,this.state.speed);
        document.onkeydown = this.onKeyDown;
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
        this.checkIfOutOfBounds()
        this.checkIfCollapsed()
        this.checkIfEat()
    }

    onKeyDown = (e) => {
        e = e || window.event;
        switch (e.keyCode){
            case 38:
            this.setState({direction:'UP'});
                break;

            case 40:
                this.setState({direction:'DOWN'});
                break;

            case 37:
                this.setState({direction:'LEFT'});
                break;

            case 39:
                this.setState({direction:'RIGHT'});
                break;
        }

    }

    moveSnake = () => {
        let dots = [...this.state.snakeDots];
        let head = dots[dots.length-1];

        switch (this.state.direction){
            case "RIGHT":
                head = [head[0] + 2, head[1]];
                break;
            case "LEFT":
                head = [head[0] - 2, head[1]];
                break;
            case "DOWN":
                head = [head[0], head[1] + 2];
                break;
            case "UP":
                head = [head[0], head[1] - 2];
                break;
        }
        dots.push(head); //adding head
        dots.shift(); // removing tail

        this.setState({
            snakeDots: dots
        })
    }

    checkIfOutOfBounds(){
        let head = this.state.snakeDots[this.state.snakeDots.length-1];
        if(head[0] >= 100 || head[1] >= 100 || head[0] < 0 || head[1] < 0){
            this.onGameOver();
        }

    }

    inCreaseSpeed(){
        if (this.state.speed > 10){
            this.setState({speed: this.state.speed -10})
        }
    }

    checkIfCollapsed(){
        let snake = [...this.state.snakeDots];
        let head = snake[snake.length-1];
        snake.pop();
        snake.forEach(dot => {
            if (head[0] === dot[0] && head[1] === dot[1]){
                this.onGameOver()
            }
        })

    }

    checkIfEat(){
        let head = this.state.snakeDots[this.state.snakeDots.length-1];
        let food = this.state.food;

        if (head[0] === food[0] && head[1] === food[1]){
            this.setState({
                food: getRandomLocation()
            })
            this.enlargeSnake();
            this.inCreaseSpeed();
            this.setState({points: this.state.points + 10})
        }
    }

    enlargeSnake(){
        let newSnake = [...this.state.snakeDots];
        newSnake.unshift([])
        this.setState({
            snakeDots: newSnake
        })
    }

    checkIfHighScore(){
        if (this.state.points > this.state.highScore){
            this.setState({highScore: this.state.points})
        }
    }

    onGameOver(){
        this.checkIfHighScore()
        alert(`Game Over. Snake length is ${this.state.snakeDots.length} `);
        this.setState({
            points: 0,
            food: getRandomLocation(),
            speed: 100,
            direction: 'RIGHT',
            snakeDots: [
                [0,0],
                [2,0],
                [4,0]
            ]
        })
    }

    render() {
      return (
          <div>
              <center><h1>Your HighScore is {this.state.highScore}</h1></center>
          <center><h1>You reached {this.state.points} points</h1></center>
          <div className={"game-area"}>
              <Snake snakeDots={this.state.snakeDots}/>
              <Food dot={this.state.food}/>
          </div>
          </div>
      );
  }
}

export default App;
