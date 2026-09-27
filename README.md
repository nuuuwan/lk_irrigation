# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--27_12:09:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **272,364 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 12:09:13 | Magura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.028 |  |
| 2026-09-27 12:07:29 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:06:37 | Baddegama (Gin Ganga) | 4.66 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-27 12:06:26 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.022 |  |
| 2026-09-27 12:06:22 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:06:18 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-09-27 12:06:09 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.019 |  |
| 2026-09-27 12:05:30 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.047 |  |
| 2026-09-27 12:05:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.46 | 🟡 Alert | -0.041 |  |
| 2026-09-27 12:04:59 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-09-27 12:04:47 | Panadugama (Nilwala Ganga) | 5.31 | 🟡 Alert | -0.030 |  |
| 2026-09-27 12:04:47 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.102 |  |
| 2026-09-27 12:04:39 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:04:30 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.093 |  |
| 2026-09-27 12:04:18 | Glencourse (Kelani Ganga) | 11.95 | 🟢 Normal | -0.055 |  |
| 2026-09-27 12:03:55 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 12:03:29 | Hanwella (Kelani Ganga) | 4.31 | 🟢 Normal | -0.050 |  |
| 2026-09-27 12:03:22 | Putupaula (Kalu Ganga) | 2.76 | 🟢 Normal | -0.020 |  |
| 2026-09-27 12:03:22 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:03:21 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-09-27 12:03:18 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-27 12:02:58 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-09-27 12:02:51 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-09-27 12:02:27 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:02:22 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:02:21 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:02:17 | Rathnapura (Kalu Ganga) | 3.37 | 🟢 Normal | -0.121 |  |
| 2026-09-27 12:02:13 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:02:11 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.045 |  |
| 2026-09-27 12:01:43 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.040 |  |
| 2026-09-27 12:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:01:36 | Ellagawa (Kalu Ganga) | 8.41 | 🟢 Normal | -0.021 |  |
| 2026-09-27 12:01:32 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-09-27 12:01:07 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:01:04 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:01:01 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:00:50 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.043 |  |
| 2026-09-27 12:00:49 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:00:13 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-27 12:03:55 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-27 12:06:37 | Baddegama (Gin Ganga) | 4.66 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-27 12:04:47 | Panadugama (Nilwala Ganga) | 5.31 | 🟡 Alert | -0.030 |  |
| 2026-09-27 12:05:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.46 | 🟡 Alert | -0.041 |  |
| 2026-09-27 12:06:18 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-09-27 12:03:18 | Deraniyagala (Kelani Ganga) | 1.35 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-09-27 12:00:13 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:01:01 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:07:29 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:02:22 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:00:49 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:06:22 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:01:07 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:03:22 | Dunamale (Aththanagalu Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:04:39 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:02:13 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:01:32 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:01:04 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:02:27 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-27 12:02:51 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-09-27 12:02:58 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-09-27 12:03:21 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-09-27 12:06:09 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.019 |  |
| 2026-09-27 12:03:22 | Putupaula (Kalu Ganga) | 2.76 | 🟢 Normal | -0.020 |  |
| 2026-09-27 12:04:59 | Urawa (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-09-27 12:01:28 | Nawalapitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | -0.020 |  |
| 2026-09-27 12:01:36 | Ellagawa (Kalu Ganga) | 8.41 | 🟢 Normal | -0.021 |  |
| 2026-09-27 12:06:26 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.022 |  |
| 2026-09-27 12:09:13 | Magura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.028 |  |
| 2026-09-27 12:01:43 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.040 |  |
| 2026-09-27 12:00:50 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.043 |  |
| 2026-09-27 12:02:11 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.045 |  |
| 2026-09-27 12:05:30 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.047 |  |
| 2026-09-27 12:03:29 | Hanwella (Kelani Ganga) | 4.31 | 🟢 Normal | -0.050 |  |
| 2026-09-27 12:04:18 | Glencourse (Kelani Ganga) | 11.95 | 🟢 Normal | -0.055 |  |
| 2026-09-27 12:04:30 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.093 |  |
| 2026-09-27 12:04:47 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.102 |  |
| 2026-09-27 12:02:17 | Rathnapura (Kalu Ganga) | 3.37 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)