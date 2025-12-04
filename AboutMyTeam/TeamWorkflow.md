# Team Workflow

## Team Members

| STD-ID   | Name                  | Role     | Responsibilities                                                                 |
|----------|----------------------|---------|-------------------------------------------------------------------------------|
| 016-8    | นราธิป พรหมประกาย   | Admin   | สร้าง repository, สร้างโฟลเดอร์ Project/AboutMyTeam, สร้าง WorkFlow.md, Merge branch ของสมาชิกทั้งหมด |
| 216-0    | ปกรณ์ จำนงค์นารถ     | Maintain| ตรวจสอบโค้ด, Review Pull Request, แนะนำปรับปรุง logic และ style             |
| 025-7    | วีรภัทร วิเศษสมบัติ  | Write   | เขียนโปรแกรม Bubble Sort, เขียนไฟล์โปรไฟล์ของตัวเอง                         |



## Team Collaboration Process

1. **Branch per Member**  
   - สมาชิกทุกคนสร้าง branch ของตัวเอง เช่น `Narathip_0168`, `Pakorn_2160`,`Veerapat_0257`  
   - ทุกคนทำงานบน branch ของตัวเองเท่านั้น

2. **Write Role**
   - สร้างไฟล์โปรแกรม Bubble Sort (`Project/bubble_sort.py`)  
   - รับ input เป็นจำนวนเต็มและแปลงเป็น int  
   - ใส่ exception handling กรณี input ไม่ถูกต้อง หรือ error ที่ไม่คาดคิด

3. **Maintain Role**
   - ตรวจสอบโค้ดใน branch ของสมาชิก  
   - Review logic ของ Bubble Sort และผลลัพธ์  
   - ให้คำแนะนำก่อน merge

4. **Admin Role**
   - Merge branch ของสมาชิกเข้ากับ `main`  
   - ตรวจสอบว่าไฟล์ `.md` และโปรแกรมอยู่ครบในโฟลเดอร์ `Project`  

---

## Bubble Sort Python Example

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def main():
    try:
        nums = input("Enter integers separated by space: ").strip().split()
        nums = [int(x) for x in nums]
        sorted_nums = bubble_sort(nums)
        print("Sorted numbers:", sorted_nums)
    except ValueError:
        print("Error: Please enter valid integers only.")
    except Exception as e:
        print("Unexpected error:", e)

if __name__ == "__main__":
    main()
```
