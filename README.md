# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--08_17:09:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **12,618 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-08 17:09:26 | Glencourse (Kelani Ganga) | 10.01 | 🟢 Normal | -0.042 |  |
| 2025-12-08 17:08:46 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-08 17:08:32 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.030 |  |
| 2025-12-08 17:08:13 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.018 |  |
| 2025-12-08 17:08:05 | Panadugama (Nilwala Ganga) | 3.43 | 🟢 Normal | -0.030 |  |
| 2025-12-08 17:06:10 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-08 17:05:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-08 17:05:58 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.009 |  |
| 2025-12-08 17:05:38 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.009 |  |
| 2025-12-08 17:05:36 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.045 |  |
| 2025-12-08 17:05:16 | Galgamuwa (Mee Oya) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 17:05:03 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:04:44 | Norwood (Kelani Ganga) | 1.22 | 🟢 Normal | 0.270 | 🔺 Rising |
| 2025-12-08 17:03:50 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:03:49 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-08 17:03:41 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -18.000 |  |
| 2025-12-08 17:03:40 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | -0.041 |  |
| 2025-12-08 17:03:39 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -18.000 |  |
| 2025-12-08 17:03:32 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | -0.067 |  |
| 2025-12-08 17:03:24 | Weraganthota (Mahaweli Ganga) | -1.28 | 🟢 Normal | -0.346 |  |
| 2025-12-08 17:03:16 | Rathnapura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.052 |  |
| 2025-12-08 17:03:12 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.011 |  |
| 2025-12-08 17:02:37 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | -0.010 |  |
| 2025-12-08 17:02:30 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:02:30 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-08 17:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | -0.030 |  |
| 2025-12-08 17:02:13 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:02:11 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-08 17:02:02 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:01:59 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:01:59 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.011 |  |
| 2025-12-08 17:01:46 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:01:28 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:01:23 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:01:13 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:00:23 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:23:33 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-08 17:04:44 | Norwood (Kelani Ganga) | 1.22 | 🟢 Normal | 0.270 | 🔺 Rising |
| 2025-12-08 17:02:30 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2025-12-08 17:02:11 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2025-12-08 17:03:49 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-08 17:05:16 | Galgamuwa (Mee Oya) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-08 17:05:58 | Thaldena (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2025-12-08 17:01:13 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:05:03 | Nakkala (Kumbukkan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:00:23 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:01:37 | Yaka Wewa (Ma Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:01:46 | Giriulla (Maha Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:02:13 | Horowpothana (Yan Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:01:59 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:01:28 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:02:02 | Katharagama (Menik Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:02:30 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:03:50 | Manampitiya (Mahaweli Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2025-12-08 16:23:33 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:01:23 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2025-12-08 17:05:58 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | -0.009 |  |
| 2025-12-08 17:05:38 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.009 |  |
| 2025-12-08 17:02:37 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | -0.010 |  |
| 2025-12-08 17:06:10 | Urawa (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-08 17:08:46 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2025-12-08 17:03:12 | Thanamalwila (Kirindi Oya) | 1.22 | 🟢 Normal | -0.011 |  |
| 2025-12-08 17:01:59 | Siyambalanduwa (Heda Oya) | 0.81 | 🟢 Normal | -0.011 |  |
| 2025-12-08 17:08:13 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.018 |  |
| 2025-12-08 16:02:41 | Thanthirimale (Malwathu Oya) | 4.20 | 🟢 Normal | -0.029 |  |
| 2025-12-08 17:08:32 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.030 |  |
| 2025-12-08 17:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.34 | 🟢 Normal | -0.030 |  |
| 2025-12-08 17:08:05 | Panadugama (Nilwala Ganga) | 3.43 | 🟢 Normal | -0.030 |  |
| 2025-12-08 17:03:40 | Hanwella (Kelani Ganga) | 2.30 | 🟢 Normal | -0.041 |  |
| 2025-12-08 17:09:26 | Glencourse (Kelani Ganga) | 10.01 | 🟢 Normal | -0.042 |  |
| 2025-12-08 17:05:36 | Dunamale (Aththanagalu Oya) | 1.92 | 🟢 Normal | -0.045 |  |
| 2025-12-08 17:03:16 | Rathnapura (Kalu Ganga) | 1.94 | 🟢 Normal | -0.052 |  |
| 2025-12-08 17:03:32 | Ellagawa (Kalu Ganga) | 6.03 | 🟢 Normal | -0.067 |  |
| 2025-12-08 17:03:24 | Weraganthota (Mahaweli Ganga) | -1.28 | 🟢 Normal | -0.346 |  |
| 2025-12-08 17:03:41 | Pitabeddara (Nilwala Ganga) | 0.94 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)