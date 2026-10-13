# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_09:16:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,608 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 09:16:31 | Urawa (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.329 |  |
| 2026-10-13 09:11:46 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:11:27 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:08:56 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.056 |  |
| 2026-10-13 09:06:40 | Panadugama (Nilwala Ganga) | 6.16 | 🟠 Minor Flood | -0.047 |  |
| 2026-10-13 09:06:37 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | -0.041 |  |
| 2026-10-13 09:06:17 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-10-13 09:06:07 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-13 09:04:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-10-13 09:04:49 | Magura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.127 |  |
| 2026-10-13 09:04:47 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:04:35 | Pitabeddara (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.187 |  |
| 2026-10-13 09:04:18 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-10-13 09:04:15 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.040 |  |
| 2026-10-13 09:04:13 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:04:05 | Hanwella (Kelani Ganga) | 3.56 | 🟢 Normal | -0.050 |  |
| 2026-10-13 09:04:04 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:03:58 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-10-13 09:03:56 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-13 09:03:44 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:03:42 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | -0.052 |  |
| 2026-10-13 09:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.23 | 🟡 Alert | -0.011 |  |
| 2026-10-13 09:03:19 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:03:08 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-10-13 09:02:50 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.000 |  |
| 2026-10-13 09:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-13 09:02:39 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-10-13 09:02:37 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:02:37 | Rathnapura (Kalu Ganga) | 3.42 | 🟢 Normal | -0.148 |  |
| 2026-10-13 09:02:21 | Moraketiya (Walawe Ganga) | 1.26 | 🟢 Normal | -0.040 |  |
| 2026-10-13 09:02:05 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:02:04 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:01:50 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-13 09:01:50 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-10-13 09:01:11 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.021 |  |
| 2026-10-13 09:01:05 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.048 |  |
| 2026-10-13 09:00:23 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:00:17 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.050 |  |
| 2026-10-13 09:00:17 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 09:06:40 | Panadugama (Nilwala Ganga) | 6.16 | 🟠 Minor Flood | -0.047 |  |
| 2026-10-13 09:02:50 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.000 |  |
| 2026-10-13 09:03:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.23 | 🟡 Alert | -0.011 |  |
| 2026-10-13 09:03:56 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-13 09:06:07 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-13 09:01:50 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-13 09:03:58 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-10-13 09:02:04 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:03:19 | Giriulla (Maha Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:04:47 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:03:44 | Baddegama (Gin Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:04:04 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:11:46 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:04:13 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:02:05 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:02:37 | Manampitiya (Mahaweli Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:11:27 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:00:23 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-13 09:02:49 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-13 09:04:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-10-13 09:06:17 | Badalgama (Maha Oya) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-10-13 09:03:08 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-10-13 09:00:17 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-10-13 09:01:50 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-10-13 09:04:18 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-10-13 09:02:39 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-10-13 09:01:11 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.021 |  |
| 2026-10-13 09:02:21 | Moraketiya (Walawe Ganga) | 1.26 | 🟢 Normal | -0.040 |  |
| 2026-10-13 09:04:15 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.040 |  |
| 2026-10-13 09:06:37 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | -0.041 |  |
| 2026-10-13 09:01:05 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.048 |  |
| 2026-10-13 09:04:05 | Hanwella (Kelani Ganga) | 3.56 | 🟢 Normal | -0.050 |  |
| 2026-10-13 09:00:17 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.050 |  |
| 2026-10-13 09:03:42 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | -0.052 |  |
| 2026-10-13 09:08:56 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.056 |  |
| 2026-10-13 09:04:49 | Magura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.127 |  |
| 2026-10-13 09:02:37 | Rathnapura (Kalu Ganga) | 3.42 | 🟢 Normal | -0.148 |  |
| 2026-10-13 09:04:35 | Pitabeddara (Nilwala Ganga) | 2.45 | 🟢 Normal | -0.187 |  |
| 2026-10-13 09:16:31 | Urawa (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.329 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)