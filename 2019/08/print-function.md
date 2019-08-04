# Print function

## Format

```
print("<some-description-with-{}>".format(1st-place-value, 2nd-place-value,...))
```

### For example

```
print("My name is {}.".format("Jake Chung"))

```

Same thing, but firstname, lastname
```
firstname = 'Jake'
lastname = 'Chung'
print("my name is {} {}.".format(firstname, lastname))
```

The result of this is
```
my name is Jake Chung.
```

Just changing the output format:
```
# If we want official format:
print("Name: {}, {}".format(lastname, firstname))
```

The result is:
```
Name: Chung, Jake
```