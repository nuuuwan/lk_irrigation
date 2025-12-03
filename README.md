# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_08:16:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **8,091 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 08:16:25 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:12:47 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2025-12-03 08:11:55 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:11:28 | Panadugama (Nilwala Ganga) | 3.04 | 🟢 Normal | -0.022 |  |
| 2025-12-03 08:11:22 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:11:07 | Nagalagam Street (Kelani Ganga) | 1.45 | 🟡 Alert | -0.031 |  |
| 2025-12-03 08:08:54 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:08:07 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.011 |  |
| 2025-12-03 08:07:52 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:07:13 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-03 08:05:56 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:05:42 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:05:12 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.059 |  |
| 2025-12-03 08:05:00 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | -0.050 |  |
| 2025-12-03 08:04:39 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-03 08:04:20 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:03:32 | Hanwella (Kelani Ganga) | 5.59 | 🟢 Normal | -0.092 |  |
| 2025-12-03 08:03:26 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-03 08:03:24 | Putupaula (Kalu Ganga) | 3.05 | 🟡 Alert | -0.071 |  |
| 2025-12-03 08:03:19 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:03:09 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-03 08:03:01 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-03 08:02:43 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:02:33 | Giriulla (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:02:27 | Thanthirimale (Malwathu Oya) | 7.47 | 🟠 Minor Flood | -0.030 |  |
| 2025-12-03 08:02:16 | Katharagama (Menik Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.79 | 🟢 Normal | -0.110 |  |
| 2025-12-03 08:02:01 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | -0.011 |  |
| 2025-12-03 08:01:24 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | -0.024 |  |
| 2025-12-03 08:01:23 | Ellagawa (Kalu Ganga) | 7.81 | 🟢 Normal | -0.151 |  |
| 2025-12-03 08:01:20 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:01:16 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:01:04 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-03 08:00:20 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.011 |  |
| 2025-12-03 07:43:57 | Panadugama (Nilwala Ganga) | 3.05 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-03 08:02:27 | Thanthirimale (Malwathu Oya) | 7.47 | 🟠 Minor Flood | -0.030 |  |
| 2025-12-03 08:11:07 | Nagalagam Street (Kelani Ganga) | 1.45 | 🟡 Alert | -0.031 |  |
| 2025-12-03 08:03:24 | Putupaula (Kalu Ganga) | 3.05 | 🟡 Alert | -0.071 |  |
| 2025-12-03 08:04:39 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2025-12-03 08:01:04 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-03 08:03:09 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-03 08:07:52 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:05:56 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:02:33 | Giriulla (Maha Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:01:20 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:03:19 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:02:43 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:04:20 | Glencourse (Kelani Ganga) | 11.03 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:11:55 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:01:16 | Siyambalanduwa (Heda Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:11:22 | Dunamale (Aththanagalu Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:08:54 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:02:16 | Katharagama (Menik Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:16:25 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2025-12-03 08:07:13 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-03 08:12:47 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2025-12-03 08:03:01 | Urawa (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2025-12-03 08:03:26 | Deraniyagala (Kelani Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-03 08:08:07 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.011 |  |
| 2025-12-03 08:00:20 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.011 |  |
| 2025-12-03 08:02:01 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | -0.011 |  |
| 2025-12-02 18:12:00 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.018 |  |
| 2025-12-03 08:11:28 | Panadugama (Nilwala Ganga) | 3.04 | 🟢 Normal | -0.022 |  |
| 2025-12-03 08:01:24 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | -0.024 |  |
| 2025-12-03 08:05:00 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | -0.050 |  |
| 2025-12-03 08:05:12 | Rathnapura (Kalu Ganga) | 2.11 | 🟢 Normal | -0.059 |  |
| 2025-12-03 08:03:32 | Hanwella (Kelani Ganga) | 5.59 | 🟢 Normal | -0.092 |  |
| 2025-12-03 07:00:10 | Horowpothana (Yan Oya) | 3.16 | 🟢 Normal | -0.103 |  |
| 2025-12-03 08:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.79 | 🟢 Normal | -0.110 |  |
| 2025-12-02 18:07:24 | Galgamuwa (Mee Oya) | 2.52 | 🟢 Normal | -0.120 |  |
| 2025-12-03 08:01:23 | Ellagawa (Kalu Ganga) | 7.81 | 🟢 Normal | -0.151 |  |

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)