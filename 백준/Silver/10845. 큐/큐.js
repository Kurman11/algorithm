const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map(line => line.trim().split(' '));
const [n,...arr] = input;
const arr1 =[]

for(let i=0; i<n; i++){
  switch(arr[i][0]){
    case 'push':
      arr1.push(arr[i][1])
      break

    case 'pop':
      if(arr1.length === 0){
        console.log(-1)
      } else{
        console.log(arr1.shift())
      }
      break

    case 'size':
      console.log(arr1.length)
        break
          
    case 'empty':
      if(arr1.length === 0){
        console.log(1)
      } else{
        console.log(0)
      }
      break

    case 'front':
      if(arr1.length === 0){
        console.log(-1)
      } else{
        console.log(arr1[0])
      }
      break
      
    default:
      if(arr1.length === 0){
        console.log(-1)
      } else{
        console.log(arr1[arr1.length - 1])
      }
  }
}