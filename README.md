# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--17_17:15:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **48,230 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 17:15:21 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | -0.050 |  |
| 2026-01-17 17:09:38 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:08:53 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:08:47 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:08:44 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | -0.009 |  |
| 2026-01-17 17:08:30 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:08:07 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:07:14 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:07:07 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:06:13 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:05:58 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-01-17 17:04:40 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:04:28 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:04:14 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-01-17 17:04:04 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:04:01 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:03:54 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | -0.010 |  |
| 2026-01-17 17:03:43 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:03:34 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 17:03:34 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:03:32 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:03:28 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.031 |  |
| 2026-01-17 17:02:52 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.080 |  |
| 2026-01-17 17:02:41 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:02:31 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-01-17 17:02:29 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:02:21 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-17 17:02:16 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:02:12 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-01-17 17:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-01-17 17:01:58 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:01:58 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:01:52 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:01:35 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:01:30 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-17 17:01:16 | Weraganthota (Mahaweli Ganga) | -1.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:01:13 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-17 17:01:12 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:01:07 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-17 17:00:35 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-17 16:32:46 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 16:23:32 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 17:02:31 | Kithulgala (Kelani Ganga) | 1.71 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-01-17 17:01:07 | Baddegama (Gin Ganga) | 0.86 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-17 17:02:21 | Deraniyagala (Kelani Ganga) | 0.32 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-17 17:01:30 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-01-17 17:03:34 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 17:01:16 | Weraganthota (Mahaweli Ganga) | -1.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:02:16 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:03:43 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:01:58 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:04:01 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:07:07 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:04:28 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:08:30 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:03:32 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:04:04 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:04:40 | Padiyathalawa (Maduru Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:09:38 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:02:29 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:08:07 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:01:58 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:02:41 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:07:14 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:01:52 | Manampitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:03:34 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:06:13 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:08:53 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:01:35 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:01:12 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 17:08:44 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | -0.009 |  |
| 2026-01-17 17:03:54 | Ellagawa (Kalu Ganga) | 3.99 | 🟢 Normal | -0.010 |  |
| 2026-01-17 17:01:13 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-17 17:00:35 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-01-17 17:02:12 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-01-17 17:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-01-17 17:04:14 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.030 |  |
| 2026-01-17 17:05:58 | Thawalama (Gin Ganga) | 1.14 | 🟢 Normal | -0.030 |  |
| 2026-01-17 17:03:28 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.031 |  |
| 2026-01-17 17:15:21 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | -0.050 |  |
| 2026-01-17 17:02:52 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.080 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)