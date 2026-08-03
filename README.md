# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_18:05:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,001 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 18:05:47 | Rathnapura (Kalu Ganga) | 8.24 | 🟠 Minor Flood | 0.140 | 🔺 Rising |
| 2026-08-03 18:05:45 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:05:28 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:05:05 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-08-03 18:04:45 | Nagalagam Street (Kelani Ganga) | 0.84 | 🟢 Normal | -0.016 |  |
| 2026-08-03 18:04:12 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-08-03 18:03:54 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 18:03:52 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:48 | Peradeniya (Mahaweli Ganga) | 9.72 | 🔴 Major Flood | -0.010 |  |
| 2026-08-03 18:03:46 | Ellagawa (Kalu Ganga) | 7.92 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-08-03 18:03:45 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.039 |  |
| 2026-08-03 18:03:29 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-03 18:03:28 | Thawalama (Gin Ganga) | 3.33 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-08-03 18:03:22 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:17 | Nawalapitiya (Mahaweli Ganga) | 6.10 | 🔴 Major Flood | -0.538 |  |
| 2026-08-03 18:03:11 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-08-03 18:02:57 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:02:56 | Hanwella (Kelani Ganga) | 5.80 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-08-03 18:02:45 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:02:42 | Badalgama (Maha Oya) | 3.14 | 🟢 Normal | -0.050 |  |
| 2026-08-03 18:02:41 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:02:38 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:02:34 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.094 |  |
| 2026-08-03 18:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-08-03 18:02:17 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-03 18:01:41 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:00:53 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:00:48 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:00:31 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:00:23 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.070 |  |
| 2026-08-03 18:00:16 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-03 17:36:02 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 18:03:48 | Peradeniya (Mahaweli Ganga) | 9.72 | 🔴 Major Flood | -0.010 |  |
| 2026-08-03 18:03:17 | Nawalapitiya (Mahaweli Ganga) | 6.10 | 🔴 Major Flood | -0.538 |  |
| 2026-08-03 18:05:47 | Rathnapura (Kalu Ganga) | 8.24 | 🟠 Minor Flood | 0.140 | 🔺 Rising |
| 2026-08-03 17:04:01 | Holombuwa (Kelani Ganga) | 3.68 | 🟠 Minor Flood | -0.235 |  |
| 2026-08-03 17:05:19 | Glencourse (Kelani Ganga) | 15.65 | 🟡 Alert | 0.464 | 🔺 Rising |
| 2026-08-03 17:04:53 | Norwood (Kelani Ganga) | 2.55 | 🟡 Alert | -0.231 |  |
| 2026-08-03 17:04:45 | Kithulgala (Kelani Ganga) | 3.50 | 🟡 Alert | -0.663 |  |
| 2026-08-03 17:04:09 | Magura (Kalu Ganga) | 2.52 | 🟢 Normal | 0.395 | 🔺 Rising |
| 2026-08-03 18:02:56 | Hanwella (Kelani Ganga) | 5.80 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-08-03 18:05:05 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-08-03 18:03:28 | Thawalama (Gin Ganga) | 3.33 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-08-03 18:03:46 | Ellagawa (Kalu Ganga) | 7.92 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-08-03 18:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-08-03 18:04:12 | Urawa (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-08-03 18:03:11 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-08-03 17:06:29 | Panadugama (Nilwala Ganga) | 3.62 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-03 18:03:29 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-08-03 18:02:17 | Putupaula (Kalu Ganga) | 1.50 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-03 18:03:54 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 18:02:45 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:01:41 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:02:57 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:05:45 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 17:14:41 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:52 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 17:01:04 | Baddegama (Gin Ganga) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:00:16 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:05:28 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:02:38 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:22 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:00:31 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:00:53 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:02:41 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:04:45 | Nagalagam Street (Kelani Ganga) | 0.84 | 🟢 Normal | -0.016 |  |
| 2026-08-03 18:03:45 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.039 |  |
| 2026-08-03 18:02:42 | Badalgama (Maha Oya) | 3.14 | 🟢 Normal | -0.050 |  |
| 2026-08-03 18:00:23 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.070 |  |
| 2026-08-03 18:02:34 | Giriulla (Maha Oya) | 1.61 | 🟢 Normal | -0.094 |  |
| 2026-08-03 17:02:35 | Deraniyagala (Kelani Ganga) | 4.31 | 🟢 Normal | -0.817 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)