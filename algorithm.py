a = [int(x) for x in input().split(":")]
b = [int(x) for x in input().split(":")]

start_time = a[0] * 3600 + a[1] * 60 + a[2]
end_time = b[0] * 3600 + b[1] * 60 + b[2]

if start_time > end_time:
    end_time += 24 * 3600

time_diff =  end_time - start_time

def lead_zero(n):
    return f"0{n}" if n < 10 else n

print(f"{lead_zero(time_diff // 3600)}:{lead_zero(time_diff % 3600 // 60)}:{lead_zero(time_diff % 60)}")