# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_09:11:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,539 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Rathnapura — Alert; 🟡 Pitabeddara — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 09:11:09 | Urawa (Nilwala Ganga) | 2.78 | 🟡 Alert | -0.137 |  |
| 2026-09-24 09:10:41 | Baddegama (Gin Ganga) | 4.21 | 🟠 Minor Flood | 0.038 | 🔺 Rising |
| 2026-09-24 09:08:55 | Rathnapura (Kalu Ganga) | 5.35 | 🟡 Alert | 0.157 | 🔺 Rising |
| 2026-09-24 09:07:13 | Kithulgala (Kelani Ganga) | 2.56 | 🟢 Normal | -0.021 |  |
| 2026-09-24 09:06:43 | Thawalama (Gin Ganga) | 5.22 | 🟡 Alert | 0.043 | 🔺 Rising |
| 2026-09-24 09:06:38 | Pitabeddara (Nilwala Ganga) | 4.83 | 🟡 Alert | 0.088 | 🔺 Rising |
| 2026-09-24 09:06:19 | Panadugama (Nilwala Ganga) | 6.57 | 🟠 Minor Flood | 0.062 | 🔺 Rising |
| 2026-09-24 09:06:17 | Hanwella (Kelani Ganga) | 4.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 09:06:02 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:05:59 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:05:57 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:05:52 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 09:05:46 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:05:42 | Nawalapitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.133 |  |
| 2026-09-24 09:05:26 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:04:57 | Glencourse (Kelani Ganga) | 12.95 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-24 09:04:51 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-09-24 09:04:48 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-24 09:04:47 | Holombuwa (Kelani Ganga) | 1.76 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-09-24 09:04:27 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:04:26 | Magura (Kalu Ganga) | 4.65 | 🟡 Alert | 0.054 | 🔺 Rising |
| 2026-09-24 09:04:22 | Ellagawa (Kalu Ganga) | 7.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 09:04:21 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-24 09:03:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.65 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 09:03:46 | Peradeniya (Mahaweli Ganga) | 3.95 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-09-24 09:03:31 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 09:03:22 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:02:56 | Deraniyagala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.030 |  |
| 2026-09-24 09:02:51 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-09-24 09:02:46 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:02:28 | Dunamale (Aththanagalu Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:02:21 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:02:12 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:02:06 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.044 | 🔺 Rising |
| 2026-09-24 09:01:59 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:00:52 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:00:51 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:00:27 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | -0.011 |  |
| 2026-09-24 09:00:14 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 09:06:19 | Panadugama (Nilwala Ganga) | 6.57 | 🟠 Minor Flood | 0.062 | 🔺 Rising |
| 2026-09-24 09:10:41 | Baddegama (Gin Ganga) | 4.21 | 🟠 Minor Flood | 0.038 | 🔺 Rising |
| 2026-09-24 09:03:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.65 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-24 09:08:55 | Rathnapura (Kalu Ganga) | 5.35 | 🟡 Alert | 0.157 | 🔺 Rising |
| 2026-09-24 09:06:38 | Pitabeddara (Nilwala Ganga) | 4.83 | 🟡 Alert | 0.088 | 🔺 Rising |
| 2026-09-24 09:04:26 | Magura (Kalu Ganga) | 4.65 | 🟡 Alert | 0.054 | 🔺 Rising |
| 2026-09-24 09:02:06 | Thalgahagoda (Nilwala Ganga) | 1.55 | 🟡 Alert | 0.044 | 🔺 Rising |
| 2026-09-24 09:06:43 | Thawalama (Gin Ganga) | 5.22 | 🟡 Alert | 0.043 | 🔺 Rising |
| 2026-09-24 09:11:09 | Urawa (Nilwala Ganga) | 2.78 | 🟡 Alert | -0.137 |  |
| 2026-09-24 09:03:46 | Peradeniya (Mahaweli Ganga) | 3.95 | 🟢 Normal | 0.238 | 🔺 Rising |
| 2026-09-24 09:04:51 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-09-24 09:04:47 | Holombuwa (Kelani Ganga) | 1.76 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-09-24 09:04:57 | Glencourse (Kelani Ganga) | 12.95 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-24 09:04:21 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-24 09:05:52 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 09:03:31 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 09:06:17 | Hanwella (Kelani Ganga) | 4.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-24 09:04:48 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-24 09:04:22 | Ellagawa (Kalu Ganga) | 7.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-24 09:02:12 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:00:51 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:05:57 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:00:52 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:06:02 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:02:46 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:05:46 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:05:59 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:03:22 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:02:28 | Dunamale (Aththanagalu Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:04:27 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:01:59 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:05:26 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:02:21 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-24 09:02:51 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | -0.010 |  |
| 2026-09-24 09:00:27 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | -0.011 |  |
| 2026-09-24 09:00:14 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.020 |  |
| 2026-09-24 09:07:13 | Kithulgala (Kelani Ganga) | 2.56 | 🟢 Normal | -0.021 |  |
| 2026-09-24 09:02:56 | Deraniyagala (Kelani Ganga) | 1.89 | 🟢 Normal | -0.030 |  |
| 2026-09-24 09:05:42 | Nawalapitiya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.133 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)