import sched, time

s = sched.scheduler(time.time, time.sleep)

def say(text):
    print(f"[{time.strftime('%H:%M:%S')}] {text}")

start = time.time()
print("Старт. Отсчет времени от t0 = 0\n")

s.enter(2, 1, say, ("Прошло 2 секунды (приоритет 1)",))
s.enter(2, 1, say, ("Прошло 2 секунды (приоритет 0 - сработает ПЕРВЫМ)",))
s.enter(1, 1, say("Прошло 1 секунда",))
s.enterabs(start + 3, 1, say, ("Абсолютное время е0+3 с",))
s.enter(0.5, 1, say, ("Прошло 0.5 секунды",))

print("Очередь до run():", len(s.queue), "задач")
print("run() блокирует поток, пока все задачи не выполняется:\n")
print("\nГотово. Пустая очередь?", s.empty())
