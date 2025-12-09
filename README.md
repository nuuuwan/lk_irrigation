# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--09_17:22:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **13,475 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-09 17:22:45 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:12:09 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.035 |  |
| 2025-12-09 17:10:12 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.009 |  |
| 2025-12-09 17:08:53 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:07:22 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:06:49 | Hanwella (Kelani Ganga) | 2.05 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-09 17:06:45 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:06:34 | Siyambalanduwa (Heda Oya) | 1.49 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2025-12-09 17:06:23 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-09 17:06:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | -0.038 |  |
| 2025-12-09 17:05:56 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2025-12-09 17:05:48 | Urawa (Nilwala Ganga) | 2.34 | 🟢 Normal | 1.124 | 🔺 Rising |
| 2025-12-09 17:05:25 | Horowpothana (Yan Oya) | 2.95 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2025-12-09 17:05:16 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | -0.010 |  |
| 2025-12-09 17:05:11 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:04:37 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:04:32 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | -0.069 |  |
| 2025-12-09 17:04:16 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:03:44 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-09 17:03:40 | Kithulgala (Kelani Ganga) | 0.86 | 🟢 Normal | -58.426 |  |
| 2025-12-09 17:03:27 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:03:11 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.030 |  |
| 2025-12-09 17:03:10 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-09 17:02:50 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:02:39 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -58.426 |  |
| 2025-12-09 17:02:16 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 17:02:10 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | -0.040 |  |
| 2025-12-09 17:02:04 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.049 |  |
| 2025-12-09 17:02:02 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-09 17:02:00 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:02:00 | Yaka Wewa (Ma Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:01:59 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:01:24 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2025-12-09 17:01:20 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 17:01:16 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:01:11 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-09 17:01:00 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.228 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-09 17:05:48 | Urawa (Nilwala Ganga) | 2.34 | 🟢 Normal | 1.124 | 🔺 Rising |
| 2025-12-09 17:01:00 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2025-12-09 17:05:25 | Horowpothana (Yan Oya) | 2.95 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2025-12-09 17:06:34 | Siyambalanduwa (Heda Oya) | 1.49 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2025-12-09 17:06:49 | Hanwella (Kelani Ganga) | 2.05 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2025-12-09 17:03:44 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2025-12-09 17:06:23 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2025-12-09 17:01:11 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2025-12-09 17:02:02 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-09 17:02:16 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 17:01:20 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-09 17:02:00 | Yaka Wewa (Ma Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:22:45 | Galgamuwa (Mee Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:05:11 | Pitabeddara (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:07:22 | Padiyathalawa (Maduru Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:01:16 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:04:37 | Dunamale (Aththanagalu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:03:27 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:08:53 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:04:16 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:02:00 | Manampitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-09 16:08:08 | Thanthirimale (Malwathu Oya) | 3.21 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:06:45 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:01:59 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:02:50 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-09 17:10:12 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.009 |  |
| 2025-12-09 17:05:56 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.009 |  |
| 2025-12-09 17:01:24 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2025-12-09 17:03:10 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-09 17:05:16 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | -0.010 |  |
| 2025-12-09 17:03:11 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.030 |  |
| 2025-12-09 17:12:09 | Glencourse (Kelani Ganga) | 9.85 | 🟢 Normal | -0.035 |  |
| 2025-12-09 17:06:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.61 | 🟢 Normal | -0.038 |  |
| 2025-12-09 17:02:10 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | -0.040 |  |
| 2025-12-09 16:02:45 | Thaldena (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.042 |  |
| 2025-12-09 17:02:04 | Nakkala (Kumbukkan Oya) | 1.32 | 🟢 Normal | -0.049 |  |
| 2025-12-09 17:04:32 | Ellagawa (Kalu Ganga) | 5.61 | 🟢 Normal | -0.069 |  |
| 2025-12-09 17:03:40 | Kithulgala (Kelani Ganga) | 0.86 | 🟢 Normal | -58.426 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)