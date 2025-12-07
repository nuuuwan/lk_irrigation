# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--07_13:02:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **11,594 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-07 13:02:23 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.060 |  |
| 2025-12-07 13:01:53 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.080 |  |
| 2025-12-07 13:01:49 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.011 |  |
| 2025-12-07 13:01:21 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:01:08 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:01:07 | Thanthirimale (Malwathu Oya) | 5.85 | 🟡 Alert | -0.082 |  |
| 2025-12-07 13:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-07 13:01:03 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.012 |  |
| 2025-12-07 13:00:54 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-07 12:24:40 | Thanthirimale (Malwathu Oya) | 5.90 | 🟡 Alert | -0.082 |  |
| 2025-12-07 12:13:12 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-07 12:12:16 | Glencourse (Kelani Ganga) | 10.17 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-07 12:11:25 | Galgamuwa (Mee Oya) | 1.45 | 🟢 Normal | -0.037 |  |
| 2025-12-07 12:10:32 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.012 |  |
| 2025-12-07 12:10:29 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.012 |  |
| 2025-12-07 12:08:07 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.009 |  |
| 2025-12-07 12:06:56 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.010 |  |
| 2025-12-07 12:05:59 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.011 |  |
| 2025-12-07 12:05:42 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.121 |  |
| 2025-12-07 12:05:11 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-07 12:04:47 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.070 |  |
| 2025-12-07 12:04:14 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2025-12-07 12:04:13 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2025-12-07 12:04:09 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.060 |  |
| 2025-12-07 12:04:09 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.039 |  |
| 2025-12-07 12:04:04 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.013 |  |
| 2025-12-07 12:03:58 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-07 12:03:52 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.081 |  |
| 2025-12-07 12:03:43 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.060 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-07 13:01:07 | Thanthirimale (Malwathu Oya) | 5.85 | 🟡 Alert | -0.082 |  |
| 2025-12-07 12:03:58 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2025-12-07 12:12:16 | Glencourse (Kelani Ganga) | 10.17 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2025-12-07 13:01:21 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:01:08 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-07 12:02:05 | Yaka Wewa (Ma Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2025-12-07 13:00:54 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-07 12:02:16 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-07 12:03:10 | Badalgama (Maha Oya) | 2.76 | 🟢 Normal | 0.000 |  |
| 2025-12-07 12:05:11 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-07 12:13:12 | Kuda Oya (Kirindi Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2025-12-07 12:08:07 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.009 |  |
| 2025-12-07 12:03:16 | Moraketiya (Walawe Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-07 13:01:03 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2025-12-07 12:06:56 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.010 |  |
| 2025-12-07 12:02:10 | Katharagama (Menik Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2025-12-07 12:03:14 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | -0.010 |  |
| 2025-12-07 12:04:14 | Urawa (Nilwala Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2025-12-07 12:01:49 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.011 |  |
| 2025-12-07 13:01:49 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.011 |  |
| 2025-12-07 13:01:03 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.012 |  |
| 2025-12-07 12:04:04 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | -0.013 |  |
| 2025-12-07 12:02:13 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | -0.020 |  |
| 2025-12-07 12:04:13 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2025-12-07 12:03:08 | Hanwella (Kelani Ganga) | 2.35 | 🟢 Normal | -0.020 |  |
| 2025-12-07 12:11:25 | Galgamuwa (Mee Oya) | 1.45 | 🟢 Normal | -0.037 |  |
| 2025-12-07 12:04:09 | Deraniyagala (Kelani Ganga) | 0.48 | 🟢 Normal | -0.039 |  |
| 2025-12-07 12:03:23 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | -0.045 |  |
| 2025-12-07 12:03:43 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | -0.060 |  |
| 2025-12-07 12:04:09 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.060 |  |
| 2025-12-07 13:02:23 | Manampitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.060 |  |
| 2025-12-07 12:04:47 | Thalgahagoda (Nilwala Ganga) | 0.72 | 🟢 Normal | -0.070 |  |
| 2025-12-07 12:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | -0.072 |  |
| 2025-12-07 13:01:53 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.080 |  |
| 2025-12-07 12:03:52 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.081 |  |
| 2025-12-07 12:05:42 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.121 |  |
| 2025-12-07 12:03:07 | Kithulgala (Kelani Ganga) | 1.74 | 🟢 Normal | -0.341 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)