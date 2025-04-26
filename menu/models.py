from django.db import models
from django.urls import NoReverseMatch, reverse
from django.utils.text import slugify


class Menu(models.Model):
    name = models.CharField(verbose_name="Название меню", max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name="items", verbose_name="Меню"
    )
    title = models.CharField(max_length=200, verbose_name="Название пункта")
    url = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="URL (или именованный URL)"
    )
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="Slug"
    )
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="children",
        verbose_name="Родительский пункт",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Автоматически генерируем slug из названия
        super().save(*args, **kwargs)

    def get_parent_url(self):
        if self.parent:
            return self.parent.get_absolute_url()
        return reverse("menu:home")

    def get_absolute_url(self):
        path = [self.slug]
        parent = self.parent
        while parent:
            path.insert(0, parent.slug)
            parent = parent.parent
        return reverse("menu:menu_page", kwargs={"slug_path": '/'.join(path)})
