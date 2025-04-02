from pathlib import Path
import sys

def show_structure(path: Path, prefix="", output_file=None):
    if not path.exists():
        print("❌ 指定されたパスが存在しません", file=output_file)
        return
    
    for item in sorted(path.iterdir()):
        if item.is_dir():
            line = f"{prefix}📁 {item.name}/"
            print(line)
            if output_file:
                print(line, file=output_file)
            show_structure(item, prefix + "    ", output_file)
        else:
            line = f"{prefix}📄 {item.name}"
            print(line)
            if output_file:
                print(line, file=output_file)

# メイン処理
if len(sys.argv) > 1:
    target_path = Path(sys.argv[1]).resolve()
else:
    target_path = Path(".").resolve()

output_filename = "directory_structure.txt"
with open(output_filename, "w", encoding="utf-8") as f:
    exec_dir = Path.cwd().resolve()
    header = f"📂 実行ディレクトリ: {exec_dir}\n📂 表示対象ディレクトリ: {target_path}\n"
    print(header)
    print(header, file=f)
    show_structure(target_path, output_file=f)

print(f"\n✅ 構造を '{output_filename}' に出力しました！")
