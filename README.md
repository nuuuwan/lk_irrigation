# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_10:13:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,388 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 10:13:25 | Thawalama (Gin Ganga) | 2.87 | 🟢 Normal | -0.061 |  |
| 2026-09-26 10:10:57 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:10:20 | Magura (Kalu Ganga) | 4.03 | 🟡 Alert | -0.121 |  |
| 2026-09-26 10:09:33 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-26 10:09:00 | Rathnapura (Kalu Ganga) | 5.03 | 🟢 Normal | -0.050 |  |
| 2026-09-26 10:08:51 | Glencourse (Kelani Ganga) | 13.18 | 🟢 Normal | -0.067 |  |
| 2026-09-26 10:08:26 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | -0.010 |  |
| 2026-09-26 10:07:17 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | -0.042 |  |
| 2026-09-26 10:06:37 | Panadugama (Nilwala Ganga) | 5.99 | 🟡 Alert | -0.030 |  |
| 2026-09-26 10:06:15 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:05:51 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-26 10:05:45 | Ellagawa (Kalu Ganga) | 8.96 | 🟢 Normal | -0.010 |  |
| 2026-09-26 10:05:18 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:05:15 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-09-26 10:05:09 | Kithulgala (Kelani Ganga) | 2.84 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-09-26 10:04:50 | Deraniyagala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 10:04:44 | Putupaula (Kalu Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:04:36 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:04:09 | Thalgahagoda (Nilwala Ganga) | 2.00 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-09-26 10:03:44 | Pitabeddara (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.040 |  |
| 2026-09-26 10:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.03 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 10:03:29 | Nawalapitiya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-09-26 10:03:19 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-09-26 10:03:18 | Baddegama (Gin Ganga) | 4.82 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 10:03:17 | Hanwella (Kelani Ganga) | 5.60 | 🟢 Normal | -0.071 |  |
| 2026-09-26 10:03:09 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:03:03 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:02:55 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:02:41 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:02:23 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-26 10:02:18 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:02:16 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.021 |  |
| 2026-09-26 10:02:11 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:01:29 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-09-26 10:01:19 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:00:45 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:00:24 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:00:14 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.060 |  |
| 2026-09-26 10:00:10 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 10:04:09 | Thalgahagoda (Nilwala Ganga) | 2.00 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-09-26 10:03:18 | Baddegama (Gin Ganga) | 4.82 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 10:03:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.03 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 10:06:37 | Panadugama (Nilwala Ganga) | 5.99 | 🟡 Alert | -0.030 |  |
| 2026-09-26 10:10:20 | Magura (Kalu Ganga) | 4.03 | 🟡 Alert | -0.121 |  |
| 2026-09-26 10:05:09 | Kithulgala (Kelani Ganga) | 2.84 | 🟢 Normal | 0.202 | 🔺 Rising |
| 2026-09-26 10:02:23 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-26 10:05:51 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-26 10:09:33 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-26 10:04:50 | Deraniyagala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 10:03:09 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:02:18 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:01:19 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:02:55 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:06:15 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:10:57 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:00:45 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:04:36 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:03:03 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:05:18 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:04:44 | Putupaula (Kalu Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:02:41 | Thanthirimale (Malwathu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:00:24 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:02:11 | Thanamalwila (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-09-26 10:05:45 | Ellagawa (Kalu Ganga) | 8.96 | 🟢 Normal | -0.010 |  |
| 2026-09-26 10:01:29 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.010 |  |
| 2026-09-26 10:08:26 | Badalgama (Maha Oya) | 2.96 | 🟢 Normal | -0.010 |  |
| 2026-09-26 10:03:29 | Nawalapitiya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-09-26 10:05:15 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-09-26 10:00:10 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-09-26 10:03:19 | Giriulla (Maha Oya) | 1.76 | 🟢 Normal | -0.020 |  |
| 2026-09-26 10:02:16 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.021 |  |
| 2026-09-26 10:03:44 | Pitabeddara (Nilwala Ganga) | 2.13 | 🟢 Normal | -0.040 |  |
| 2026-09-26 10:07:17 | Peradeniya (Mahaweli Ganga) | 3.74 | 🟢 Normal | -0.042 |  |
| 2026-09-26 10:09:00 | Rathnapura (Kalu Ganga) | 5.03 | 🟢 Normal | -0.050 |  |
| 2026-09-26 10:00:14 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | -0.060 |  |
| 2026-09-26 10:13:25 | Thawalama (Gin Ganga) | 2.87 | 🟢 Normal | -0.061 |  |
| 2026-09-26 10:08:51 | Glencourse (Kelani Ganga) | 13.18 | 🟢 Normal | -0.067 |  |
| 2026-09-26 10:03:17 | Hanwella (Kelani Ganga) | 5.60 | 🟢 Normal | -0.071 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)