# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_09:18:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,720 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Magura — Alert; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 09:18:04 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:12:33 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:08:59 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-09-22 09:08:55 | Panadugama (Nilwala Ganga) | 5.01 | 🟡 Alert | -0.020 |  |
| 2026-09-22 09:07:33 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:07:10 | Badalgama (Maha Oya) | 3.19 | 🟢 Normal | -0.042 |  |
| 2026-09-22 09:06:06 | Rathnapura (Kalu Ganga) | 4.60 | 🟢 Normal | -0.042 |  |
| 2026-09-22 09:06:01 | Holombuwa (Kelani Ganga) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-09-22 09:05:58 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-22 09:05:33 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.039 |  |
| 2026-09-22 09:05:20 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-22 09:05:15 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 09:05:09 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-22 09:04:32 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-09-22 09:04:29 | Hanwella (Kelani Ganga) | 4.54 | 🟢 Normal | -0.060 |  |
| 2026-09-22 09:04:24 | Glencourse (Kelani Ganga) | 12.31 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-22 09:04:18 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-09-22 09:04:16 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:04:11 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.000 |  |
| 2026-09-22 09:04:08 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:04:02 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-22 09:03:11 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.040 |  |
| 2026-09-22 09:03:06 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:03:05 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-22 09:02:54 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.20 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 09:02:50 | Putupaula (Kalu Ganga) | 2.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 09:02:46 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.010 |  |
| 2026-09-22 09:02:05 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-22 09:02:00 | Nagalagam Street (Kelani Ganga) | 0.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-22 09:01:55 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:01:33 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:01:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:01:18 | Nawalapitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-09-22 09:01:13 | Ellagawa (Kalu Ganga) | 8.99 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:01:10 | Magura (Kalu Ganga) | 4.77 | 🟡 Alert | 0.000 |  |
| 2026-09-22 09:01:07 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:01:03 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-09-22 09:00:59 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 09:00:09 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 09:05:15 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 09:02:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.20 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 09:01:10 | Magura (Kalu Ganga) | 4.77 | 🟡 Alert | 0.000 |  |
| 2026-09-22 09:04:11 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.000 |  |
| 2026-09-22 09:08:55 | Panadugama (Nilwala Ganga) | 5.01 | 🟡 Alert | -0.020 |  |
| 2026-09-22 09:01:18 | Nawalapitiya (Mahaweli Ganga) | 2.30 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-09-22 09:04:32 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | 0.157 | 🔺 Rising |
| 2026-09-22 09:03:05 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-22 09:04:24 | Glencourse (Kelani Ganga) | 12.31 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-22 09:04:02 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-22 09:02:00 | Nagalagam Street (Kelani Ganga) | 0.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-22 09:05:58 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-22 09:05:09 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-22 09:05:20 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-22 09:02:50 | Putupaula (Kalu Ganga) | 2.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 09:00:59 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 09:07:33 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:01:07 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:18:04 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:01:21 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:01:55 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:01:13 | Ellagawa (Kalu Ganga) | 8.99 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:04:08 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:04:16 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:03:06 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:12:33 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:02:54 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:02:46 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.010 |  |
| 2026-09-22 09:02:05 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-22 09:00:09 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-09-22 09:08:59 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-09-22 09:06:01 | Holombuwa (Kelani Ganga) | 2.43 | 🟢 Normal | -0.020 |  |
| 2026-09-22 09:01:03 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-09-22 09:04:18 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.020 |  |
| 2026-09-22 09:05:33 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.039 |  |
| 2026-09-22 09:03:11 | Giriulla (Maha Oya) | 1.90 | 🟢 Normal | -0.040 |  |
| 2026-09-22 09:07:10 | Badalgama (Maha Oya) | 3.19 | 🟢 Normal | -0.042 |  |
| 2026-09-22 09:06:06 | Rathnapura (Kalu Ganga) | 4.60 | 🟢 Normal | -0.042 |  |
| 2026-09-22 09:04:29 | Hanwella (Kelani Ganga) | 4.54 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)