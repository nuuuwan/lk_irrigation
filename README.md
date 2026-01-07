# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--08_00:13:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,511 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-08 00:13:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-01-08 00:12:52 | Pitabeddara (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-08 00:12:43 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-01-08 00:12:28 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-01-08 00:10:04 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-08 00:08:47 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-08 00:06:53 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:05:30 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.181 |  |
| 2026-01-08 00:05:13 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.049 |  |
| 2026-01-08 00:05:13 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-01-08 00:04:47 | Siyambalanduwa (Heda Oya) | 1.37 | 🟢 Normal | -0.019 |  |
| 2026-01-08 00:04:46 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-01-08 00:04:29 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-01-08 00:03:06 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:02:42 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:02:21 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:02:21 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:02:19 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-01-08 00:02:13 | Panadugama (Nilwala Ganga) | 3.47 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-01-08 00:02:12 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-01-08 00:02:08 | Katharagama (Menik Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-01-08 00:01:46 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:01:38 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.011 |  |
| 2026-01-08 00:01:18 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | -0.010 |  |
| 2026-01-08 00:01:01 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.005 |  |
| 2026-01-08 00:00:42 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.071 |  |
| 2026-01-08 00:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:00:19 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-07 23:58:21 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | -0.021 |  |
| 2026-01-07 23:56:13 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.350 | 🔺 Rising |
| 2026-01-07 23:55:33 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | -0.181 |  |
| 2026-01-07 23:44:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.51 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-01-07 23:35:19 | Manampitiya (Mahaweli Ganga) | 2.43 | 🟢 Normal | -0.071 |  |
| 2026-01-07 23:34:21 | Manampitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.071 |  |
| 2026-01-07 23:29:37 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 23:56:13 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.350 | 🔺 Rising |
| 2026-01-08 00:02:13 | Panadugama (Nilwala Ganga) | 3.47 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-01-08 00:04:29 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-01-08 00:13:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-01-08 00:12:43 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-01-08 00:12:52 | Pitabeddara (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-01-08 00:10:04 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-07 23:01:40 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 18:01:49 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-08 00:02:21 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:02:21 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:02:42 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:01:21 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-07 23:06:34 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:03:06 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:01:46 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:24:34 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | 0.000 |  |
| 2026-01-07 23:05:57 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:00:19 | Dunamale (Aththanagalu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:01:59 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-07 22:05:54 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:06:53 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-08 00:01:01 | Nakkala (Kumbukkan Oya) | 1.24 | 🟢 Normal | -0.005 |  |
| 2026-01-08 00:12:28 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.009 |  |
| 2026-01-08 00:08:47 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-08 00:02:12 | Yaka Wewa (Ma Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-01-08 00:01:18 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | -0.010 |  |
| 2026-01-08 00:02:08 | Katharagama (Menik Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-01-08 00:02:19 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-01-08 00:01:38 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.011 |  |
| 2026-01-08 00:05:13 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.011 |  |
| 2026-01-08 00:04:47 | Siyambalanduwa (Heda Oya) | 1.37 | 🟢 Normal | -0.019 |  |
| 2026-01-07 23:58:21 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | -0.021 |  |
| 2026-01-08 00:04:46 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-01-07 18:03:25 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | -0.023 |  |
| 2026-01-08 00:05:13 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.049 |  |
| 2026-01-08 00:00:42 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | -0.071 |  |
| 2026-01-08 00:05:30 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.181 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)