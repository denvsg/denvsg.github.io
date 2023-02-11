use std::sync::{Arc, Mutex};

use tokio::{io::AsyncWriteExt, net::TcpStream};

use crate::{response, SharedData};

pub async fn index(stream: &mut TcpStream) {
    let response = "index page server";
    stream.write_all(response::response(
        "200 OK", response, "text/html").as_bytes()).await.unwrap();

    stream.flush().await.unwrap();
}

pub async fn visit_count(stream: &mut TcpStream, shared_data: Arc<Mutex<SharedData>>) {
    shared_data.lock().unwrap().visit_count += 1;

    let visit_count = shared_data.lock().unwrap().visit_count;

    let response = format!("{} Times!", visit_count);

    stream.write_all(response::response(
        "200 OK", &response, "text/html").as_bytes()).await.unwrap();

    stream.flush().await.unwrap();
}

pub async fn not_fount(stream: &mut TcpStream) {
    let response = "404 Not Found";

    stream.write_all(response::response("404 NOT FOUND", response, "text/html").as_bytes()).await.unwrap();

    stream.flush().await.unwrap();
}
