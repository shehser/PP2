#Open the file "demofile.txt" and overwrite the content:
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())

  # Append new lines ('a' mode adds to the end)
with open("sample.txt", "a") as file:
    file.write("This line was appended later.\n")
