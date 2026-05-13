# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_04:28:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,246 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 04:28:54 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.023 |  |
| 2026-05-14 04:23:37 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-14 04:19:41 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-14 04:15:21 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-05-14 04:07:41 | Baddegama (Gin Ganga) | 3.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 04:06:24 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.074 |  |
| 2026-05-14 04:06:06 | Ellagawa (Kalu Ganga) | 8.28 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-14 04:05:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2026-05-14 04:05:38 | Magura (Kalu Ganga) | 4.78 | 🟡 Alert | -0.105 |  |
| 2026-05-14 04:05:09 | Thawalama (Gin Ganga) | 2.58 | 🟢 Normal | -0.056 |  |
| 2026-05-14 04:04:36 | Moragaswewa (Deduru Oya) | 2.02 | 🟢 Normal | -0.105 |  |
| 2026-05-14 04:04:25 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.042 |  |
| 2026-05-14 04:04:24 | Rathnapura (Kalu Ganga) | 4.91 | 🟢 Normal | -0.144 |  |
| 2026-05-14 04:04:11 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.128 |  |
| 2026-05-14 04:03:48 | Putupaula (Kalu Ganga) | 2.39 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-14 04:03:14 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.041 |  |
| 2026-05-14 04:03:14 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.109 |  |
| 2026-05-14 04:03:03 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:02:49 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:02:31 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:02:07 | Badalgama (Maha Oya) | 2.84 | 🟢 Normal | -0.092 |  |
| 2026-05-14 04:01:51 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:01:49 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:01:11 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.040 |  |
| 2026-05-14 04:01:11 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.056 |  |
| 2026-05-14 04:01:00 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -1.123 |  |
| 2026-05-14 04:00:53 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:00:35 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.022 |  |
| 2026-05-14 04:00:21 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 04:05:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2026-05-14 03:02:30 | Dunamale (Aththanagalu Oya) | 3.38 | 🟡 Alert | -0.040 |  |
| 2026-05-14 04:05:38 | Magura (Kalu Ganga) | 4.78 | 🟡 Alert | -0.105 |  |
| 2026-05-13 18:02:23 | Galgamuwa (Mee Oya) | 2.97 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-14 04:19:41 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-14 04:03:48 | Putupaula (Kalu Ganga) | 2.39 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-14 04:23:37 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-14 04:06:06 | Ellagawa (Kalu Ganga) | 8.28 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-14 03:04:58 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 04:07:41 | Baddegama (Gin Ganga) | 3.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 04:00:21 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:00:53 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:03:03 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:02:49 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:01:51 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:02:31 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-14 03:03:58 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:01:49 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:06:39 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-14 03:05:57 | Thanamalwila (Kirindi Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:15:21 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.009 |  |
| 2026-05-14 03:03:08 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | -0.011 |  |
| 2026-05-14 04:00:35 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.022 |  |
| 2026-05-14 04:28:54 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.023 |  |
| 2026-05-14 04:01:11 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.040 |  |
| 2026-05-14 04:03:14 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.041 |  |
| 2026-05-14 04:04:25 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.042 |  |
| 2026-05-13 18:02:14 | Thanthirimale (Malwathu Oya) | 3.35 | 🟢 Normal | -0.051 |  |
| 2026-05-14 04:05:09 | Thawalama (Gin Ganga) | 2.58 | 🟢 Normal | -0.056 |  |
| 2026-05-14 04:01:11 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.056 |  |
| 2026-05-14 02:05:26 | Panadugama (Nilwala Ganga) | 4.79 | 🟢 Normal | -0.065 |  |
| 2026-05-14 04:06:24 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.074 |  |
| 2026-05-14 04:02:07 | Badalgama (Maha Oya) | 2.84 | 🟢 Normal | -0.092 |  |
| 2026-05-14 04:04:36 | Moragaswewa (Deduru Oya) | 2.02 | 🟢 Normal | -0.105 |  |
| 2026-05-14 04:03:14 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.109 |  |
| 2026-05-14 04:04:11 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.128 |  |
| 2026-05-14 04:04:24 | Rathnapura (Kalu Ganga) | 4.91 | 🟢 Normal | -0.144 |  |
| 2026-05-14 04:01:00 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -1.123 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)