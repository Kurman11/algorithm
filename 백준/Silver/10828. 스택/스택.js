const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map(line => line.trim().split(' '));
const [n,...arr] = input;
const arr1 =[]

for (let i = 0; i<n; i++){
  if (arr[i].length == 2){
    arr1.push(arr[i][1]);
  } else if(arr[i] == 'pop'){
    if (arr1.length == 0){
      console.log(-1);
    } else {
      console.log(arr1.pop());
    }
  } else if(arr[i] == 'size'){
    console.log(arr1.length);
  } else if(arr[i] == 'empty'){
    if(arr1.length == 0){
      console.log(1)
    }else{
      console.log(0)
    }
  } else if(arr[i] == 'top'){
    if(arr1.length == 0){
      console.log(-1)
    } else{
      console.log(arr1[arr1.length-1])
    }
  }
}