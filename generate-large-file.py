import os

def generate(mb, filename):
    file = open(filename, "w")
    file.write("")
    file.close()
    # 1024 chars
    # str = "tycnwbpaszafrdsgnqxqvzrbumwcabmfgcpaptcbsaubskfeegceanetvwggfaeudskfzrszfhnkdzegfkhncrbnqynuzekwxsmckspmcqxuvkvfzhmhramhfymtrddavvygecqpttbhdkgpkqfunffgvgxquhxbnzbfgrmzkeqtsyyekscrexraqmtfhbdweprgtcvypyhvrsdvugwrxubbxpyvsnyqpsmvxrrvmwzprfdupvxrmtqgafnmzuhkzrcgzpbspremcfaguabtfwfgnpcqcqpwutrucrpctykrgzzzunxaepspqrvcnzrebwfnxzqhbxbersanvsacfzkhtmgrehvzwaugruvtfkueeqhbkachkvhkruxuvnacrxfkhhbbqxmygwdrzeswfrbpwwptpdwgmqetbuhwabpvxrbgkkxfhhsavhmadwkpefvavvxemxzwxrfbctrkkxtsweddkussrsxadtshdskmyyxdptmuxttbfuuwdvtdgpvqgbskhwccxhdnuscapsdxfqaayywuecarushhkzfcfsqehmqprswpsqnfwkhcsqhkckdgpnkutaacystsdschgyzqqcwefasmdbabmertnxbeubghhghkgpdkwcympqfefebpkpdmmahzmmaeftdpndxcnrpfpnzdgnegchftdzydnfquhzbwtrfnmpvstnygwqfcdtuykvzunuenyspsucbchrdafcvnuceckpqhwmcxhfkzmtpqxgsqbsctvuremeudbcymeuzkpnfyfbvrgsfssdmfsqbymxatmdmtseymmkarxpuvfdmbfmhwqvfpkwrzqryzfuvqhaktvznarbvnsnuckuaqswqarkzvvxfuyzbxprbugskgysuuerbgekrysfxgttewgnypgmgyqqpchmgzpaumyedxbamgkucwzzuqabuswqtsqkfneysbqmywwrpvtwbwrakshkmhqstrsvdhvcpvvwyffkxaxwdpmkerypbzukquqkyh"
    # 1000 chars
    str = "cqbwfcbrnwmrxwdchreersfmcgaywtsfxabxyhazfwzkhqfwfruwwqduvmewrszgzdxumzfdtnbdshzravpwcdtehppqvabnvcsyfcwkkcqqtytkpuzrwtexwgmeggrpmdyyxytcnrfqzantaspvtazmsabtnacqustpkqsamtqbbmbmzbzpxztabwfbukbaazxyemydvgqagakacusrbwaxkkcxyymdbmkhtuqussmgxymwxfxtnmtkregucrhsqdvwfszxvktyzggehrupmddrdbkygbcczbyddgezsahybnpaydrgtmrvhakysghpxphhnektdsgxhdccpbvetdpgkdvuwrvfnxbnygdbyrvtuczarrmnqnkvydxurykebxrwwbtuvmgaqnbxubmdmvhcshnpcwgkxsbfffybxddazaqrrupbxatsnvrbcecsfcgnxedymrpgsvnwaetsnumrfeewkppnkvbbpxdbgdkbhaxsvdgbpurhegewuwkrhpthkpdchxvtpeznugdghuwdfhkdbkysbgunmfuzxtwmmggdbtfumpyvupzgfwxrazgmrkwmurvpmkpdxhxkbhvctugyuuetmpzbvwukpmbwzeskeswtqfdrfqyqkpzkvcmadggexaznunbnyyfuhhpuhytznhrdbyrqnuqxwtgbbvgrrkaatsnbawnxhkezxqapbzfpeqrewbzztgsufevwwmvpkuzhypqwasaceebgcutceenzmasxxsackegtspeumwpsbpxfgnbgdnrdadudreumzaqwweauewvptbhgwfmzfgrdcrrqutsxhhzpuaxqftkutfsvwrykfnhnezgmudwbbubpanpzqzwxvbafutntxhhpngzcfphupuckvfummtuutukaereaqqmvbhtqmyqnrvefckzdqbgnkxmcnvwvhadmztqftpfnpysmunqgcpyruucfbbxbsyspzqqkhgwvdawcbgukhqtg"
    # print(len(str))
    file = open(filename, "a")
    # while True:
    for i in range(mb * 1000):
        # size = os.path.getsize(filename)
        # if size > mb * 1024:
        #     break
        file.write(str)
    file.close()
    print(os.path.getsize(filename))

if __name__ == "__main__":
    generate(104, "large.txt")
