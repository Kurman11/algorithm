function solution(arr) {
    var ar = 0;
    var cnt = 0;
    for (const i of arr){
        ar += i
        cnt += 1
    }
    
    var answer = ar/cnt;
    return answer;
}