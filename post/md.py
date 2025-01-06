from imarkdown import MdFile, LocalFileAdapter, MdImageConverter

def main():
    adapter = LocalFileAdapter()
    converter = MdImageConverter(adapter=adapter)
    
    md_file = MdFile(name="LeetCode.md")
    converter.convert(md_file, new_name="index.zh-cn.md")

if __name__ == '__main__':
    main()