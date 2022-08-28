module base.io/dveng/go-bookstore

go 1.16

// replace base.io/dveng/go-bookstore/pkg => ./pkg
replace base.io/dveng/go-bookstore/pkg/routes => ./pkg/routes

require (
	github.com/gorilla/mux v1.8.0
	github.com/jinzhu/gorm v1.9.16
)
