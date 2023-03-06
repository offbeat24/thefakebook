console.log(solution);

function solution(wallpaper) {
  var answer = [];
  var lux = Infinity;
  var luy = Infinity;
  var rdx = 0;
  var rdy = 0;
  wallpaper.forEach((row, i) => {
    [...row].forEach((file, j) => {
      if (file === "#") {
        lux = Math.min(i, lux);
        luy = Math.min(j, luy);
        rdx = Math.max(i, rdx);
        rdy = Math.max(j, rdy);
      }
    })
  })
  answer = [lux, luy, rdx+1, rdy+1]
  return answer;
}