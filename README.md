# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_08:03:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,603 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **16** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 08:03:01 | Panadugama (Nilwala Ganga) | 5.98 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-12 08:02:50 | Ellagawa (Kalu Ganga) | 8.32 | 🟢 Normal | -0.010 |  |
| 2026-11-12 08:02:47 | Giriulla (Maha Oya) | 3.24 | 🟢 Normal | -0.090 |  |
| 2026-11-12 08:02:40 | Norwood (Kelani Ganga) | 1.50 | 🟡 Alert | -0.041 |  |
| 2026-11-12 08:02:38 | Peradeniya (Mahaweli Ganga) | 5.10 | 🟡 Alert | -0.107 |  |
| 2026-11-12 08:02:08 | Katharagama (Menik Ganga) | 0.71 | 🟢 Normal | -0.061 |  |
| 2026-11-12 08:02:08 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.101 |  |
| 2026-11-12 08:02:07 | Siyambalanduwa (Heda Oya) | 1.29 | 🟢 Normal | -0.091 |  |
| 2026-11-12 08:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-11-12 08:01:49 | Nakkala (Kumbukkan Oya) | 1.77 | 🟢 Normal | -0.075 |  |
| 2026-11-12 08:01:45 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 08:01:15 | Pitabeddara (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.135 |  |
| 2026-11-12 08:01:13 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-11-12 08:01:11 | Wellawaya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.093 |  |
| 2026-11-12 08:00:50 | Weraganthota (Mahaweli Ganga) | -1.34 | 🟢 Normal | -0.104 |  |
| 2026-11-12 07:29:19 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 07:12:10 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 07:29:19 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 07:05:36 | Moraketiya (Walawe Ganga) | 3.75 | 🟡 Alert | 0.234 | 🔺 Rising |
| 2026-11-12 07:07:55 | Dunamale (Aththanagalu Oya) | 4.23 | 🟡 Alert | 0.046 | 🔺 Rising |
| 2026-11-12 08:03:01 | Panadugama (Nilwala Ganga) | 5.98 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-11-12 07:09:22 | Magura (Kalu Ganga) | 5.46 | 🟡 Alert | -0.009 |  |
| 2026-11-12 07:03:57 | Rathnapura (Kalu Ganga) | 5.45 | 🟡 Alert | -0.019 |  |
| 2026-11-12 07:02:34 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | -0.030 |  |
| 2026-11-12 08:02:40 | Norwood (Kelani Ganga) | 1.50 | 🟡 Alert | -0.041 |  |
| 2026-11-12 08:02:38 | Peradeniya (Mahaweli Ganga) | 5.10 | 🟡 Alert | -0.107 |  |
| 2026-11-12 07:18:34 | Thawalama (Gin Ganga) | 4.65 | 🟡 Alert | -0.198 |  |
| 2026-11-12 07:08:13 | Badalgama (Maha Oya) | 4.55 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-11-12 07:01:41 | Horowpothana (Yan Oya) | 2.27 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-11-12 07:04:41 | Hanwella (Kelani Ganga) | 5.65 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-12 08:01:45 | Galgamuwa (Mee Oya) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-12 07:02:38 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-11-12 07:03:15 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-12 08:01:13 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-11-12 08:02:50 | Ellagawa (Kalu Ganga) | 8.32 | 🟢 Normal | -0.010 |  |
| 2026-11-12 08:01:50 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.020 |  |
| 2026-11-12 07:04:14 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | -0.030 |  |
| 2026-11-12 07:00:41 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.034 |  |
| 2026-11-12 07:04:57 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | -0.047 |  |
| 2026-11-12 07:13:07 | Thaldena (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.055 |  |
| 2026-11-12 07:01:13 | Moragaswewa (Deduru Oya) | 3.56 | 🟢 Normal | -0.060 |  |
| 2026-11-12 08:02:08 | Katharagama (Menik Ganga) | 0.71 | 🟢 Normal | -0.061 |  |
| 2026-11-12 07:03:02 | Urawa (Nilwala Ganga) | 2.19 | 🟢 Normal | -0.068 |  |
| 2026-11-12 08:01:49 | Nakkala (Kumbukkan Oya) | 1.77 | 🟢 Normal | -0.075 |  |
| 2026-11-12 07:09:02 | Holombuwa (Kelani Ganga) | 2.03 | 🟢 Normal | -0.078 |  |
| 2026-11-12 07:09:38 | Glencourse (Kelani Ganga) | 13.71 | 🟢 Normal | -0.082 |  |
| 2026-11-12 08:02:47 | Giriulla (Maha Oya) | 3.24 | 🟢 Normal | -0.090 |  |
| 2026-11-12 08:02:07 | Siyambalanduwa (Heda Oya) | 1.29 | 🟢 Normal | -0.091 |  |
| 2026-11-12 08:01:11 | Wellawaya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.093 |  |
| 2026-11-12 08:02:08 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | -0.101 |  |
| 2026-11-12 08:00:50 | Weraganthota (Mahaweli Ganga) | -1.34 | 🟢 Normal | -0.104 |  |
| 2026-11-12 08:01:15 | Pitabeddara (Nilwala Ganga) | 2.79 | 🟢 Normal | -0.135 |  |
| 2026-11-12 07:03:44 | Kuda Oya (Kirindi Oya) | 3.11 | 🟢 Normal | -0.173 |  |
| 2026-11-12 07:03:51 | Thanamalwila (Kirindi Oya) | 3.10 | 🟢 Normal | -0.431 |  |
| 2026-11-12 07:01:52 | Padiyathalawa (Maduru Oya) | 1.51 | 🟢 Normal | -576.000 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)