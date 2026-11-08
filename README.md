# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--09_00:03:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,633 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert; 🟡 Magura — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Thalgahagoda — Alert; 🟡 Moraketiya — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **9** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-09 00:03:08 | Dunamale (Aththanagalu Oya) | 3.98 | 🟡 Alert | 0.099 | 🔺 Rising |
| 2026-11-09 00:02:13 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-09 00:02:12 | Magura (Kalu Ganga) | 4.75 | 🟡 Alert | 0.120 | 🔺 Rising |
| 2026-11-09 00:02:02 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.020 |  |
| 2026-11-09 00:01:50 | Giriulla (Maha Oya) | 3.98 | 🟢 Normal | 0.342 | 🔺 Rising |
| 2026-11-09 00:01:37 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | -0.146 |  |
| 2026-11-09 00:01:34 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-09 00:01:09 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-09 00:01:00 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.083 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 23:02:47 | Panadugama (Nilwala Ganga) | 5.72 | 🟡 Alert | 0.139 | 🔺 Rising |
| 2026-11-09 00:02:12 | Magura (Kalu Ganga) | 4.75 | 🟡 Alert | 0.120 | 🔺 Rising |
| 2026-11-09 00:03:08 | Dunamale (Aththanagalu Oya) | 3.98 | 🟡 Alert | 0.099 | 🔺 Rising |
| 2026-11-08 23:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.60 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-11-08 23:04:12 | Thalgahagoda (Nilwala Ganga) | 1.42 | 🟡 Alert | 0.000 |  |
| 2026-11-08 23:00:32 | Moraketiya (Walawe Ganga) | 3.06 | 🟡 Alert | -0.020 |  |
| 2026-11-08 23:05:03 | Thawalama (Gin Ganga) | 4.19 | 🟡 Alert | -0.067 |  |
| 2026-11-08 23:05:00 | Hanwella (Kelani Ganga) | 4.70 | 🟢 Normal | 0.366 | 🔺 Rising |
| 2026-11-09 00:01:50 | Giriulla (Maha Oya) | 3.98 | 🟢 Normal | 0.342 | 🔺 Rising |
| 2026-11-08 23:06:43 | Badalgama (Maha Oya) | 3.78 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-11-08 23:11:24 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-11-08 23:05:11 | Yaka Wewa (Ma Oya) | 1.18 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-08 22:12:22 | Putupaula (Kalu Ganga) | 2.04 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-11-08 23:04:45 | Urawa (Nilwala Ganga) | 1.70 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-11-08 18:01:44 | Thanthirimale (Malwathu Oya) | 1.64 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-11-08 23:11:21 | Baddegama (Gin Ganga) | 3.24 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-08 23:05:30 | Glencourse (Kelani Ganga) | 13.50 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-08 23:04:12 | Rathnapura (Kalu Ganga) | 4.22 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-11-08 23:03:00 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-08 23:01:57 | Horowpothana (Yan Oya) | 3.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-09 00:01:34 | Kuda Oya (Kirindi Oya) | 1.86 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-09 00:01:09 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-08 23:02:16 | Moragaswewa (Deduru Oya) | 3.38 | 🟢 Normal | 0.000 |  |
| 2026-11-09 00:02:13 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-11-08 23:05:51 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-08 23:04:37 | Siyambalanduwa (Heda Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-11-08 23:01:29 | Thanamalwila (Kirindi Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-08 22:08:41 | Norwood (Kelani Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-11-08 18:02:22 | Galgamuwa (Mee Oya) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-11-08 23:07:10 | Wellawaya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.018 |  |
| 2026-11-09 00:02:02 | Nawalapitiya (Mahaweli Ganga) | 1.77 | 🟢 Normal | -0.020 |  |
| 2026-11-08 18:01:41 | Weraganthota (Mahaweli Ganga) | -2.78 | 🟢 Normal | -0.020 |  |
| 2026-11-08 23:02:03 | Ellagawa (Kalu Ganga) | 8.16 | 🟢 Normal | -0.020 |  |
| 2026-11-08 23:10:31 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.039 |  |
| 2026-11-08 23:03:37 | Pitabeddara (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.079 |  |
| 2026-11-09 00:01:00 | Thaldena (Mahaweli Ganga) | 0.98 | 🟢 Normal | -0.083 |  |
| 2026-11-08 23:02:55 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.129 |  |
| 2026-11-09 00:01:37 | Peradeniya (Mahaweli Ganga) | 4.10 | 🟢 Normal | -0.146 |  |
| 2026-11-08 23:03:57 | Holombuwa (Kelani Ganga) | 2.60 | 🟢 Normal | -0.329 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)