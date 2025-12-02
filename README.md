# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--02_23:07:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,788 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-02 23:07:28 | Badalgama (Maha Oya) | 3.45 | 🟢 Normal | -0.009 |  |
| 2025-12-02 23:07:28 | Ellagawa (Kalu Ganga) | 8.95 | 🟢 Normal | -0.076 |  |
| 2025-12-02 23:05:28 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:04:49 | Rathnapura (Kalu Ganga) | 2.66 | 🟢 Normal | -0.079 |  |
| 2025-12-02 23:04:22 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:04:18 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.030 |  |
| 2025-12-02 23:04:17 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-02 23:04:15 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2025-12-02 23:03:36 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2025-12-02 23:03:21 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.020 |  |
| 2025-12-02 23:02:43 | Katharagama (Menik Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:02:37 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:02:32 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:02:23 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:02:17 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:01:37 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-02 23:01:09 | Kuda Oya (Kirindi Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.49 | 🟡 Alert | -0.054 |  |
| 2025-12-02 23:01:06 | Horowpothana (Yan Oya) | 3.57 | 🟢 Normal | -0.040 |  |
| 2025-12-02 23:00:44 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:00:19 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:00:07 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | -0.061 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-02 22:05:04 | Thanthirimale (Malwathu Oya) | 7.86 | 🔴 Major Flood | -0.038 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-02 22:04:01 | Nagalagam Street (Kelani Ganga) | 1.89 | 🟠 Minor Flood | 0.016 | 🔺 Rising |
| 2025-12-02 23:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.49 | 🟡 Alert | -0.054 |  |
| 2025-12-02 22:03:07 | Putupaula (Kalu Ganga) | 3.45 | 🟡 Alert | -0.058 |  |
| 2025-12-02 23:04:17 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-02 23:00:19 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-02 22:01:52 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:01:37 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:05:28 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:02:17 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-02 22:06:26 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:17:24 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:02:23 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:02:43 | Katharagama (Menik Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:04:22 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:00:44 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:02:37 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:01:09 | Kuda Oya (Kirindi Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:02:32 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2025-12-02 23:07:28 | Badalgama (Maha Oya) | 3.45 | 🟢 Normal | -0.009 |  |
| 2025-12-02 22:07:54 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.010 |  |
| 2025-12-02 23:03:36 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | -0.010 |  |
| 2025-12-02 23:04:15 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2025-12-02 23:01:19 | Nawalapitiya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2025-12-02 18:12:00 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.018 |  |
| 2025-12-02 22:01:10 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2025-12-02 23:03:21 | Dunamale (Aththanagalu Oya) | 2.46 | 🟢 Normal | -0.020 |  |
| 2025-12-02 22:07:15 | Giriulla (Maha Oya) | 2.31 | 🟢 Normal | -0.025 |  |
| 2025-12-02 23:04:18 | Kithulgala (Kelani Ganga) | 2.12 | 🟢 Normal | -0.030 |  |
| 2025-12-02 23:01:06 | Horowpothana (Yan Oya) | 3.57 | 🟢 Normal | -0.040 |  |
| 2025-12-02 23:00:07 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | -0.061 |  |
| 2025-12-02 23:07:28 | Ellagawa (Kalu Ganga) | 8.95 | 🟢 Normal | -0.076 |  |
| 2025-12-02 23:04:49 | Rathnapura (Kalu Ganga) | 2.66 | 🟢 Normal | -0.079 |  |
| 2025-12-02 22:06:12 | Hanwella (Kelani Ganga) | 6.46 | 🟢 Normal | -0.101 |  |
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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)