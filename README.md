# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_14:27:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,902 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 14:27:16 | Moragaswewa (Deduru Oya) | 0.89 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-14 14:16:52 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-14 14:16:35 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-14 14:11:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | -2.667 |  |
| 2026-04-14 14:10:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -2.667 |  |
| 2026-04-14 14:10:27 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:10:22 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:08:28 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:08:23 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-04-14 14:07:44 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:06:13 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.019 |  |
| 2026-04-14 14:04:36 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:04:28 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:03:57 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-14 14:03:48 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-04-14 14:03:47 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.050 |  |
| 2026-04-14 14:03:47 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-14 14:03:34 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-04-14 14:03:31 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:03:24 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-04-14 14:03:02 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-04-14 14:02:57 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | -0.011 |  |
| 2026-04-14 14:02:55 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-14 14:02:53 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:02:50 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-14 14:02:45 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:01:52 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | -0.031 |  |
| 2026-04-14 14:01:27 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:01:26 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:01:25 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-14 14:01:12 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-14 14:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:00:57 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | -0.034 |  |
| 2026-04-14 14:00:51 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:00:36 | Thanthirimale (Malwathu Oya) | 4.07 | 🟢 Normal | -0.050 |  |
| 2026-04-14 14:00:35 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-14 14:00:18 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-04-14 14:00:08 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:59:35 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 14:00:18 | Weraganthota (Mahaweli Ganga) | -2.83 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-04-14 14:03:34 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-04-14 14:16:52 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-04-14 14:27:16 | Moragaswewa (Deduru Oya) | 0.89 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-14 14:03:47 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-14 14:01:25 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-14 14:03:57 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-14 14:02:55 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-14 14:10:27 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:00:08 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:01:04 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:01:27 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:01:26 | Giriulla (Maha Oya) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:08:28 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:02:53 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-14 13:02:46 | Panadugama (Nilwala Ganga) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:03:31 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:04:28 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:07:44 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:02:45 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:00:51 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:04:36 | Thawalama (Gin Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:10:22 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-14 14:16:35 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-14 14:02:50 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-14 14:03:24 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-04-14 14:00:35 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-04-14 14:01:12 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-14 13:59:35 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-04-14 14:02:57 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | -0.011 |  |
| 2026-04-14 14:08:23 | Rathnapura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-04-14 14:06:13 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | -0.019 |  |
| 2026-04-14 14:03:48 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-04-14 14:03:02 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.021 |  |
| 2026-04-14 14:01:52 | Thanamalwila (Kirindi Oya) | 1.48 | 🟢 Normal | -0.031 |  |
| 2026-04-14 14:00:57 | Ellagawa (Kalu Ganga) | 4.43 | 🟢 Normal | -0.034 |  |
| 2026-04-14 14:03:47 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.050 |  |
| 2026-04-14 14:00:36 | Thanthirimale (Malwathu Oya) | 4.07 | 🟢 Normal | -0.050 |  |
| 2026-04-14 14:11:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | -2.667 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)