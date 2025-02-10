import os
def get_directory_size(path):
	total_size = 0
	for dirpath, dirnames, filenames in os.walk(path):
		total_size += sum(os.path.getsize(os.path.join(dirpath, f)) for f in  filenames if not os.path.islink(os.path.join(dirpath, f)))
	return total_size

def format_size(size):
	units = ['bytes', 'KB', 'MB', 'GB', 'TB']
	for unit in units:
		if size < 1024.0:
			return f"{size:.2f} {unit}"
		size /= 1024.0

def analyze_directory():
	items = [(item_name, get_directory_size(item_path) if os.path.isdir(item_path) else os.path.getsize(item_path))
		for item_name in os.listdir('.')
		for item_path in [os.path.join('.', item_name)]]

	items.sort(key=lambda x: x[1], reverse=True)

	for name, size in items:
		print(f"{name}: {format_size(size)}")

if __name__ == "__main__":
	analyze_directory()
