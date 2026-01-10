# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--10_13:23:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,813 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 13:23:21 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:18:36 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:16:58 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:14:49 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:08:57 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:08:33 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:08:20 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:08:15 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-10 13:08:00 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-10 13:07:26 | Baddegama (Gin Ganga) | 0.81 | 🟢 Normal | -0.037 |  |
| 2026-01-10 13:07:15 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.036 |  |
| 2026-01-10 13:06:55 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-10 13:06:38 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-10 13:06:01 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.260 |  |
| 2026-01-10 13:05:50 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:05:21 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-01-10 13:05:10 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 13:04:58 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | -0.012 |  |
| 2026-01-10 13:04:46 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-01-10 13:04:28 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-10 13:04:16 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.019 |  |
| 2026-01-10 13:04:14 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-10 13:03:56 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:03:30 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:03:25 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 13:03:14 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | -0.030 |  |
| 2026-01-10 13:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:02:13 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:02:08 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:01:51 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:01:27 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:01:23 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-10 13:01:22 | Weraganthota (Mahaweli Ganga) | -1.29 | 🟢 Normal | -0.020 |  |
| 2026-01-10 13:01:16 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:01:14 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | -0.010 |  |
| 2026-01-10 13:00:43 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:00:34 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:00:29 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-10 13:01:23 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-01-10 13:04:14 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-01-10 13:04:28 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-10 13:06:55 | Thaldena (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-10 13:08:00 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-01-10 13:05:10 | Glencourse (Kelani Ganga) | 8.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 13:03:25 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-10 13:08:15 | Thanthirimale (Malwathu Oya) | 1.89 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-10 13:02:08 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:01:16 | Nakkala (Kumbukkan Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:02:14 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:01:51 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:05:50 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:00:43 | Horowpothana (Yan Oya) | 2.73 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:08:33 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:18:36 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:03:30 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:08:20 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:00:29 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:01:27 | Siyambalanduwa (Heda Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:16:58 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:03:14 | Katharagama (Menik Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:08:57 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:00:34 | Manampitiya (Mahaweli Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:02:13 | Rathnapura (Kalu Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:14:49 | Thawalama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:23:21 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:03:56 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-10 13:04:46 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-01-10 13:01:14 | Ellagawa (Kalu Ganga) | 4.06 | 🟢 Normal | -0.010 |  |
| 2026-01-10 13:06:38 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-10 13:05:21 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-01-10 13:04:58 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | -0.012 |  |
| 2026-01-10 13:04:16 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.019 |  |
| 2026-01-10 13:01:22 | Weraganthota (Mahaweli Ganga) | -1.29 | 🟢 Normal | -0.020 |  |
| 2026-01-10 13:03:02 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.33 | 🟢 Normal | -0.030 |  |
| 2026-01-10 13:07:15 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.036 |  |
| 2026-01-10 13:07:26 | Baddegama (Gin Ganga) | 0.81 | 🟢 Normal | -0.037 |  |
| 2026-01-10 13:06:01 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.260 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)