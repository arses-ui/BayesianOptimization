import cv2 
import numpy as np 
from tkinter import filedialog, Tk, Label, Button 
from PIL import Image, ImageTk

def calculate_line_Width(image): 

    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Optional: Morphological cleaning
    kernel = np.ones((5,5), np.uint8)
    cleaned = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    # Find contours
    contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    display_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    display_img = display_img.copy()
    widths = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        rect = cv2.boundingRect(cnt)
        x,y, w, h =  cv2.boundingRect(cnt)
        # box = cv2.boxPoints(rect)
        # box = np.int32(box)

        if area > 1000 and  w < h:  # Filter out small noise
            thickness = w
            widths.append(thickness)
            cv2.rectangle(display_img,(x,y),(x+w,y+h),(0,255,0),2)
            center = (int((x+x+w)/2), int((y+y+h)/2))
            cv2.putText(display_img,f"{thickness:.1f}px", center, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)   

    if not widths:
        return "No line-like regions found"
    
    return display_img,  f"Estimated line width: {np.mean(widths):.2f} px"

def open_file():
    image = filedialog.askopenfilename()
    if image:
        result_img, result_text = calculate_line_Width(image)       
        
        if result_img is None: 
            result_label.config(text = result_text)
            return 

        rgb_img = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(rgb_img).resize((512, 384))
        img_tk = ImageTk.PhotoImage(pil_img)

        image_label.config(image=img_tk)
        image_label.image = img_tk

        result_label.config(text=result_text)


# GUI setup
root = Tk()
root.title("Line Width Estimator (Half-Rectangle)")

upload_btn = Button(root, text="Upload Image", command=open_file)
upload_btn.pack(pady=10)

image_label = Label(root)
image_label.pack()

result_label = Label(root, text="Upload an image to begin")
result_label.pack(pady=10)

root.mainloop()