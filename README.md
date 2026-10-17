# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--17_20:27:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **290,647 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Padiyathalawa — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Rathnapura — Alert; 🟡 Holombuwa — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **2** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 20:27:39 | Pitabeddara (Nilwala Ganga) | 2.80 | 🟢 Normal | 2160.000 | 🔺 Rising |
| 2026-10-17 20:27:38 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | 2160.000 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-17 20:09:33 | Padiyathalawa (Maduru Oya) | 4.50 | 🟠 Minor Flood | 2.497 | 🔺 Rising |
| 2026-10-17 20:07:54 | Panadugama (Nilwala Ganga) | 6.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 20:01:02 | Thalgahagoda (Nilwala Ganga) | 2.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-17 20:05:01 | Rathnapura (Kalu Ganga) | 6.15 | 🟡 Alert | 0.675 | 🔺 Rising |
| 2026-10-17 20:05:42 | Holombuwa (Kelani Ganga) | 3.30 | 🟡 Alert | 0.582 | 🔺 Rising |
| 2026-10-17 20:11:36 | Norwood (Kelani Ganga) | 1.69 | 🟡 Alert | 0.253 | 🔺 Rising |
| 2026-10-17 20:02:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.52 | 🟡 Alert | -0.023 |  |
| 2026-10-17 20:27:39 | Pitabeddara (Nilwala Ganga) | 2.80 | 🟢 Normal | 2160.000 | 🔺 Rising |
| 2026-10-17 20:04:02 | Glencourse (Kelani Ganga) | 11.21 | 🟢 Normal | 0.563 | 🔺 Rising |
| 2026-10-17 20:03:03 | Peradeniya (Mahaweli Ganga) | 3.87 | 🟢 Normal | 0.291 | 🔺 Rising |
| 2026-10-17 20:07:40 | Thawalama (Gin Ganga) | 3.00 | 🟢 Normal | 0.272 | 🔺 Rising |
| 2026-10-17 20:07:06 | Manampitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-10-17 20:04:46 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-10-17 20:04:13 | Horowpothana (Yan Oya) | 2.68 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-10-17 19:17:43 | Urawa (Nilwala Ganga) | 1.60 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-17 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | 0.000 |  |
| 2026-10-17 20:03:54 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-17 20:04:47 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-17 20:00:45 | Moraketiya (Walawe Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-10-17 20:02:04 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-17 20:03:05 | Dunamale (Aththanagalu Oya) | 2.82 | 🟢 Normal | 0.000 |  |
| 2026-10-17 20:09:10 | Putupaula (Kalu Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2026-10-17 20:01:51 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-17 20:04:41 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | -0.010 |  |
| 2026-10-17 20:01:11 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-17 20:05:45 | Baddegama (Gin Ganga) | 3.23 | 🟢 Normal | -0.019 |  |
| 2026-10-17 20:06:22 | Badalgama (Maha Oya) | 3.00 | 🟢 Normal | -0.019 |  |
| 2026-10-17 20:00:10 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-10-17 20:02:58 | Moragaswewa (Deduru Oya) | 1.25 | 🟢 Normal | -0.031 |  |
| 2026-10-17 15:04:20 | Ellagawa (Kalu Ganga) | 7.50 | 🟢 Normal | -0.039 |  |
| 2026-10-17 18:01:56 | Thanthirimale (Malwathu Oya) | 2.41 | 🟢 Normal | -0.040 |  |
| 2026-10-17 15:01:44 | Galgamuwa (Mee Oya) | 1.60 | 🟢 Normal | -0.045 |  |
| 2026-10-17 20:07:03 | Hanwella (Kelani Ganga) | 3.04 | 🟢 Normal | -0.079 |  |
| 2026-10-17 20:03:28 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.096 |  |
| 2026-10-17 20:03:32 | Nawalapitiya (Mahaweli Ganga) | 2.61 | 🟢 Normal | -0.249 |  |
| 2026-10-17 20:04:20 | Deraniyagala (Kelani Ganga) | 2.16 | 🟢 Normal | -0.456 |  |
| 2026-10-17 20:03:27 | Giriulla (Maha Oya) | 1.66 | 🟢 Normal | -3.830 |  |
| 2026-10-17 19:12:11 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -8.308 |  |
| 2026-10-17 13:09:01 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | -50.400 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)