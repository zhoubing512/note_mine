# -*- coding: UTF-8 -*-
import re, psutil, time, sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, '..')
import cmsc.time_tools as tt

class NvidiaInfo:
    """
    Nvidia显卡信息的类。只用于两台jisuan服务器中。
    如何使用：
        定义对象：ni = MODULE_NAME.NvidiaInfo()
        使用方式1：print(ni)
        使用方式2：ni.print_nvidia_info()
        使用方式3：ni
    """
    def __init__(self, nvinfo_file = '/share/sysinfo/nvidia-info', psinfo_file = '/share/sysinfo/psinfo'):
        self.__nvinfo_file = nvinfo_file
        self.__psinfo_file = psinfo_file
        self.nvidia_info = None

    # 当 nvidia_info 被读取时 自动刷新
    def __getattribute__(self, item):
        if item == 'nvidia_info':
            self.__refresh_nvidia_info()
            return self.__nvidia_info
        else:
            return super().__getattribute__(item)

    # 从self.nvidia_info取得所有的gpu
    def __get_sys_gpu(self):
        for info in self.__nvidia_info:
            if info[:4] == "GPU ":
                yield info

    # 从psinfo文件获取进程信息，存入self.psinfo字典
    def __parse_psinfo(self):
        self._psinfo = {}
        with open(self.__psinfo_file, 'r') as file:
            ps_lines = file.readlines()

        for pinfo in ps_lines:
            ps_match = re.match('^(\S+) +(\S+) +\S+ +\S+ +(\S+) +\S+ +\S+ +(.+)', pinfo)
            if ps_match:
                self._psinfo[ps_match.group(2)] = {"user": ps_match.group(1), "stime": ps_match.group(3),
                                             "cmd": ps_match.group(4)}

    # 从nvidia-info文件解析系统的显卡信息
    def __parse_nvidia_info(self):
        self.__nvidia_info = {}
        with open(self.__nvinfo_file, 'r') as file:
            info_list = file.readlines()

        cur_dict = self.__nvidia_info
        # 当前数据的缩进层级
        cur_level = 0
        # 用来标记是否缩进, 缩进需要建立子字典
        shift_flag = False
        # 用来标记缩进了却未建立子字典的情况
        unshift_flag = False
        # 用来标记是否已开始读取进程信息
        reading_process = False
        # 使用一个栈来存储父字典
        dict_stack = []
        for line in info_list:
            # 空行或注释行 则跳过
            if line.strip() == "" or re.match('====', line): continue

            # 是否有键值对
            key_val_match = re.match('^( *)([\S ]+) : (.+)', line)
            # 用于无键值对的 行数据获取
            match_key = re.match('^( *)([\S ]+)', line)
            last_level, cur_level = cur_level, len(match_key.group(1)) // 4

            # 是否需要弹出到上级字典
            if last_level > cur_level and not reading_process:
                for i in range(last_level - cur_level - unshift_flag):
                    cur_dict = dict_stack.pop()
                unshift_flag = False

            # 如果不是键值对 则需要建立子字典  Processes除外
            if not key_val_match:
                dict_stack.append(cur_dict)
                cur_dict[match_key.group(2).strip()] = {} if match_key.group(2).strip() != "Processes" else []
                cur_dict = cur_dict[match_key.group(2).strip()]
                reading_process = match_key.group(2).strip() == "Processes"
                shift_flag = True
            # 如果是键值对 则更新数据
            else:
                # 当没有进程时Processes的值为None, 是键值对的形式, 不会走上一步, 因此这里还需要建一个空列表
                if key_val_match.group(2).strip() == "Processes":
                    cur_dict[key_val_match.group(2).strip()] = []
                    continue

                # 如果已开始读取进程信息
                if reading_process and key_val_match.group(2).strip() in (
                "Process ID", "Type", "Name", "Used GPU Memory"):
                    # 开始读取
                    if key_val_match.group(2).strip() == "Process ID": process = {}
                    # 更新数据
                    process[key_val_match.group(2).strip()] = key_val_match.group(3).strip()
                    # 读取完毕 更新到进程列表
                    if key_val_match.group(2).strip() == "Used GPU Memory": cur_dict.append(process)
                    continue

                # 如果未开始读取进程信息
                cur_dict[key_val_match.group(2).strip()] = key_val_match.group(3).strip()
                # 如果缩进了, 但是未建立子字典, 做一个标记
                if last_level < cur_level and not shift_flag: unshift_flag = True
                # 使用后恢复缩进标记
                shift_flag = False
        # for循环完成后 self.nvidia_info 已更新

    # 使用psinfo更新nvidia_info
    def __update_nvidia_info(self):
        for gpu in self.__get_sys_gpu():
            try:
                for proc in self.__nvidia_info[gpu]["Processes"]:
                    pid = proc["Process ID"]
                    # 使用psinf更新进程信息
                    proc["CMD"] = ' '.join(self._psinfo[pid]['cmd'].split())
                    proc["Process Inner ID"] = pid
                    proc["User"] = self._psinfo[pid]['user']
                    proc["Stime"] = self._psinfo[pid]['stime']
                    # 更新容器内部对应的inner_pid
                    inner_ppids = {}
                    for inner_proc in psutil.process_iter():
                        if ' '.join(' '.join(inner_proc.cmdline()).split()) == proc["CMD"] and inner_proc.username() == proc[
                            "User"] \
                                and proc["Stime"] in time.strftime("%b%d %H:%M %Y %m月%d %m月%d日",
                                                                time.localtime(inner_proc.create_time())).split():
                            inner_ppids[inner_proc.pid] = inner_proc.ppid()
                    for pi in inner_ppids:
                        if inner_ppids[pi] not in inner_ppids:
                            proc["Process Inner ID"] = str(pi)
                            break
            except:
                print("'Please run again to refresh! ")

    def _fill_title(self, title, title_len = 26):
        title = title + ' ' * max(title_len - len(title), 1)
        return title

    def __refresh_nvidia_info(self):
        self.__parse_psinfo()
        self.__parse_nvidia_info()
        self.__update_nvidia_info()

    def print_nvidia_info(self, title_len = 26):
        # ft = self._fill_title
        # self.__refresh_nvidia_info()
        nvidia_info = self.nvidia_info
        print("\n============================ Nvidia Infomation ============================")
        try: 
            print(f"System Info")
            print("{0:{len}}: {1}".format('Time', tt.format_unixtime(tt.to_unixtime(nvidia_info['Timestamp'])), len = title_len))
            print("{0:{len}}: {1}".format('Driver Version', nvidia_info['Driver Version'], len = title_len))
            print("{0:{len}}: {1}".format('CUDA Version', nvidia_info['CUDA Version'], len = title_len))
            print("{0:{len}}: {1}".format('Attached GPUs', nvidia_info['Attached GPUs'], len = title_len))
            # print(f"{ft('Time')}: {tt.format_unixtime(tt.to_unixtime(nvidia_info['Timestamp']))}")

            for i, gpu in enumerate(self.__get_sys_gpu()):
                print("\n{0:{len}}: {1}".format('GPU', i, len = title_len))
                print("{0:{len}}: {1}".format('Bus-Id', ' '.join(gpu.split()[1:]), len = title_len))
                print("{0:{len}}: {1}".format('GPU Name', nvidia_info[gpu]['Product Name'], len = title_len))
                print("{0:{len}}: {1}".format('Persistence Mode', nvidia_info[gpu]['Persistence Mode'], len = title_len))
                print("{0:{len}}: {1}".format('Display Active', nvidia_info[gpu]['Display Active'], len = title_len))
                print("{0:{len}}: {1}".format('Performance State', nvidia_info[gpu]['Performance State'], len = title_len))
                print("{0:{len}}: {1}".format('Compute Mode', nvidia_info[gpu]['Compute Mode'], len = title_len))

                print("{mu:{len}}: {used:s} / {total:s} ({usage:.2f} %)".format(
                    mu = 'Memory Usage'
                    , used = nvidia_info[gpu]['FB Memory Usage']['Used']
                    , total = nvidia_info[gpu]['FB Memory Usage']['Total']
                    , usage = 100 * int(nvidia_info[gpu]['FB Memory Usage']['Used'].split()[0]) / int(
                        nvidia_info[gpu]['FB Memory Usage']['Total'].split()[0])
                    , len = title_len
                ))
                print("{0:{len}}: {1}".format('GPU Usage', nvidia_info[gpu]['Utilization']['Gpu'], len = title_len))
                print("{0:{len}}: {1}".format('Power Usage', nvidia_info[gpu]['Power Readings']['Power Draw'] + ' / ' + nvidia_info[gpu]['Power Readings']['Power Limit'], len = title_len))
                print("{0:{len}}: {1}".format('Temperature', nvidia_info[gpu]['Temperature']['GPU Current Temp'] + ' / ' + nvidia_info[gpu]['Temperature']['GPU Shutdown Temp'], len = title_len))
                print("{0:{len}}: {1}".format('Volatile Uncorr. ECC(SB)', nvidia_info[gpu]['ECC Errors']['Volatile']['Single Bit']['Total'], len = title_len))
                print("{0:{len}}: {1}".format('Volatile Uncorr. ECC(DB)', nvidia_info[gpu]['ECC Errors']['Volatile']['Double Bit']['Total'], len = title_len))

                print(f"Processes:")
                # print(f"{ft('', 4)}{ft('PID', 6)}{ft('USER', 8)}{ft('MEMORY', 10)}{ft('STIME', 7)}CMD")
                print("{0:4}{1:6}{2:8}{3:10}{4:7}{5}".format('', 'PID', 'USER', 'MEMORY', 'STIME', 'CMD'))
                for i, proc in enumerate(nvidia_info[gpu]["Processes"]):
                    # print('\t'.join([str(i), proc["Process Inner ID"], proc["User"], proc["Used GPU Memory"], proc["Stime"], proc["CMD"]]))
                    # print(f"{ft(str(i), 4)}{ft(proc['Process Inner ID'], 6)}{ft(proc['User'], 8)}{ft(proc['Used GPU Memory'], 10)}{ft(proc['Stime'], 7)}{proc['CMD']}")
                    print("{0:4}{1:6}{2:8}{3:10}{4:7}{5}".format(str(i), proc['Process Inner ID'], proc['User'], proc['Used GPU Memory'], proc['Stime'], proc['CMD']))
        except:
            print("'Please run again to refresh! ")
        print("\n========================== Nvidia Infomation End ==========================")

    def __to_info_str(self, title_len = 26):
        nvidia_info = self.nvidia_info
        info_list = ["\n============================ Nvidia Infomation ============================"]
        try: 
            info_list.append(f"System Info")
            info_list.append("{0:{len}}: {1}".format('Time', tt.format_unixtime(tt.to_unixtime(nvidia_info['Timestamp'])), len = title_len))
            info_list.append("{0:{len}}: {1}".format('Driver Version', nvidia_info['Driver Version'], len = title_len))
            info_list.append("{0:{len}}: {1}".format('CUDA Version', nvidia_info['CUDA Version'], len = title_len))
            info_list.append("{0:{len}}: {1}".format('Attached GPUs', nvidia_info['Attached GPUs'], len = title_len))
            # info_list.append(f"{ft('Time')}: {tt.format_unixtime(tt.to_unixtime(nvidia_info['Timestamp']))}")

            for i, gpu in enumerate(self.__get_sys_gpu()):
                info_list.append("\n{0:{len}}: {1}".format('GPU', i, len = title_len))
                info_list.append("{0:{len}}: {1}".format('Bus-Id', ' '.join(gpu.split()[1:]), len = title_len))
                info_list.append("{0:{len}}: {1}".format('GPU Name', nvidia_info[gpu]['Product Name'], len = title_len))
                info_list.append("{0:{len}}: {1}".format('Persistence Mode', nvidia_info[gpu]['Persistence Mode'], len = title_len))
                info_list.append("{0:{len}}: {1}".format('Display Active', nvidia_info[gpu]['Display Active'], len = title_len))
                info_list.append("{0:{len}}: {1}".format('Performance State', nvidia_info[gpu]['Performance State'], len = title_len))
                info_list.append("{0:{len}}: {1}".format('Compute Mode', nvidia_info[gpu]['Compute Mode'], len = title_len))

                info_list.append("{mu:{len}}: {used:s} / {total:s} ({usage:.2f} %)".format(
                    mu = 'Memory Usage'
                    , used = nvidia_info[gpu]['FB Memory Usage']['Used']
                    , total = nvidia_info[gpu]['FB Memory Usage']['Total']
                    , usage = 100 * int(nvidia_info[gpu]['FB Memory Usage']['Used'].split()[0]) / int(
                        nvidia_info[gpu]['FB Memory Usage']['Total'].split()[0])
                    , len = title_len
                ))
                info_list.append("{0:{len}}: {1}".format('GPU Usage', nvidia_info[gpu]['Utilization']['Gpu'], len = title_len))
                info_list.append("{0:{len}}: {1}".format('Power Usage', nvidia_info[gpu]['Power Readings']['Power Draw'] + ' / ' + nvidia_info[gpu]['Power Readings']['Power Limit'], len = title_len))
                info_list.append("{0:{len}}: {1}".format('Temperature', nvidia_info[gpu]['Temperature']['GPU Current Temp'] + ' / ' + nvidia_info[gpu]['Temperature']['GPU Shutdown Temp'], len = title_len))
                info_list.append("{0:{len}}: {1}".format('Volatile Uncorr. ECC(SB)', nvidia_info[gpu]['ECC Errors']['Volatile']['Single Bit']['Total'], len = title_len))
                info_list.append("{0:{len}}: {1}".format('Volatile Uncorr. ECC(DB)', nvidia_info[gpu]['ECC Errors']['Volatile']['Double Bit']['Total'], len = title_len))

                info_list.append(f"Processes:")
                # info_list.append(f"{ft('', 4)}{ft('PID', 6)}{ft('USER', 8)}{ft('MEMORY', 10)}{ft('STIME', 7)}CMD")
                info_list.append("{0:4}{1:6}{2:8}{3:10}{4:7}{5}".format('', 'PID', 'USER', 'MEMORY', 'STIME', 'CMD'))
                for i, proc in enumerate(nvidia_info[gpu]["Processes"]):
                    # info_list.append('\t'.join([str(i), proc["Process Inner ID"], proc["User"], proc["Used GPU Memory"], proc["Stime"], proc["CMD"]]))
                    # info_list.append(f"{ft(str(i), 4)}{ft(proc['Process Inner ID'], 6)}{ft(proc['User'], 8)}{ft(proc['Used GPU Memory'], 10)}{ft(proc['Stime'], 7)}{proc['CMD']}")
                    info_list.append("{0:4}{1:6}{2:8}{3:10}{4:7}{5}".format(str(i), proc['Process Inner ID'], proc['User'], proc['Used GPU Memory'], proc['Stime'], proc['CMD']))
        except:
            info_list.append('Please run again to refresh! ')
        info_list.append("\n========================== Nvidia Infomation End ==========================")
        return '\n'.join(info_list)

    # 当类被作为string使用时的值
    def __str__(self):
        return self.__to_info_str()

    # 当类被直接运行时的值
    def __repr__(self):
        return self.__to_info_str()
    