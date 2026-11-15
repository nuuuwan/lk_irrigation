# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--15_13:02:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **316,509 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **24** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 13:02:51 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 13:02:49 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 13:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | -0.010 |  |
| 2026-11-15 13:02:35 | Hanwella (Kelani Ganga) | 2.42 | 🟢 Normal | -0.030 |  |
| 2026-11-15 13:02:32 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-11-15 13:02:27 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-11-15 13:02:27 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | -0.030 |  |
| 2026-11-15 13:02:22 | Thanamalwila (Kirindi Oya) | 1.71 | 🟢 Normal | -0.020 |  |
| 2026-11-15 13:02:16 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-15 13:02:10 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-11-15 13:02:01 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-15 13:01:42 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-15 13:01:32 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-15 13:01:27 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-15 13:01:20 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-11-15 13:01:13 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-15 13:01:12 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-11-15 13:01:11 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-15 13:01:06 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.022 |  |
| 2026-11-15 13:00:43 | Panadugama (Nilwala Ganga) | 4.78 | 🟢 Normal | -0.032 |  |
| 2026-11-15 13:00:31 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-15 13:00:29 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-15 12:23:43 | Panadugama (Nilwala Ganga) | 4.80 | 🟢 Normal | -0.032 |  |
| 2026-11-15 12:21:44 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-15 12:21:44 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | -0.010 |  |
| 2026-11-15 13:02:27 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-11-15 13:02:10 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-11-15 13:01:13 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-15 12:02:17 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-11-15 13:01:11 | Manampitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-15 13:02:16 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-15 13:00:31 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-11-15 13:01:42 | Moragaswewa (Deduru Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-11-15 12:02:36 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-15 12:02:13 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-11-15 13:01:27 | Horowpothana (Yan Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-11-15 12:03:24 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-11-15 12:08:28 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-15 12:03:59 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-15 13:02:49 | Padiyathalawa (Maduru Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 13:02:01 | Moraketiya (Walawe Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-15 13:02:51 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-15 13:01:20 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-11-15 12:03:42 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-11-15 12:06:16 | Badalgama (Maha Oya) | 2.84 | 🟢 Normal | 0.000 |  |
| 2026-11-15 12:06:24 | Urawa (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-15 13:02:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | -0.010 |  |
| 2026-11-15 12:04:46 | Glencourse (Kelani Ganga) | 10.55 | 🟢 Normal | -0.010 |  |
| 2026-11-15 13:01:12 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-11-15 13:00:29 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-15 13:01:32 | Wellawaya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-11-15 12:03:38 | Peradeniya (Mahaweli Ganga) | 2.87 | 🟢 Normal | -0.010 |  |
| 2026-11-15 13:02:32 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-11-15 12:07:06 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | -0.019 |  |
| 2026-11-15 12:03:17 | Ellagawa (Kalu Ganga) | 5.63 | 🟢 Normal | -0.020 |  |
| 2026-11-15 13:02:22 | Thanamalwila (Kirindi Oya) | 1.71 | 🟢 Normal | -0.020 |  |
| 2026-11-15 13:01:06 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | -0.022 |  |
| 2026-11-15 12:11:31 | Rathnapura (Kalu Ganga) | 1.92 | 🟢 Normal | -0.028 |  |
| 2026-11-15 12:03:22 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | -0.030 |  |
| 2026-11-15 13:02:35 | Hanwella (Kelani Ganga) | 2.42 | 🟢 Normal | -0.030 |  |
| 2026-11-15 13:02:27 | Baddegama (Gin Ganga) | 2.60 | 🟢 Normal | -0.030 |  |
| 2026-11-15 13:00:43 | Panadugama (Nilwala Ganga) | 4.78 | 🟢 Normal | -0.032 |  |
| 2026-11-15 12:01:17 | Thawalama (Gin Ganga) | 2.01 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)