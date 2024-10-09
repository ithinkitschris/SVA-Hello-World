let circleX;
let circleY;
let velocity;
let strokeColor;
let lastTime;
let duration = 1000;

function setup() {

  //Sets Frame Rate
  frameRate(60);
  createCanvas(windowWidth, windowHeight);
  background("black");

  circleX = width/2;
  circleY = height/2;
  strokeColor = 200;
  velocity = windowHeight / 2;
  lastTime = millis();
}

function draw() { 

//Time difference between frames
let currentTime = millis();
let timeDiff = currentTime - lastTime;

//Movement Logic
circleY += (velocity / duration) * timeDiff;

if (circleY >= height || circleY <= 0) {
  velocity *= -1;
  createCanvas(windowWidth, windowHeight);
  background("black");
}

lastTime = currentTime;

//Draws Information Textboxes
fill("black");
stroke(0,0); 
rect(0, height/2-50, 400,70);
rect(width-200,height/2-50, 150,70);

//Draws Information Text
fill(255);
textSize(35);
text(`${int((millis()/1000))}`, width-200, height/2);

//Draws Circles
noFill();
let circleSize = map(circleY, windowHeight/2, windowHeight, 0, windowWidth);
strokeWeight(2);
stroke(strokeColor);
circle(circleX, circleY ,circleSize);

}