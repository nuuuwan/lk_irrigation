# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_16:23:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,582 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 16:23:33 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:12:46 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | -0.055 |  |
| 2025-12-08 16:11:39 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.078 |  |
| 2025-12-08 16:09:49 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:08:40 | Panadugama (Nilwala Ganga) | 3.46 | 🟢 Normal | -0.045 |  |
| 2025-12-08 16:07:50 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:07:43 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.051 |  |
| 2025-12-08 16:07:38 | Putupaula (Kalu Ganga) | 1.07 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-08 16:07:08 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.016 |  |
| 2025-12-08 16:07:01 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-08 16:06:39 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-08 16:06:19 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:05:52 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.080 |  |
| 2025-12-08 16:05:38 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:04:55 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:04:32 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.039 |  |
| 2025-12-08 16:03:53 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 16:03:27 | Galgamuwa (Mee Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:03:01 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.032 |  |
| 2025-12-08 16:02:48 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2025-12-08 16:02:41 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | -0.029 |  |
| 2025-12-08 16:02:41 | Weraganthota (Mahaweli Ganga) | -0.93 | 🟢 Normal | -0.209 |  |
| 2025-12-08 16:02:33 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:02:23 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.37 | 🟢 Normal | -0.041 |  |
| 2025-12-08 16:02:19 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.032 |  |
| 2025-12-08 16:02:15 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | -0.021 |  |
| 2025-12-08 16:02:13 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.050 |  |
| 2025-12-08 16:02:07 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2025-12-08 16:01:37 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:01:33 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:01:21 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.053 |  |
| 2025-12-08 16:01:13 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-08 16:01:08 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.095 |  |
| 2025-12-08 16:00:21 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-08 16:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 16:02:07 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2025-12-08 16:07:01 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2025-12-08 16:07:38 | Putupaula (Kalu Ganga) | 1.07 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2025-12-08 16:03:53 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 16:01:33 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:01:37 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 15:01:23 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:03:27 | Galgamuwa (Mee Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:09:49 | Padiyathalawa (Maduru Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:02:23 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:05:38 | Siyambalanduwa (Heda Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:02:33 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:07:50 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:23:33 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:04:55 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:06:19 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2025-12-08 16:00:21 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | -0.010 |  |
| 2025-12-08 16:01:13 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2025-12-08 16:02:48 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2025-12-08 16:07:08 | Urawa (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.016 |  |
| 2025-12-08 16:06:39 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | -0.020 |  |
| 2025-12-08 16:02:15 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | -0.021 |  |
| 2025-12-08 15:05:36 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.022 |  |
| 2025-12-08 16:02:41 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | -0.029 |  |
| 2025-12-08 16:03:01 | Peradeniya (Mahaweli Ganga) | 2.65 | 🟢 Normal | -0.032 |  |
| 2025-12-08 16:02:19 | Thaldena (Mahaweli Ganga) | 0.66 | 🟢 Normal | -0.032 |  |
| 2025-12-08 16:04:32 | Hanwella (Kelani Ganga) | 2.34 | 🟢 Normal | -0.039 |  |
| 2025-12-08 16:02:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.37 | 🟢 Normal | -0.041 |  |
| 2025-12-08 16:08:40 | Panadugama (Nilwala Ganga) | 3.46 | 🟢 Normal | -0.045 |  |
| 2025-12-08 16:02:13 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.050 |  |
| 2025-12-08 16:07:43 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.051 |  |
| 2025-12-08 16:01:21 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.053 |  |
| 2025-12-08 16:12:46 | Dunamale (Aththanagalu Oya) | 1.96 | 🟢 Normal | -0.055 |  |
| 2025-12-08 16:11:39 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | -0.078 |  |
| 2025-12-08 16:05:52 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.080 |  |
| 2025-12-08 16:01:08 | Ellagawa (Kalu Ganga) | 6.10 | 🟢 Normal | -0.095 |  |
| 2025-12-08 16:02:41 | Weraganthota (Mahaweli Ganga) | -0.93 | 🟢 Normal | -0.209 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)