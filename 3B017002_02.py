import json
import os


def read_json_file(filename: str) -> dict:
    """
    讀取並返回 JSON 檔案的內容。

    Args:
        filename: 要讀取的 JSON 檔案的檔名。

    Returns:
        dict: JSON 檔案的內容。
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: 檔案 '{filename}' 沒找到.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: 無法解碼Json檔： '{filename}'.")
        return {}


def get_student_info(data: dict, student_id: str) -> dict:
    """
    根據學號返回該學生的個人資料字典，找不到該學生則拋出 ValueError。

    Args:
        data: 包含學生資料的字典。
        student_id: 學生的學號。

    Returns:
        dict: 學生的個人資料字典。
    """
    for student in data:
        if student['student_id'] == student_id:
            # 對課程名稱進行單獨處理，確保中文字符被解析

            return student
    raise ValueError(f"學號 {student_id} 找不到.")


def add_course(data: dict, student_id: str, course_name: str, course_score: float) -> None:
    """
    為指定學生添加一門課程及其分數，如果找不到該學生則拋出 ValueError，並檢查課程名稱和分數不可為空字串。

    Args:
        data: 包含學生資料的字典。
        student_id: 學生的學號。
        course_name: 課程名稱。
        course_score: 課程分數。

    Raises:
        ValueError: 找不到學生或課程名稱和分數為空字串。
    """
    if course_name == "" or course_score == "":
        raise ValueError("課程名稱或分數不可空白.")

    for student in data:
        if student['student_id'] == student_id:
            student['courses'].append({'name': course_name, 'score': course_score})
            return
    raise ValueError(f"學號 {student_id} 找不到.")


def calculate_average_score(student_data: dict) -> float:
    """
    計算並返回一位學生所有課程的平均分數，如果該學生沒有課程，則返回 0.0。

    Args:
        student_data: 學生的資料字典。

    Returns:
        float: 學生所有課程的平均分數。
    """
    if not student_data['courses']:
        return 0.0

    total_score = sum(course['score'] for course in student_data['courses'])
    return total_score / len(student_data['courses'])


# 主程式
def main():
    filename = 'students.json'
    if not os.path.isfile(filename):
        print(f"Error: 檔案 '{filename}' 不存在.")
        return

    data = read_json_file(filename)
    if not data:
        return

    while True:
        print("***************選單***************")
        print("1. 查詢指定學號成績")
        print("2. 新增指定學號的課程名稱與分數")
        print("3. 顯示指定學號的各科平均分數")
        print("4. 離開")
        print("**********************************")
        choice = input("請選擇操作項目：")

        if choice == '1':
            student_id = input("請輸入學號: ")
            try:
                student_info = get_student_info(data, student_id)  # 此處修正
                print("=>學生資料:", json.dumps(student_info, indent=2, ensure_ascii=False))

            except ValueError as e:
                print(f"=>發生錯誤: {e}")

        elif choice == '2':
            student_id = input("請輸入學號: ")
            course_name = input("請輸入要新增課程的名稱: ")
            course_score_input = input("請輸入要新增課程的分數: ")
            if course_score_input.strip():  # 檢查課程分數是否為空字串
                try:
                    course_score = float(course_score_input)
                    add_course(data, student_id, course_name, course_score)
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                    print("=>課程已成功新增。")
                except ValueError as e:
                    print(f"=>其它例外: {e}")
            else:
                print("=>其它例外: 課程名稱或分數不可空白.")
        elif choice == '3':
            student_id = input("請輸入學號: ")
            try:
                student_info = get_student_info(data, student_id)  # 此處修正
                average_score = calculate_average_score(student_info)
                print("=>各科平均分數:", average_score)
            except ValueError as e:
                print(f"=>發生錯誤: {e}")

        elif choice == '4':
            print("=>程式結束。")
            break

        else:
            print("=>請輸入有效的選項。")


if __name__ == "__main__":
    main()
