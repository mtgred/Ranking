(function() {
  Raphael.fn.drawGrid = function(x, y, w, h, xlabels, ylabels, color) {
    var columnWidth, font, i, label, p, rowHeight, _len, _len2;
    color = color || "#000";
    font = {
      font: '12px Lato, Helvetica, sans-serif',
      fill: color
    };
    rowHeight = h / (ylabels.length - 1);
    columnWidth = w / (xlabels.length - 1);
    p = [];
    for (i = 0, _len = ylabels.length; i < _len; i++) {
      label = ylabels[i];
      p = p.concat(["M", Math.round(x) + .5, Math.round(y + i * rowHeight) + .5, "H", Math.round(x + w) + .5]);
      this.text(x - 24, h + y - i * rowHeight, label).attr(font);
    }
    for (i = 0, _len2 = xlabels.length; i < _len2; i++) {
      label = xlabels[i];
      p = p.concat(["M", Math.round(x + i * columnWidth) + .5, Math.round(y) + .5, "V", Math.round(y + h) + .5]);
      this.text(x + i * columnWidth, h + 24, label).attr(font);
    }
    return this.path(p.join(",")).attr({
      stroke: color
    });
  };
  Raphael.fn.drawGraph = function(x, y, w, h, xdata, ydata, color) {
    var dots, i, line, p, xi, xmax, xmin, xratio, ymax, ymin, yratio, ystart, _ref;
    xmin = xdata[0];
    xmax = xdata[xdata.length - 1];
    xratio = (xmax - xmin) / w;
    ymin = 1000;
    ymax = 3200;
    yratio = (ymax - ymin) / h;
    ystart = y + h - (1500 - ymin) / yratio;
    p = ["M", x, ystart, "C", x, ystart];
    dots = (function() {
      var _len, _results;
      _results = [];
      for (i = 0, _len = xdata.length; i < _len; i++) {
        xi = xdata[i];
        _results.push([(xi.getTime() - xmin) / xratio + x, h + y - (ydata[i] - ymin) / yratio]);
      }
      return _results;
    })();
    for (i = 1, _ref = dots.length - 1; (1 <= _ref ? i < _ref : i > _ref); (1 <= _ref ? i += 1 : i -= 1)) {
      p = p.concat([dots[i - 1][0], dots[i - 1][1], dots[i][0], dots[i][1], dots[i + 1][0], dots[i + 1][1]]);
    }
    return line = this.path(p).attr({
      stroke: color,
      "stroke-width": 2,
      "stroke-linejoin": "round"
    });
  };
  window.onload = function() {
    var d, i, k, r, s, victories, xdata, ydata, years, _i, _len;
    victories = 0;
    xdata = (function() {
      var _i, _len, _results;
      _results = [];
      for (_i = 0, _len = dates.length; _i < _len; _i++) {
        d = dates[_i];
        _results.push(new Date(d));
      }
      return _results;
    })();
    ydata = (function() {
      var _len, _results;
      _results = [];
      for (i = 0, _len = scores.length; i < _len; i++) {
        s = scores[i];
        if (s === 10) {
          victories++;
        }
        _results.push((7.5 + victories) / (i + 51) * 10000);
      }
      return _results;
    })();
    years = {};
    for (_i = 0, _len = xdata.length; _i < _len; _i++) {
      d = xdata[_i];
      years[d.getFullYear()] = true;
    }
    r = Raphael("paper", 880, 480);
    r.drawGrid(40, 10, 800, 450, (function() {
      var _results;
      _results = [];
      for (k in years) {
        _results.push(k);
      }
      return _results;
    })(), [1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200], "#333");
    return r.drawGraph(40, 10, 800, 450, xdata, ydata, "hsb(.6,.5,1)");
  };
}).call(this);
