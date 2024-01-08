function squareSum(numbers){
  return numbers.reduce(function(sum, n){
    return (n*n) + sum;
  }, 0)
}

function squareSum(numbers){
  return numbers.reduce((x,y)=>x+y*y,0)
}
