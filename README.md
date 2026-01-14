# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--15_00:10:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **45,781 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 00:10:47 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-15 00:10:35 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:10:04 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-01-15 00:08:52 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.379 |  |
| 2026-01-15 00:08:41 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -108.000 |  |
| 2026-01-15 00:08:40 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -108.000 |  |
| 2026-01-15 00:08:33 | Peradeniya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -0.034 |  |
| 2026-01-15 00:08:03 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:07:55 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | -0.041 |  |
| 2026-01-15 00:07:23 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-01-15 00:07:06 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-15 00:07:01 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:06:36 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:05:55 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:05:44 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:05:42 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | -0.379 |  |
| 2026-01-15 00:05:27 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:04:53 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-15 00:04:05 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:03:51 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:03:40 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:03:30 | Siyambalanduwa (Heda Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:03:01 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-01-15 00:02:51 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:02:42 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-15 00:02:37 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-01-15 00:02:34 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-15 00:02:21 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:02:18 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:02:17 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-01-15 00:01:47 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-01-15 00:01:30 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:01:28 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.319 | 🔺 Rising |
| 2026-01-15 00:01:18 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-14 23:16:09 | Peradeniya (Mahaweli Ganga) | 2.30 | 🟢 Normal | -0.034 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-15 00:01:28 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.319 | 🔺 Rising |
| 2026-01-14 21:11:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.70 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-14 23:11:33 | Panadugama (Nilwala Ganga) | 3.32 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-01-15 00:10:47 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-01-15 00:07:06 | Baddegama (Gin Ganga) | 1.34 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 18:00:19 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:03:40 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:01:30 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-14 18:02:43 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:10:35 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:02:21 | Ellagawa (Kalu Ganga) | 4.13 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:02:18 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:03:51 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:05:55 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:03:30 | Siyambalanduwa (Heda Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:06:36 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:02:51 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:07:01 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:05:27 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-01-14 23:03:38 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:05:44 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:01:18 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:08:03 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-15 00:10:04 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-01-15 00:07:23 | Yaka Wewa (Ma Oya) | 0.94 | 🟢 Normal | -0.009 |  |
| 2026-01-14 22:05:30 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-01-15 00:03:01 | Manampitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.010 |  |
| 2026-01-15 00:02:34 | Thawalama (Gin Ganga) | 1.21 | 🟢 Normal | -0.010 |  |
| 2026-01-15 00:02:42 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-01-15 00:04:53 | Hanwella (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-01-15 00:02:17 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-01-14 23:03:29 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.010 |  |
| 2026-01-15 00:01:47 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.011 |  |
| 2026-01-15 00:02:37 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-01-14 18:02:52 | Thanthirimale (Malwathu Oya) | 2.20 | 🟢 Normal | -0.020 |  |
| 2026-01-15 00:08:33 | Peradeniya (Mahaweli Ganga) | 2.27 | 🟢 Normal | -0.034 |  |
| 2026-01-15 00:07:55 | Horowpothana (Yan Oya) | 2.65 | 🟢 Normal | -0.041 |  |
| 2026-01-15 00:08:52 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.379 |  |
| 2026-01-15 00:08:41 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -108.000 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)