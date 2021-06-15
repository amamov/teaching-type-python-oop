"""
# * 객체지향 프로그래밍
# * [로봇 관리 프로그램]
# * siri, bixby, jarvis, droid
# * 로봇 이름(name), 로봇 코드번호(code), 로복 제조일자(created_at), 로봇 작동 여부(is_ok), 
# * 로봇 스킬(skill) 점수 : 번역(translate), 계산(cal), 학습(learning)
# * 하드코딩 -> array list 자료구조 사용 -> hash map 자료구조 사용 -> function 자료구조 사용 -> class 자료구조 사용
"""


# * 객체지향 프로그래밍 : using class

from datetime import datetime


class Robot:
    def __init__(self, name, code, created_at, is_ok):
        self.name = name
        self.code = code
        self.created_at = datetime(created_at, 8, 2)
        self.is_ok = is_ok
        self.skills = {}

    def save_skill_grade(self, trans, cal, learn=0):
        self.skills["trans"] = trans
        self.skills["cal"] = cal
        self.skills["learn"] = learn

    @classmethod
    def grade_total(cls, robots):
        total = 0
        for robot in robots:
            total += robot.skills["trans"] + robot.skills["cal"] + robot.skills["learn"]
        return total

    @classmethod
    def all_code(cls, robots):
        codes = []
        for robot in robots:
            codes.append(robot.code)
        return codes


siri = Robot("siri", 129083, 2021, True)
bixby = Robot("bixby", 4637824, 2020, False)
jarvis = Robot("siri", 129083, 2023, True)
droid = Robot("droid", 2364786, 2018, False)


# * robot의 점수를 합산해주는 프로그램


robots = [siri, bixby, jarvis, droid]

robot_total = Robot.grade_total(robots)

print(robot_total)


# * jarvis에서 learn 기능이 사라졌다면??
jarvis.skills["learn"] = 0


print(robot_total)


# * robot의 코드를 반환하는 리스트가 필요하다면?

print(Robot.all_code(robots))


# * droid에서 code 번호 수정이 필요하다면??
droid.code = 12389712

print(Robot.all_code(robots))
