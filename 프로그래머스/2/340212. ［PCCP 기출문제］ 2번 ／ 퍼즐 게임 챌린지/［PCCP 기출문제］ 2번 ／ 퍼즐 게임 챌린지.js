function solution(diffs, times, limit) {
  let low = 1;
  let high = 100001;
  while (low <= high) {
    let midLevel = Math.floor((low + high) / 2);

    let levelTime = helper(midLevel, diffs, times, limit);
    // console.log(`현재: ${levelTime}, 최대: ${limit}, 현재레벨:${i}`);
    if (levelTime) high = midLevel - 1;
    else low = midLevel + 1;
  }
  return low;
}

function helper(level, diffs, times, limit) {
  let sum = times[0];

  for (let i = 1; i < diffs.length; i++) {
    if (level >= diffs[i]) sum += times[i];
    else sum += (diffs[i] - level) * (times[i - 1] + times[i]) + times[i];

    if (sum > limit) return false;
  }

  return true;
}