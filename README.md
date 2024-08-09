# Oscar's Lab Website

## Categories

To list all people in a category, add `people_category: <category>` to the front matter of the category page, and include the following snippet in the body of the page:

```markdown
{% include people_row %}
```

To list all posts related to this category, add:

```markdown
{% include updates_row %}
```

### Person Status

Sets how they appear on the 'People' page.

- `student`
- `Masters`
- `PhD`
- `PostDoc`
- `Alumni`

### Projects

If a person or post has this tag, they appear at the bottom of the related 'Project' page.

- `biomin` - Biomineralisation
- `geochem` - Geochemical Modelling
- `precip` - CaCO3 Precipitation
- `sensors` - Sensor Development
- `global` - Global Calcification

### Funders

- `leverhulme` - Funded by the Leverhulme Trust
- `NERC` - Funded by NERC

### Jobs

- `job` - makes the post appear on the 'Jobs' page

### Other categories with no specific function

- `research`
- `paper`
- `conference`
- `fieldwork`
- `outreach`
- `teaching`
- `grant`
- `physiology`
- `machine-learning`
- `coral`
