# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--09_00:37:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **67,901 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 00:37:40 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 2944.800 | 🔺 Rising |
| 2026-02-09 00:37:39 | Magura (Kalu Ganga) | 0.09 | 🟢 Normal | 2944.800 | 🔺 Rising |
| 2026-02-09 00:30:39 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:23:13 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:22:47 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:22:20 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:12:12 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 2944.800 | 🔺 Rising |
| 2026-02-09 00:12:11 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 2944.800 | 🔺 Rising |
| 2026-02-09 00:10:45 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-09 00:10:31 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:09:49 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:08:40 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:07:33 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | -0.017 |  |
| 2026-02-09 00:06:30 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.039 |  |
| 2026-02-09 00:06:09 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.113 |  |
| 2026-02-09 00:05:06 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.032 |  |
| 2026-02-09 00:04:58 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:04:00 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -36.000 |  |
| 2026-02-09 00:03:58 | Padiyathalawa (Maduru Oya) | 0.83 | 🟢 Normal | -36.000 |  |
| 2026-02-09 00:03:27 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:03:21 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.012 |  |
| 2026-02-09 00:03:20 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:03:07 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-02-09 00:03:04 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-09 00:03:01 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:02:36 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.100 |  |
| 2026-02-09 00:02:19 | Peradeniya (Mahaweli Ganga) | 2.37 | 🟢 Normal | 2.164 | 🔺 Rising |
| 2026-02-09 00:02:15 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:02:00 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:01:50 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.021 |  |
| 2026-02-09 00:01:26 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:01:23 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:01:10 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:00:59 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:00:52 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:00:49 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:00:45 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-02-08 23:59:16 | Peradeniya (Mahaweli Ganga) | 2.26 | 🟢 Normal | 2.164 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 00:37:40 | Magura (Kalu Ganga) | 0.91 | 🟢 Normal | 2944.800 | 🔺 Rising |
| 2026-02-09 00:02:19 | Peradeniya (Mahaweli Ganga) | 2.37 | 🟢 Normal | 2.164 | 🔺 Rising |
| 2026-02-09 00:03:04 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-09 00:10:45 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-02-09 00:09:49 | Kithulgala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:02:15 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:00:52 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:00:59 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:23:13 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:02:00 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:03:20 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:02:44 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:20:36 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:04:58 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:01:23 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.000 |  |
| 2026-02-08 22:03:44 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:05:30 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:00:49 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:04:37 | Dunamale (Aththanagalu Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:01:10 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-08 23:05:11 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:10:31 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:08:40 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:30:39 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:01:26 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-09 00:03:27 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:03:48 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-02-09 00:00:45 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2026-02-09 00:03:21 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | -0.012 |  |
| 2026-02-09 00:07:33 | Horowpothana (Yan Oya) | 1.81 | 🟢 Normal | -0.017 |  |
| 2026-02-09 00:01:50 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.021 |  |
| 2026-02-08 22:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.68 | 🟢 Normal | -0.022 |  |
| 2026-02-09 00:03:07 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-02-09 00:05:06 | Rathnapura (Kalu Ganga) | 0.64 | 🟢 Normal | -0.032 |  |
| 2026-02-09 00:06:30 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | -0.039 |  |
| 2026-02-09 00:02:36 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.100 |  |
| 2026-02-09 00:06:09 | Putupaula (Kalu Ganga) | 0.37 | 🟢 Normal | -0.113 |  |
| 2026-02-08 18:02:12 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.187 |  |
| 2026-02-09 00:04:00 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)