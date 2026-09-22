# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_19:06:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,105 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 19:06:27 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:06:10 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:06:06 | Hanwella (Kelani Ganga) | 4.56 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:05:55 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:05:17 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:04:53 | Glencourse (Kelani Ganga) | 12.41 | 🟢 Normal | -0.039 |  |
| 2026-09-22 19:04:36 | Holombuwa (Kelani Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-09-22 19:04:27 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 19:04:22 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | -0.048 |  |
| 2026-09-22 19:04:11 | Thalgahagoda (Nilwala Ganga) | 1.53 | 🟡 Alert | 0.000 |  |
| 2026-09-22 19:04:11 | Nawalapitiya (Mahaweli Ganga) | 2.49 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-09-22 19:04:04 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:04:02 | Peradeniya (Mahaweli Ganga) | 3.23 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-09-22 19:04:01 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:04:00 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:03:40 | Magura (Kalu Ganga) | 4.64 | 🟡 Alert | -0.028 |  |
| 2026-09-22 19:03:35 | Deraniyagala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-09-22 19:03:29 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:03:27 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-09-22 19:03:27 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.16 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 19:02:55 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-22 19:02:27 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:02:05 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:01:28 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:01:11 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:00:39 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:00:13 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-22 18:39:10 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:33:58 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 19:04:27 | Baddegama (Gin Ganga) | 4.10 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 19:03:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.16 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 19:04:11 | Thalgahagoda (Nilwala Ganga) | 1.53 | 🟡 Alert | 0.000 |  |
| 2026-09-22 19:03:40 | Magura (Kalu Ganga) | 4.64 | 🟡 Alert | -0.028 |  |
| 2026-09-22 19:04:02 | Peradeniya (Mahaweli Ganga) | 3.23 | 🟢 Normal | 0.230 | 🔺 Rising |
| 2026-09-22 19:04:11 | Nawalapitiya (Mahaweli Ganga) | 2.49 | 🟢 Normal | 0.208 | 🔺 Rising |
| 2026-09-22 19:00:13 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-22 18:10:20 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-22 19:02:55 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-09-22 18:02:59 | Giriulla (Maha Oya) | 1.95 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-22 18:04:23 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:00:33 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:00:39 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:03:27 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:01:28 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:01:11 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:04:56 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:04:01 | Pitabeddara (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:39:10 | Norwood (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:06:06 | Hanwella (Kelani Ganga) | 4.56 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:04:00 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:02:05 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:04:04 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:05:55 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:03:29 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:06:10 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:06:27 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:08:21 | Rathnapura (Kalu Ganga) | 4.17 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:02:27 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-22 19:05:17 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:02:46 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-22 18:01:44 | Putupaula (Kalu Ganga) | 2.97 | 🟢 Normal | -0.010 |  |
| 2026-09-22 18:10:57 | Panadugama (Nilwala Ganga) | 4.81 | 🟢 Normal | -0.011 |  |
| 2026-09-22 18:08:36 | Thawalama (Gin Ganga) | 2.78 | 🟢 Normal | -0.019 |  |
| 2026-09-22 19:03:35 | Deraniyagala (Kelani Ganga) | 1.86 | 🟢 Normal | -0.020 |  |
| 2026-09-22 19:03:27 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-09-22 19:04:36 | Holombuwa (Kelani Ganga) | 1.46 | 🟢 Normal | -0.020 |  |
| 2026-09-22 19:04:53 | Glencourse (Kelani Ganga) | 12.41 | 🟢 Normal | -0.039 |  |
| 2026-09-22 19:04:22 | Ellagawa (Kalu Ganga) | 8.68 | 🟢 Normal | -0.048 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)