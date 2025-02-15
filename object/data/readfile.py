import os

folder = "Office/"
domains = os.listdir(folder)
domains.sort()
for d in range(len(domains)):
    dom = domains[d]
    if os.path.isdir(os.path.join(folder, dom)):
        dom_new = dom.replace(" ", "_")
        print(dom, dom_new)
        os.rename(os.path.join(folder, dom), os.path.join(folder, dom_new))

        # Handle the 'images' subdirectory
        subdir = os.listdir(os.path.join(folder, dom_new))[0]  # This should be 'images'
        classes = os.listdir(os.path.join(folder, dom_new, subdir))
        classes.sort()

        f = open(dom_new[0] + "_list.txt", "w")
        for c in range(len(classes)):
            cla = classes[c]
            cla_new = cla.replace(" ", "_")
            print(cla, cla_new)
            os.rename(
                os.path.join(folder, dom_new, subdir, cla),
                os.path.join(folder, dom_new, subdir, cla_new),
            )

            files = os.listdir(os.path.join(folder, dom_new, subdir, cla_new))
            files.sort()

            for file in files:
                file_new = file.replace(" ", "_")
                # Rename the file
                os.rename(
                    os.path.join(folder, dom_new, subdir, cla_new, file),
                    os.path.join(folder, dom_new, subdir, cla_new, file_new),
                )
                print(file, file_new)
                # Write the complete path including the file
                full_path = os.path.join(folder, dom_new, subdir, cla_new, file_new)
                f.write(f"{full_path} {c}\n")
        f.close()
