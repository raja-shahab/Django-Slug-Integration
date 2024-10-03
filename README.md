# Django-Slug-Integration

This project demonstrates how to implement **slugs** in Django URLs for individual pages or posts. Slugs are human-readable identifiers typically used in URLs for better SEO, readability, and user experience.

## Features

- **Slug generation**: Automatically generate a slug based on the title or other fields.
- **SEO-friendly URLs**: Use slugs instead of ID numbers for cleaner URLs.
- **Django Admin integration**: Slugs can be manually edited from the Django admin panel.
- **Unique slugs**: Ensure slugs are unique for every page.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap for styling)
- **Database**: SQLite (default Django database)

## Workflow

1. **Create a page/post**: When creating a new page or post, a slug is automatically generated from the title.
2. **Access the page by slug**: The page can be accessed via its slug in the URL, rather than using the database ID.
3. **Edit the slug manually**: In the Django admin panel, you can edit the slug manually if needed.

## Example

### URL Format

- Without slug: `http://example.com/page/1/`
- With slug: `http://example.com/page/my-first-blog-post/`

### Slug Generation Code

Here's an example of how slugs are generated in this project:

\`\`\`

    from django.db import models
    from django.utils.text import slugify
    
    class Post(models.Model):
        title = models.CharField(max_length=200)
        content = models.TextField()
        slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
\`\`\`

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! If you find any bugs or improvements, feel free to submit a pull request or open an issue.

## Query

For any query, please feel free to reach out to rajashahab912@gmail.com
