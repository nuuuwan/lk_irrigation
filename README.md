# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--25_20:10:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **82,967 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 20:10:34 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 6.128 | 🔺 Rising |
| 2026-02-25 20:09:47 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | 6.128 | 🔺 Rising |
| 2026-02-25 20:07:58 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-25 20:07:21 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:06:24 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.093 |  |
| 2026-02-25 20:05:44 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:05:36 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:04:27 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.020 |  |
| 2026-02-25 20:03:58 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | -0.049 |  |
| 2026-02-25 20:03:39 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-25 20:03:38 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:03:25 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.023 |  |
| 2026-02-25 20:03:02 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:03:00 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.049 |  |
| 2026-02-25 20:02:48 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:02:47 | Dunamale (Aththanagalu Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:02:44 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-02-25 20:02:34 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:02:30 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:02:17 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:02:17 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.061 |  |
| 2026-02-25 20:02:12 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-25 20:02:10 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:02:05 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-02-25 20:01:53 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.011 |  |
| 2026-02-25 20:01:52 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:01:39 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-02-25 20:01:34 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-02-25 20:01:23 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.020 |  |
| 2026-02-25 20:01:19 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-02-25 20:01:16 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:01:14 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:01:04 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:00:26 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 19:37:10 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.006 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 20:10:34 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 6.128 | 🔺 Rising |
| 2026-02-25 20:03:39 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-02-25 20:07:58 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-25 18:00:27 | Weraganthota (Mahaweli Ganga) | -1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 20:02:48 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:03:02 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:00:26 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:03:25 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:03:38 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-02-25 18:04:22 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:05:36 | Magura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:01:14 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:01:52 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-25 19:03:20 | Panadugama (Nilwala Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:01:16 | Padiyathalawa (Maduru Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:01:04 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:02:30 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:02:47 | Dunamale (Aththanagalu Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:02:34 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:02:17 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:07:21 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:05:44 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-25 20:02:10 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-02-25 19:37:10 | Pitabeddara (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.006 |  |
| 2026-02-25 18:02:19 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-02-25 20:02:12 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-25 20:01:39 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-02-25 20:01:53 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | -0.011 |  |
| 2026-02-25 20:01:19 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.011 |  |
| 2026-02-25 20:01:34 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.020 |  |
| 2026-02-25 20:02:44 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-02-25 20:01:23 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | -0.020 |  |
| 2026-02-25 20:04:27 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.020 |  |
| 2026-02-25 20:03:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | -0.023 |  |
| 2026-02-25 20:02:05 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-02-25 20:03:58 | Glencourse (Kelani Ganga) | 8.37 | 🟢 Normal | -0.049 |  |
| 2026-02-25 20:03:00 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.049 |  |
| 2026-02-25 20:02:17 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.061 |  |
| 2026-02-25 20:06:24 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)