import sublime
import sublime_plugin

class MultiRegionSelectionNavigationListener(sublime_plugin.EventListener):
	def on_hover(self, view, point, hover_zone):
		def popup_navigator(href):
			# Bring the clicked region into view
			index = int(href)
			sels = list(view.sel())
			if not (0 <= index < len(sels)):
				return
			target = sels[index]
			view.show(target, show_surrounds=True)

		# We only care about text area hovers
		if hover_zone != sublime.HOVER_TEXT:
			view.hide_popup()
			return

		# Target multi-region selection only
		sels = list(view.sel())
		if not sels or len(sels) == 1:
			view.hide_popup()
			return

		# Check if mouse is inside one of the selections
		hovered_region_index = None
		for i, r in enumerate(sels):
			if r.contains(point):
				hovered_region_index = i
				break
		if hovered_region_index is None:
			view.hide_popup()
			return

		# Prepare the popup content for other regions
		items_html = []
		for i, r in enumerate(sels):
			# Skip the one being hovered
			if i == hovered_region_index:
				continue

			# Cap the maximum length to show
			text = view.substr(r)
			if len(text) > 50:
				text = text[:50 - 3] + "..."

			# Adding to the popup html
			line_no = view.rowcol(r.begin())[0] + 1
			items_html.append(
				f'<div><a href="{i}" style="text-decoration: none"><span style="background-color: black">line {line_no} ({r.begin()}, {r.end()}) </span><span style="background-color: navy">{sublime.html_format_command(text)}</span></a></div><div style="font-size: 4"><br></div>'
			)

		if items_html:
			html = ("\n".join(items_html))[:-36]
			if html:
				# Show the clickable popup
				view.show_popup(
					html,
					flags=sublime.HIDE_ON_MOUSE_MOVE_AWAY,
					location=point,
					max_width=800,
					on_navigate=popup_navigator
				)
		else:
			view.hide_popup()
