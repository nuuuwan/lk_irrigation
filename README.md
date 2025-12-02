# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--02_10:26:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,356 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-02 10:26:14 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:11:32 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:10:39 | Glencourse (Kelani Ganga) | 11.41 | 🟢 Normal | -0.035 |  |
| 2025-12-02 10:08:40 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:07:18 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:06:51 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2025-12-02 10:06:19 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2025-12-02 10:06:16 | Hanwella (Kelani Ganga) | 7.43 | 🟡 Alert | -0.070 |  |
| 2025-12-02 10:05:48 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.020 |  |
| 2025-12-02 10:05:30 | Galgamuwa (Mee Oya) | 3.18 | 🟢 Normal | -0.024 |  |
| 2025-12-02 10:05:05 | Badalgama (Maha Oya) | 3.61 | 🟢 Normal | -0.011 |  |
| 2025-12-02 10:04:55 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:04:22 | Nagalagam Street (Kelani Ganga) | 2.19 | 🔴 Major Flood | -0.030 |  |
| 2025-12-02 10:04:14 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:04:01 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.011 |  |
| 2025-12-02 10:03:35 | Putupaula (Kalu Ganga) | 3.84 | 🟡 Alert | -0.020 |  |
| 2025-12-02 10:03:27 | Thanthirimale (Malwathu Oya) | 8.52 | 🔴 Major Flood | -0.117 |  |
| 2025-12-02 10:03:25 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:03:11 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:02:58 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-02 10:02:55 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | -0.017 |  |
| 2025-12-02 10:02:45 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-02 10:02:37 | Ellagawa (Kalu Ganga) | 9.90 | 🟢 Normal | -0.067 |  |
| 2025-12-02 10:02:26 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:02:22 | Horowpothana (Yan Oya) | 4.52 | 🟢 Normal | -0.283 |  |
| 2025-12-02 10:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.15 | 🟡 Alert | -0.050 |  |
| 2025-12-02 10:02:18 | Dunamale (Aththanagalu Oya) | 2.80 | 🟢 Normal | -0.041 |  |
| 2025-12-02 10:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:02:08 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:01:48 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.226 |  |
| 2025-12-02 10:01:44 | Giriulla (Maha Oya) | 2.54 | 🟢 Normal | -0.010 |  |
| 2025-12-02 10:01:35 | Rathnapura (Kalu Ganga) | 3.78 | 🟢 Normal | -0.114 |  |
| 2025-12-02 10:01:15 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-02 10:01:11 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.020 |  |
| 2025-12-02 10:00:41 | Nakkala (Kumbukkan Oya) | 1.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-02 10:04:22 | Nagalagam Street (Kelani Ganga) | 2.19 | 🔴 Major Flood | -0.030 |  |
| 2025-12-02 10:03:27 | Thanthirimale (Malwathu Oya) | 8.52 | 🔴 Major Flood | -0.117 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-02 10:03:35 | Putupaula (Kalu Ganga) | 3.84 | 🟡 Alert | -0.020 |  |
| 2025-12-02 10:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.15 | 🟡 Alert | -0.050 |  |
| 2025-12-02 10:06:16 | Hanwella (Kelani Ganga) | 7.43 | 🟡 Alert | -0.070 |  |
| 2025-12-02 10:00:41 | Nakkala (Kumbukkan Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:02:08 | Yaka Wewa (Ma Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:04:14 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:03:25 | Deraniyagala (Kelani Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:11:32 | Panadugama (Nilwala Ganga) | 3.11 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:07:18 | Moraketiya (Walawe Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:04:55 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:02:26 | Thawalama (Gin Ganga) | 1.83 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:26:14 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:08:40 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2025-12-02 10:02:45 | Siyambalanduwa (Heda Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-02 10:02:58 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-02 10:01:44 | Giriulla (Maha Oya) | 2.54 | 🟢 Normal | -0.010 |  |
| 2025-12-02 10:01:15 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2025-12-02 10:04:01 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | -0.011 |  |
| 2025-12-02 10:05:05 | Badalgama (Maha Oya) | 3.61 | 🟢 Normal | -0.011 |  |
| 2025-12-02 10:06:19 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | -0.011 |  |
| 2025-12-02 10:02:55 | Kuda Oya (Kirindi Oya) | 1.77 | 🟢 Normal | -0.017 |  |
| 2025-12-02 10:05:48 | Magura (Kalu Ganga) | 1.96 | 🟢 Normal | -0.020 |  |
| 2025-12-02 10:01:11 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | -0.020 |  |
| 2025-12-02 10:06:51 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2025-12-02 10:05:30 | Galgamuwa (Mee Oya) | 3.18 | 🟢 Normal | -0.024 |  |
| 2025-12-02 10:10:39 | Glencourse (Kelani Ganga) | 11.41 | 🟢 Normal | -0.035 |  |
| 2025-12-02 10:02:18 | Dunamale (Aththanagalu Oya) | 2.80 | 🟢 Normal | -0.041 |  |
| 2025-12-02 10:02:37 | Ellagawa (Kalu Ganga) | 9.90 | 🟢 Normal | -0.067 |  |
| 2025-12-02 10:01:35 | Rathnapura (Kalu Ganga) | 3.78 | 🟢 Normal | -0.114 |  |
| 2025-12-01 14:07:27 | Manampitiya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.135 |  |
| 2025-12-02 10:01:48 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.226 |  |
| 2025-12-02 10:02:22 | Horowpothana (Yan Oya) | 4.52 | 🟢 Normal | -0.283 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)