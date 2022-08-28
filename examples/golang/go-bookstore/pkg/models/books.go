package models

import (
	"base.io/dveng/go-bookstore/pkg/config"
	"github.com/jinzhu/gorm"
)

var db *gorm.DB

//Book record book type
type Book struct {
	gorm.Model
	Name        string `gorm:""json:"name"`
	Authors     string `json:"author"`
	Publication string `json:"publication"`
}

func init() {
	config.Connect()
	db = config.GetDB()
	db.AutoMigrate(&Book{})
}

// CreateBook add book to database
func (b *Book) CreateBook() *Book {
	db.NewRecord(b)
	db.Create(&b)
	return b
}

// GetAllBooks ...
func GetAllBooks() []Book {
	var Books []Book
	db.Find(&Books)
	return Books
}

// GetBookByID ...
func GetBookByID(id int64) (*Book, *gorm.DB) {
	var getBook Book
	db := db.Where("ID=?", id).Find(&getBook)
	return &getBook, db
}

// DeleteBook ...
func DeleteBook(id int64) Book {
	var book Book
	db.Where("ID=?", id).Delete(&book)
	return book
}
