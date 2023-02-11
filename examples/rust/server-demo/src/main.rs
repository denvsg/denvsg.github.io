#[allow(clippy::unused_io_amount)]
use std::sync::{Arc, Mutex};

use tokio::{
    io::AsyncReadExt,
    net::{TcpListener, TcpStream},
};

mod handlers;
mod response;

pub struct SharedData {
    pub visit_count: u32,
}

#[tokio::main]
async fn main() {
    println!("Hello, world!");
    let listener: TcpListener = TcpListener::bind("127.0.0.1:8000").await.unwrap();

    let shared_data = Arc::new(Mutex::new(SharedData { visit_count: 0 }));

    loop {
        let (mut stream, _) = listener.accept().await.unwrap();

        let shared_data = Arc::clone(&shared_data);

        tokio::spawn(async move {
            let mut buffer = [0; 1024];

            stream.read(&mut buffer).await.unwrap();
            println!("{}", String::from_utf8_lossy(&buffer));

            route(&mut stream, &buffer, shared_data).await;
        });
    }
}

async fn route(stream: &mut TcpStream, buf: &[u8], shared_data: Arc<Mutex<SharedData>>) {
    if buf.starts_with(b"GET / HTTP/1.1") {
        handlers::index(stream).await;
    } else if buf.starts_with(b"GET /count") {
        handlers::visit_count(stream, shared_data).await;
    } else {
        handlers::not_fount(stream).await;
    }
}