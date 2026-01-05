# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--05_15:13:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **37,407 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 15:13:24 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.011 |  |
| 2026-01-05 15:13:12 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-05 15:11:26 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:10:57 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:08:56 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 15:08:48 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.092 |  |
| 2026-01-05 15:08:10 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-01-05 15:08:03 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-05 15:06:36 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:06:21 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 15:05:44 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-05 15:05:16 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:04:31 | Padiyathalawa (Maduru Oya) | 1.33 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-01-05 15:04:21 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-05 15:04:17 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-05 15:04:08 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:03:54 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:03:49 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:03:17 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:03:10 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:03:09 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-01-05 15:03:00 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.030 |  |
| 2026-01-05 15:02:45 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:02:41 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 15:02:40 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:02:37 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:02:16 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:02:16 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-01-05 15:02:13 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:01:52 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.010 |  |
| 2026-01-05 15:01:45 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-01-05 15:01:30 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:01:10 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-01-05 15:00:57 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-01-05 15:00:54 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:00:19 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:00:10 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-01-05 15:00:06 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-05 15:01:45 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.211 | 🔺 Rising |
| 2026-01-05 15:04:31 | Padiyathalawa (Maduru Oya) | 1.33 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-01-05 15:08:10 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-01-05 15:08:03 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-05 15:04:21 | Yaka Wewa (Ma Oya) | 0.85 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-05 15:04:17 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-05 15:06:21 | Glencourse (Kelani Ganga) | 8.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 15:02:41 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 15:08:56 | Manampitiya (Mahaweli Ganga) | 1.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-05 15:05:44 | Weraganthota (Mahaweli Ganga) | -1.50 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-05 15:02:16 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:00:06 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:03:00 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:02:45 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:03:10 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:03:54 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:00:54 | Siyambalanduwa (Heda Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:00:19 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:02:40 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:05:16 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:02:37 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:03:49 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:06:36 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:01:30 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:11:26 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:10:57 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:04:08 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:02:13 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-05 15:03:09 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-01-05 15:01:52 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.010 |  |
| 2026-01-05 15:01:10 | Moragaswewa (Deduru Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-01-05 15:13:12 | Magura (Kalu Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-01-05 15:00:57 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-01-05 15:00:10 | Baddegama (Gin Ganga) | 1.19 | 🟢 Normal | -0.011 |  |
| 2026-01-05 15:13:24 | Panadugama (Nilwala Ganga) | 2.39 | 🟢 Normal | -0.011 |  |
| 2026-01-05 15:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.030 |  |
| 2026-01-05 15:02:16 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | -0.030 |  |
| 2026-01-05 15:08:48 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.092 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)