const duration = 120;
let timeLeft;
let startTime;
let interval;

const label = document.querySelector('.time');
const start = document.querySelector('.start');
const stop = document.querySelector('.stop')


start.addEventListener('click', () => {
    startTime = Date.now();

    interval = setInterval(() => {
      const t = Math.ceil(duration - (Date.now() - startTime) / 1000);
      label.innerHTML = Math.max(0, t);
    }, 200);
});

stop.addEventListener('click', () => {
  clearInterval(interval);
})