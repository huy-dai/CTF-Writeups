import pwn

MAX_LEN = 200
X_BASIS = "x"
Z_BASIS = "+"


def get_num_errs(measurement_str: str) -> int:
    measurement_str = measurement_str.replace("?", "x")

    conn.recvline()  # How many bases would you like to check?
    conn.sendline(str(len(measurement_str)).encode("utf-8"))
    conn.recvline()  # Please enter your xx bases: \r\n

    conn.sendline(measurement_str.encode("utf-8"))
    err_str = conn.recvline().decode("utf-8")  # Errors: ?\r\n

    num_errs = int(err_str[:-2].split(" ")[-1])
    return num_errs


best_str = ""
conn = pwn.remote("misc.chal.csaw.io", 5001)
for i in range(1, MAX_LEN):

    x_errs = get_num_errs(best_str + X_BASIS)
    z_errs = get_num_errs(best_str + Z_BASIS)

    if x_errs < z_errs:
        best_str += X_BASIS
    elif z_errs < x_errs:
        best_str += Z_BASIS
    else:
        best_str += "?"

    print(best_str)

print(best_str)