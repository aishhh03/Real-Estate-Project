const EventEmitter = require('events');

class NumberMultiplier extends EventEmitter {
  multiply(a, b) {
    const result = a * b;
    this.emit('result', result);
  }
}

const numberMultiplier = new NumberMultiplier();

numberMultiplier.on('result', (result) => {
  console.log('Multiplication result:', result);
});

// Trigger multiplication event
const num1 = 9592;
const num2 = 6665;
numberMultiplier.multiply(num1, num2);
