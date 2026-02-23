# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--24_00:05:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **81,317 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 00:05:34 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | -0.048 |  |
| 2026-02-24 00:04:52 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.110 |  |
| 2026-02-24 00:04:16 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.019 |  |
| 2026-02-24 00:04:12 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-02-24 00:04:04 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-24 00:04:03 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.011 |  |
| 2026-02-24 00:03:51 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:03:48 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-02-24 00:03:33 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:03:24 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.023 |  |
| 2026-02-24 00:03:15 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.068 |  |
| 2026-02-24 00:03:12 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:03:11 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-02-24 00:03:00 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | -0.011 |  |
| 2026-02-24 00:02:42 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:02:33 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:02:21 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-24 00:02:12 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-02-24 00:02:11 | Manampitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -180.000 |  |
| 2026-02-24 00:02:10 | Manampitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -180.000 |  |
| 2026-02-24 00:02:09 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.015 |  |
| 2026-02-24 00:02:04 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:02:01 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:01:44 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-24 00:01:40 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:01:25 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:01:21 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-24 00:01:08 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:00:52 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:00:47 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-23 23:56:02 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-23 23:37:29 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.023 |  |
| 2026-02-23 23:25:02 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-23 23:12:51 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 00:02:21 | Peradeniya (Mahaweli Ganga) | 1.96 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-24 00:01:21 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-23 23:05:20 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:00:52 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:01:33 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:01:25 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:59 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:03:33 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:03:12 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:00:47 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:02:33 | Siyambalanduwa (Heda Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:01:08 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-23 23:25:02 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-23 23:12:51 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:02:42 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-23 18:02:43 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-02-23 23:09:22 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:01:40 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:03:51 | Thanamalwila (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-24 00:04:04 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-02-24 00:03:11 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-02-24 00:03:48 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-02-24 00:04:12 | Panadugama (Nilwala Ganga) | 2.32 | 🟢 Normal | -0.010 |  |
| 2026-02-24 00:01:44 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-02-23 23:00:37 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-24 00:03:00 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | -0.011 |  |
| 2026-02-24 00:04:03 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | -0.011 |  |
| 2026-02-24 00:02:09 | Hanwella (Kelani Ganga) | 0.65 | 🟢 Normal | -0.015 |  |
| 2026-02-23 23:06:30 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.019 |  |
| 2026-02-24 00:04:16 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.019 |  |
| 2026-02-24 00:03:24 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.023 |  |
| 2026-02-23 18:03:52 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | -0.028 |  |
| 2026-02-24 00:02:12 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.030 |  |
| 2026-02-23 22:05:05 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | -0.033 |  |
| 2026-02-24 00:05:34 | Ellagawa (Kalu Ganga) | 4.65 | 🟢 Normal | -0.048 |  |
| 2026-02-24 00:03:15 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | -0.068 |  |
| 2026-02-23 22:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.089 |  |
| 2026-02-24 00:04:52 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.110 |  |
| 2026-02-24 00:02:11 | Manampitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)