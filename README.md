# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--02_20:27:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,699 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-02 20:27:57 | Putupaula (Kalu Ganga) | 3.54 | 🟡 Alert | -0.022 |  |
| 2025-12-02 20:11:52 | Ellagawa (Kalu Ganga) | 9.15 | 🟢 Normal | 0.000 |  |
| 2025-12-02 20:09:50 | Thanthirimale (Malwathu Oya) | 7.93 | 🔴 Major Flood | -0.035 |  |
| 2025-12-02 20:08:54 | Giriulla (Maha Oya) | 2.36 | 🟢 Normal | -0.019 |  |
| 2025-12-02 20:08:39 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2025-12-02 20:08:31 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 20:07:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.61 | 🟡 Alert | -0.027 |  |
| 2025-12-02 20:07:17 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-02 20:06:53 | Hanwella (Kelani Ganga) | 6.65 | 🟢 Normal | -0.089 |  |
| 2025-12-02 20:06:26 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.061 |  |
| 2025-12-02 20:06:16 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.009 |  |
| 2025-12-02 20:05:55 | Badalgama (Maha Oya) | 3.50 | 🟢 Normal | -0.010 |  |
| 2025-12-02 20:05:25 | Nagalagam Street (Kelani Ganga) | 1.89 | 🟠 Minor Flood | -0.015 |  |
| 2025-12-02 20:05:20 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | -0.006 |  |
| 2025-12-02 20:04:52 | Ellagawa (Kalu Ganga) | 9.15 | 🟢 Normal | 0.000 |  |
| 2025-12-02 20:04:12 | Rathnapura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.091 |  |
| 2025-12-02 20:04:11 | Katharagama (Menik Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-02 20:03:27 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-02 20:03:15 | Dunamale (Aththanagalu Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2025-12-02 20:02:50 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | -6.353 |  |
| 2025-12-02 20:02:42 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-02 20:02:41 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | 0.000 |  |
| 2025-12-02 20:02:34 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-02 20:02:33 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -6.353 |  |
| 2025-12-02 20:02:04 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2025-12-02 20:02:02 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-02 20:01:56 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 20:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-02 20:01:26 | Horowpothana (Yan Oya) | 3.73 | 🟢 Normal | -0.053 |  |
| 2025-12-02 20:01:19 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2025-12-02 20:00:46 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.040 |  |
| 2025-12-02 20:00:32 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-02 20:00:27 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.011 |  |
| 2025-12-02 20:00:12 | Nakkala (Kumbukkan Oya) | 1.47 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-02 20:09:50 | Thanthirimale (Malwathu Oya) | 7.93 | 🔴 Major Flood | -0.035 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-02 20:05:25 | Nagalagam Street (Kelani Ganga) | 1.89 | 🟠 Minor Flood | -0.015 |  |
| 2025-12-02 20:27:57 | Putupaula (Kalu Ganga) | 3.54 | 🟡 Alert | -0.022 |  |
| 2025-12-02 20:07:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.61 | 🟡 Alert | -0.027 |  |
| 2025-12-02 20:02:42 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2025-12-02 20:04:11 | Katharagama (Menik Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-02 20:00:32 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-02 20:01:38 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.000 |  |
| 2025-12-02 20:01:56 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 20:02:02 | Magura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2025-12-02 20:08:31 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 20:11:52 | Ellagawa (Kalu Ganga) | 9.15 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:17:24 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-02 20:02:41 | Glencourse (Kelani Ganga) | 11.10 | 🟢 Normal | 0.000 |  |
| 2025-12-02 20:03:15 | Dunamale (Aththanagalu Oya) | 2.54 | 🟢 Normal | 0.000 |  |
| 2025-12-02 20:07:17 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-02 20:05:20 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | -0.006 |  |
| 2025-12-02 20:08:39 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.009 |  |
| 2025-12-02 20:06:16 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.009 |  |
| 2025-12-02 20:05:55 | Badalgama (Maha Oya) | 3.50 | 🟢 Normal | -0.010 |  |
| 2025-12-02 20:03:27 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2025-12-02 20:01:19 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2025-12-02 20:02:34 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2025-12-02 20:00:27 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.011 |  |
| 2025-12-02 20:00:12 | Nakkala (Kumbukkan Oya) | 1.47 | 🟢 Normal | -0.011 |  |
| 2025-12-02 18:12:00 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.018 |  |
| 2025-12-02 20:08:54 | Giriulla (Maha Oya) | 2.36 | 🟢 Normal | -0.019 |  |
| 2025-12-02 20:02:04 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.020 |  |
| 2025-12-02 20:00:46 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | -0.040 |  |
| 2025-12-02 20:01:26 | Horowpothana (Yan Oya) | 3.73 | 🟢 Normal | -0.053 |  |
| 2025-12-02 20:06:26 | Holombuwa (Kelani Ganga) | 1.12 | 🟢 Normal | -0.061 |  |
| 2025-12-02 20:06:53 | Hanwella (Kelani Ganga) | 6.65 | 🟢 Normal | -0.089 |  |
| 2025-12-02 20:04:12 | Rathnapura (Kalu Ganga) | 2.90 | 🟢 Normal | -0.091 |  |
| 2025-12-02 18:07:24 | Galgamuwa (Mee Oya) | 2.52 | 🟢 Normal | -0.120 |  |
| 2025-12-02 20:02:50 | Baddegama (Gin Ganga) | 1.47 | 🟢 Normal | -6.353 |  |

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)