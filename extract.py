from warcio.archiveiterator import ArchiveIterator

# Replace with the path to your WARC file
file_path = "CC-MAIN-20241003094020-20241003124020-00000.warc.gz"
# Output file where extracted content will be saved
output_file_path = "extracted_content.txt"

with open(file_path, 'rb') as stream, open(output_file_path, 'w', encoding='utf-8') as output_file:
    for record in ArchiveIterator(stream):
        if record.rec_type == 'response':
            url = record.rec_headers.get_header('WARC-Target-URI')
            output_file.write(f"URL: {url}\n")  # Write URL to output file
            content = record.content_stream().read()
            output_file.write(content.decode('utf-8', errors='ignore') + "\n\n")  # Write content to output file

