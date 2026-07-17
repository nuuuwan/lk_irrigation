# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--18_03:18:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **209,201 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-18 03:18:12 | Thalgahagoda (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-07-18 03:13:56 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:13:02 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-18 03:09:15 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:09:13 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:08:26 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-18 03:08:07 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:07:38 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:07:20 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:07:17 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-18 03:06:29 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:06:10 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:05:56 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:04:47 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.076 |  |
| 2026-07-18 03:04:00 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-07-18 03:03:58 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:03:28 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.015 |  |
| 2026-07-18 03:03:24 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-07-18 03:03:15 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:02:53 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:02:52 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-07-18 03:02:21 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:02:20 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:02:15 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-07-18 03:02:12 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:02:04 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:01:51 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-07-18 03:01:37 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-07-18 03:01:30 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-18 03:01:37 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-07-18 03:02:15 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-07-18 03:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-07-18 03:03:24 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-07-18 01:01:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-07-18 03:18:12 | Thalgahagoda (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-07-18 03:08:26 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-18 02:04:46 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-18 03:13:02 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-18 03:07:17 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-18 03:01:30 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:01:51 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:02:20 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:01:59 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:03:15 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:07:20 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-07-17 18:06:03 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-07-17 23:03:17 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-07-18 01:06:30 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:13:56 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:07:38 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:09:15 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:06:10 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-07-18 00:00:24 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:27:29 | Moraketiya (Walawe Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:02:12 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:02:04 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:02:53 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:06:29 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:03:58 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-17 18:03:48 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:05:56 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-18 02:02:58 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:08:07 | Thanamalwila (Kirindi Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-07-18 03:04:00 | Deraniyagala (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-07-18 03:03:28 | Siyambalanduwa (Heda Oya) | 0.35 | 🟢 Normal | -0.015 |  |
| 2026-07-18 03:02:52 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.020 |  |
| 2026-07-17 18:00:15 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.030 |  |
| 2026-07-18 03:04:47 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.076 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)