# Maintainability: A measure of how easy it is to maintain a codebase.

# Often times, you can put in a little bit of design effort up front to
# save yourself a lot of maintenance effort down the road.

# There is a famous problem in maintainability known as coupling.
# Coupling is when changing one line of code requires changing
# one or more other lines of code as well.

# There are different degrees and categories of coupling.
# Loose coupling is when changing one line of code MIGHT require
#   changing another line of code, or maybe not.
# Tight coupling is when changing one line of code almost surely
#   requires changing another.

# If a line of code is coupled to MANY other lines of code, sprawled
# across the entire codebase, then that's pervasive coupling.
# If a line of code is coupled to just a FEW other lines of code,
# perhaps even adjacent lines of code, that's local coupling.

# Coupling can make something hard to change.

# However, coupling is, to some extent, inevitable. It occurs at interfaces
# due to dependencies.

# Dependency: when one code component requires another code component.

# An interface is the part of a code component that other components
# directly interact with.

# We can't fully get rid of coupling. But maybe we can intentionally
# reorganize it, or move it around, to mitigate its affects.
# It might be possible to move coupling around so that the components
# with the tightest, most pervasive coupling, are also components
# that are very "stable" and unlikely to ever need to be changed.

# Encapsulation is a tool (a technique) that can:
# 1. It can help control coupling
# 2. It can also help establish class invariants

# Encapsulation is colocation (bundling) of data (attributes) with the
# behaviors (functions) that operate on that data.


