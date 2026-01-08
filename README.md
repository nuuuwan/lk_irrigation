# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_17:05:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **40,137 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 17:05:17 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.019 |  |
| 2026-01-08 17:05:05 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-08 17:04:45 | Katharagama (Menik Ganga) | 0.59 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-01-08 17:04:28 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-08 17:03:32 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-08 17:03:27 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-08 17:03:23 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-01-08 17:03:16 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.029 |  |
| 2026-01-08 17:03:13 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 17:02:52 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 17:02:50 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-01-08 17:02:41 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 17:02:25 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-01-08 17:01:45 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-08 17:01:38 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 17:01:30 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-01-08 17:01:18 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-01-08 17:01:10 | Manampitiya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.050 |  |
| 2026-01-08 17:00:44 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-01-08 17:00:19 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-08 16:59:48 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:32:56 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-01-08 16:30:32 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.007 |  |
| 2026-01-08 16:22:00 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.024 |  |
| 2026-01-08 16:17:50 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:11:05 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:10:30 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:09:48 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-08 16:08:42 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 16:07:53 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:07:41 | Katharagama (Menik Ganga) | 0.50 | 🟢 Normal | 0.095 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 16:06:22 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-01-08 16:02:03 | Thanamalwila (Kirindi Oya) | 0.99 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-01-08 16:02:31 | Padiyathalawa (Maduru Oya) | 1.50 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-01-08 17:04:45 | Katharagama (Menik Ganga) | 0.59 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-01-08 17:05:05 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-01-08 17:00:19 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-08 16:07:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-08 17:03:32 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-01-08 17:04:28 | Baddegama (Gin Ganga) | 0.99 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-08 17:01:45 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-08 16:01:17 | Weraganthota (Mahaweli Ganga) | -1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 16:05:36 | Thaldena (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 16:08:42 | Rathnapura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 17:03:13 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 17:02:41 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 17:01:38 | Yaka Wewa (Ma Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:06:46 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:59:48 | Horowpothana (Yan Oya) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:07:53 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-01-08 15:04:34 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-08 17:03:27 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:04:09 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:10:30 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:05:37 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-08 17:02:52 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 16:30:32 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.007 |  |
| 2026-01-08 17:01:30 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-01-08 17:03:23 | Siyambalanduwa (Heda Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-01-08 16:01:45 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-01-08 17:00:44 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-01-08 17:05:17 | Glencourse (Kelani Ganga) | 8.56 | 🟢 Normal | -0.019 |  |
| 2026-01-08 17:01:18 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-01-08 17:02:25 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-01-08 17:02:50 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-01-08 16:22:00 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.024 |  |
| 2026-01-08 17:03:16 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | -0.029 |  |
| 2026-01-08 17:01:10 | Manampitiya (Mahaweli Ganga) | 2.35 | 🟢 Normal | -0.050 |  |
| 2026-01-08 16:05:33 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | -0.077 |  |
| 2026-01-08 16:02:40 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.108 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)