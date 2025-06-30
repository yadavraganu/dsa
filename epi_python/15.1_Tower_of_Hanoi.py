def toh(disk_num, source, target, help):
    if disk_num == 1:
        print(f"Move disk 1 from {source} to {target}")
    else:
        move_to_help = toh(disk_num - 1, source, help, target)
        print(f"Move disk {disk_num} from {source} to {target}")
        move_from_help = toh(disk_num - 1, help, target, source)

if __name__ == "__main__":
    disk_num = 3
    toh(disk_num, 'A', 'C', 'B')