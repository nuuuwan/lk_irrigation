# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--02_22:07:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,765 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-02 22:07:54 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.010 |  |
| 2025-12-02 22:07:52 | Katharagama (Menik Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2025-12-02 22:07:15 | Giriulla (Maha Oya) | 2.31 | 🟢 Normal | -0.025 |  |
| 2025-12-02 22:06:26 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | 0.000 |  |
| 2025-12-02 22:06:12 | Hanwella (Kelani Ganga) | 6.46 | 🟢 Normal | -0.101 |  |
| 2025-12-02 22:05:32 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 22:05:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.54 | 🟡 Alert | -0.038 |  |
| 2025-12-02 22:05:04 | Thanthirimale (Malwathu Oya) | 7.86 | 🔴 Major Flood | -0.038 |  |
| 2025-12-02 22:04:49 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-02 22:04:30 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-02 22:04:17 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.029 |  |
| 2025-12-02 22:04:15 | Rathnapura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.069 |  |
| 2025-12-02 22:04:01 | Nagalagam Street (Kelani Ganga) | 1.89 | 🟠 Minor Flood | 0.016 | 🔺 Rising |
| 2025-12-02 22:03:54 | Badalgama (Maha Oya) | 3.46 | 🟢 Normal | 2.717 | 🔺 Rising |
| 2025-12-02 22:03:54 | Ellagawa (Kalu Ganga) | 9.03 | 🟢 Normal | -0.081 |  |
| 2025-12-02 22:03:51 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.011 |  |
| 2025-12-02 22:03:31 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-02 22:03:18 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | -0.040 |  |
| 2025-12-02 22:03:07 | Putupaula (Kalu Ganga) | 3.45 | 🟡 Alert | -0.058 |  |
| 2025-12-02 22:03:00 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2025-12-02 22:02:47 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2025-12-02 22:02:32 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-02 22:02:14 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-02 22:02:09 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-02 22:01:52 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 22:01:21 | Kuda Oya (Kirindi Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2025-12-02 22:01:15 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-02 22:01:10 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2025-12-02 22:00:52 | Horowpothana (Yan Oya) | 3.61 | 🟢 Normal | -0.040 |  |
| 2025-12-02 22:00:41 | Moraketiya (Walawe Ganga) | 1.41 | 🟢 Normal | -0.142 |  |
| 2025-12-02 22:00:18 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-02 22:00:16 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-02 21:39:23 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 2.717 | 🔺 Rising |
| 2025-12-02 21:26:59 | Moraketiya (Walawe Ganga) | 1.49 | 🟢 Normal | -0.142 |  |
| 2025-12-02 21:24:36 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | 0.000 |  |

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
| 2025-12-02 22:05:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.54 | 🟡 Alert | -0.038 |  |
| 2025-12-02 22:03:07 | Putupaula (Kalu Ganga) | 3.45 | 🟡 Alert | -0.058 |  |
| 2025-12-02 22:03:54 | Badalgama (Maha Oya) | 3.46 | 🟢 Normal | 2.717 | 🔺 Rising |
| 2025-12-02 22:00:16 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2025-12-02 22:02:09 | Nawalapitiya (Mahaweli Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2025-12-02 22:01:52 | Yaka Wewa (Ma Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 22:02:32 | Magura (Kalu Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2025-12-02 22:05:32 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2025-12-02 22:02:14 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2025-12-02 22:06:26 | Panadugama (Nilwala Ganga) | 3.07 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:17:24 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-02 22:07:52 | Katharagama (Menik Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2025-12-02 22:01:15 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-02 22:07:54 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.010 |  |
| 2025-12-02 22:04:30 | Baddegama (Gin Ganga) | 1.43 | 🟢 Normal | -0.010 |  |
| 2025-12-02 22:04:49 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2025-12-02 22:00:18 | Siyambalanduwa (Heda Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2025-12-02 22:01:21 | Kuda Oya (Kirindi Oya) | 1.72 | 🟢 Normal | -0.010 |  |
| 2025-12-02 22:03:31 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2025-12-02 22:02:47 | Urawa (Nilwala Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2025-12-02 22:03:51 | Holombuwa (Kelani Ganga) | 1.08 | 🟢 Normal | -0.011 |  |
| 2025-12-02 18:12:00 | Manampitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.018 |  |
| 2025-12-02 22:01:10 | Nakkala (Kumbukkan Oya) | 1.43 | 🟢 Normal | -0.020 |  |
| 2025-12-02 22:03:00 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.020 |  |
| 2025-12-02 22:07:15 | Giriulla (Maha Oya) | 2.31 | 🟢 Normal | -0.025 |  |
| 2025-12-02 22:04:17 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.029 |  |
| 2025-12-02 22:00:52 | Horowpothana (Yan Oya) | 3.61 | 🟢 Normal | -0.040 |  |
| 2025-12-02 22:03:18 | Dunamale (Aththanagalu Oya) | 2.48 | 🟢 Normal | -0.040 |  |
| 2025-12-02 22:04:15 | Rathnapura (Kalu Ganga) | 2.74 | 🟢 Normal | -0.069 |  |
| 2025-12-02 22:03:54 | Ellagawa (Kalu Ganga) | 9.03 | 🟢 Normal | -0.081 |  |
| 2025-12-02 22:06:12 | Hanwella (Kelani Ganga) | 6.46 | 🟢 Normal | -0.101 |  |
| 2025-12-02 18:07:24 | Galgamuwa (Mee Oya) | 2.52 | 🟢 Normal | -0.120 |  |
| 2025-12-02 22:00:41 | Moraketiya (Walawe Ganga) | 1.41 | 🟢 Normal | -0.142 |  |

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)