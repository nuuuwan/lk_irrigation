# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--09_05:11:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **68,063 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 05:11:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.146 |  |
| 2026-02-09 05:11:13 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:10:48 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:10:26 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:08:26 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:07:22 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-02-09 05:07:16 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 05:07:10 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-02-09 05:06:58 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:06:42 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:06:06 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:06:05 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-02-09 05:05:20 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-09 05:04:39 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-09 05:04:06 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:03:56 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.205 |  |
| 2026-02-09 05:03:51 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:03:38 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:03:18 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:03:11 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:02:47 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:02:46 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-02-09 05:02:43 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-02-09 05:02:36 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:02:21 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 05:02:13 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.316 |  |
| 2026-02-09 05:01:31 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:01:30 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-02-09 05:01:14 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:01:01 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:00:19 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.316 |  |
| 2026-02-09 05:00:16 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-09 04:58:30 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.005 |  |
| 2026-02-09 04:26:41 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-09 04:21:33 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-09 04:19:54 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:16:28 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-09 04:15:55 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 05:07:22 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-02-09 05:00:16 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-02-09 05:05:20 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-09 04:04:37 | Nawalapitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-02-09 05:04:39 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-09 05:02:21 | Dunamale (Aththanagalu Oya) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 05:07:16 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-09 04:16:28 | Glencourse (Kelani Ganga) | 8.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-09 05:06:42 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:10:48 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:04:06 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:03:18 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-08 18:02:44 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:11:13 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:03:38 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:01:01 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:02:47 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:01:31 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:03:51 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:02:36 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:03:11 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:06:58 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:19:54 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:06:06 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:08:26 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-09 05:10:26 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-09 04:58:30 | Padiyathalawa (Maduru Oya) | 0.78 | 🟢 Normal | -0.005 |  |
| 2026-02-09 05:07:10 | Magura (Kalu Ganga) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-02-08 18:03:48 | Thanthirimale (Malwathu Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-02-09 05:02:46 | Manampitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.010 |  |
| 2026-02-09 05:06:05 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-02-09 05:01:30 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | -0.011 |  |
| 2026-02-09 01:13:08 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | -0.018 |  |
| 2026-02-09 05:02:43 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | -0.020 |  |
| 2026-02-09 05:11:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.146 |  |
| 2026-02-08 18:02:12 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | -0.187 |  |
| 2026-02-09 05:03:56 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.205 |  |
| 2026-02-09 05:02:13 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.316 |  |
| 2026-02-09 04:04:32 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | -1.068 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)