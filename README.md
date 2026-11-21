# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--22_04:03:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,366 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 04:03:00 | Giriulla (Maha Oya) | 2.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 04:02:55 | Badalgama (Maha Oya) | 3.28 | 🟢 Normal | -0.072 |  |
| 2026-11-22 04:02:52 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-22 04:02:38 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 04:02:37 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.033 |  |
| 2026-11-22 04:02:35 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | -0.090 |  |
| 2026-11-22 04:02:25 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-22 04:02:08 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-11-22 04:01:57 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-22 04:01:49 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-22 04:01:47 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-11-22 04:01:44 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.049 |  |
| 2026-11-22 04:01:43 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 04:01:24 | Moraketiya (Walawe Ganga) | 2.96 | 🟢 Normal | 1.675 | 🔺 Rising |
| 2026-11-22 04:01:18 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-22 04:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-22 04:01:07 | Panadugama (Nilwala Ganga) | 4.76 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-22 04:00:47 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-22 04:00:39 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-11-22 03:50:46 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.013 |  |
| 2026-11-22 03:39:24 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-22 03:37:26 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-22 03:29:45 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-22 04:01:24 | Moraketiya (Walawe Ganga) | 2.96 | 🟢 Normal | 1.675 | 🔺 Rising |
| 2026-11-22 03:06:35 | Rathnapura (Kalu Ganga) | 2.59 | 🟢 Normal | 1.130 | 🔺 Rising |
| 2026-11-22 04:01:18 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-11-22 03:04:16 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-22 04:03:00 | Giriulla (Maha Oya) | 2.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-22 04:01:49 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-22 03:08:17 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-22 04:01:07 | Panadugama (Nilwala Ganga) | 4.76 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-22 04:02:38 | Deraniyagala (Kelani Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-22 04:02:25 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:00:46 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-22 04:01:57 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-11-22 04:00:47 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-22 04:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-22 04:01:43 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-22 04:02:08 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:00:19 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-11-22 01:01:46 | Pitabeddara (Nilwala Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-11-22 03:03:13 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-11-22 03:13:23 | Ellagawa (Kalu Ganga) | 5.38 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-22 04:02:52 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-22 03:37:26 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-22 03:02:10 | Manampitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:02:22 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-22 03:39:24 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-22 03:29:45 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-22 03:03:30 | Thanamalwila (Kirindi Oya) | 1.67 | 🟢 Normal | -0.005 |  |
| 2026-11-22 04:01:47 | Dunamale (Aththanagalu Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-11-22 03:50:46 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.013 |  |
| 2026-11-22 04:00:39 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-11-22 03:03:04 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | -0.032 |  |
| 2026-11-22 04:02:37 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.033 |  |
| 2026-11-22 03:03:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.26 | 🟢 Normal | -0.041 |  |
| 2026-11-22 04:01:44 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.049 |  |
| 2026-11-22 03:09:34 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.064 |  |
| 2026-11-22 04:02:55 | Badalgama (Maha Oya) | 3.28 | 🟢 Normal | -0.072 |  |
| 2026-11-22 04:02:35 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | -0.090 |  |
| 2026-11-22 03:00:59 | Peradeniya (Mahaweli Ganga) | 2.80 | 🟢 Normal | -0.152 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)