function solution(info, query) {
  const binarySearch = (array, targetValue) => {
    let left = 0;
    let right = array.length - 1;
    if (array[right] < targetValue) {
      return -1;
    } else if (right === 0) {
      return 0;
    }
    while (left <= right) {
      if (right - left <= 1) {
        return left + 1;
      }
      let mid = Math.floor((left + right) / 2);
      if (array[mid] >= targetValue) {
        right = mid;
      } else if (array[mid] < targetValue) {
        left = mid;
      }
    }
  };

  var answer = [];
  var dic = {};
  for (lang of ["java", "python", "cpp", "-"]) {
    for (group of ["frontend", "backend", "-"]) {
      for (career of ["junior", "senior", "-"]) {
        for (food of ["chicken", "pizza", "-"])
          dic[lang + group + career + food] = [];
      }
    }
  }

  const newInfo = Array(info)[0];
  const Q = Array(query)[0];

  for (item of newInfo) {
    const I = item.split(" ").filter((item) => item !== "and");
    for (a of ["-", I[0]]) {
      for (b of ["-", I[1]]) {
        for (c of ["-", I[2]]) {
          for (d of ["-", I[3]]) {
            dic[a + b + c + d].push(+I[4]);
          }
        }
      }
    }
  }
  for (lang of ["java", "python", "cpp", "-"]) {
    for (group of ["frontend", "backend", "-"]) {
      for (career of ["junior", "senior", "-"]) {
        for (food of ["chicken", "pizza", "-"])
          dic[lang + group + career + food].sort((a, b) => a - b);
      }
    }
  }
  for (item of Q) {
    const I = item.split(" ").filter((item) => item !== "and");
    answer.push(
      dic[I[0] + I[1] + I[2] + I[3]].length -
        binarySearch(dic[I[0] + I[1] + I[2] + I[3]], I[4])
    );
  }
  return answer;
}
