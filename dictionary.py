import json

def create_patient():
    new_patient = {"last name": "Smith",
                      "first name": "Bob",
                      "age": 60,
                      "married": False,
                      "test results": [0, 16, 23, 2.3]
                      }
    return new_patient


def save_json(patient):
    import json
    filename = "patient_data.txt"
    out_file = open(filename, 'w')
    json.dump(create_patient, out_file)
    out_file.close()


if __name__ == "__main__":
    x = create_patient()
    save_json(x)


#def read_dictionary(my_dict):
 #   my_key = "night"
  #  y = my_dict[my_key]
   # print("The definition of {} is {}".format(my_key, y))
    #return


#def add_info(my_dict):
   # my_dict["lunch"] = "The meal I eat in the middle of the day"
    #my_dict["day"] = "when I'm not sleeping"
    #return my_dict


#if __name__ == "__main__":
    #x = create_dictrionary()
    #read_dictionary(x)
    #x = add_info(x)
    #print(x)
    #z = x.get("lunch")
    #print(z)
    #print(type(x))