from imarkdown import MdFile, LocalFileAdapter, MdImageConverter

def main():
    adapter = LocalFileAdapter()
    converter = MdImageConverter(adapter=adapter)
    
    md_file = MdFile(name="优化算法-动手学深度学习.zh-cn.md")
    converter.convert(md_file, new_name="优化算法-动手学深度学习.zh-cn/优化算法-动手学深度学习.zh-cn.md")

if __name__ == '__main__':
    main()