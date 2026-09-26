# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--26_19:20:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **271,738 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 19:20:23 | Nawalapitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.030 |  |
| 2026-09-26 19:11:00 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.019 |  |
| 2026-09-26 19:10:21 | Thawalama (Gin Ganga) | 2.83 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-26 19:09:30 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 19:07:51 | Rathnapura (Kalu Ganga) | 4.82 | 🟢 Normal | -0.065 |  |
| 2026-09-26 19:06:49 | Glencourse (Kelani Ganga) | 13.01 | 🟢 Normal | -0.064 |  |
| 2026-09-26 19:06:07 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | -0.010 |  |
| 2026-09-26 19:06:03 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-09-26 19:06:02 | Baddegama (Gin Ganga) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 19:05:45 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:05:36 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:05:27 | Hanwella (Kelani Ganga) | 5.26 | 🟢 Normal | -0.029 |  |
| 2026-09-26 19:05:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.89 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-26 19:05:22 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:04:49 | Kithulgala (Kelani Ganga) | 2.53 | 🟢 Normal | -0.019 |  |
| 2026-09-26 19:04:34 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:04:34 | Deraniyagala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.050 |  |
| 2026-09-26 19:03:28 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-09-26 19:03:24 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:03:14 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:03:08 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-26 19:02:51 | Panadugama (Nilwala Ganga) | 5.84 | 🟡 Alert | -0.021 |  |
| 2026-09-26 19:02:51 | Magura (Kalu Ganga) | 3.57 | 🟢 Normal | -0.040 |  |
| 2026-09-26 19:02:23 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:02:21 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 19:02:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:02:11 | Ellagawa (Kalu Ganga) | 8.88 | 🟢 Normal | -0.020 |  |
| 2026-09-26 19:02:10 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.034 |  |
| 2026-09-26 19:02:08 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:02:05 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:01:26 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-09-26 19:01:25 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:01:13 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 19:00:14 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.051 |  |
| 2026-09-26 19:00:09 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-26 19:06:02 | Baddegama (Gin Ganga) | 4.83 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 19:09:30 | Thalgahagoda (Nilwala Ganga) | 1.95 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-26 19:05:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.89 | 🟠 Minor Flood | -0.019 |  |
| 2026-09-26 19:02:51 | Panadugama (Nilwala Ganga) | 5.84 | 🟡 Alert | -0.021 |  |
| 2026-09-26 19:10:21 | Thawalama (Gin Ganga) | 2.83 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-09-26 18:03:05 | Pitabeddara (Nilwala Ganga) | 1.59 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-26 19:01:13 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 19:02:21 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-26 19:00:09 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:03:14 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:02:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:01:25 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-26 18:05:10 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:02:05 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:05:22 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:02:08 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:05:45 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:04:34 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:05:36 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:03:24 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:02:23 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-26 19:06:07 | Peradeniya (Mahaweli Ganga) | 2.99 | 🟢 Normal | -0.010 |  |
| 2026-09-26 19:06:03 | Urawa (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-09-26 19:03:08 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-09-26 19:03:28 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-09-26 18:02:21 | Thanthirimale (Malwathu Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-09-26 19:11:00 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.019 |  |
| 2026-09-26 19:04:49 | Kithulgala (Kelani Ganga) | 2.53 | 🟢 Normal | -0.019 |  |
| 2026-09-26 19:01:26 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-09-26 19:02:11 | Ellagawa (Kalu Ganga) | 8.88 | 🟢 Normal | -0.020 |  |
| 2026-09-26 19:05:27 | Hanwella (Kelani Ganga) | 5.26 | 🟢 Normal | -0.029 |  |
| 2026-09-26 19:20:23 | Nawalapitiya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.030 |  |
| 2026-09-26 19:02:10 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.034 |  |
| 2026-09-26 19:02:51 | Magura (Kalu Ganga) | 3.57 | 🟢 Normal | -0.040 |  |
| 2026-09-26 19:04:34 | Deraniyagala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.050 |  |
| 2026-09-26 19:00:14 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.051 |  |
| 2026-09-26 19:06:49 | Glencourse (Kelani Ganga) | 13.01 | 🟢 Normal | -0.064 |  |
| 2026-09-26 19:07:51 | Rathnapura (Kalu Ganga) | 4.82 | 🟢 Normal | -0.065 |  |
| 2026-09-26 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.23 | 🟢 Normal | -0.089 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)