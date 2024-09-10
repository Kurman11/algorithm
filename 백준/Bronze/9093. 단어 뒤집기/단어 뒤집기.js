const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map(line => line.trim().split(' '));
const n = parseInt(input.shift())

for(let i=0; i < n; i++){
  const arr = []
  for(const item of input[i]){
    arr.push(item.split('').reverse().join(''))
  }
  console.log(arr.join(' '))
}