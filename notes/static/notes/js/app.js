/*
Let's write VanillaJS for now
Later we shall include webpack and other bundling systems to make this look extra pretty and fluid
 */
$(document).ready(function() {
	
	// toolbar options
	var toolbarOptions = [
	  ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
	  ['blockquote', 'code-block'],

	  ['link','image'],

	  [{ 'header': 1 }, { 'header': 2 }],               // custom button values
	  [{ 'list': 'ordered'}, { 'list': 'bullet' }],
	  [{ 'script': 'sub'}, { 'script': 'super' }],      // superscript/subscript
	  [{ 'indent': '-1'}, { 'indent': '+1' }],          // outdent/indent
	  [{ 'direction': 'rtl' }],                         // text direction

	  [{ 'size': ['small', false, 'large', 'huge'] }],  // custom dropdown
	  [{ 'header': [1, 2, 3, 4, 5, 6, false] }],

	  [{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme
	  [{ 'font': [] }],
	  [{ 'align': [] }],

	  ['clean']                                         // remove formatting button
	];

	var Font = Quill.import('formats/font');
	Font.whitelist = ['lato','robotoslab'];
	Quill.register(Font, true);

	// Initialize Quill Editor
	var quill = new Quill('#notesEditor', {
		modules: {
			toolbar: '#toolbarContainer',
		},
		theme: 'snow'
	});

	// find the hidden input in form
	// assign it to var
	var hiddenNotesContent = $('#createNotesForm #noteContentBody');

	// fetch quill's body val -> wash it with JSON.stringify method
	// assign it to hiddenNotesContent
	hiddenNotesContent.val(JSON.stringify(quill.getContents()));

	// Track Quill's text change event
	// Assign var content accordingly
	quill.on('text-change', function() {
		hiddenNotesContent.val(JSON.stringify(quill.getContents()));
	});
});