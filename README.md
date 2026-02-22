# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_00:17:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,413 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 00:17:22 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.019 |  |
| 2026-02-23 00:10:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.97 | 🟢 Normal | -0.005 |  |
| 2026-02-23 00:10:35 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | -0.149 |  |
| 2026-02-23 00:08:10 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:07:14 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-23 00:06:45 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-02-23 00:06:32 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-02-23 00:06:03 | Hanwella (Kelani Ganga) | 1.23 | 🟢 Normal | -0.095 |  |
| 2026-02-23 00:05:53 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:05:32 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | -0.062 |  |
| 2026-02-23 00:05:29 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.067 |  |
| 2026-02-23 00:05:07 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 00:04:38 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-23 00:04:35 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.040 |  |
| 2026-02-23 00:04:27 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | -0.060 |  |
| 2026-02-23 00:04:17 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | -0.005 |  |
| 2026-02-23 00:04:08 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:04:00 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.053 |  |
| 2026-02-23 00:03:50 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:03:43 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:03:35 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-23 00:03:16 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-23 00:03:15 | Dunamale (Aththanagalu Oya) | 0.79 | 🟢 Normal | -0.059 |  |
| 2026-02-23 00:03:06 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-02-23 00:03:00 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.160 |  |
| 2026-02-23 00:02:56 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:02:43 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | -0.039 |  |
| 2026-02-23 00:02:10 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-02-23 00:02:01 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:01:57 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:01:43 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-23 00:00:59 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:00:39 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-02-23 00:00:21 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-02-23 00:00:20 | Manampitiya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.096 |  |
| 2026-02-23 00:00:08 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 00:02:10 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-02-23 00:04:38 | Glencourse (Kelani Ganga) | 9.18 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-23 00:01:43 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-02-22 18:04:47 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-23 00:03:35 | Thanamalwila (Kirindi Oya) | 1.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-23 00:03:16 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-23 00:05:07 | Putupaula (Kalu Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 00:02:01 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:05:53 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:03:43 | Nakkala (Kumbukkan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:01:57 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:00:08 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:01:10 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:03:50 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:08:10 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:02:56 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:04:08 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:00:59 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-23 00:10:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.97 | 🟢 Normal | -0.005 |  |
| 2026-02-23 00:04:17 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | -0.005 |  |
| 2026-02-23 00:06:45 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | -0.009 |  |
| 2026-02-23 00:07:14 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-23 00:00:21 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-02-23 00:03:06 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-02-23 00:17:22 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.019 |  |
| 2026-02-23 00:00:39 | Thalgahagoda (Nilwala Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-02-23 00:06:32 | Pitabeddara (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.030 |  |
| 2026-02-23 00:02:43 | Badalgama (Maha Oya) | 2.48 | 🟢 Normal | -0.039 |  |
| 2026-02-23 00:04:35 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | -0.040 |  |
| 2026-02-23 00:04:00 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.053 |  |
| 2026-02-23 00:03:15 | Dunamale (Aththanagalu Oya) | 0.79 | 🟢 Normal | -0.059 |  |
| 2026-02-23 00:04:27 | Panadugama (Nilwala Ganga) | 3.34 | 🟢 Normal | -0.060 |  |
| 2026-02-23 00:05:32 | Baddegama (Gin Ganga) | 2.32 | 🟢 Normal | -0.062 |  |
| 2026-02-23 00:05:29 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.067 |  |
| 2026-02-23 00:06:03 | Hanwella (Kelani Ganga) | 1.23 | 🟢 Normal | -0.095 |  |
| 2026-02-23 00:00:20 | Manampitiya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.096 |  |
| 2026-02-22 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | -0.108 |  |
| 2026-02-23 00:10:35 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | -0.149 |  |
| 2026-02-23 00:03:00 | Rathnapura (Kalu Ganga) | 1.98 | 🟢 Normal | -0.160 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)