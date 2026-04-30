# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--01_03:12:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,621 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 03:12:05 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-01 03:11:16 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-05-01 03:09:16 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.114 |  |
| 2026-05-01 03:06:41 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:06:36 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.053 |  |
| 2026-05-01 03:05:30 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.281 |  |
| 2026-05-01 03:05:06 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:04:57 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:04:48 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-05-01 03:04:32 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-01 03:04:11 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.032 |  |
| 2026-05-01 03:04:09 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-05-01 03:04:02 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:03:42 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-01 03:03:39 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.094 |  |
| 2026-05-01 03:03:35 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2026-05-01 03:03:20 | Kithulgala (Kelani Ganga) | 1.29 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-05-01 03:03:19 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-01 03:03:13 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-01 03:02:55 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:02:44 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:02:38 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:02:36 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-05-01 03:02:32 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:01:22 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:01:14 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:01:02 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-01 03:00:45 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:46:58 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-01 02:45:16 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-01 02:39:48 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-05-01 02:24:56 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.281 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-01 03:03:35 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | 0.429 | 🔺 Rising |
| 2026-05-01 03:03:20 | Kithulgala (Kelani Ganga) | 1.29 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-05-01 03:03:19 | Moragaswewa (Deduru Oya) | 0.98 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-01 03:04:32 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-01 03:03:13 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-01 03:12:05 | Panadugama (Nilwala Ganga) | 2.09 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-05-01 03:01:02 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-01 02:39:48 | Thawalama (Gin Ganga) | 1.33 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-05-01 03:01:22 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:02:44 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:04:57 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:05:06 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:02:55 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:02:38 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:04:02 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:02:32 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:06:41 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:02:32 | Thanthirimale (Malwathu Oya) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-05-01 02:06:45 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:01:14 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-05-01 03:11:16 | Holombuwa (Kelani Ganga) | 0.24 | 🟢 Normal | -0.009 |  |
| 2026-05-01 03:03:42 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-05-01 03:04:09 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-05-01 03:02:36 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:02:01 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.010 |  |
| 2026-05-01 02:00:20 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:03:14 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-05-01 02:12:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.97 | 🟢 Normal | -0.012 |  |
| 2026-05-01 02:18:59 | Horowpothana (Yan Oya) | 1.95 | 🟢 Normal | -0.013 |  |
| 2026-05-01 03:04:48 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-05-01 00:03:12 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-05-01 03:04:11 | Manampitiya (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.032 |  |
| 2026-05-01 00:05:11 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.042 |  |
| 2026-05-01 03:06:36 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.053 |  |
| 2026-05-01 03:03:39 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.094 |  |
| 2026-05-01 03:09:16 | Rathnapura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.114 |  |
| 2026-05-01 02:06:43 | Yaka Wewa (Ma Oya) | 1.08 | 🟢 Normal | -0.140 |  |
| 2026-05-01 03:05:30 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.281 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)