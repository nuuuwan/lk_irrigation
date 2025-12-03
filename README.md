# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_09:15:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,126 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 09:15:48 | Panadugama (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.019 |  |
| 2025-12-03 09:12:55 | Manampitiya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.005 |  |
| 2025-12-03 09:10:35 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:08:24 | Horowpothana (Yan Oya) | 2.95 | 🟢 Normal | -0.098 |  |
| 2025-12-03 09:07:21 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.022 |  |
| 2025-12-03 09:07:10 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.059 |  |
| 2025-12-03 09:06:55 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-03 09:06:46 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:06:31 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2025-12-03 09:05:38 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-03 09:05:07 | Hanwella (Kelani Ganga) | 5.51 | 🟢 Normal | -0.078 |  |
| 2025-12-03 09:04:56 | Giriulla (Maha Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2025-12-03 09:04:42 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:04:23 | Katharagama (Menik Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:04:21 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:03:46 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.023 |  |
| 2025-12-03 09:03:40 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.011 |  |
| 2025-12-03 09:03:27 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:03:27 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.060 |  |
| 2025-12-03 09:03:21 | Thanthirimale (Malwathu Oya) | 7.40 | 🟠 Minor Flood | -0.168 |  |
| 2025-12-03 09:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.73 | 🟢 Normal | -0.059 |  |
| 2025-12-03 09:03:07 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:03:04 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:02:38 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:02:35 | Putupaula (Kalu Ganga) | 2.98 | 🟢 Normal | -0.071 |  |
| 2025-12-03 09:02:23 | Nagalagam Street (Kelani Ganga) | 1.43 | 🟡 Alert | -0.018 |  |
| 2025-12-03 09:02:23 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2025-12-03 09:02:17 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:02:11 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:01:48 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.030 |  |
| 2025-12-03 09:01:47 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:01:14 | Ellagawa (Kalu Ganga) | 7.66 | 🟢 Normal | -0.150 |  |
| 2025-12-03 09:01:10 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-03 09:00:09 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-03 09:03:21 | Thanthirimale (Malwathu Oya) | 7.40 | 🟠 Minor Flood | -0.168 |  |
| 2025-12-03 09:02:23 | Nagalagam Street (Kelani Ganga) | 1.43 | 🟡 Alert | -0.018 |  |
| 2025-12-03 09:05:38 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2025-12-03 09:06:55 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-03 09:06:46 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:03:27 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:00:09 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:02:38 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:03:04 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:02:11 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:04:21 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:04:20 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:10:35 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:03:07 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:04:23 | Katharagama (Menik Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:02:17 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:04:42 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:01:47 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2025-12-03 09:12:55 | Manampitiya (Mahaweli Ganga) | 2.88 | 🟢 Normal | -0.005 |  |
| 2025-12-03 09:04:56 | Giriulla (Maha Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2025-12-03 09:06:31 | Thawalama (Gin Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2025-12-03 09:01:10 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2025-12-03 09:02:23 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.010 |  |
| 2025-12-03 09:03:40 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.011 |  |
| 2025-12-03 09:15:48 | Panadugama (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.019 |  |
| 2025-12-03 09:07:21 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.022 |  |
| 2025-12-03 09:03:46 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.023 |  |
| 2025-12-03 09:01:48 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | -0.030 |  |
| 2025-12-03 09:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.73 | 🟢 Normal | -0.059 |  |
| 2025-12-03 09:07:10 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.059 |  |
| 2025-12-03 09:03:27 | Deraniyagala (Kelani Ganga) | 0.92 | 🟢 Normal | -0.060 |  |
| 2025-12-03 09:02:35 | Putupaula (Kalu Ganga) | 2.98 | 🟢 Normal | -0.071 |  |
| 2025-12-03 09:05:07 | Hanwella (Kelani Ganga) | 5.51 | 🟢 Normal | -0.078 |  |
| 2025-12-03 09:08:24 | Horowpothana (Yan Oya) | 2.95 | 🟢 Normal | -0.098 |  |
| 2025-12-02 18:07:24 | Galgamuwa (Mee Oya) | 2.52 | 🟢 Normal | -0.120 |  |
| 2025-12-03 09:01:14 | Ellagawa (Kalu Ganga) | 7.66 | 🟢 Normal | -0.150 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)