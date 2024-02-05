import sqlite3

Connection = sqlite3.connect("TESTDB.db")
Cursor = Connection.cursor()

class Database:
    def getAllStudents():
        Cursor.execute("SELECT * FROM STUDENTS ORDER BY Name ASC;")
        Students = Cursor.fetchall()
        return Students

    def updateStudent(columnName, newValue, where):
        Cursor.execute("UPDATE STUDENTS SET "+columnName+" = ? WHERE ID = ?;", (newValue, where,))
        print("Veri güncellendi.")
        print(Database.getAllStudents())

    def searchStudent(value):
        value = '%' + value + '%'
        Cursor.execute("SELECT * FROM STUDENTS WHERE Name LIKE ? OR Surname LIKE ?;", (value, value,))
        Students = Cursor.fetchall()
        return Students

    def getAllStudents():
        Cursor.execute("SELECT * FROM STUDENTS ORDER BY Name ASC;")
        Students = Cursor.fetchall()
        return Students

    def deleteStudents(studentID):
        Cursor.execute("DELETE FROM STUDENTS WHERE ID = ?;", (studentID,))
        print("Öğrenci silindi.")
        print(Database.getAllStudents())

    def instertStudents(studentName, studentSurname, studentID):
        Cursor.execute("INSERT INTO STUDENTS (ID, Name, Surname) VALUES (?, ?, ?);", (studentID, studentName, studentSurname,))
        print("Öğrenci eklendi.")
        print(Database.getAllStudents())

while True:
    print("\nMerhaba, öğrenci veri tabanında ne işlem yapmak istersiniz?")
    print("[1] Öğrenci Ara")
    print("[2] Öğrenci Güncelleştir")
    print("[3] Öğrenci Ekle")
    print("[4] Öğrenci Sil")
    print("[Q] Çıkış")


    option = str(input("Seçenek: ")) 
    match option:
        case "1":
            searchValue = input("Aranacak öğrenci adı ya da soyadı: ")
            print(Database.searchStudent(searchValue))
        case "2":
            print(Database.getAllStudents())
            studentId = input("Güncellenecek öğrenci ID: ")
            print("Güncellenecek olan bilgiyi seçiniz?\n[1] Ad\n[2] Soyad\n")
            newValue = input("Seçeneğiniz: ")
            match newValue:
                case "1":
                    newValue = input("Yeni ad: ")
                    Database.updateStudent("Name", newValue, studentId)
                case "2":
                    newValue = input("Yeni soyad: ")
                    Database.updateStudent("Surname", newValue, studentId)
                case _:
                    print("Geçersiz seçim.")
        case "3":
            studentName = input("Öğrenci adı: ")
            studentSurname = input("Öğrenci soyadı: ")
            studentID = input("Öğrenci ID: ")
            Database.instertStudents(studentName, studentSurname, studentID)
        case "4":
            print(Database.getAllStudents())
            studentID = input("Silinecek öğrenci ID: ")
            Database.deleteStudents(studentID)
        case "Q":
            print("Çıkış yapılıyor...")
            break
        
        case _:
            print("Ana menüye dönülüyor...")
            