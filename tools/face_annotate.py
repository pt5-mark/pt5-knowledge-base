#!/usr/bin/env python3
"""
Image Face Detection and Annotation Tool
使用OpenCV和face_recognition库实现人脸检测和标注
"""
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import sys
import os

def detect_faces(image_path):
    """
    检测图片中的人脸
    返回人脸位置列表 [(x, y, w, h), ...]
    """
    # 读取图片
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not load image from {image_path}")
        return None, []
    
    # 转换为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 加载人脸检测器
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # 检测人脸
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    
    return image, faces

def annotate_faces(image_path, names, output_path=None):
    """
    在图片上标注人脸
    
    Args:
        image_path: 输入图片路径
        names: 人名列表，按从左到右顺序
        output_path: 输出图片路径（可选）
    """
    # 检测人脸
    image, faces = detect_faces(image_path)
    if image is None:
        return False
    
    if len(faces) == 0:
        print("No faces detected in the image.")
        return False
    
    print(f"Detected {len(faces)} face(s)")
    
    # 按x坐标排序（从左到右）
    faces = sorted(faces, key=lambda f: f[0])
    
    # 转换为PIL Image以便使用中文
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(image_rgb)
    draw = ImageDraw.Draw(pil_image)
    
    # 尝试加载中文字体
    try:
        # 尝试常见中文字体
        font_paths = [
            '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc',
            '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',
            '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc',
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
        ]
        font = None
        for font_path in font_paths:
            if os.path.exists(font_path):
                font = ImageFont.truetype(font_path, 30)
                break
        
        if font is None:
            font = ImageFont.load_default()
    except:
        font = ImageFont.load_default()
    
    # 为每个人脸画框和标注
    for i, (x, y, w, h) in enumerate(faces):
        # 画人脸框
        draw.rectangle([x, y, x+w, y+h], outline="red", width=3)
        
        # 获取名字
        if i < len(names):
            name = names[i]
        else:
            name = f"Person {i+1}"
        
        # 计算文字位置（框上方）
        text_y = y - 40 if y - 40 > 0 else y + h + 10
        
        # 画文字背景
        bbox = draw.textbbox((0, 0), name, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        draw.rectangle([x, text_y, x + text_width + 10, text_y + text_height + 10], 
                       fill="red")
        
        # 画文字
        draw.text((x + 5, text_y + 5), name, font=font, fill="white")
        
        print(f"  Face {i+1}: {name} at ({x}, {y})")
    
    # 保存结果
    if output_path is None:
        base, ext = os.path.splitext(image_path)
        output_path = f"{base}_annotated{ext}"
    
    pil_image.save(output_path)
    print(f"\n✅ Annotated image saved to: {output_path}")
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python face_annotate.py <image_path> [name1] [name2] ...")
        print("Example: python face_annotate.py photo.jpg \"张三\" \"李四\" \"王五\"")
        sys.exit(1)
    
    image_path = sys.argv[1]
    names = sys.argv[2:] if len(sys.argv) > 2 else []
    
    annotate_faces(image_path, names)

if __name__ == "__main__":
    main()
