# Written to fill current drive by truncating file size. Will create new file if existing Garbage file is present
import shutil
import os


# function to confirm user exit
def press_to_exit():
    input("Press Enter to exit...")
    print("Goodbye")
    exit()


# Returns total,used, and free for drive in GiB
def get_usage(param):
    total, used, free = shutil.disk_usage("/")
    if param == "total":
        return total
    elif param == "used":
        return used
    elif param == "free":
        return free
    else:
        print("Invalid")


# returns size of file required to leave desiredGiB on disk
def calculate_size_for_desiredGiB(desired):
    GiBs = ((1024 ** 3) * desired)
    size = get_usage("free") - GiBs
    return int(size)


# ------------------------------------------------------------------------------------
print("Total: %.2f GiB" % (get_usage("total") / (2 ** 30)))
print("Used: %.2f GiB" % (get_usage("used") / (2 ** 30)))
print("Free: %.2f GiB" % (get_usage("free") / (2 ** 30)))

# Error handling in the case that entered value exceeds available disk space, is a negative input, or NaN
try:
    desiredGiB = float(input("Enter desired remaining space on HDD (GiB): "))
except ValueError:
    print("*Error: Input must be a number*")
    press_to_exit()

if desiredGiB <= 0:
    print("*Error: Must be a positive value*")
    press_to_exit()
if desiredGiB > get_usage("free") / (2 ** 30):
    print("*Error: Desired remaining space on HDD exceeds free disk space*")
    press_to_exit()

sizeInBytes = calculate_size_for_desiredGiB(desiredGiB)
print("Size needed to leave %d GiB on drive: %2f GiB" % (desiredGiB, sizeInBytes/2**30))

# fills HDD with garbage.dat if remaining space > desired remaining space
if get_usage("free") / (2 ** 30) > desiredGiB:
    i = 0
    while os.path.exists("Garbage(%s).dat" % i):
        i += 1

    print("Creating file of size %d bytes..." % sizeInBytes)

    with open("Garbage(%s).dat" % i, "wb") as out:
        out.truncate(sizeInBytes)

    print("File creation complete! Remaining Space on drive: %.2f GiB" % (get_usage("free") / (2 ** 30)))
    press_to_exit()


