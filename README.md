# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_16:03:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,300 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 16:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-29 16:03:42 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-10-29 16:03:38 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.029 |  |
| 2026-10-29 16:03:37 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.049 |  |
| 2026-10-29 16:03:36 | Putupaula (Kalu Ganga) | 3.68 | 🟡 Alert | 0.000 |  |
| 2026-10-29 16:03:12 | Baddegama (Gin Ganga) | 4.01 | 🟠 Minor Flood | -0.022 |  |
| 2026-10-29 16:03:05 | Hanwella (Kelani Ganga) | 3.43 | 🟢 Normal | -0.040 |  |
| 2026-10-29 16:02:58 | Giriulla (Maha Oya) | 1.84 | 🟢 Normal | -0.030 |  |
| 2026-10-29 16:02:46 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-29 16:02:37 | Ellagawa (Kalu Ganga) | 9.84 | 🟢 Normal | -0.030 |  |
| 2026-10-29 16:02:24 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-29 16:02:15 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | -0.010 |  |
| 2026-10-29 16:02:07 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-10-29 16:01:58 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-29 16:01:47 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-29 16:00:35 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 16:00:34 | Moragaswewa (Deduru Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-29 16:00:30 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 16:00:09 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 15:19:16 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 15:02:02 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 16:03:12 | Baddegama (Gin Ganga) | 4.01 | 🟠 Minor Flood | -0.022 |  |
| 2026-10-29 15:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.24 | 🟠 Minor Flood | -0.063 |  |
| 2026-10-29 16:03:36 | Putupaula (Kalu Ganga) | 3.68 | 🟡 Alert | 0.000 |  |
| 2026-10-29 15:03:16 | Panadugama (Nilwala Ganga) | 5.76 | 🟡 Alert | -0.024 |  |
| 2026-10-29 16:01:47 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-29 16:02:24 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-29 16:01:58 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-29 15:02:58 | Pitabeddara (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-10-29 16:00:35 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 16:00:30 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 16:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-29 15:19:16 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 15:02:25 | Galgamuwa (Mee Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-10-29 16:02:46 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-29 15:02:50 | Moraketiya (Walawe Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 16:00:09 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 15:02:18 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | 0.000 |  |
| 2026-10-29 15:01:46 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-29 15:04:40 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | 0.000 |  |
| 2026-10-29 15:08:02 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-29 15:05:34 | Urawa (Nilwala Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-29 15:05:00 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 15:07:46 | Glencourse (Kelani Ganga) | 10.92 | 🟢 Normal | -0.009 |  |
| 2026-10-29 15:06:09 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.009 |  |
| 2026-10-29 16:02:15 | Weraganthota (Mahaweli Ganga) | -2.99 | 🟢 Normal | -0.010 |  |
| 2026-10-29 15:02:17 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | -0.010 |  |
| 2026-10-29 15:04:02 | Peradeniya (Mahaweli Ganga) | 2.91 | 🟢 Normal | -0.010 |  |
| 2026-10-29 16:00:34 | Moragaswewa (Deduru Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-10-29 15:00:43 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | -0.010 |  |
| 2026-10-29 16:02:07 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-10-29 15:03:51 | Thawalama (Gin Ganga) | 2.42 | 🟢 Normal | -0.020 |  |
| 2026-10-29 16:03:42 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-10-29 16:03:38 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.029 |  |
| 2026-10-29 16:02:58 | Giriulla (Maha Oya) | 1.84 | 🟢 Normal | -0.030 |  |
| 2026-10-29 16:02:37 | Ellagawa (Kalu Ganga) | 9.84 | 🟢 Normal | -0.030 |  |
| 2026-10-29 16:03:05 | Hanwella (Kelani Ganga) | 3.43 | 🟢 Normal | -0.040 |  |
| 2026-10-29 16:03:37 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.049 |  |
| 2026-10-29 15:02:51 | Rathnapura (Kalu Ganga) | 4.56 | 🟢 Normal | -0.056 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)