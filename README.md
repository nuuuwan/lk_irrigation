# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_03:13:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,218 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 03:13:17 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.068 |  |
| 2026-01-12 03:11:49 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:11:49 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:10:07 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.045 |  |
| 2026-01-12 03:09:19 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 03:09:14 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-01-12 03:08:28 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-12 03:08:23 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-12 03:06:55 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-01-12 03:06:54 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:05:36 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:05:36 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-12 03:05:22 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:04:28 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-12 03:04:23 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 03:03:39 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:03:38 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:03:30 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 03:03:25 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:03:11 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.510 | 🔺 Rising |
| 2026-01-12 03:03:04 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.014 |  |
| 2026-01-12 03:02:56 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | -0.061 |  |
| 2026-01-12 03:02:28 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | -0.015 |  |
| 2026-01-12 03:02:26 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 03:02:15 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-12 03:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:01:51 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 03:01:49 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 03:01:40 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:01:01 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:45:32 | Magura (Kalu Ganga) | 1.19 | 🟢 Normal | 0.510 | 🔺 Rising |
| 2026-01-12 02:44:57 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:43:10 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | -0.061 |  |
| 2026-01-12 02:42:09 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.023 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 03:03:11 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.510 | 🔺 Rising |
| 2026-01-12 01:03:26 | Dunamale (Aththanagalu Oya) | 1.05 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-01-12 03:09:14 | Holombuwa (Kelani Ganga) | 0.81 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-01-12 03:06:55 | Glencourse (Kelani Ganga) | 10.32 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-01-12 00:11:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-12 03:04:28 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-12 03:08:28 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-01-11 18:00:33 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-12 03:08:23 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-01-12 03:01:49 | Manampitiya (Mahaweli Ganga) | 1.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 03:05:36 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-12 03:01:51 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 03:02:26 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 03:04:23 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 03:03:30 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 03:09:19 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 02:08:16 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 03:11:49 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:01:30 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:01:01 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:03:25 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:19 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:03:38 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:01:40 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:06:54 | Panadugama (Nilwala Ganga) | 2.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:11:49 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-12 02:10:41 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:05:22 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-12 01:02:49 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:03:39 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:05:36 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-12 03:02:15 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-01-12 01:00:07 | Padiyathalawa (Maduru Oya) | 1.07 | 🟢 Normal | -0.011 |  |
| 2026-01-12 03:03:04 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.014 |  |
| 2026-01-12 03:02:28 | Siyambalanduwa (Heda Oya) | 1.17 | 🟢 Normal | -0.015 |  |
| 2026-01-12 03:10:07 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.045 |  |
| 2026-01-12 03:02:56 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | -0.061 |  |
| 2026-01-12 03:13:17 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | -0.068 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)