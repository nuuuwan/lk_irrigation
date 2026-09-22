# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_06:31:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,595 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert; 🟡 Magura — Alert; 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 06:31:59 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.002 |  |
| 2026-09-22 06:10:11 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 06:08:08 | Thalgahagoda (Nilwala Ganga) | 1.56 | 🟡 Alert | -0.048 |  |
| 2026-09-22 06:07:46 | Holombuwa (Kelani Ganga) | 2.48 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-22 06:07:45 | Rathnapura (Kalu Ganga) | 4.74 | 🟢 Normal | -0.066 |  |
| 2026-09-22 06:07:40 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 06:07:14 | Ellagawa (Kalu Ganga) | 8.99 | 🟢 Normal | 0.000 |  |
| 2026-09-22 06:06:43 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.009 |  |
| 2026-09-22 06:05:13 | Badalgama (Maha Oya) | 3.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 06:05:12 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-09-22 06:05:01 | Panadugama (Nilwala Ganga) | 5.10 | 🟡 Alert | 0.000 |  |
| 2026-09-22 06:04:47 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-22 06:04:42 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-09-22 06:04:14 | Glencourse (Kelani Ganga) | 12.23 | 🟢 Normal | -0.020 |  |
| 2026-09-22 06:04:08 | Peradeniya (Mahaweli Ganga) | 3.27 | 🟢 Normal | -0.560 |  |
| 2026-09-22 06:04:02 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.049 |  |
| 2026-09-22 06:04:01 | Panadugama (Nilwala Ganga) | 5.10 | 🟡 Alert | 0.000 |  |
| 2026-09-22 06:03:58 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.001 |  |
| 2026-09-22 06:03:54 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-09-22 06:03:19 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-22 06:02:47 | Thawalama (Gin Ganga) | 2.63 | 🟢 Normal | -0.039 |  |
| 2026-09-22 06:02:45 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 06:02:37 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.035 |  |
| 2026-09-22 06:02:32 | Hanwella (Kelani Ganga) | 4.75 | 🟢 Normal | -0.080 |  |
| 2026-09-22 06:02:17 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.027 |  |
| 2026-09-22 06:02:11 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-09-22 06:02:11 | Dunamale (Aththanagalu Oya) | 2.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 06:02:10 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-22 06:02:01 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.031 |  |
| 2026-09-22 06:01:55 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-22 06:01:47 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 06:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.20 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 06:01:08 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-09-22 06:00:55 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-09-22 06:00:53 | Magura (Kalu Ganga) | 4.82 | 🟡 Alert | -0.040 |  |
| 2026-09-22 06:00:46 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 06:00:42 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-09-22 06:00:28 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-09-22 05:53:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 06:07:40 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 06:01:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.20 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 06:05:01 | Panadugama (Nilwala Ganga) | 5.10 | 🟡 Alert | 0.000 |  |
| 2026-09-22 06:00:53 | Magura (Kalu Ganga) | 4.82 | 🟡 Alert | -0.040 |  |
| 2026-09-22 06:08:08 | Thalgahagoda (Nilwala Ganga) | 1.56 | 🟡 Alert | -0.048 |  |
| 2026-09-22 06:01:08 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-09-22 06:02:10 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-09-22 06:07:46 | Holombuwa (Kelani Ganga) | 2.48 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-09-22 06:03:19 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-22 06:02:11 | Dunamale (Aththanagalu Oya) | 2.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 06:00:46 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 06:05:13 | Badalgama (Maha Oya) | 3.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 06:02:45 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 06:01:47 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 06:04:47 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-22 06:07:14 | Ellagawa (Kalu Ganga) | 8.99 | 🟢 Normal | 0.000 |  |
| 2026-09-22 05:53:10 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 06:10:11 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-21 18:01:53 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-22 06:01:55 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-09-22 06:03:58 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.001 |  |
| 2026-09-22 06:31:59 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.002 |  |
| 2026-09-22 06:06:43 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | -0.009 |  |
| 2026-09-22 06:02:11 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-09-22 06:00:55 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-09-22 06:04:42 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-09-22 06:03:54 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-09-22 06:05:12 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.020 |  |
| 2026-09-22 06:00:28 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-09-22 06:04:14 | Glencourse (Kelani Ganga) | 12.23 | 🟢 Normal | -0.020 |  |
| 2026-09-22 06:00:42 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-09-22 06:02:17 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -0.027 |  |
| 2026-09-22 06:02:01 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.031 |  |
| 2026-09-22 06:02:37 | Pitabeddara (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.035 |  |
| 2026-09-22 06:02:47 | Thawalama (Gin Ganga) | 2.63 | 🟢 Normal | -0.039 |  |
| 2026-09-22 06:04:02 | Giriulla (Maha Oya) | 2.10 | 🟢 Normal | -0.049 |  |
| 2026-09-22 06:07:45 | Rathnapura (Kalu Ganga) | 4.74 | 🟢 Normal | -0.066 |  |
| 2026-09-22 06:02:32 | Hanwella (Kelani Ganga) | 4.75 | 🟢 Normal | -0.080 |  |
| 2026-09-22 06:04:08 | Peradeniya (Mahaweli Ganga) | 3.27 | 🟢 Normal | -0.560 |  |

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)