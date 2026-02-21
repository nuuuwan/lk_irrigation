# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_14:22:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **79,130 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 14:22:58 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:16:09 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-02-21 14:08:52 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.026 |  |
| 2026-02-21 14:06:21 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-02-21 14:06:09 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:06:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | -0.069 |  |
| 2026-02-21 14:05:45 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 14:04:56 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:04:55 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-21 14:04:45 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.009 |  |
| 2026-02-21 14:04:38 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.038 |  |
| 2026-02-21 14:04:21 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:04:17 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-02-21 14:04:09 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:03:56 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:03:54 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 14:03:49 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.061 |  |
| 2026-02-21 14:03:30 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:03:19 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-02-21 14:03:19 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.061 |  |
| 2026-02-21 14:03:00 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-02-21 14:02:59 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-02-21 14:02:42 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-02-21 14:02:40 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-21 14:02:29 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-02-21 14:02:25 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.011 |  |
| 2026-02-21 14:02:24 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:02:11 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:01:55 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 14:01:51 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:01:37 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-02-21 14:01:34 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-21 14:01:17 | Manampitiya (Mahaweli Ganga) | 2.47 | 🟢 Normal | -0.061 |  |
| 2026-02-21 14:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:01:05 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:00:50 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:00:47 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | -0.060 |  |
| 2026-02-21 14:00:34 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 14:04:17 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-02-21 14:06:21 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-02-21 14:02:40 | Deraniyagala (Kelani Ganga) | 0.22 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-02-21 14:05:45 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-21 14:03:54 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 14:01:55 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 14:00:50 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:01:51 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:01:05 | Horowpothana (Yan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:04:09 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:22:58 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:06:09 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-02-21 13:08:29 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:02:24 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:03:30 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:04:21 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:04:56 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:02:11 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:03:56 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 14:16:09 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | -0.009 |  |
| 2026-02-21 14:04:45 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | -0.009 |  |
| 2026-02-21 14:02:42 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-02-21 14:01:37 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-02-21 14:02:59 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-02-21 14:02:29 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-02-21 14:04:55 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-02-21 14:00:34 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-02-21 14:01:34 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-02-21 14:02:25 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | -0.011 |  |
| 2026-02-21 14:03:00 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-02-21 14:03:19 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-02-21 14:08:52 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.026 |  |
| 2026-02-21 14:04:38 | Thanamalwila (Kirindi Oya) | 0.93 | 🟢 Normal | -0.038 |  |
| 2026-02-21 14:00:47 | Weraganthota (Mahaweli Ganga) | -1.80 | 🟢 Normal | -0.060 |  |
| 2026-02-21 14:01:17 | Manampitiya (Mahaweli Ganga) | 2.47 | 🟢 Normal | -0.061 |  |
| 2026-02-21 14:03:49 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.061 |  |
| 2026-02-21 14:03:19 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | -0.061 |  |
| 2026-02-21 14:06:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)