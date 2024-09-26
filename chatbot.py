def calculate_bmi(weight, height):
    """
    計算BMI的函數
    :param weight: 體重（公斤）
    :param height: 身高（公尺）
    :return: BMI值
    """
    bmi = weight / (height ** 2)
    return bmi

if __name__ == "__main__":
    # 從使用者那裡獲取體重和身高
    weight = float(input("請輸入您的體重（公斤）："))
    height = float(input("請輸入您的身高（公尺）："))

    # 計算BMI
    bmi = calculate_bmi(weight, height)

    # 輸出BMI值
    print(f"您的BMI值為：{bmi:.2f}")