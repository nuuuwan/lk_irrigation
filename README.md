# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_10:08:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **267,754 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Magura — Alert; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 10:08:02 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.047 |  |
| 2026-09-22 10:07:54 | Thawalama (Gin Ganga) | 2.75 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-22 10:07:24 | Rathnapura (Kalu Ganga) | 4.55 | 🟢 Normal | -0.049 |  |
| 2026-09-22 10:07:05 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-09-22 10:07:01 | Ellagawa (Kalu Ganga) | 8.97 | 🟢 Normal | -0.018 |  |
| 2026-09-22 10:06:42 | Glencourse (Kelani Ganga) | 12.28 | 🟢 Normal | -0.029 |  |
| 2026-09-22 10:06:21 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 10:06:18 | Magura (Kalu Ganga) | 4.77 | 🟡 Alert | 0.000 |  |
| 2026-09-22 10:06:03 | Holombuwa (Kelani Ganga) | 2.29 | 🟢 Normal | -0.140 |  |
| 2026-09-22 10:05:03 | Hanwella (Kelani Ganga) | 4.51 | 🟢 Normal | -0.030 |  |
| 2026-09-22 10:04:56 | Badalgama (Maha Oya) | 3.13 | 🟢 Normal | -0.062 |  |
| 2026-09-22 10:04:36 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-22 10:04:33 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:04:21 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:04:14 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 10:04:04 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:04:03 | Deraniyagala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-22 10:03:33 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.040 |  |
| 2026-09-22 10:03:15 | Nawalapitiya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -0.029 |  |
| 2026-09-22 10:02:47 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:02:37 | Nagalagam Street (Kelani Ganga) | 0.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-22 10:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.20 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 10:02:28 | Putupaula (Kalu Ganga) | 2.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 10:02:26 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.021 |  |
| 2026-09-22 10:02:06 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:02:04 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:02:00 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:02:00 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:01:51 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:01:47 | Thanthirimale (Malwathu Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-09-22 10:01:47 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-22 10:01:31 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:00:46 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:00:28 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 10:04:14 | Baddegama (Gin Ganga) | 4.18 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 10:02:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.20 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 10:06:18 | Magura (Kalu Ganga) | 4.77 | 🟡 Alert | 0.000 |  |
| 2026-09-22 09:04:11 | Thalgahagoda (Nilwala Ganga) | 1.50 | 🟡 Alert | 0.000 |  |
| 2026-09-22 09:08:55 | Panadugama (Nilwala Ganga) | 5.01 | 🟡 Alert | -0.020 |  |
| 2026-09-22 10:04:36 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-22 10:04:03 | Deraniyagala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-22 10:07:54 | Thawalama (Gin Ganga) | 2.75 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-09-22 10:02:37 | Nagalagam Street (Kelani Ganga) | 0.81 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-22 10:02:28 | Putupaula (Kalu Ganga) | 2.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 10:06:21 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 09:07:33 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:00:28 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:02:04 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:01:31 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:01:51 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:02:00 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:04:21 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:02:00 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:04:04 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:02:47 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:04:33 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-22 09:12:33 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:00:46 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:02:06 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 10:01:47 | Thanthirimale (Malwathu Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-09-22 10:01:47 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-22 10:07:01 | Ellagawa (Kalu Ganga) | 8.97 | 🟢 Normal | -0.018 |  |
| 2026-09-22 09:08:59 | Pitabeddara (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.019 |  |
| 2026-09-22 10:07:05 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-09-22 10:02:26 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | -0.021 |  |
| 2026-09-22 10:06:42 | Glencourse (Kelani Ganga) | 12.28 | 🟢 Normal | -0.029 |  |
| 2026-09-22 10:03:15 | Nawalapitiya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -0.029 |  |
| 2026-09-22 10:05:03 | Hanwella (Kelani Ganga) | 4.51 | 🟢 Normal | -0.030 |  |
| 2026-09-22 10:03:33 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.040 |  |
| 2026-09-22 10:08:02 | Peradeniya (Mahaweli Ganga) | 3.10 | 🟢 Normal | -0.047 |  |
| 2026-09-22 10:07:24 | Rathnapura (Kalu Ganga) | 4.55 | 🟢 Normal | -0.049 |  |
| 2026-09-22 10:04:56 | Badalgama (Maha Oya) | 3.13 | 🟢 Normal | -0.062 |  |
| 2026-09-22 10:06:03 | Holombuwa (Kelani Ganga) | 2.29 | 🟢 Normal | -0.140 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)