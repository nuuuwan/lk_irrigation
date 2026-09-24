# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--24_08:14:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **269,500 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Pitabeddara — Alert; 🟡 Rathnapura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 08:14:10 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:11:57 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:11:44 | Rathnapura (Kalu Ganga) | 5.20 | 🟡 Alert | 0.115 | 🔺 Rising |
| 2026-09-24 08:11:09 | Thawalama (Gin Ganga) | 5.18 | 🟡 Alert | 0.098 | 🔺 Rising |
| 2026-09-24 08:08:50 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | 0.090 | 🔺 Rising |
| 2026-09-24 08:08:45 | Kithulgala (Kelani Ganga) | 2.58 | 🟢 Normal | -0.171 |  |
| 2026-09-24 08:08:09 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-09-24 08:08:06 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 08:07:58 | Panadugama (Nilwala Ganga) | 6.51 | 🟠 Minor Flood | 0.123 | 🔺 Rising |
| 2026-09-24 08:07:37 | Baddegama (Gin Ganga) | 4.17 | 🟠 Minor Flood | 0.061 | 🔺 Rising |
| 2026-09-24 08:07:33 | Putupaula (Kalu Ganga) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:06:56 | Thalgahagoda (Nilwala Ganga) | 1.51 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-09-24 08:06:27 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:05:57 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-24 08:05:52 | Glencourse (Kelani Ganga) | 12.88 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-24 08:05:31 | Urawa (Nilwala Ganga) | 2.93 | 🟡 Alert | -0.133 |  |
| 2026-09-24 08:05:20 | Pitabeddara (Nilwala Ganga) | 4.74 | 🟡 Alert | 0.178 | 🔺 Rising |
| 2026-09-24 08:05:19 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:05:19 | Hanwella (Kelani Ganga) | 4.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-24 08:05:10 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-24 08:04:47 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 4.596 | 🔺 Rising |
| 2026-09-24 08:04:18 | Dunamale (Aththanagalu Oya) | 2.54 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-24 08:04:00 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 4.596 | 🔺 Rising |
| 2026-09-24 08:03:49 | Ellagawa (Kalu Ganga) | 7.82 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:03:39 | Holombuwa (Kelani Ganga) | 1.67 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-09-24 08:03:31 | Deraniyagala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.032 |  |
| 2026-09-24 08:03:21 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:03:21 | Peradeniya (Mahaweli Ganga) | 3.71 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-09-24 08:03:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.65 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-24 08:03:05 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:02:58 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-09-24 08:02:41 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-09-24 08:02:31 | Nawalapitiya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.244 |  |
| 2026-09-24 08:02:11 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:01:49 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:01:34 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:01:06 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-09-24 08:00:45 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:00:17 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-24 08:07:58 | Panadugama (Nilwala Ganga) | 6.51 | 🟠 Minor Flood | 0.123 | 🔺 Rising |
| 2026-09-24 08:07:37 | Baddegama (Gin Ganga) | 4.17 | 🟠 Minor Flood | 0.061 | 🔺 Rising |
| 2026-09-24 08:03:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.65 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-24 08:05:20 | Pitabeddara (Nilwala Ganga) | 4.74 | 🟡 Alert | 0.178 | 🔺 Rising |
| 2026-09-24 08:11:44 | Rathnapura (Kalu Ganga) | 5.20 | 🟡 Alert | 0.115 | 🔺 Rising |
| 2026-09-24 08:11:09 | Thawalama (Gin Ganga) | 5.18 | 🟡 Alert | 0.098 | 🔺 Rising |
| 2026-09-24 08:08:50 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | 0.090 | 🔺 Rising |
| 2026-09-24 08:06:56 | Thalgahagoda (Nilwala Ganga) | 1.51 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-09-24 08:05:31 | Urawa (Nilwala Ganga) | 2.93 | 🟡 Alert | -0.133 |  |
| 2026-09-24 08:04:47 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 4.596 | 🔺 Rising |
| 2026-09-24 08:03:21 | Peradeniya (Mahaweli Ganga) | 3.71 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-09-24 08:03:39 | Holombuwa (Kelani Ganga) | 1.67 | 🟢 Normal | 0.196 | 🔺 Rising |
| 2026-09-24 08:08:09 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-09-24 08:04:18 | Dunamale (Aththanagalu Oya) | 2.54 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-24 08:02:58 | Giriulla (Maha Oya) | 1.54 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-09-24 08:05:52 | Glencourse (Kelani Ganga) | 12.88 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-09-24 08:00:17 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-24 08:05:19 | Hanwella (Kelani Ganga) | 4.73 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-24 08:05:57 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-24 08:05:10 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-24 08:08:06 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-24 08:00:45 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:01:34 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:01:49 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:11:57 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:03:49 | Ellagawa (Kalu Ganga) | 7.82 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:14:10 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:03:05 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:06:27 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:07:33 | Putupaula (Kalu Ganga) | 2.61 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:03:21 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:05:19 | Kuda Oya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-24 08:02:11 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-24 07:23:05 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.007 |  |
| 2026-09-24 08:01:06 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-09-24 08:02:41 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.020 |  |
| 2026-09-24 08:03:31 | Deraniyagala (Kelani Ganga) | 1.92 | 🟢 Normal | -0.032 |  |
| 2026-09-24 08:08:45 | Kithulgala (Kelani Ganga) | 2.58 | 🟢 Normal | -0.171 |  |
| 2026-09-24 08:02:31 | Nawalapitiya (Mahaweli Ganga) | 2.79 | 🟢 Normal | -0.244 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)