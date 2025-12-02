# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--02_17:03:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **7,579 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-02 17:03:47 | Glencourse (Kelani Ganga) | 11.21 | 🟢 Normal | -0.020 |  |
| 2025-12-02 17:03:30 | Rathnapura (Kalu Ganga) | 3.16 | 🟢 Normal | -0.088 |  |
| 2025-12-02 17:03:27 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-02 17:03:22 | Putupaula (Kalu Ganga) | 3.64 | 🟡 Alert | -0.041 |  |
| 2025-12-02 17:03:12 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-02 17:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.74 | 🟡 Alert | -0.059 |  |
| 2025-12-02 17:02:58 | Badalgama (Maha Oya) | 3.54 | 🟢 Normal | -0.010 |  |
| 2025-12-02 17:02:35 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.023 |  |
| 2025-12-02 17:02:27 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-02 17:02:13 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-02 17:02:01 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-02 17:01:56 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-02 17:01:27 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-02 16:11:38 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-02 16:10:55 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.023 |  |
| 2025-12-02 16:10:42 | Galgamuwa (Mee Oya) | 2.73 | 🟢 Normal | -0.150 |  |
| 2025-12-02 16:09:55 | Hanwella (Kelani Ganga) | 7.00 | 🟡 Alert | -0.067 |  |
| 2025-12-02 16:09:29 | Nagalagam Street (Kelani Ganga) | 2.01 | 🟠 Minor Flood | -0.044 |  |
| 2025-12-02 16:08:03 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.009 |  |
| 2025-12-02 16:07:30 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-02 16:05:43 | Ellagawa (Kalu Ganga) | 9.50 | 🟢 Normal | -0.061 |  |
| 2025-12-02 16:05:21 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | -0.012 |  |
| 2025-12-02 16:04:46 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-02 16:04:32 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-02 16:04:30 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2025-12-02 16:04:29 | Horowpothana (Yan Oya) | 3.97 | 🟢 Normal | -0.056 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-02 15:02:35 | Thanthirimale (Malwathu Oya) | 8.19 | 🔴 Major Flood | -1.040 |  |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-12-02 16:09:29 | Nagalagam Street (Kelani Ganga) | 2.01 | 🟠 Minor Flood | -0.044 |  |
| 2025-12-02 15:21:21 | Manampitiya (Mahaweli Ganga) | 3.00 | 🟡 Alert | 0.025 | 🔺 Rising |
| 2025-12-02 17:03:22 | Putupaula (Kalu Ganga) | 3.64 | 🟡 Alert | -0.041 |  |
| 2025-12-02 17:03:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.74 | 🟡 Alert | -0.059 |  |
| 2025-12-02 16:09:55 | Hanwella (Kelani Ganga) | 7.00 | 🟡 Alert | -0.067 |  |
| 2025-12-02 17:03:12 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-02 16:11:38 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2025-12-02 16:00:27 | Nakkala (Kumbukkan Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-02 16:02:00 | Yaka Wewa (Ma Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-02 16:04:32 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2025-12-02 15:17:24 | Padiyathalawa (Maduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2025-12-02 16:02:34 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2025-12-02 17:01:27 | Siyambalanduwa (Heda Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-02 16:01:53 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2025-12-02 17:02:27 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2025-12-02 17:02:13 | Kuda Oya (Kirindi Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2025-12-02 16:08:03 | Magura (Kalu Ganga) | 1.88 | 🟢 Normal | -0.009 |  |
| 2025-12-02 16:04:30 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2025-12-02 17:03:27 | Wellawaya (Kirindi Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2025-12-02 17:01:56 | Baddegama (Gin Ganga) | 1.59 | 🟢 Normal | -0.010 |  |
| 2025-12-02 16:02:58 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2025-12-02 17:02:58 | Badalgama (Maha Oya) | 3.54 | 🟢 Normal | -0.010 |  |
| 2025-12-02 16:03:33 | Norwood (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2025-12-02 17:02:01 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2025-12-02 16:05:21 | Panadugama (Nilwala Ganga) | 3.08 | 🟢 Normal | -0.012 |  |
| 2025-12-02 17:03:47 | Glencourse (Kelani Ganga) | 11.21 | 🟢 Normal | -0.020 |  |
| 2025-12-02 16:01:45 | Holombuwa (Kelani Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2025-12-02 16:03:07 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.020 |  |
| 2025-12-02 16:02:27 | Katharagama (Menik Ganga) | 0.29 | 🟢 Normal | -0.021 |  |
| 2025-12-02 17:02:35 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | -0.023 |  |
| 2025-12-02 16:04:29 | Horowpothana (Yan Oya) | 3.97 | 🟢 Normal | -0.056 |  |
| 2025-12-02 16:05:43 | Ellagawa (Kalu Ganga) | 9.50 | 🟢 Normal | -0.061 |  |
| 2025-12-02 17:03:30 | Rathnapura (Kalu Ganga) | 3.16 | 🟢 Normal | -0.088 |  |
| 2025-12-02 16:10:42 | Galgamuwa (Mee Oya) | 2.73 | 🟢 Normal | -0.150 |  |

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)