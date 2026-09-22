# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_15:06:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,951 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 15:06:25 | Thawalama (Gin Ganga) | 2.78 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-22 15:06:01 | Thalgahagoda (Nilwala Ganga) | 1.53 | 🟡 Alert | 0.000 |  |
| 2026-09-22 15:05:05 | Holombuwa (Kelani Ganga) | 1.59 | 🟢 Normal | -0.147 |  |
| 2026-09-22 15:04:51 | Rathnapura (Kalu Ganga) | 4.26 | 🟢 Normal | -0.057 |  |
| 2026-09-22 15:04:47 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | -0.011 |  |
| 2026-09-22 15:04:20 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-22 15:04:18 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:04:08 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-09-22 15:04:01 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:03:49 | Dunamale (Aththanagalu Oya) | 2.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 15:03:43 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:03:27 | Hanwella (Kelani Ganga) | 4.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-22 15:03:24 | Putupaula (Kalu Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:03:10 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.17 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-22 15:03:01 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:02:49 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-22 15:02:25 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:02:22 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-09-22 15:02:12 | Deraniyagala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.050 |  |
| 2026-09-22 15:02:04 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-09-22 15:01:48 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:01:47 | Ellagawa (Kalu Ganga) | 8.83 | 🟢 Normal | -0.020 |  |
| 2026-09-22 15:01:35 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-09-22 15:01:33 | Magura (Kalu Ganga) | 4.73 | 🟡 Alert | -0.020 |  |
| 2026-09-22 15:01:30 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.010 |  |
| 2026-09-22 15:01:24 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | -0.030 |  |
| 2026-09-22 15:01:19 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:01:16 | Nawalapitiya (Mahaweli Ganga) | 2.26 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-22 15:00:51 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:00:47 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.011 |  |
| 2026-09-22 15:00:27 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.021 |  |
| 2026-09-22 15:00:12 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.010 |  |
| 2026-09-22 14:28:24 | Holombuwa (Kelani Ganga) | 1.68 | 🟢 Normal | -0.147 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 15:03:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.17 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-22 15:01:24 | Baddegama (Gin Ganga) | 4.13 | 🟠 Minor Flood | -0.030 |  |
| 2026-09-22 15:06:01 | Thalgahagoda (Nilwala Ganga) | 1.53 | 🟡 Alert | 0.000 |  |
| 2026-09-22 15:01:33 | Magura (Kalu Ganga) | 4.73 | 🟡 Alert | -0.020 |  |
| 2026-09-22 14:00:24 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-09-22 15:06:25 | Thawalama (Gin Ganga) | 2.78 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-22 15:01:16 | Nawalapitiya (Mahaweli Ganga) | 2.26 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-22 15:04:20 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-22 15:02:49 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-22 15:03:27 | Hanwella (Kelani Ganga) | 4.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-22 15:03:49 | Dunamale (Aththanagalu Oya) | 2.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 15:02:25 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:03:10 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:01:19 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:04:18 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:02:22 | Pitabeddara (Nilwala Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:10:41 | Panadugama (Nilwala Ganga) | 4.87 | 🟢 Normal | 0.000 |  |
| 2026-09-22 14:03:00 | Glencourse (Kelani Ganga) | 12.65 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:01:48 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:04:01 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:03:01 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:03:24 | Putupaula (Kalu Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:00:51 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:03:43 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-22 15:01:35 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-09-22 15:02:04 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-09-22 15:00:12 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.010 |  |
| 2026-09-22 15:01:30 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.010 |  |
| 2026-09-22 15:04:08 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-09-22 15:04:47 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | -0.011 |  |
| 2026-09-22 15:00:47 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.011 |  |
| 2026-09-22 15:01:47 | Ellagawa (Kalu Ganga) | 8.83 | 🟢 Normal | -0.020 |  |
| 2026-09-22 15:00:27 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.021 |  |
| 2026-09-22 14:05:22 | Badalgama (Maha Oya) | 2.99 | 🟢 Normal | -0.021 |  |
| 2026-09-22 14:04:27 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-09-22 15:02:22 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-09-22 15:02:12 | Deraniyagala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.050 |  |
| 2026-09-22 15:04:51 | Rathnapura (Kalu Ganga) | 4.26 | 🟢 Normal | -0.057 |  |
| 2026-09-22 15:05:05 | Holombuwa (Kelani Ganga) | 1.59 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)