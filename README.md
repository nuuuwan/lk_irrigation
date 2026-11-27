# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--28_00:22:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **327,510 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Panadugama — Alert; 🟡 Moraketiya — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 00:22:27 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-28 00:22:25 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-28 00:18:12 | Dunamale (Aththanagalu Oya) | 3.59 | 🟡 Alert | 0.131 | 🔺 Rising |
| 2026-11-28 00:18:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.18 | 🟡 Alert | -0.016 |  |
| 2026-11-28 00:13:24 | Magura (Kalu Ganga) | 3.82 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-28 00:12:15 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-11-28 00:10:11 | Thanamalwila (Kirindi Oya) | 3.50 | 🟢 Normal | -0.123 |  |
| 2026-11-28 00:08:26 | Putupaula (Kalu Ganga) | 1.41 | 🟢 Normal | -0.019 |  |
| 2026-11-28 00:08:13 | Holombuwa (Kelani Ganga) | 2.53 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-11-28 00:07:26 | Rathnapura (Kalu Ganga) | 3.14 | 🟢 Normal | -0.028 |  |
| 2026-11-28 00:07:09 | Pitabeddara (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-28 00:06:54 | Panadugama (Nilwala Ganga) | 5.38 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-11-28 00:06:51 | Urawa (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-11-28 00:06:35 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-11-28 00:06:03 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-28 00:05:28 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-28 00:05:24 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-28 00:04:53 | Siyambalanduwa (Heda Oya) | 1.22 | 🟢 Normal | -0.086 |  |
| 2026-11-28 00:04:28 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.028 |  |
| 2026-11-28 00:04:21 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.039 |  |
| 2026-11-28 00:03:59 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-11-28 00:03:47 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-28 00:03:39 | Moraketiya (Walawe Ganga) | 3.78 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-11-28 00:03:30 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.086 |  |
| 2026-11-28 00:03:24 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-11-28 00:03:12 | Badalgama (Maha Oya) | 4.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-28 00:02:57 | Giriulla (Maha Oya) | 3.75 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-28 00:02:53 | Glencourse (Kelani Ganga) | 12.69 | 🟢 Normal | -0.092 |  |
| 2026-11-28 00:02:47 | Wellawaya (Kirindi Oya) | 1.84 | 🟢 Normal | -0.019 |  |
| 2026-11-28 00:02:25 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.040 |  |
| 2026-11-28 00:02:22 | Kuda Oya (Kirindi Oya) | 4.09 | 🟢 Normal | -0.119 |  |
| 2026-11-28 00:02:22 | Hanwella (Kelani Ganga) | 4.02 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-11-28 00:01:55 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-28 00:01:27 | Yaka Wewa (Ma Oya) | 0.00 | 🟢 Normal | -0.501 |  |
| 2026-11-28 00:01:16 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-28 00:01:08 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | 0.000 |  |
| 2026-11-28 00:00:59 | Moragaswewa (Deduru Oya) | 2.84 | 🟢 Normal | -0.030 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-28 00:18:12 | Dunamale (Aththanagalu Oya) | 3.59 | 🟡 Alert | 0.131 | 🔺 Rising |
| 2026-11-28 00:06:54 | Panadugama (Nilwala Ganga) | 5.38 | 🟡 Alert | 0.050 | 🔺 Rising |
| 2026-11-28 00:03:39 | Moraketiya (Walawe Ganga) | 3.78 | 🟡 Alert | 0.029 | 🔺 Rising |
| 2026-11-28 00:18:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.18 | 🟡 Alert | -0.016 |  |
| 2026-11-28 00:03:24 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | 0.285 | 🔺 Rising |
| 2026-11-28 00:08:13 | Holombuwa (Kelani Ganga) | 2.53 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-11-28 00:02:22 | Hanwella (Kelani Ganga) | 4.02 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-11-28 00:06:35 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-11-28 00:01:55 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-11-28 00:06:51 | Urawa (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-11-28 00:07:09 | Pitabeddara (Nilwala Ganga) | 2.58 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-28 00:03:59 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-11-28 00:02:57 | Giriulla (Maha Oya) | 3.75 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-11-28 00:13:24 | Magura (Kalu Ganga) | 3.82 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-28 00:05:24 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-28 00:03:12 | Badalgama (Maha Oya) | 4.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-28 00:01:16 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-11-28 00:03:47 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | 0.000 |  |
| 2026-11-27 18:04:37 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-28 00:22:27 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-28 00:06:03 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-28 00:01:08 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | 0.000 |  |
| 2026-11-28 00:05:28 | Thalgahagoda (Nilwala Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-28 00:12:15 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-11-28 00:02:47 | Wellawaya (Kirindi Oya) | 1.84 | 🟢 Normal | -0.019 |  |
| 2026-11-28 00:08:26 | Putupaula (Kalu Ganga) | 1.41 | 🟢 Normal | -0.019 |  |
| 2026-11-28 00:04:28 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.028 |  |
| 2026-11-28 00:07:26 | Rathnapura (Kalu Ganga) | 3.14 | 🟢 Normal | -0.028 |  |
| 2026-11-28 00:00:59 | Moragaswewa (Deduru Oya) | 2.84 | 🟢 Normal | -0.030 |  |
| 2026-11-27 18:01:42 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | -0.031 |  |
| 2026-11-28 00:04:21 | Thawalama (Gin Ganga) | 2.31 | 🟢 Normal | -0.039 |  |
| 2026-11-28 00:02:25 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.040 |  |
| 2026-11-27 18:00:16 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | -0.041 |  |
| 2026-11-28 00:03:30 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.086 |  |
| 2026-11-28 00:04:53 | Siyambalanduwa (Heda Oya) | 1.22 | 🟢 Normal | -0.086 |  |
| 2026-11-28 00:02:53 | Glencourse (Kelani Ganga) | 12.69 | 🟢 Normal | -0.092 |  |
| 2026-11-28 00:02:22 | Kuda Oya (Kirindi Oya) | 4.09 | 🟢 Normal | -0.119 |  |
| 2026-11-28 00:10:11 | Thanamalwila (Kirindi Oya) | 3.50 | 🟢 Normal | -0.123 |  |
| 2026-11-28 00:01:27 | Yaka Wewa (Ma Oya) | 0.00 | 🟢 Normal | -0.501 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)