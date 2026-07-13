class Solution:
    def convertTimeToSeconds(self, time: str) -> int:
        hours, minutes, seconds = map(int, time.split(":"))
        return hours * 3600 + minutes * 60 + seconds

    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        start_sec = self.convertTimeToSeconds(startTime)
        end_sec = self.convertTimeToSeconds(endTime)

        return end_sec - start_sec
