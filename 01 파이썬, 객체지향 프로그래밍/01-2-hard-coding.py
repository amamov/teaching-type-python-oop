"""
# * hard-coding
# * [로봇 관리 프로그램]
# * siri, bixby, jarvis, droid
# * 로봇 이름(name), 로봇 코드번호(code), 로봇 제조일자(created_at), 로봇 작동 여부(is_ok), 
# * 로봇 스킬(skill) 점수 : 번역(translate), 계산(cal), 학습(learning)
# * 하드코딩 -> array list 자료구조 사용 -> hash map 자료구조 사용 -> function 자료구조 사용 -> class 자료구조 사용
"""

from datetime import datetime

# * 하드코딩

robot_name_1 = "siri"
robot_code_1 = 912083902
robot_created_at_1 = datetime(2012, 4, 3)
robot_is_ok_1 = True
robot_skill_grade_1 = {
    "trans": 98,
    "cal": 48,
    "learn": 88,
}

robot_name_2 = "bixby"
robot_code_2 = 12348979128
robot_created_at_2 = datetime(2032, 6, 4)
robot_is_ok_2 = False
robot_skill_grade_2 = {
    "trans": 45,
    "cal": 32,
    "learn": 22,
}

robot_name_3 = "jarvis"
robot_code_3 = 234792387
robot_created_at_3 = datetime(2012, 6, 3)
robot_is_ok_3 = True
robot_skill_grade_3 = {
    "trans": 21,
    "cal": 19,
    "learn": 90,
}

robot_name_4 = "droid"
robot_code_4 = 12749234
robot_created_at_4 = datetime(2032, 6, 3)
robot_is_ok_4 = True
robot_skill_grade_4 = {
    "trans": 432,
    "cal": 324,
    "learn": 123,
}


# * list 자료구조 사용
robot_name = ["siri", "bixby", "jarvis", "droid"]
robot_code = [912083902, 12348979128, 234792387, 12749234]
robot_created_at = [
    datetime(2012, 4, 3),
    datetime(2032, 6, 4),
    datetime(2012, 6, 3),
    datetime(2032, 6, 3),
]
robot_is_ok = [True, False, True, True]
robot_skill_grade = [
    {
        "trans": 98,
        "cal": 48,
        "learn": 88,
    },
    {
        "trans": 45,
        "cal": 32,
        "learn": 22,
    },
    {
        "trans": 21,
        "cal": 19,
        "learn": 90,
    },
    {
        "trans": 432,
        "cal": 324,
        "learn": 123,
    },
]

print(robot_name[0])
print(robot_name[2])
print(robot_name[3])

# * dict 자료구조

siri = {
    "name": "siri",
    "code": 129083,
    "created_at": datetime(2021, 8, 2),
    "is_ok": True,
    "skill_grade": {"trans": 98, "cal": 50, "learn": 40},
}

bixby = {
    "name": "bixby",
    "code": 4637824,
    "created_at": datetime(2020, 8, 2),
    "is_ok": False,
    "skill_grade": {"trans": 45, "cal": 98, "learn": 67},
}

jarvis = {
    "name": "jarvis",
    "code": 2364786,
    "created_at": datetime(2023, 8, 2),
    "is_ok": True,
    "skill_grade": {"trans": 25, "cal": 78, "learn": 68},
}

droid = {
    "name": "droid",
    "code": 2364786,
    "created_at": datetime(2018, 8, 2),
    "is_ok": False,
    "skill_grade": {"trans": 67, "cal": 30, "learn": 21},
}


# * fucntion


def robot(name, code, created_at, is_ok, skill_grade):
    return {
        "name": name,
        "code": code,
        "created_at": created_at,
        "is_ok": is_ok,
        "skill_grade": skill_grade,
    }


siri = robot("siri", 129083, 2021, True, {"trans": 98, "cal": 50, "learn": 40})
bixby = robot("bixby", 4637824, 2020, False, {"trans": 45, "cal": 98, "learn": 67})
jarvis = robot("siri", 129083, 2023, True, {"trans": 25, "cal": 78, "learn": 68})
droid = robot("droid", 2364786, 2018, False, {"trans": 67, "cal": 30, "learn": 21})
droid_2 = robot(
    "droid-2", 2364781236, 2018, False, {"trans": 67, "cal": 30, "learn": 21}
)


# * class


class Robot:
    def __init__(self, name, code, created_at, is_ok, skill_grade):
        self.name = name
        self.code = code
        self.created_at = created_at
        self.is_ok = is_ok
        self.skill_grade = skill_grade


siri = Robot("siri", 129083, 2021, True, {"trans": 98, "cal": 50, "learn": 40})
bixby = Robot("bixby", 4637824, 2020, False, {"trans": 45, "cal": 98, "learn": 67})
jarvis = Robot("siri", 129083, 2023, True, {"trans": 25, "cal": 78, "learn": 68})
droid = Robot("droid", 2364786, 2018, False, {"trans": 67, "cal": 30, "learn": 21})
droid_2 = Robot(
    "droid-2", 2364781236, 2018, False, {"trans": 67, "cal": 30, "learn": 21}
)
