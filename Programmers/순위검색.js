const cl = console.log;

function solution(info, query) {
  const binarySearch = (array, targetValue) => {
    let left = 0;
    let right = array.length - 1;

    while (left <= right) {
      if (right - left <= 1) {
        if (array[left] === targetValue) {
          return left;
        } else {
          return left + 1;
        }
      }
      let mid = Math.floor((left + right) / 2);
      if (array[mid] >= targetValue) {
        right = mid;
      } else if (array[mid] < targetValue) {
        left = mid;
      }
    }
  };

  const BS = (array, target) => {
    var left = 0;
    var right = array.length - 1;
    if (target <= array[0]) {
      return 0;
    } else if (target > array[right]) {
      return right;
    }
    while (left <= right) {
      if (right - left == 1) {
        if (array[left] === target) {
          return left;
        }
        return left + 1;
      }
      var mid = Math.floor((right + left) / 2);
      if (array[mid] >= target) {
        right = mid;
      } else {
        left = mid;
      }
    }
  };

  var answer = [];
  var dic = {};
  const newInfo = Array(info)[0];
  const Q = Array(query)[0];

  for (lang of ["java", "python", "cpp", "-"]) {
    for (group of ["frontend", "backend", "-"]) {
      for (career of ["junior", "senior", "-"]) {
        for (food of ["chicken", "pizza", "-"])
          dic[lang + group + career + food] = [];
      }
    }
  }

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
        BS(dic[I[0] + I[1] + I[2] + I[3]], +I[4])
    );
  }

  const test = [1, 2, 3, 4, 5, 6, 7, 8, 9].sort((a, b) => a - b);
  const testNum = 10;
  console.log(">>>> test", BS(test, testNum));
  return answer;
}

console.log(
  solution(
    [
      "java backend junior pizza 150",
      "python frontend senior chicken 210",
      "python frontend senior chicken 150",
      "cpp backend senior pizza 260",
      "java backend junior chicken 80",
      "python backend senior chicken 50",
    ],
    [
      "java and backend and junior and pizza 100",
      "python and frontend and senior and chicken 200",
      "cpp and - and senior and pizza 250",
      "- and backend and senior and - 150",
      "- and - and - and chicken 100",
      "- and - and - and - 150",
      "- and - and - and - 5000",
    ]
  )
);
