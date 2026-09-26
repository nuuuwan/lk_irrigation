# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_12:11:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,468 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 12:11:44 | Rathnapura (Kalu Ganga) | 4.97 | 🟢 Normal | -0.035 |  |
| 2026-09-26 12:09:09 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | 3.429 | 🔺 Rising |
| 2026-09-26 12:08:06 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | 3.429 | 🔺 Rising |
| 2026-09-26 12:08:02 | Baddegama (Gin Ganga) | 4.82 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 12:07:19 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:07:02 | Magura (Kalu Ganga) | 3.94 | 🟢 Normal | -0.028 |  |
| 2026-09-26 12:06:53 | Deraniyagala (Kelani Ganga) | 2.01 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-26 12:06:02 | Glencourse (Kelani Ganga) | 13.12 | 🟢 Normal | -0.021 |  |
| 2026-09-26 12:05:43 | Urawa (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-26 12:05:35 | Panadugama (Nilwala Ganga) | 5.95 | 🟡 Alert | 0.414 | 🔺 Rising |
| 2026-09-26 12:05:20 | Ellagawa (Kalu Ganga) | 8.97 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:05:14 | Kithulgala (Kelani Ganga) | 2.68 | 🟢 Normal | -0.078 |  |
| 2026-09-26 12:04:53 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:04:46 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:04:35 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:04:33 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:04:32 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.348 |  |
| 2026-09-26 12:04:28 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-26 12:04:11 | Thalgahagoda (Nilwala Ganga) | 1.98 | 🟠 Minor Flood | -0.021 |  |
| 2026-09-26 12:04:09 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-26 12:04:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.01 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-26 12:03:48 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-09-26 12:03:31 | Pitabeddara (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.895 | 🔺 Rising |
| 2026-09-26 12:03:16 | Giriulla (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:03:14 | Hanwella (Kelani Ganga) | 5.47 | 🟢 Normal | -0.071 |  |
| 2026-09-26 12:02:56 | Thawalama (Gin Ganga) | 2.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 12:02:39 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:02:34 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:02:29 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | 0.433 | 🔺 Rising |
| 2026-09-26 12:02:29 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:02:29 | Putupaula (Kalu Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:02:26 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-09-26 12:02:24 | Dunamale (Aththanagalu Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:02:14 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -0.010 |  |
| 2026-09-26 12:01:55 | Nawalapitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-09-26 12:01:24 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-26 12:01:23 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:00:48 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:00:20 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-09-26 12:00:16 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 11:59:29 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 12:08:02 | Baddegama (Gin Ganga) | 4.82 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 12:04:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.01 | 🟠 Minor Flood | -0.010 |  |
| 2026-09-26 12:04:11 | Thalgahagoda (Nilwala Ganga) | 1.98 | 🟠 Minor Flood | -0.021 |  |
| 2026-09-26 12:05:35 | Panadugama (Nilwala Ganga) | 5.95 | 🟡 Alert | 0.414 | 🔺 Rising |
| 2026-09-26 12:09:09 | Holombuwa (Kelani Ganga) | 1.20 | 🟢 Normal | 3.429 | 🔺 Rising |
| 2026-09-26 12:03:31 | Pitabeddara (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.895 | 🔺 Rising |
| 2026-09-26 12:02:29 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | 0.433 | 🔺 Rising |
| 2026-09-26 12:01:55 | Nawalapitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-09-26 12:01:24 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-09-26 12:06:53 | Deraniyagala (Kelani Ganga) | 2.01 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-26 12:05:43 | Urawa (Nilwala Ganga) | 1.11 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-26 12:02:56 | Thawalama (Gin Ganga) | 2.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 12:01:23 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:07:19 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:02:29 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:03:16 | Giriulla (Maha Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-09-26 11:59:29 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:04:35 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:04:46 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:05:20 | Ellagawa (Kalu Ganga) | 8.97 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:02:39 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:00:16 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:02:24 | Dunamale (Aththanagalu Oya) | 2.57 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:04:53 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:02:29 | Putupaula (Kalu Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:00:48 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:02:34 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 12:04:09 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-26 12:02:26 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.010 |  |
| 2026-09-26 12:02:14 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -0.010 |  |
| 2026-09-26 12:04:28 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-09-26 12:03:48 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-09-26 12:00:20 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.011 |  |
| 2026-09-26 12:06:02 | Glencourse (Kelani Ganga) | 13.12 | 🟢 Normal | -0.021 |  |
| 2026-09-26 12:07:02 | Magura (Kalu Ganga) | 3.94 | 🟢 Normal | -0.028 |  |
| 2026-09-26 12:11:44 | Rathnapura (Kalu Ganga) | 4.97 | 🟢 Normal | -0.035 |  |
| 2026-09-26 12:03:14 | Hanwella (Kelani Ganga) | 5.47 | 🟢 Normal | -0.071 |  |
| 2026-09-26 12:05:14 | Kithulgala (Kelani Ganga) | 2.68 | 🟢 Normal | -0.078 |  |
| 2026-09-26 12:04:32 | Peradeniya (Mahaweli Ganga) | 3.30 | 🟢 Normal | -0.348 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)