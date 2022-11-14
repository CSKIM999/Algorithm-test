const cl = console.log;

function solution(info, query) {
  const BS = (array, target) => {
    var left = 0;
    var right = array.length - 1;
    if (target <= array[0]) {
      return 0;
    } else if (target > array[right]) {
      return false;
    } else if (array.length === 0) {
      return false;
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
    const node = BS(dic[I[0] + I[1] + I[2] + I[3]], +I[4]);
    cl(node, dic[I[0] + I[1] + I[2] + I[3]].length);
    node !== false
      ? answer.push(dic[I[0] + I[1] + I[2] + I[3]].length - node)
      : answer.push(0);
  }

  return answer;
}

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
    "cpp and frontend and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150",
  ]
);
