// let strokeColor;
// let strokeWeightT;
// let velocity;
// let circleX;
// let circleY;
// let circleSize;

// function setup() {
//   frameRate (30);
//   createCanvas(windowWidth, windowHeight);
//   background(0);
//   strokeColor = 200;
//   strokeWeightT = 2;
//   velocity = 20;
//   circleX = width/2;
//   circleY = height/2;
// }

// function draw() {

//   noFill();
//   stroke (strokeColor);
//   strokeWeight (strokeWeightT);
//   let circleSize = 500;
//   circle (circleX, circleY, circleSize);

// }


let balls = [];
let gravity = 1;
let ballFill;
let lastBallTime = 0;
let ballInterval = 1000;

function setup() {
  frameRate(60);
  createCanvas(windowWidth, windowHeight);
  background(0);
  
  // Deteriorated loop function
  // for (let i = 0; i < 5; i++) {
  //   let ball = new Ball(random(width), random(height), random(100, 500), 0, 0);
  //   balls.push(ball);
  // }
}

function draw() {
  background(0);

  let currentTime = millis();
  
  if (currentTime - lastBallTime >= ballInterval) {
    let ball = new Ball(random(width), -200, random(100,250), 0, 0);
    balls.push(ball);
    lastBallTime = currentTime;
  }

  // Move, bounce, and display the ball
  for (let ball of balls) {
  ball.move();
  ball.bounce();
  ball.display();
  }

  // if (int(millis() / 1000) % 10 === 0) {
  //   clear();
  // }

  // Diagnostic text
  fill(255);
  textSize(32);
  text(`${int((millis())/1000)}`,width - 200,height/2);


}

// Ball class definition
class Ball {
  constructor(x, y, diameter, xSpeed, ySpeed) {
    this.xPosition = x;
    this.yPosition = y;
    this.diameter = diameter;
    this.xSpeed = xSpeed;
    this.ySpeed = ySpeed;
    this.ballFill = [0,0,0,0];
    this.strokeWeightT = 2;
  }

  // Move the ball by updating its speed and position
  move() {
    this.xSpeed;
    this.ySpeed = this.ySpeed + gravity;
    
    this.xPosition += this.xSpeed;
    this.yPosition += this.ySpeed;

  }

  // Draw the ball
  display() {
    fill(this.ballFill);
    stroke(200);
    strokeWeight(this.strokeWeightT);
    circle(this.xPosition, this.yPosition, this.diameter);

    // if (this.ballFill > 0) {
    //   this.ballFill -=10;
    //   // this.ballFill = constrain(this.ballFill, 0,200);
    // }

    if (this.strokeWeightT > 0) {
      this.strokeWeightT -= 0.5;
      this.strokeWeightT = constrain(this.strokeWeightT, 2, 30);
    }
  }

  // Handle bouncing at the edges of the screen
  bounce() {
    if (this.yPosition + this.diameter / 2 > height) {
      this.ySpeed *= -1; 
      this.xSpeed = random(-10,10);
      this.yPosition = height - (this.diameter / 2 + 20);
      this.strokeWeightT = 30;
      // this.ballFill = (0,0,0,255);
    }

    if (this.xPosition + this.diameter / 2 > width) {
      this.xSpeed = -this.xSpeed;
      this.xPosition = width - this.diameter / 2;
    }

    if (this.xPosition - this.diameter / 2 < 0) {
      this.xSpeed *= -1;
      this.xPosition = this.diameter / 2 + 10
    }

    this.ySpeed = this.ySpeed * 0.998;
  }
}

