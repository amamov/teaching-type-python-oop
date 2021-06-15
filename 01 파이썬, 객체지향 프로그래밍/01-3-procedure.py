"""
# * 절차지향 프로그래밍
# * [로봇 관리 프로그램]
# * siri, bixby, jarvis, droid
# * 로봇 이름(name), 로봇 코드번호(code), 로복 제조일자(created_at), 로봇 작동 여부(is_ok), 
# * 로봇 스킬(skill) 점수 : 번역(translate), 계산(cal), 학습(learning)
# * 하드코딩 -> array list 자료구조 사용 -> hash map 자료구조 사용 -> function 자료구조 사용 -> class 자료구조 사용
"""

# * 절차지향 프로그래밍

from datetime import datetime


def robot(name, code, created_at, is_ok, skill_grade):
    return {
        "name": name,
        "code": code,
        "created_at": datetime(created_at, 8, 2),
        "is_ok": is_ok,
        "skill_grade": skill_grade,
    }


siri = robot("siri", 129083, 2021, True, {"trans": 98, "cal": 50, "learn": 40})
bixby = robot("bixby", 4637824, 2020, False, {"trans": 45, "cal": 98, "learn": 67})
jarvis = robot("siri", 129083, 2023, True, {"trans": 25, "cal": 78, "learn": 68})
droid = robot("droid", 2364786, 2018, False, {"trans": 67, "cal": 30, "learn": 21})


# * robot의 점수를 합산해주는 프로그램
def robot_grade_total(robots):
    total = 0
    for robot in robots:
        total += (
            robot["skill_grade"]["trans"]
            + robot["skill_grade"]["cal"]
            + robot["skill_grade"]["learn"]
        )
    return total


robots = [siri, bixby, jarvis, droid]

robot_total = robot_grade_total(robots)

print(robot_total)


# * jarvis에서 learn 기능이 사라졌다면??
jarvis = robot("siri", 129083, 2023, True, {"trans": 25, "cal": 78})


# robots = [siri, bixby, jarvis, droid]

# robot_total = robot_grade_total(robots)

# print(robot_total)

robots = [siri, bixby, droid]

robot_total = robot_grade_total(robots)


def special_robot_total(robot):
    return robot["skill_grade"]["trans"] + robot["skill_grade"]["cal"]


print(robot_total + special_robot_total(jarvis))

# * robot의 코드를 반환하는 리스트가 필요하다면?


robots.append(jarvis)


codes = []
for robot in robots:
    codes.append(robot["code"])

print(codes)


# * droid에서 code 번호 수정이 필요하다면??
droid["code"] = 23189712

codes = []
for robot in robots:
    codes.append(robot["code"])

print(codes)
