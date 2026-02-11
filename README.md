# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--11_17:32:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **70,325 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-11 17:32:45 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-11 17:20:54 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:10:35 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-02-11 17:10:21 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:09:35 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:08:08 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.031 |  |
| 2026-02-11 17:07:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.59 | 🟢 Normal | -0.028 |  |
| 2026-02-11 17:06:30 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-11 17:06:22 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:06:19 | Weraganthota (Mahaweli Ganga) | -2.79 | 🟢 Normal | -0.086 |  |
| 2026-02-11 17:05:40 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:05:37 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:05:17 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:04:55 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:04:35 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-02-11 17:04:11 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:04:05 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:03:55 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:03:46 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:03:46 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-11 17:03:32 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:03:30 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-11 17:03:27 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:03:09 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-11 17:03:09 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:02:46 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-02-11 17:02:44 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:02:42 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-02-11 17:02:21 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-11 17:02:02 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-11 17:01:51 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:01:50 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-11 17:01:43 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:01:43 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:01:37 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:01:32 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:01:14 | Manampitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-11 17:00:49 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-11 17:10:35 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-02-11 17:03:09 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-02-11 17:02:02 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-02-11 17:01:14 | Manampitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-02-11 17:32:45 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-02-11 17:01:50 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-11 17:02:21 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-11 17:03:30 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-11 17:05:17 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:01:32 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:03:55 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:01:37 | Yaka Wewa (Ma Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:03:27 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:09:35 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:06:22 | Magura (Kalu Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:05:40 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:03:09 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:03:46 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:01:43 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:10:21 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:04:55 | Padiyathalawa (Maduru Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:01:43 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:03:32 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:02:44 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:04:05 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:00:49 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:01:51 | Thanthirimale (Malwathu Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:20:54 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:04:11 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-11 17:05:37 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-11 16:15:43 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-02-11 17:03:46 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-02-11 17:06:30 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.010 |  |
| 2026-02-11 17:02:46 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | -0.010 |  |
| 2026-02-11 17:04:35 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-02-11 17:02:42 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-02-11 17:07:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.59 | 🟢 Normal | -0.028 |  |
| 2026-02-11 17:08:08 | Peradeniya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.031 |  |
| 2026-02-11 17:06:19 | Weraganthota (Mahaweli Ganga) | -2.79 | 🟢 Normal | -0.086 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)