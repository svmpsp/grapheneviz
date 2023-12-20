ARKANA_BUILD_REPO := git@github.com:svmpsp/arkana-build-tools.git
ARKANA_BUILD_CLONE_OUTPUT_DIR := tmp_arkana
ARKANA_BUILD_TOOLS_DIR := arkana-build-tools
ARKANA_BUILD_MAKEFILES_DIR := arkana-build-tools/makefiles

$(ARKANA_BUILD_TOOLS_DIR):
	rm -rf $(ARKANA_BUILD_TOOLS_DIR)
	git clone $(ARKANA_BUILD_REPO) $(ARKANA_BUILD_CLONE_OUTPUT_DIR) && cp -r $(ARKANA_BUILD_CLONE_OUTPUT_DIR)/$@ ./ && rm -rf $(ARKANA_BUILD_CLONE_OUTPUT_DIR)

-include $(ARKANA_BUILD_MAKEFILES_DIR)/common.mk
-include $(ARKANA_BUILD_MAKEFILES_DIR)/python.mk
-include $(ARKANA_BUILD_MAKEFILES_DIR)/sphinx.mk
