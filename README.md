# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_23:03:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,603 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Panadugama — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Thalgahagoda — Alert; 🟡 Moraketiya — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 23:03:00 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-08 23:02:55 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.129 |  |
| 2026-11-08 23:02:47 | Panadugama (Nilwala Ganga) | 5.72 | 🟡 Alert | 0.139 | 🔺 Rising |
| 2026-11-08 23:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.60 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-11-08 23:02:18 | Dunamale (Aththanagalu Oya) | 3.88 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-11-08 23:02:16 | Moragaswewa (Deduru Oya) | 3.38 | 🟢 Normal | 0.000 |  |
| 2026-11-08 23:02:03 | Ellagawa (Kalu Ganga) | 8.16 | 🟢 Normal | -0.020 |  |
| 2026-11-08 23:01:57 | Horowpothana (Yan Oya) | 3.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-08 23:01:42 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-08 23:01:37 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-08 23:01:29 | Thanamalwila (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-08 23:00:57 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.090 |  |
| 2026-11-08 23:00:32 | Moraketiya (Walawe Ganga) | 3.06 | 🟡 Alert | -0.020 |  |
| 2026-11-08 22:24:33 | Yaka Wewa (Ma Oya) | 1.12 | 🟢 Normal | 0.145 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 22:17:24 | Magura (Kalu Ganga) | 4.53 | 🟡 Alert | 0.142 | 🔺 Rising |
| 2026-11-08 23:02:47 | Panadugama (Nilwala Ganga) | 5.72 | 🟡 Alert | 0.139 | 🔺 Rising |
| 2026-11-08 23:02:18 | Dunamale (Aththanagalu Oya) | 3.88 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-11-08 23:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.60 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-11-08 22:19:09 | Thalgahagoda (Nilwala Ganga) | 1.42 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-11-08 23:00:32 | Moraketiya (Walawe Ganga) | 3.06 | 🟡 Alert | -0.020 |  |
| 2026-11-08 22:02:21 | Thawalama (Gin Ganga) | 4.26 | 🟡 Alert | -0.061 |  |
| 2026-11-08 22:09:18 | Hanwella (Kelani Ganga) | 4.36 | 🟢 Normal | 0.392 | 🔺 Rising |
| 2026-11-08 22:04:51 | Glencourse (Kelani Ganga) | 13.45 | 🟢 Normal | 0.220 | 🔺 Rising |
| 2026-11-08 22:01:00 | Urawa (Nilwala Ganga) | 1.63 | 🟢 Normal | 0.216 | 🔺 Rising |
| 2026-11-08 22:03:06 | Giriulla (Maha Oya) | 3.33 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-11-08 22:07:32 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-11-08 22:24:33 | Yaka Wewa (Ma Oya) | 1.12 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-11-08 22:12:22 | Putupaula (Kalu Ganga) | 2.04 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-08 18:01:44 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-08 22:11:18 | Baddegama (Gin Ganga) | 3.19 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-08 22:01:06 | Peradeniya (Mahaweli Ganga) | 4.48 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-08 23:03:00 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-08 22:09:24 | Badalgama (Maha Oya) | 3.63 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-08 23:01:57 | Horowpothana (Yan Oya) | 3.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-08 23:01:37 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-08 23:02:16 | Moragaswewa (Deduru Oya) | 3.38 | 🟢 Normal | 0.000 |  |
| 2026-11-08 22:18:03 | Pitabeddara (Nilwala Ganga) | 2.76 | 🟢 Normal | 0.000 |  |
| 2026-11-08 23:01:42 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-08 22:08:58 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-08 22:08:24 | Rathnapura (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-11-08 23:01:29 | Thanamalwila (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-08 22:01:38 | Kuda Oya (Kirindi Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-11-08 22:08:41 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-08 18:02:22 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-11-08 18:01:41 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.020 |  |
| 2026-11-08 22:03:08 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | -0.020 |  |
| 2026-11-08 22:02:07 | Wellawaya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-11-08 23:02:03 | Ellagawa (Kalu Ganga) | 8.16 | 🟢 Normal | -0.020 |  |
| 2026-11-08 22:08:50 | Thaldena (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.027 |  |
| 2026-11-08 23:00:57 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.090 |  |
| 2026-11-08 23:02:55 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.129 |  |
| 2026-11-08 22:08:59 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.204 |  |
| 2026-11-08 22:05:36 | Holombuwa (Kelani Ganga) | 2.92 | 🟢 Normal | -0.432 |  |

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)