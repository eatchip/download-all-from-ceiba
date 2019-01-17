# download-all-from-ceiba
You can download all the courseware from ceiba by input your ID and password 

#專案內容：一鍵下載ceiba所有課件
#應用場景：用戶可通過輸入自己的學號和密碼一鍵下載台灣大學ceiba上的課件，也可以對程式做一些簡單的調整，來下載指定課程的所有課件
#實現方式：通過selenium套件模擬瀏覽器登錄，進行各項操作。通過pywin32來實現對於電腦本身一些窗口的自動控制。
#後期發展：如果有同學有興趣，希望可以在原有程式的基礎上做以下優化。
1.不用pywin32，用request，因為模擬鼠標右擊會造成電腦不能夠在下載程式的過程中做其他事情，不方便。
2.將其放到雲端服務器上跑，可以讓不會程式的小白使用。
3.做出易用性較強的交互界面
