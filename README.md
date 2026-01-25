# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--26_01:46:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **55,717 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-26 01:46:24 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:42:13 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:29:32 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:15:58 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:11:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 01:11:16 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:10:56 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:08:13 | Thalgahagoda (Nilwala Ganga) | 1.97 | 🟠 Minor Flood | 25.374 | 🔺 Rising |
| 2026-01-26 01:06:13 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:06:06 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:06:00 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:05:25 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:05:03 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-01-26 01:04:50 | Glencourse (Kelani Ganga) | 8.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:04:26 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | 25.374 | 🔺 Rising |
| 2026-01-26 01:04:00 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-26 01:03:43 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-01-26 01:03:15 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 01:03:11 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:02:39 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:02:37 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:02:14 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.067 |  |
| 2026-01-26 01:02:05 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:01:54 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-26 01:01:49 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:01:46 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.012 |  |
| 2026-01-26 01:01:31 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:01:29 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:01:12 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:00:47 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:00:46 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:00:37 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-26 01:08:13 | Thalgahagoda (Nilwala Ganga) | 1.97 | 🟠 Minor Flood | 25.374 | 🔺 Rising |
| 2026-01-26 00:04:32 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-01-26 00:04:17 | Putupaula (Kalu Ganga) | 0.30 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-01-25 18:00:27 | Thanthirimale (Malwathu Oya) | 1.80 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-26 01:04:00 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-26 01:03:15 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 01:11:59 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-26 01:00:47 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:10:56 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:02:05 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:29:32 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-26 00:02:24 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:05:25 | Horowpothana (Yan Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-01-25 18:04:15 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-26 00:07:15 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:02:37 | Pitabeddara (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:03:11 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:01:31 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:46:24 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-26 00:51:07 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-01-26 00:03:20 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:04:50 | Glencourse (Kelani Ganga) | 8.27 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:01:29 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:01:49 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:02:39 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:00:46 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:06:06 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:42:13 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:00:37 | Manampitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:06:13 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:15:58 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:01:12 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:11:16 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-26 01:05:03 | Padiyathalawa (Maduru Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-01-26 01:01:54 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-26 01:03:43 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-01-26 01:01:46 | Deraniyagala (Kelani Ganga) | 0.29 | 🟢 Normal | -0.012 |  |
| 2026-01-25 18:01:26 | Weraganthota (Mahaweli Ganga) | -2.35 | 🟢 Normal | -0.020 |  |
| 2026-01-26 01:02:14 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | -0.067 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)