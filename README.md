# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--25_04:13:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **54,924 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 04:13:01 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -0.036 |  |
| 2026-01-25 04:12:49 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:12:48 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:11:48 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:09:58 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-01-25 04:07:06 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:06:11 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:06:02 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.173 |  |
| 2026-01-25 04:05:55 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 04:05:36 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:05:25 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:04:18 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-25 04:03:19 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:03:18 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:03:07 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:03:06 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.005 |  |
| 2026-01-25 04:02:57 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:02:57 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:02:45 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-01-25 04:02:33 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:02:33 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:01:55 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-25 04:01:48 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-25 04:01:41 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-01-25 04:01:31 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | -0.026 |  |
| 2026-01-25 04:00:58 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:00:39 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.229 |  |
| 2026-01-25 04:00:34 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-25 03:56:08 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | -0.036 |  |
| 2026-01-25 03:55:45 | Thawalama (Gin Ganga) | 0.99 | 🟢 Normal | -0.036 |  |
| 2026-01-25 03:55:24 | Manampitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.229 |  |
| 2026-01-25 03:38:11 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | -0.026 |  |
| 2026-01-25 03:32:28 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:31:53 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:26:21 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-25 04:01:41 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-01-25 02:02:47 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-01-25 02:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.31 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-25 03:02:08 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-25 04:01:55 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-25 04:05:55 | Glencourse (Kelani Ganga) | 8.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-25 04:01:48 | Ellagawa (Kalu Ganga) | 3.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-25 04:00:34 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-25 04:04:18 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-24 23:03:01 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:03:18 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:02:57 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-24 18:03:22 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-25 02:37:06 | Magura (Kalu Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:03:19 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:05:25 | Hanwella (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:05:36 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:08:29 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:02:33 | Padiyathalawa (Maduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:02:57 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:05:15 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-25 03:02:12 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:03:07 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:07:06 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:12:49 | Rathnapura (Kalu Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:06:11 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:02:33 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:11:48 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-25 04:03:06 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.005 |  |
| 2026-01-25 03:10:06 | Wellawaya (Kirindi Oya) | 0.81 | 🟢 Normal | -0.009 |  |
| 2026-01-24 18:01:40 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-25 04:09:58 | Dunamale (Aththanagalu Oya) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-01-24 18:00:14 | Weraganthota (Mahaweli Ganga) | -2.33 | 🟢 Normal | -0.020 |  |
| 2026-01-25 04:02:45 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-01-25 04:01:31 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | -0.026 |  |
| 2026-01-25 04:13:01 | Thawalama (Gin Ganga) | 0.98 | 🟢 Normal | -0.036 |  |
| 2026-01-25 04:06:02 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.173 |  |
| 2026-01-25 04:00:39 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.229 |  |
| 2026-01-25 03:21:26 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | -1.193 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)