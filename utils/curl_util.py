def sample_util(cnt : int):
    with open(f"/Users/kimdohoon/Desktop/CURLTEST/{cnt}.txt", "w") as file:
        file.write("TEST is SUCCEED")
    return (f"{cnt} test is finished")