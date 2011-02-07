window.onload = function() {  
   var data = [];
   
  var R = Raphael(document.getElementById('paper'), 500, 500);
  var circle = R.circle(100, 100, 50).attr({
    fill: "#ff0000",
    stroke: "none",
    opacity: .5
  });
  
  function start() {
    this.ox = this.attr("cx");
    this.oy = this.attr("cy");
    this.attr({opacity: 1});
  }
  
  function move(dx, dy) {
    this.attr({cx: this.ox + dx, cy: this.oy + dy});
  }
  
  function up() {
    this.attr({opacity: .5});
  }
  
  circle.drag(move, start, up);
  
  var button = R.rect(4, 4, 50, 20).attr({
    stroke: "#ccc",
    fill: "#fff",
    "stroke-width": 2
  }).click(moveright);
  
  function moveright() {
    var at = circle.attr();
    circle.animate({cx: 200, cy: 200}, 800, "bounce");
  }
};
