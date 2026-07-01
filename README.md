# seoul indie

https://girlypop.no/seoul_indie/

## data structure

`data/seoul_indie.yaml` contains nodes. edges are calculated from `connects_to`-fields on nodes.

```yaml
nodes:
- id: string # unique
  type: group|person # <-- determines the icon displayed (star or triangle)
  name: string
  url: string # determines where users are sent upon clicking a node
  connects_to:
  - string # another nodes[].id
  - target: string # another nodes[].id
    label: string # Produced|Remixed|Featured|Collaborated with|Sound director for|Gave lessons to, but also anything else like 2014-2017, the years in which a person was in a band
```

## contributing

to change relationships, add people or groups, edit `data/seoul_indie.yaml` and submit a pull request

### stuff that should be noted if you want to add nodes or edges

please think about the directionality: `x` produced `y`, thus the connection should lie with `x`, to `y`. no connections are necessarily going out of `y`.
`x` could also be a member of the group `z`, which is also a connection _from_ `x` to `z`.

```yaml
- id: x
  type: person
  name: x
  url: ''
  connects_to:
  - target: y
    label: Produced
  - z
- id: y
  type: person
  name: y
  url: ''
- id: z
  type: group
  name: z
  url: ''
```

### stuff i want help with

- i wanna change out the maniadb links to youtube videos where it's possible (especially for groups and solo artists)
- more people, more groups!!! (it's kind of ok if the source is "trust me bro", and it's also totally ok if it's regarding groups outside of seoul)

## ideas/roadmap

- [x] more concise way to define groups and people and the connections between them
- [ ] support urls for edges
- [ ] click node to show neighborhood (will break urls the way they work now, but enables neighborhood view on mobile), click anywhere else to clear neighborhood view
- [ ] support more urls for nodes
- [ ] click node to open a sidebar (desktop)/drawer (mobile) showing any urls associated to the node
- [ ] click edge to open a sidebar (desktop)/drawer (mobile) showing any urls associated to the edge