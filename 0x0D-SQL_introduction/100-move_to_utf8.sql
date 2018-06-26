-- converts hbtn_0c_0 to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 collate utf8mb4_unicode_ci;
USE htbn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 collate utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name CHARACTER SET utf8mb4 collate utf8mb4_unicode_ci;
