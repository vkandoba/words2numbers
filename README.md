# words2numbers
Convert russian text with num words to a sequence of digits. 

make_num(“номер двести двадцать два добавить шестьсот сорок и один”) == “222641” 

It allows to parse numbers, that someone has spoken to dialog system or voice interface. In these cases, a voice recognition engine produces text with numbers as words instead of digits.

It could be useful, when you ask client some numerical information like a ticket number, a bank account or personal id.
