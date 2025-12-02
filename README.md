# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_01:04:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,847 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 01:04:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.41 | 🟡 Alert | -0.029 |  |
| 2025-12-03 01:03:01 | Thanthirimale (Malwathu Oya) | 7.75 | 🟠 Minor Flood | -0.039 |  |
| 2025-12-03 01:02:56 | Giriulla (Maha Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2025-12-03 01:02:40 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-03 01:02:33 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-03 01:02:25 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2025-12-03 01:02:16 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.022 |  |
| 2025-12-03 01:01:32 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | -0.020 |  |
| 2025-12-03 01:01:27 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-03 01:01:23 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-03 01:01:16 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.011 |  |
| 2025-12-03 01:01:11 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2025-12-03 01:01:01 | Horowpothana (Yan Oya) | 3.49 | 🟢 Normal | -0.030 |  |
| 2025-12-03 01:00:28 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-03 00:26:40 | Putupaula (Kalu Ganga) | 3.37 | 🟡 Alert | -0.034 |  |
| 2025-12-03 00:13:42 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2025-12-03 00:11:21 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | -0.018 |  |
| 2025-12-03 00:08:43 | Deraniyagala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.022 |  |
| 2025-12-03 00:08:05 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | -1.059 |  |
| 2025-12-03 00:07:31 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | -1.059 |  |
| 2025-12-03 00:06:09 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | 0.000 |  |
| 2025-12-03 00:05:54 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-03 00:05:36 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-03 00:05:30 | Giriulla (Maha Oya) | 2.28 | 🟢 Normal | -0.010 |  |
| 2025-12-03 00:05:15 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-03 00:04:08 | Nagalagam Street (Kelani Ganga) | 1.89 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-03 01:03:01 | Thanthirimale (Malwathu Oya) | 7.75 | 🟠 Minor Flood | -0.039 |  |
| 2025-12-03 01:04:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.41 | 🟡 Alert | -0.029 |  |
| 2025-12-03 00:26:40 | Putupaula (Kalu Ganga) | 3.37 | 🟡 Alert | -0.034 |  |
| 2025-12-03 00:01:40 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2025-12-03 01:01:27 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-03 00:02:15 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-03 00:03:50 | Yaka Wewa (Ma Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-03 00:13:42 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2025-12-03 00:06:09 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | 0.000 |  |
| 2025-12-03 01:01:23 | Padiyathalawa (Maduru Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2025-12-03 01:02:40 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-03 01:02:25 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2025-12-03 00:05:54 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-03 00:03:05 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2025-12-03 01:00:28 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-03 00:02:51 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-03 00:04:15 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2025-12-03 01:02:33 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-03 00:05:36 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2025-12-03 01:01:11 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.010 |  |
| 2025-12-03 01:02:56 | Giriulla (Maha Oya) | 2.27 | 🟢 Normal | -0.010 |  |
| 2025-12-03 01:01:16 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.011 |  |
| 2025-12-02 18:12:00 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.018 |  |
| 2025-12-03 00:11:21 | Dunamale (Aththanagalu Oya) | 2.44 | 🟢 Normal | -0.018 |  |
| 2025-12-03 01:01:32 | Badalgama (Maha Oya) | 3.42 | 🟢 Normal | -0.020 |  |
| 2025-12-03 01:02:16 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.022 |  |
| 2025-12-03 01:01:01 | Horowpothana (Yan Oya) | 3.49 | 🟢 Normal | -0.030 |  |
| 2025-12-03 00:01:58 | Moraketiya (Walawe Ganga) | 1.30 | 🟢 Normal | -0.049 |  |
| 2025-12-03 00:02:59 | Ellagawa (Kalu Ganga) | 8.90 | 🟢 Normal | -0.057 |  |
| 2025-12-03 00:04:08 | Rathnapura (Kalu Ganga) | 2.59 | 🟢 Normal | -0.071 |  |
| 2025-12-03 00:02:25 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.072 |  |
| 2025-12-03 00:04:36 | Hanwella (Kelani Ganga) | 6.26 | 🟢 Normal | -0.119 |  |
| 2025-12-02 18:07:24 | Galgamuwa (Mee Oya) | 2.52 | 🟢 Normal | -0.120 |  |
| 2025-12-03 00:08:05 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | -1.059 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)