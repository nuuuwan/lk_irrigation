# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--25_15:12:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **27,596 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 15:12:49 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.029 |  |
| 2025-12-25 15:11:11 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.029 |  |
| 2025-12-25 15:08:27 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:07:55 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.009 |  |
| 2025-12-25 15:07:51 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | -0.093 |  |
| 2025-12-25 15:06:52 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | 0.452 | 🔺 Rising |
| 2025-12-25 15:06:30 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 15:05:32 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.014 |  |
| 2025-12-25 15:05:19 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:05:05 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:04:49 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 15:04:27 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-25 15:04:24 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.078 |  |
| 2025-12-25 15:04:18 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:04:05 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:03:54 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:03:48 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-25 15:03:43 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-25 15:03:20 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.022 |  |
| 2025-12-25 15:03:15 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.037 |  |
| 2025-12-25 15:02:59 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:02:51 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:02:43 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2025-12-25 15:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 15:02:27 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:02:25 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2025-12-25 15:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | -0.030 |  |
| 2025-12-25 15:02:08 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-25 15:01:47 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 15:01:46 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:01:44 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.051 |  |
| 2025-12-25 15:01:39 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 15:01:15 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:00:50 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2025-12-25 15:00:22 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:00:11 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-25 14:31:36 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.029 |  |
| 2025-12-25 14:23:03 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.452 | 🔺 Rising |
| 2025-12-25 14:22:29 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.014 |  |
| 2025-12-25 14:21:59 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.004 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-25 15:06:52 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | 0.452 | 🔺 Rising |
| 2025-12-25 15:02:43 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2025-12-25 15:03:48 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2025-12-25 15:02:08 | Baddegama (Gin Ganga) | 1.88 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2025-12-25 15:06:30 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-25 15:01:47 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 15:01:39 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 15:02:40 | Nawalapitiya (Mahaweli Ganga) | 0.87 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 15:04:49 | Thalgahagoda (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-25 15:02:27 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:01:15 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:08:27 | Galgamuwa (Mee Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:04:18 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:04:05 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:01:46 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:00:22 | Siyambalanduwa (Heda Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:05:05 | Dunamale (Aththanagalu Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:02:51 | Thaldena (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:03:54 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:02:59 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2025-12-25 15:05:19 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2025-12-25 14:21:59 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.004 |  |
| 2025-12-25 15:07:55 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.009 |  |
| 2025-12-25 15:03:43 | Hanwella (Kelani Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2025-12-25 14:00:49 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2025-12-25 15:00:50 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | -0.010 |  |
| 2025-12-25 15:00:11 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | -0.010 |  |
| 2025-12-25 15:04:27 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2025-12-25 15:05:32 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | -0.014 |  |
| 2025-12-25 15:02:25 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2025-12-25 15:03:20 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | -0.022 |  |
| 2025-12-25 15:12:49 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.029 |  |
| 2025-12-25 15:11:11 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.029 |  |
| 2025-12-25 15:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.88 | 🟢 Normal | -0.030 |  |
| 2025-12-25 15:03:15 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.037 |  |
| 2025-12-25 14:08:43 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.043 |  |
| 2025-12-25 15:01:44 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.051 |  |
| 2025-12-25 15:04:24 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.078 |  |
| 2025-12-25 15:07:51 | Weraganthota (Mahaweli Ganga) | -1.62 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)