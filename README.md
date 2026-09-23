# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_04:26:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,343 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thawalama — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert; 🟡 Urawa — Alert; 🟡 Baddegama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 04:26:21 | Glencourse (Kelani Ganga) | 12.76 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:19:28 | Thalgahagoda (Nilwala Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:15:42 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | -0.023 |  |
| 2026-09-24 04:15:39 | Nawalapitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-24 04:11:50 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.057 |  |
| 2026-09-24 04:10:43 | Rathnapura (Kalu Ganga) | 4.57 | 🟢 Normal | 0.303 | 🔺 Rising |
| 2026-09-24 04:10:26 | Norwood (Kelani Ganga) | 1.34 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-09-24 04:08:45 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:08:37 | Thalgahagoda (Nilwala Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:08:29 | Baddegama (Gin Ganga) | 3.96 | 🟡 Alert | 0.061 | 🔺 Rising |
| 2026-09-24 04:07:54 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:06:53 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-24 04:06:33 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:06:17 | Urawa (Nilwala Ganga) | 3.12 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-09-24 04:06:14 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 04:06:09 | Hanwella (Kelani Ganga) | 4.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 04:06:07 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:05:30 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-24 04:04:46 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:04:36 | Pitabeddara (Nilwala Ganga) | 3.38 | 🟢 Normal | 0.502 | 🔺 Rising |
| 2026-09-24 04:04:28 | Panadugama (Nilwala Ganga) | 5.21 | 🟡 Alert | 0.169 | 🔺 Rising |
| 2026-09-24 04:04:22 | Kithulgala (Kelani Ganga) | 2.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 04:04:20 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:03:56 | Deraniyagala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.031 |  |
| 2026-09-24 04:03:19 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-09-24 04:03:12 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:02:52 | Thawalama (Gin Ganga) | 4.78 | 🟡 Alert | 0.186 | 🔺 Rising |
| 2026-09-24 04:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.81 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-24 04:02:13 | Ellagawa (Kalu Ganga) | 7.79 | 🟢 Normal | -0.052 |  |
| 2026-09-24 04:02:09 | Peradeniya (Mahaweli Ganga) | 3.70 | 🟢 Normal | -0.066 |  |
| 2026-09-24 04:01:22 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:01:16 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:00:45 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:00:33 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:00:21 | Magura (Kalu Ganga) | 4.21 | 🟡 Alert | 0.165 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 04:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.81 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-24 04:02:52 | Thawalama (Gin Ganga) | 4.78 | 🟡 Alert | 0.186 | 🔺 Rising |
| 2026-09-24 04:04:28 | Panadugama (Nilwala Ganga) | 5.21 | 🟡 Alert | 0.169 | 🔺 Rising |
| 2026-09-24 04:00:21 | Magura (Kalu Ganga) | 4.21 | 🟡 Alert | 0.165 | 🔺 Rising |
| 2026-09-24 04:06:17 | Urawa (Nilwala Ganga) | 3.12 | 🟡 Alert | 0.100 | 🔺 Rising |
| 2026-09-24 04:08:29 | Baddegama (Gin Ganga) | 3.96 | 🟡 Alert | 0.061 | 🔺 Rising |
| 2026-09-24 04:04:36 | Pitabeddara (Nilwala Ganga) | 3.38 | 🟢 Normal | 0.502 | 🔺 Rising |
| 2026-09-24 04:10:43 | Rathnapura (Kalu Ganga) | 4.57 | 🟢 Normal | 0.303 | 🔺 Rising |
| 2026-09-24 04:10:26 | Norwood (Kelani Ganga) | 1.34 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-09-24 04:15:39 | Nawalapitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-09-24 04:05:30 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-24 04:06:53 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-24 04:04:22 | Kithulgala (Kelani Ganga) | 2.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 04:06:14 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 04:06:09 | Hanwella (Kelani Ganga) | 4.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 04:00:33 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:04:46 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:01:22 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:21:42 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:04:20 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:09:53 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:26:21 | Glencourse (Kelani Ganga) | 12.76 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:00:45 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:07:54 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:06:07 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:08:45 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-09-24 03:02:58 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:03:31 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:19:28 | Thalgahagoda (Nilwala Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:06:33 | Kuda Oya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-24 04:01:16 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-23 18:10:48 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-09-23 18:01:34 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.020 |  |
| 2026-09-24 04:03:19 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-09-24 04:15:42 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | -0.023 |  |
| 2026-09-24 04:03:56 | Deraniyagala (Kelani Ganga) | 1.78 | 🟢 Normal | -0.031 |  |
| 2026-09-24 04:02:13 | Ellagawa (Kalu Ganga) | 7.79 | 🟢 Normal | -0.052 |  |
| 2026-09-24 04:11:50 | Holombuwa (Kelani Ganga) | 1.44 | 🟢 Normal | -0.057 |  |
| 2026-09-24 04:02:09 | Peradeniya (Mahaweli Ganga) | 3.70 | 🟢 Normal | -0.066 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)