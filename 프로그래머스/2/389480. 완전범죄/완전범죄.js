// function solution(info, n, m) {
//   info.sort((a, b) => {
//     if (a[0] == b[0]) return a[1] - b[1];
//     else return b[0] - a[0];
//   });
//   let b_sum = 0;
//   let i = 0;
//   while (info.length !== 0) {
//     if (i === info.length || b_sum === m - 1) break;

//     if (b_sum + info[i][1] < m) {
//       b_sum += info[i][1];
//       info.splice(i, 1);
//     } else {
//       i++;
//     }
//   }
//   //   console.log(info);

//   let a_sum = 0;
//   let j = info.length - 1;
//   while (j !== -1) {
//     // 다 잡거나 a가 넘어가면
//     if (a_sum + info[j][0] < n) {
//       a_sum += info[j][0];
//       j--;
//     } else {
//       a_sum = -1;
//       break;
//     }
//   }
//   console.log(a_sum);
//   return a_sum;
// }

function solution(info, n, m) {
    var answer = 0;

    // A 대비 B가 훔쳤을 때 가성비가 좋은 비율 순으로 내림차순 정렬
    // 같은 경우 B가 훔쳤을 때 큰 값 순으로 정렬
    info.sort((a,b) => {
        const aRatio = a[0]/a[1];
        const bRatio = b[0]/b[1];

        return aRatio !== bRatio ? bRatio-aRatio : b[1] - a[1];
    });

    // B가 m이 넘지않는 범위에서 최대 훔칠 수 있는 흔적의 합 계산
    // 그 외는 전부 A가 훔치는 걸로 생각
    let sumB = 0;
    for (let i = 0; i< info.length; i++){
        if (sumB+info[i][1] < m){
            sumB+=info[i][1];
        } else {
            answer+=info[i][0];
        }
    }

    return answer >= n ? -1 : answer;
}