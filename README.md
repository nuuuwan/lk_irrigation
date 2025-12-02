# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--03_02:31:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,890 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-03 02:31:33 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2025-12-03 02:15:36 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | -0.019 |  |
| 2025-12-03 02:11:48 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.018 |  |
| 2025-12-03 02:10:25 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-03 02:10:14 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.009 |  |
| 2025-12-03 02:07:55 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-03 02:07:49 | Hanwella (Kelani Ganga) | 6.02 | 🟢 Normal | -0.139 |  |
| 2025-12-03 02:07:34 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-03 02:06:43 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | -0.198 |  |
| 2025-12-03 02:06:10 | Nagalagam Street (Kelani Ganga) | 1.83 | 🟠 Minor Flood | -0.031 |  |
| 2025-12-03 02:05:53 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-03 02:04:54 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.080 |  |
| 2025-12-03 02:04:30 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2025-12-03 02:03:59 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.132 |  |
| 2025-12-03 02:03:36 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.036 |  |
| 2025-12-03 02:03:30 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-03 02:02:51 | Giriulla (Maha Oya) | 2.25 | 🟢 Normal | -0.020 |  |
| 2025-12-03 02:02:41 | Yaka Wewa (Ma Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-03 02:02:41 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-03 02:02:20 | Horowpothana (Yan Oya) | 3.45 | 🟢 Normal | -0.039 |  |
| 2025-12-03 02:02:19 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2025-12-03 02:02:18 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-03 02:02:08 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-03 02:02:07 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.005 |  |
| 2025-12-03 02:01:58 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.005 |  |
| 2025-12-03 02:01:52 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2025-12-03 02:01:23 | Badalgama (Maha Oya) | 3.40 | 🟢 Normal | -0.020 |  |
| 2025-12-03 02:00:56 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-03 02:00:32 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-03 02:00:32 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-03 02:06:10 | Nagalagam Street (Kelani Ganga) | 1.83 | 🟠 Minor Flood | -0.031 |  |
| 2025-12-03 01:03:01 | Thanthirimale (Malwathu Oya) | 7.75 | 🟠 Minor Flood | -0.039 |  |
| 2025-12-03 01:04:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.41 | 🟡 Alert | -0.029 |  |
| 2025-12-03 01:08:00 | Putupaula (Kalu Ganga) | 3.34 | 🟡 Alert | -0.044 |  |
| 2025-12-03 02:07:34 | Baddegama (Gin Ganga) | 1.51 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2025-12-03 02:00:32 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-03 02:02:41 | Nakkala (Kumbukkan Oya) | 1.42 | 🟢 Normal | 0.000 |  |
| 2025-12-03 01:24:14 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2025-12-03 02:02:41 | Yaka Wewa (Ma Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-03 02:07:55 | Magura (Kalu Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-03 02:03:30 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2025-12-03 01:02:40 | Siyambalanduwa (Heda Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-03 02:04:30 | Katharagama (Menik Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2025-12-03 02:05:53 | Holombuwa (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-03 02:00:56 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2025-12-03 02:10:25 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-03 02:01:58 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.005 |  |
| 2025-12-03 02:02:07 | Panadugama (Nilwala Ganga) | 3.06 | 🟢 Normal | -0.005 |  |
| 2025-12-03 02:31:33 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.009 |  |
| 2025-12-03 02:10:14 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.009 |  |
| 2025-12-03 02:02:18 | Padiyathalawa (Maduru Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2025-12-03 02:01:52 | Kuda Oya (Kirindi Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2025-12-02 18:12:00 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.018 |  |
| 2025-12-03 02:11:48 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.018 |  |
| 2025-12-03 02:15:36 | Dunamale (Aththanagalu Oya) | 2.40 | 🟢 Normal | -0.019 |  |
| 2025-12-03 02:02:19 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.020 |  |
| 2025-12-03 02:02:51 | Giriulla (Maha Oya) | 2.25 | 🟢 Normal | -0.020 |  |
| 2025-12-03 02:01:23 | Badalgama (Maha Oya) | 3.40 | 🟢 Normal | -0.020 |  |
| 2025-12-03 02:03:36 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.036 |  |
| 2025-12-03 02:02:20 | Horowpothana (Yan Oya) | 3.45 | 🟢 Normal | -0.039 |  |
| 2025-12-03 02:04:54 | Rathnapura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.080 |  |
| 2025-12-02 18:07:24 | Galgamuwa (Mee Oya) | 2.52 | 🟢 Normal | -0.120 |  |
| 2025-12-03 02:03:59 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | -0.132 |  |
| 2025-12-03 02:07:49 | Hanwella (Kelani Ganga) | 6.02 | 🟢 Normal | -0.139 |  |
| 2025-12-03 02:06:43 | Ellagawa (Kalu Ganga) | 8.58 | 🟢 Normal | -0.198 |  |

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)