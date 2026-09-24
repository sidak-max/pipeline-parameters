import sys
def add_numbers(a, b):
 return a + b
if __name__ == "__main__":
 num1 = int(sys.argv[1])
 num2 = int(sys.argv[2])
 result = add_numbers(num1, num2)
 print("=================================")
 print("Addition Result")
 print("=================================")
 print(f"First Number : {num1}")
 print(f"Second Number: {num2}")
 print(f"Sum : {result}")

git init
git config --global user.name "Sidak Singh"
git config --global user.email "YOUR_GITHUB_EMAIL"
git remote add origin https://github.com/YOUR_USERNAME/JenkinsLab.git
git add .
git commit -m "Add Jenkins pipeline"
git branch -M main
git push -u origin main
