# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_01:03:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,671 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Panadugama — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Thalgahagoda — Alert; 🟡 Moraketiya — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 01:03:08 | Dunamale (Aththanagalu Oya) | 4.05 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-11-09 01:02:58 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.019 |  |
| 2026-11-09 01:02:43 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-09 01:02:34 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-09 01:02:20 | Giriulla (Maha Oya) | 4.16 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-11-09 01:02:17 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-09 01:02:16 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-09 01:02:07 | Hanwella (Kelani Ganga) | 5.07 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-11-09 01:02:02 | Moragaswewa (Deduru Oya) | 3.37 | 🟢 Normal | -0.021 |  |
| 2026-11-09 01:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-11-09 01:01:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.64 | 🟡 Alert | 0.024 | 🔺 Rising |
| 2026-11-09 01:01:24 | Ellagawa (Kalu Ganga) | 8.13 | 🟢 Normal | -0.021 |  |
| 2026-11-09 01:00:36 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | -0.122 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 00:02:12 | Magura (Kalu Ganga) | 4.75 | 🟡 Alert | 0.120 | 🔺 Rising |
| 2026-11-09 00:09:20 | Panadugama (Nilwala Ganga) | 5.80 | 🟡 Alert | 0.072 | 🔺 Rising |
| 2026-11-09 01:03:08 | Dunamale (Aththanagalu Oya) | 4.05 | 🟡 Alert | 0.070 | 🔺 Rising |
| 2026-11-09 01:01:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.64 | 🟡 Alert | 0.024 | 🔺 Rising |
| 2026-11-09 00:13:03 | Thalgahagoda (Nilwala Ganga) | 1.44 | 🟡 Alert | 0.017 | 🔺 Rising |
| 2026-11-09 00:16:41 | Moraketiya (Walawe Ganga) | 3.06 | 🟡 Alert | 0.000 |  |
| 2026-11-09 00:08:46 | Thawalama (Gin Ganga) | 4.12 | 🟡 Alert | -0.066 |  |
| 2026-11-09 00:07:28 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | 0.474 | 🔺 Rising |
| 2026-11-09 01:02:20 | Giriulla (Maha Oya) | 4.16 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-11-09 00:14:32 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-11-09 00:06:03 | Badalgama (Maha Oya) | 3.94 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-11-09 01:02:07 | Hanwella (Kelani Ganga) | 5.07 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-11-09 00:16:03 | Glencourse (Kelani Ganga) | 13.61 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-11-08 23:05:11 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-08 23:04:45 | Urawa (Nilwala Ganga) | 1.70 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-11-08 18:01:44 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-09 00:12:24 | Baddegama (Gin Ganga) | 3.30 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-09 00:12:33 | Putupaula (Kalu Ganga) | 2.10 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-09 00:04:44 | Horowpothana (Yan Oya) | 3.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-09 00:17:34 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 01:02:43 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-09 01:02:17 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-09 00:07:33 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-09 01:02:16 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-09 01:02:34 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-08 18:02:22 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-11-08 23:07:10 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.018 |  |
| 2026-11-09 00:03:46 | Thanamalwila (Kirindi Oya) | 1.50 | 🟢 Normal | -0.019 |  |
| 2026-11-09 01:02:58 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.019 |  |
| 2026-11-09 01:01:59 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-11-08 18:01:41 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.020 |  |
| 2026-11-09 01:01:24 | Ellagawa (Kalu Ganga) | 8.13 | 🟢 Normal | -0.021 |  |
| 2026-11-09 01:02:02 | Moragaswewa (Deduru Oya) | 3.37 | 🟢 Normal | -0.021 |  |
| 2026-11-09 00:15:16 | Pitabeddara (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.042 |  |
| 2026-11-09 00:04:00 | Rathnapura (Kalu Ganga) | 4.17 | 🟢 Normal | -0.050 |  |
| 2026-11-09 00:01:00 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.083 |  |
| 2026-11-09 01:00:36 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | -0.122 |  |
| 2026-11-09 00:04:48 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.165 |  |
| 2026-11-09 00:08:35 | Holombuwa (Kelani Ganga) | 2.19 | 🟢 Normal | -0.381 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)