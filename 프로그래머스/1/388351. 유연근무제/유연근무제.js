function solution(schedules, timelogs, startday) {
  let successCount = 0;

  let ignoreDay = [6 - startday, 7 - startday];
  if (ignoreDay[0] < 0) ignoreDay[0] = 6;

  for (let i = 0; i < schedules.length; i++) {
    // schedule 루프
    schedules[i] = schedules[i] + 10;
    // console.log(schedules);
    let getCountBool = true;
    for (let j = 0; j < 7; j++) {
      // if ((j + startday) % 7 === 6 || (j + startday) % 7 === 0) continue;
      // timelog 루프
      if (schedules[i] % 100 >= 60) schedules[i] += 40;
      // console.log(`조정된 스케줄${schedules[i]}`);
      if (
        schedules[i] < timelogs[i][j] &&
        j != ignoreDay[0] &&
        j != ignoreDay[1]
      ) {
        getCountBool = false;
        break;
      }
    }

    if (getCountBool) successCount++;
  }
  console.log(successCount);
  return successCount;
}