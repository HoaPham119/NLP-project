import re

condition = False

[]

eql_condition = {
   "aá": "á",
   
    
}

"""
Replace chữ ko có dấu
"""
def delete_dup(text):
    print(f"input: {text}")
    check = True
    while check:
        check = False
        index = 0
        for i in text:
            # j = text.index(index+1)
            if index < len(text)-1:
                j = text[index+1]
                if i == j or condition:
                    text = text.replace(f"{i}{j}", i)
                    check = True
                else:
                    index += 1
    print(f"output: {text}")
    return text

def tien_xu_ly(text):
    return

if __name__ == "__main__":
    text = "ccộoong   hoàa"
    delete_dup(text=text)