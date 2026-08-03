# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_14:16:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **223,848 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 14:16:25 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-08-03 14:13:00 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-08-03 14:12:57 | Nawalapitiya (Mahaweli Ganga) | 8.07 | 🔴 Major Flood | 0.179 | 🔺 Rising |
| 2026-08-03 14:12:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.23 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-03 14:10:19 | Kithulgala (Kelani Ganga) | 6.71 | 🔴 Major Flood | 0.000 |  |
| 2026-08-03 14:09:21 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.028 |  |
| 2026-08-03 14:07:54 | Kithulgala (Kelani Ganga) | 6.71 | 🔴 Major Flood | 0.000 |  |
| 2026-08-03 14:06:52 | Glencourse (Kelani Ganga) | 14.00 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-08-03 14:06:41 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-03 14:06:40 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-08-03 14:06:12 | Giriulla (Maha Oya) | 2.25 | 🟢 Normal | -0.173 |  |
| 2026-08-03 14:05:58 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:05:50 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:05:27 | Holombuwa (Kelani Ganga) | 3.02 | 🟡 Alert | 1.527 | 🔺 Rising |
| 2026-08-03 14:05:03 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | -0.109 |  |
| 2026-08-03 14:05:02 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:04:44 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-03 14:04:35 | Norwood (Kelani Ganga) | 3.38 | 🟠 Minor Flood | -0.045 |  |
| 2026-08-03 14:04:14 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:03:39 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:03:38 | Deraniyagala (Kelani Ganga) | 6.24 | 🟠 Minor Flood | 0.999 | 🔺 Rising |
| 2026-08-03 14:03:32 | Hanwella (Kelani Ganga) | 5.18 | 🟢 Normal | -0.020 |  |
| 2026-08-03 14:03:31 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-03 14:03:27 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-08-03 14:03:24 | Peradeniya (Mahaweli Ganga) | 8.30 | 🟠 Minor Flood | 1.071 | 🔺 Rising |
| 2026-08-03 14:03:20 | Ellagawa (Kalu Ganga) | 7.65 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-03 14:03:17 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 14:03:15 | Rathnapura (Kalu Ganga) | 7.18 | 🟡 Alert | 0.437 | 🔺 Rising |
| 2026-08-03 14:02:31 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | 0.401 | 🔺 Rising |
| 2026-08-03 14:02:16 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:02:11 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:02:03 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:01:59 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.073 |  |
| 2026-08-03 14:01:57 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:01:34 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:01:15 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:00:47 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:00:09 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 14:12:57 | Nawalapitiya (Mahaweli Ganga) | 8.07 | 🔴 Major Flood | 0.179 | 🔺 Rising |
| 2026-08-03 14:10:19 | Kithulgala (Kelani Ganga) | 6.71 | 🔴 Major Flood | 0.000 |  |
| 2026-08-03 14:03:24 | Peradeniya (Mahaweli Ganga) | 8.30 | 🟠 Minor Flood | 1.071 | 🔺 Rising |
| 2026-08-03 14:03:38 | Deraniyagala (Kelani Ganga) | 6.24 | 🟠 Minor Flood | 0.999 | 🔺 Rising |
| 2026-08-03 14:04:35 | Norwood (Kelani Ganga) | 3.38 | 🟠 Minor Flood | -0.045 |  |
| 2026-08-03 14:05:27 | Holombuwa (Kelani Ganga) | 3.02 | 🟡 Alert | 1.527 | 🔺 Rising |
| 2026-08-03 14:03:15 | Rathnapura (Kalu Ganga) | 7.18 | 🟡 Alert | 0.437 | 🔺 Rising |
| 2026-08-03 14:02:31 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | 0.401 | 🔺 Rising |
| 2026-08-03 14:06:52 | Glencourse (Kelani Ganga) | 14.00 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-08-03 14:16:25 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-08-03 14:04:44 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-03 14:03:20 | Ellagawa (Kalu Ganga) | 7.65 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-03 14:03:31 | Putupaula (Kalu Ganga) | 1.30 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-03 14:06:41 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-03 14:12:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.23 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-03 14:00:09 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-03 14:03:17 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 14:02:03 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:01:34 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:01:15 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:01:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:01:57 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:05:02 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:05:50 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:04:14 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:05:58 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:03:39 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:02:16 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:00:43 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 14:02:11 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-03 12:01:37 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.005 |  |
| 2026-08-03 14:13:00 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.010 |  |
| 2026-08-03 14:03:27 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-08-03 14:06:40 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | -0.010 |  |
| 2026-08-03 14:03:32 | Hanwella (Kelani Ganga) | 5.18 | 🟢 Normal | -0.020 |  |
| 2026-08-03 14:09:21 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | -0.028 |  |
| 2026-08-03 14:01:59 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.073 |  |
| 2026-08-03 14:05:03 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | -0.109 |  |
| 2026-08-03 14:06:12 | Giriulla (Maha Oya) | 2.25 | 🟢 Normal | -0.173 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)