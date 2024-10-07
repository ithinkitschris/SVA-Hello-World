let circleX;
let circleY;
let velocity;
let strokeColor;

function setup() {
  createCanvas(windowWidth, windowHeight);
  background("black");
  // rect(0,0,2000,2000);
  circleX = width/2;
  circleY = height/2;
  velocity = 100;
  velocityDecrement = 1;
  strokeT = 2;
  strokeColor = 200;
  strokeDecrement = 10;
}

// function windowResized() {
//   resizeCanvas(windowWidth, windowHeight);
// }

function draw() { 

//Sets Frame Rate
frameRate(30);

//Draws Canvas
fill("black");
stroke(0,0); 
rect(0, height/2-50, 400,70);
rect(width-200,height/2-50, 150,70);

//Draws Information Text
fill(255,255,255);
textSize(35);
text(`${frameCount}`, width-150, height/2);
text(`${strokeColor}`, 100, height/2);
text(`${velocity}`, 200, height/2);
// text(`${strokeT}`, 100, height/2-50);


//Draws Circles
fill(0,0);
strokeColor = constrain(strokeColor, 0, 255);
let circleSize = map(circleY, height/2, height, 0,windowWidth);
// let strokeH = map(circleY, 0, height, 2,20);
strokeWeight(strokeT);
stroke(strokeColor);
circle(circleX, circleY ,circleSize);

//Movement Logic
circleY += velocity;

  if (circleY >= height || circleY <= 0) {
    velocity *= -1;
    velocityDecrement *= -1;
    velocity += velocityDecrement;
    strokeColor -= strokeDecrement;
  }

  if (strokeColor <= 10 || strokeColor >= 240) {
    strokeDecrement *= -1;
  }
}


// circleY = 0 + frameCount*10 % height;
// stroke(200,200,200);

  // fill(0, 0); // Transparent fill

  // let strokeH = map(mouseY, height/2, 1920, 1, 0);
  // strokeMax = constrain(strokeH, 1,0);
  // strokeWeight(strokeH);// Draw the circle at the mouse position
  
  // let size = map(mouseY, height/2, height, 0, 2000);
  // size = constrain(size, -2000,2000);
  // circle(mouseX, mouseY, size); // Draw the circle at the mouse position