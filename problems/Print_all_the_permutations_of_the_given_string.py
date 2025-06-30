def all_per_str(ip: str):
    final_res = []

    def _utils(ip, res):
        if len(res) == len(ip):
            final_res.append("".join(res))
            return
        for i in ip:
            res.append(i)
            val = _utils(ip, res)
            res.pop()

    _utils(ip, [])
    return final_res


if __name__ == "__main__":
    print(all_per_str("ABC"))
