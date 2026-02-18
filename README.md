# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--19_02:18:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **76,893 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 02:18:25 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-19 02:07:08 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:06:50 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:06:29 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.030 |  |
| 2026-02-19 02:06:16 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.060 |  |
| 2026-02-19 02:05:37 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-02-19 02:05:21 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 02:05:13 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:04:24 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -36.000 |  |
| 2026-02-19 02:04:22 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -36.000 |  |
| 2026-02-19 02:04:22 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 02:04:01 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:03:47 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -18.000 |  |
| 2026-02-19 02:03:45 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -18.000 |  |
| 2026-02-19 02:03:34 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:03:05 | Manampitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.096 |  |
| 2026-02-19 02:02:58 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-19 02:02:43 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-19 02:02:38 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.063 |  |
| 2026-02-19 02:02:35 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:02:12 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-19 02:02:09 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:01:35 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:01:02 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:00:57 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:00:28 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 01:43:42 | Panadugama (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.323 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 01:21:54 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-02-19 02:02:12 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-02-19 02:02:58 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-19 02:02:43 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-19 02:04:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.56 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-19 02:00:28 | Glencourse (Kelani Ganga) | 8.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 02:05:21 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 02:18:25 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-02-19 00:02:37 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:01:02 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:00:57 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 01:04:31 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:02:35 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 18:04:47 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:10:40 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:03:53 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-19 01:07:33 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:05:13 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:03:34 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:06:50 | Baddegama (Gin Ganga) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-02-19 01:05:04 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:04:22 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:01:35 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:07:08 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-18 18:01:21 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-19 01:28:37 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:04:01 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-19 02:02:09 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-19 01:06:12 | Padiyathalawa (Maduru Oya) | 1.24 | 🟢 Normal | -0.009 |  |
| 2026-02-19 01:03:50 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-02-18 18:01:50 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.010 |  |
| 2026-02-19 02:05:37 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-02-19 02:06:29 | Deraniyagala (Kelani Ganga) | 0.16 | 🟢 Normal | -0.030 |  |
| 2026-02-19 02:06:16 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.060 |  |
| 2026-02-19 02:02:38 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.063 |  |
| 2026-02-19 02:03:05 | Manampitiya (Mahaweli Ganga) | 2.75 | 🟢 Normal | -0.096 |  |
| 2026-02-19 01:43:42 | Panadugama (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.323 |  |
| 2026-02-19 02:03:47 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | -18.000 |  |
| 2026-02-19 02:04:24 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)