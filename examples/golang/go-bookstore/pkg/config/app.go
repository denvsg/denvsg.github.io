package config

import (
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/mysql"
)

var (
	db *gorm.DB
)

// Connect connect to database
func Connect() {
	d, err := gorm.Open("mysql", "test:1234@/books?charset=utf8&parseTime=True&loc=Local")
	if err != nil {
		panic(err)
	}
	db = d
}

// GetDB get db object
func GetDB() *gorm.DB {
	return db
}
