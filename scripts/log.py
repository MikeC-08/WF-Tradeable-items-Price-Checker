import os
import time
import queue
import re

ready = queue.Queue(1)
void_drops = queue.Queue(1)
shotdown = queue.Queue(1)
log_message = queue.Queue()
sleep_var = {
    "slow": 0.5,
    "fast": 0.05
}
speed = "slow"
timeout = False
start_waiting = 0
count = 1

def tail_ee_log(file_path):
    global speed, timeout, start_waiting, count
    if not os.path.exists(file_path):
        print(f"找不到文件: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        f.seek(0, os.SEEK_END)
        print("正在追蹤 EE.log... (等待新事件)")
        ready.put(1)
        while True:
            current_pos = f.tell()
            line = f.readline()
            if time.time() > start_waiting + 2 and start_waiting > 0 :
                timeout = True
                start_waiting = 0
                print(f"開始選擇物品| {count}選1 (timeout)")
                log_message.put(f"開始選擇物品| {count}選1 (t)")
                void_drops.put(count)
                count = 1
            if not line and shotdown.empty():
                f.seek(current_pos)
                time.sleep(sleep_var[speed])
                continue
            
            yield line.strip()

def log_checker():
    global speed, timeout, start_waiting, count
    log_path = os.path.expandvars(r'%LOCALAPPDATA%\Warframe\EE.log')
    # log_path = os.path.expandvars(r'ee.log')
    
    waiting = False
    try:
        for new_line in tail_ee_log(log_path):
            if "SQUAD Session has " in new_line:
                result = re.search(r"SQUAD Session has (.*?)/4", new_line)
                if result:
                    log_message.put(f"人數{result[1]}/4")
                    print(f"* {result[1]}/4")
                    count = int(result[1])
            
            elif "Still waiting on response" in new_line:
                if not waiting:
                    start_waiting = time.time()
                    waiting = True


                
            elif "gets reward /" in new_line and not timeout:
                start_waiting = 0
                print(f"開始選擇物品| {count}選1 (gets reward)")
                time.sleep(3)
                void_drops.put(count)
                count = 1
                
            elif "VoidProjections: GetVoidProjectionRewards" in new_line and not timeout:
                start_waiting = 0
                print(f"開始選擇物品| {count}選1 (VoidProjections)")
                time.sleep(3)
                void_drops.put(count)
                count = 1
                
            elif "ProjectionRewardChoice.lua: Relic reward screen shut down" in new_line:
                # print("選擇階段結束")
                void_drops.put(-1)
                speed = "slow"
                timeout = False
                waiting = False
                
            elif not shotdown.empty():
                break
    except Exception as e:
        print(f"[ERROR] log_checker 執行緒失敗: {repr(e)}")
        import traceback
        traceback.print_exc()
    except KeyboardInterrupt:
        print("停止追蹤。")
