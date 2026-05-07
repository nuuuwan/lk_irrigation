# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--07_16:32:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,433 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 16:32:45 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:15:37 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-07 16:13:33 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:12:02 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-05-07 16:11:13 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:10:50 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-05-07 16:08:55 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-05-07 16:08:00 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | -0.115 |  |
| 2026-05-07 16:07:17 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:06:33 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-07 16:06:18 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-07 16:05:58 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:05:42 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.059 |  |
| 2026-05-07 16:05:29 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:05:27 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 16:05:15 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:05:05 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | -0.080 |  |
| 2026-05-07 16:04:56 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-05-07 16:04:51 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.052 |  |
| 2026-05-07 16:04:28 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:04:20 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:04:03 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.020 |  |
| 2026-05-07 16:03:49 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:03:41 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-07 16:03:37 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:03:33 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-05-07 16:03:06 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | -0.100 |  |
| 2026-05-07 16:03:05 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-05-07 16:03:01 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-05-07 16:02:51 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:02:36 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:02:32 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.010 |  |
| 2026-05-07 16:02:27 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.056 |  |
| 2026-05-07 16:02:23 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-07 16:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-05-07 16:02:09 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 16:01:59 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-05-07 16:01:44 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-07 16:04:56 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.165 | 🔺 Rising |
| 2026-05-07 16:03:33 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-05-07 16:12:02 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-05-07 16:03:05 | Urawa (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-05-07 16:15:37 | Panadugama (Nilwala Ganga) | 2.41 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-05-07 16:01:59 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-05-07 16:02:23 | Deraniyagala (Kelani Ganga) | 0.47 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-07 16:06:33 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-05-07 16:06:18 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-07 16:00:25 | Manampitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-07 16:02:09 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-07 16:03:41 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-07 16:05:27 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-07 16:04:28 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:02:36 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:03:49 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:02:51 | Moragaswewa (Deduru Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:32:45 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:01:03 | Galgamuwa (Mee Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:01:07 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:01:44 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:05:58 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:05:29 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:07:17 | Rathnapura (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:13:33 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-05-07 16:08:55 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-05-07 16:02:32 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | -0.010 |  |
| 2026-05-07 16:10:50 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-05-07 16:00:48 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-05-07 16:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-05-07 16:00:58 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-07 16:03:01 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-05-07 16:04:03 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.020 |  |
| 2026-05-07 16:04:51 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.052 |  |
| 2026-05-07 16:02:27 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.056 |  |
| 2026-05-07 16:05:42 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.059 |  |
| 2026-05-07 16:05:05 | Glencourse (Kelani Ganga) | 9.72 | 🟢 Normal | -0.080 |  |
| 2026-05-07 16:03:06 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | -0.100 |  |
| 2026-05-07 16:08:00 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | -0.115 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)