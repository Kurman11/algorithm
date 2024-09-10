const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map(line => line.trim().split(' '));
const [n,...arr] = input;
const arr1 =[]

for(let i = 0; i < n; i++){
  switch(arr[i][0]){
    case 'pop':
      if (arr1.length != 0){
        console.log(arr1.pop())
      } else {
        console.log(-1)
      }
        break;

      case 'size':
        console.log(arr1.length)
        break;

      case 'empty':
        if (arr1.length != 0){
          console.log(0)
        } else {
          console.log(1)
        }
        break;

      case 'top':
        if (arr1.length != 0){
          console.log(arr1[arr1.length - 1])
        } else{
          console.log(-1)
        }
        break;

      default :
        arr1.push(arr[i][1])
        break;
  }
}