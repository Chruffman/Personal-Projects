local _, nSpace = ...; -- Namespace

--------------------------------------
-- Custom Slash Command
--------------------------------------
nSpace.commands = {
	["config"] = nSpace.Config.Toggle, -- this is a function (no knowledge of Config object)
	
	["help"] = function()
		print(" ");
		nSpace:Print("List of slash commands:")
		nSpace:Print("|cff00cc66/ct config|r - shows config menu");
		nSpace:Print("|cff00cc66/ct help|r - shows help info");
		print(" ");
	end,
	
	["example"] = {
		["test"] = function(...)
			nSpace:Print("My Value:", tostringall(...));
		end
	}
};

local function HandleSlashCommands(str)	
	if (#str == 0) then	
		-- User just entered "/ct" with no additional args.
		nSpace.commands.help();
		return;		
	end	
	
	local args = {};
	for _, arg in ipairs({ string.split(' ', str) }) do
		if (#arg > 0) then
			table.insert(args, arg);
		end
	end
	
	local path = nSpace.commands; -- required for updating found table.
	
	for id, arg in ipairs(args) do
		if (#arg > 0) then -- if string length is greater than 0.
			arg = arg:lower();			
			if (path[arg]) then
				if (type(path[arg]) == "function") then				
					-- all remaining args passed to our function!
					path[arg](select(id + 1, unpack(args))); 
					return;					
				elseif (type(path[arg]) == "table") then				
					path = path[arg]; -- another sub-table found!
				end
			else
				-- does not exist!
				nSpace.commands.help();
				return;
			end
		end
	end
end

function nSpace:Print(...)
    local hex = select(4, self.Config:GetThemeColor());
    local prefix = string.format("|cff%s%s|r", hex:upper(), "Chuff Tracker:");	
    DEFAULT_CHAT_FRAME:AddMessage(string.join(" ", prefix, ...));
end

-- WARNING: self automatically becomes events frame!
function nSpace:init(event, name)
	if (name ~= "ChuffTracker") then return end 

	-- allows using left and right buttons to move through chat 'edit' box
	for i = 1, NUM_CHAT_WINDOWS do
		_G["ChatFrame"..i.."EditBox"]:SetAltArrowKeyMode(false);
	end
	
	----------------------------------
	-- Register Slash Commands! --
	----------------------------------
	SLASH_RELOADUI1 = "/rl"; -- new slash command for reloading UI
	SlashCmdList.RELOADUI = ReloadUI;

	SLASH_FRAMESTK1 = "/fs"; -- new slash command for showing framestack tool
	SlashCmdList.FRAMESTK = function()
		LoadAddOn("Blizzard_DebugTools");
		FrameStackTooltip_Toggle();
	end

	SLASH_AuraTracker1 = "/ct";
	SlashCmdList.AuraTracker = HandleSlashCommands;
	
    nSpace:Print("Welcome back", UnitName("player").."! Congratulations on reaching level "..UnitLevel("player").."!");
end

local events = CreateFrame("Frame");
events:RegisterEvent("ADDON_LOADED");
events:SetScript("OnEvent", nSpace.init);