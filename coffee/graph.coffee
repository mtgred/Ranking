Raphael.fn.drawGrid = (x, y, w, h, xlabels, ylabels, color) ->
  color = color || "#000"
  font = font: '12px Lato, Helvetica, sans-serif', fill: color
  rowHeight = h/(ylabels.length - 1)
  columnWidth = w/(xlabels.length - 1)
  p = []
  for label, i in ylabels
    p = p.concat(["M", Math.round(x) + .5, Math.round(y + i * rowHeight) + .5, "H", Math.round(x+w) + .5])
    this.text(x - 24, h + y - i * rowHeight, label).attr(font)
  for label, i in xlabels
    p = p.concat(["M", Math.round(x + i * columnWidth) + .5, Math.round(y) + .5, "V", Math.round(y+h) + .5])
    this.text(x + i * columnWidth, h + 24, label).attr(font)
  this.path(p.join(",")).attr(stroke: color)

Raphael.fn.drawGraph = (x, y, w, h, xdata, ydata, color) ->
  xmin = xdata[0]
  xmax = xdata[xdata.length-1]
  xratio = (xmax - xmin) / w
  ymin = 1000
  ymax = 3200
  yratio = (ymax - ymin) / h
  ystart = y + h - (1500 - ymin) / yratio
  p = ["M", x, ystart, "C", x, ystart]
  dots = ([(xi.getTime() - xmin) / xratio + x, h+y - (ydata[i]-ymin)/yratio] for xi, i in xdata)
  p = p.concat [dots[i-1][0], dots[i-1][1], dots[i][0], dots[i][1], dots[i+1][0], dots[i+1][1]] for i in [1...dots.length-1]
  line = this.path(p).attr(stroke: color, "stroke-width": 2, "stroke-linejoin": "round")

window.onload = () ->
  victories = 0
  xdata = (new Date d for d in dates)
  ydata = for s, i in scores
    victories++ if s is 10
    (7.5 + victories) / (i + 51) * 10000
  years = {}
  years[d.getFullYear()] = true for d in xdata
  r = Raphael("paper", 880, 480)
  r.drawGrid(40,10,800,450,(k for k of years), [1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000,3200], "#333")
  r.drawGraph(40,10,800,450,xdata, ydata, "hsb(.6,.5,1)")
