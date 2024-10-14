let circleX;
let circleY;
let velocity;
let strokeColor;
let lastTime;
let duration = 1000;
let strokeWeightT;

function setup() {

  frameRate(60);
  createCanvas(windowWidth, windowHeight);
  background(0);

  circleX = width/2;
  circleY = height/2;
  strokeColor = 200;
  velocity = int(height / 2);
  lastTime = millis();
  strokeWeightT = 2;
}

function draw() { 

// Time difference between frames
let currentTime = millis();
let timeDiff = currentTime - lastTime;

// Movement Logic
circleY += (velocity / duration) * timeDiff;
lastTime = currentTime;

// Bounce back Logic
if (circleY >= windowHeight) {
  velocity *= -1;
  background(0);
}

if (circleY <= 0) {
  velocity *= -1;
  background(0);
}

// Draws Information Textboxes
fill(0);
stroke(0,0); 
rect(0, height/2-50, 400,70);
rect(width-500,height/2-50, 400,70);

// Draws Information Text
fill(255);
textSize(35);
text(`${int((millis()/1000))}`, width-200, height/2);
text(`${int(circleY)}`, width-400, height/2);

// Contrains circleY, ensures it does not overflow and bounces back every time.
// This was a major debugging breakthrough after an hour or two of troubleshooting.
// The circles kept overflowing and ignoring the boolean condition to reverse direction upon hitting 0 or windowHeight
// I solved this without chatGPT, pretty proud of myself if I may say so. Pretty damned simple solve actually.
circleY = constrain(circleY, 0, windowHeight);

// Draws Circles
noFill();
let circleSize = map(circleY, windowHeight/2, windowHeight, 50, windowWidth);
// let strokeWeightT = map(circleY, windowHeight/2, windowHeight, 4, 1);
strokeWeight(strokeWeightT);
stroke(strokeColor);
circle(circleX, circleY ,circleSize);

}