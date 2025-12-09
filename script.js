window.addEventListener('DOMContentLoaded', () => {
  document.getElementById('calculateBtn').addEventListener('click', calculate);
});

function calculate() {
  const distance = parseFloat(document.getElementById('distance').value);
  const urgency = parseFloat(document.getElementById('urgency').value);

  if (isNaN(distance) || isNaN(urgency)) {
    alert("Please enter both distance and urgency!");
    return;
  }

  // Calculate example values
  const speed = Math.min(120, 50 + urgency * 7); // km/h
  const fuel = (distance * (1 + urgency / 10) * 0.08).toFixed(2); // liters
  const pollution = (distance * (1 + urgency / 10) * 0.05).toFixed(2); // kg

  document.getElementById('results').innerHTML =
    `Speed: ${speed} km/h <br> Fuel consumption: ${fuel} L <br> Pollution: ${pollution} kg`;

  // Animate car
  const car = document.getElementById('car');
  const smoke = document.getElementById('smoke');

  car.style.left = 'calc(100% - 100px)';
  smoke.style.opacity = 1;
  smoke.style.animation = 'smokeRise 1s forwards';

  setTimeout(() => {
    car.style.left = '-100px';
    smoke.style.opacity = 0;
  }, 3000);
}
