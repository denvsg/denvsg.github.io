pub fn response(status: &str, content: &str, content_type: &str) -> String {
    let content_type = if content_type.contains("text") {
        format!("{}; charset=utf-8", content_type)
    } else {
        content_type.to_string()
    };

    format!("HTTP/1.1 {}\r\nContent-Length: {}\r\nContent-Type: {}\r\n\r\n{}",
            status, content.len(), content_type, content)
}