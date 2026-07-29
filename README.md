# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30_03:02:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **219,912 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-30 03:02:25 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-30 03:02:20 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.419 |  |
| 2026-07-30 03:02:15 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.016 |  |
| 2026-07-30 03:02:11 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-07-30 03:01:14 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | -0.031 |  |
| 2026-07-30 03:01:13 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-30 03:01:06 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-30 02:42:10 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-30 02:30:25 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -36.000 |  |
| 2026-07-30 02:30:24 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -36.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-30 02:07:43 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-07-30 02:06:51 | Glencourse (Kelani Ganga) | 9.08 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-07-30 02:04:11 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-07-30 02:42:10 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-07-30 02:01:13 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-07-30 02:12:19 | Hanwella (Kelani Ganga) | 0.68 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-07-30 02:01:20 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-07-30 03:02:25 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-30 01:04:21 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-30 03:02:11 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-07-30 02:00:30 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-30 03:01:06 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-30 02:01:04 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-30 02:09:23 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:03:09 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:02:57 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-30 02:01:32 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 18:01:46 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 02:02:34 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 02:11:01 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-30 00:02:09 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-30 01:04:39 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-07-30 02:03:01 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-30 02:05:38 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-30 03:01:13 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-30 02:06:41 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-29 18:01:01 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | -0.005 |  |
| 2026-07-30 02:03:02 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.007 |  |
| 2026-07-30 02:07:38 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-07-30 03:02:15 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.016 |  |
| 2026-07-30 02:02:20 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.031 |  |
| 2026-07-30 03:01:14 | Ellagawa (Kalu Ganga) | 4.85 | 🟢 Normal | -0.031 |  |
| 2026-07-29 22:20:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | -0.032 |  |
| 2026-07-30 02:16:15 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.032 |  |
| 2026-07-29 18:00:16 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.034 |  |
| 2026-07-30 02:03:26 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.091 |  |
| 2026-07-30 02:02:30 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.162 |  |
| 2026-07-30 03:02:20 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | -0.419 |  |
| 2026-07-30 02:30:25 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)