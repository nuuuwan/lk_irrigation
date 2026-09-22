# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_08:23:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,680 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert; 🟡 Magura — Alert; 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 08:23:59 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-22 08:19:23 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | -0.028 |  |
| 2026-09-22 08:16:01 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | -0.047 |  |
| 2026-09-22 08:10:21 | Panadugama (Nilwala Ganga) | 5.03 | 🟡 Alert | 0.000 |  |
| 2026-09-22 08:09:53 | Badalgama (Maha Oya) | 3.23 | 🟢 Normal | -0.062 |  |
| 2026-09-22 08:09:38 | Panadugama (Nilwala Ganga) | 5.03 | 🟡 Alert | 0.000 |  |
| 2026-09-22 08:09:23 | Rathnapura (Kalu Ganga) | 4.64 | 🟢 Normal | -0.041 |  |
| 2026-09-22 08:08:06 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-22 08:07:11 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-09-22 08:07:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 08:07:05 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-09-22 08:06:24 | Glencourse (Kelani Ganga) | 12.27 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-22 08:06:02 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-22 08:05:24 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 08:05:01 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 08:05:01 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 08:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.20 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 08:10:21 | Panadugama (Nilwala Ganga) | 5.03 | 🟡 Alert | 0.000 |  |
| 2026-09-22 08:01:54 | Magura (Kalu Ganga) | 4.77 | 🟡 Alert | -0.021 |  |
| 2026-09-22 08:16:01 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | -0.047 |  |
| 2026-09-22 08:07:11 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.198 | 🔺 Rising |
| 2026-09-22 08:03:59 | Nawalapitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-09-22 08:06:24 | Glencourse (Kelani Ganga) | 12.27 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-09-22 08:06:02 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-09-22 08:02:13 | Nagalagam Street (Kelani Ganga) | 0.75 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-22 08:04:51 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-22 08:04:52 | Holombuwa (Kelani Ganga) | 2.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-22 08:00:47 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 08:08:06 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-22 08:23:59 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-22 08:02:11 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-09-22 08:02:37 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 08:02:03 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-22 08:01:34 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 08:00:18 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-09-22 08:07:05 | Pitabeddara (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-09-22 08:04:04 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-22 08:03:14 | Ellagawa (Kalu Ganga) | 8.99 | 🟢 Normal | 0.000 |  |
| 2026-09-22 08:07:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 08:00:42 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-09-22 08:05:24 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 08:04:19 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-09-22 08:03:51 | Thawalama (Gin Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-09-22 08:00:26 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-22 08:02:24 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 08:01:55 | Thanthirimale (Malwathu Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-09-22 08:02:46 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-09-22 08:00:36 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.010 |  |
| 2026-09-22 08:19:23 | Galgamuwa (Mee Oya) | 0.25 | 🟢 Normal | -0.028 |  |
| 2026-09-22 08:09:23 | Rathnapura (Kalu Ganga) | 4.64 | 🟢 Normal | -0.041 |  |
| 2026-09-22 08:03:00 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.042 |  |
| 2026-09-22 08:04:04 | Hanwella (Kelani Ganga) | 4.60 | 🟢 Normal | -0.062 |  |
| 2026-09-22 08:09:53 | Badalgama (Maha Oya) | 3.23 | 🟢 Normal | -0.062 |  |
| 2026-09-22 08:03:28 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)