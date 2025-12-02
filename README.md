# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--02_21:12:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,730 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-02 21:12:29 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:12:21 | Ellagawa (Kalu Ganga) | 9.10 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:11:04 | Putupaula (Kalu Ganga) | 3.50 | 🟡 Alert | -0.056 |  |
| 2025-12-02 21:10:01 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:06:59 | Hanwella (Kelani Ganga) | 6.56 | 🟢 Normal | -0.090 |  |
| 2025-12-02 21:06:51 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | -0.030 |  |
| 2025-12-02 21:06:28 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:06:20 | Nagalagam Street (Kelani Ganga) | 1.87 | 🟠 Minor Flood | -0.015 |  |
| 2025-12-02 21:06:08 | Ellagawa (Kalu Ganga) | 9.10 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:04:56 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:04:49 | Glencourse (Kelani Ganga) | 11.09 | 🟢 Normal | -0.010 |  |
| 2025-12-02 21:04:28 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:04:23 | Moraketiya (Walawe Ganga) | 1.49 | 🟢 Normal | -0.009 |  |
| 2025-12-02 21:04:00 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:03:48 | Katharagama (Menik Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:03:36 | Rathnapura (Kalu Ganga) | 2.81 | 🟢 Normal | -0.091 |  |
| 2025-12-02 21:03:24 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | -0.020 |  |
| 2025-12-02 21:03:19 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-02 21:03:19 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:02:58 | Badalgama (Maha Oya) | 3.48 | 🟢 Normal | -0.021 |  |
| 2025-12-02 21:02:56 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2025-12-02 21:02:31 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:02:22 | Thanthirimale (Malwathu Oya) | 7.90 | 🔴 Major Flood | -0.034 |  |
| 2025-12-02 21:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.58 | 🟡 Alert | -0.033 |  |
| 2025-12-02 21:02:06 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.030 |  |
| 2025-12-02 21:01:48 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2025-12-02 21:01:31 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:01:22 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:00:41 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:00:27 | Horowpothana (Yan Oya) | 3.65 | 🟢 Normal | -0.081 |  |
| 2025-12-02 20:27:57 | Putupaula (Kalu Ganga) | 3.54 | 🟡 Alert | -0.056 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-02 21:02:22 | Thanthirimale (Malwathu Oya) | 7.90 | 🔴 Major Flood | -0.034 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-02 21:06:20 | Nagalagam Street (Kelani Ganga) | 1.87 | 🟠 Minor Flood | -0.015 |  |
| 2025-12-02 21:02:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.58 | 🟡 Alert | -0.033 |  |
| 2025-12-02 21:11:04 | Putupaula (Kalu Ganga) | 3.50 | 🟡 Alert | -0.056 |  |
| 2025-12-02 21:01:31 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:01:22 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:02:31 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:04:00 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 20:02:02 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:10:01 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:03:19 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:12:21 | Ellagawa (Kalu Ganga) | 9.10 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:12:29 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:17:24 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:00:41 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:03:48 | Katharagama (Menik Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:06:28 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:04:56 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:04:28 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:04:23 | Moraketiya (Walawe Ganga) | 1.49 | 🟢 Normal | -0.009 |  |
| 2025-12-02 21:04:49 | Glencourse (Kelani Ganga) | 11.09 | 🟢 Normal | -0.010 |  |
| 2025-12-02 21:01:48 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | -0.010 |  |
| 2025-12-02 21:03:19 | Thalgahagoda (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2025-12-02 20:00:12 | Nakkala (Kumbukkan Oya) | 1.47 | 🟢 Normal | -0.011 |  |
| 2025-12-02 21:02:56 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.011 |  |
| 2025-12-02 18:12:00 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.018 |  |
| 2025-12-02 20:08:54 | Giriulla (Maha Oya) | 2.36 | 🟢 Normal | -0.019 |  |
| 2025-12-02 21:03:24 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | -0.020 |  |
| 2025-12-02 21:02:58 | Badalgama (Maha Oya) | 3.48 | 🟢 Normal | -0.021 |  |
| 2025-12-02 21:06:51 | Holombuwa (Kelani Ganga) | 1.09 | 🟢 Normal | -0.030 |  |
| 2025-12-02 21:02:06 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.030 |  |
| 2025-12-02 21:00:27 | Horowpothana (Yan Oya) | 3.65 | 🟢 Normal | -0.081 |  |
| 2025-12-02 21:06:59 | Hanwella (Kelani Ganga) | 6.56 | 🟢 Normal | -0.090 |  |
| 2025-12-02 21:03:36 | Rathnapura (Kalu Ganga) | 2.81 | 🟢 Normal | -0.091 |  |
| 2025-12-02 18:07:24 | Galgamuwa (Mee Oya) | 2.52 | 🟢 Normal | -0.120 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)