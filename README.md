# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_17:16:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,884 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 17:16:00 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.037 |  |
| 2026-05-30 17:09:25 | Panadugama (Nilwala Ganga) | 3.31 | 🟢 Normal | -0.020 |  |
| 2026-05-30 17:07:55 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:07:29 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-30 17:06:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | -0.028 |  |
| 2026-05-30 17:06:31 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-05-30 17:06:29 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-05-30 17:05:57 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:05:57 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:05:36 | Baddegama (Gin Ganga) | 2.71 | 🟢 Normal | -0.019 |  |
| 2026-05-30 17:05:30 | Rathnapura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.051 |  |
| 2026-05-30 17:05:13 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.110 |  |
| 2026-05-30 17:04:57 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.028 |  |
| 2026-05-30 17:04:56 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.005 |  |
| 2026-05-30 17:04:48 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:04:33 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | -0.029 |  |
| 2026-05-30 17:04:22 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | -0.088 |  |
| 2026-05-30 17:04:20 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-05-30 17:03:42 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-30 17:03:13 | Hanwella (Kelani Ganga) | 2.75 | 🟢 Normal | -0.051 |  |
| 2026-05-30 17:03:07 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:02:52 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:02:41 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-30 17:02:40 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:02:31 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.032 |  |
| 2026-05-30 17:02:30 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-05-30 17:02:13 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-05-30 17:01:53 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:01:41 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.030 |  |
| 2026-05-30 17:01:36 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:01:29 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:01:14 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.075 |  |
| 2026-05-30 17:01:11 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.021 |  |
| 2026-05-30 17:00:54 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:00:36 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:00:04 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 17:06:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | -0.028 |  |
| 2026-05-30 17:03:42 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-05-30 17:02:41 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-30 17:07:29 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-30 15:59:44 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-30 17:07:55 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:05:57 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:03:07 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:01:36 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:01:29 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:01:53 | Giriulla (Maha Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:00:54 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:04:48 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:02:52 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:00:04 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:05:57 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:00:36 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:02:40 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 17:04:56 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.005 |  |
| 2026-05-30 16:29:03 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.008 |  |
| 2026-05-30 17:06:29 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-05-30 17:02:13 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-05-30 17:02:30 | Dunamale (Aththanagalu Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-05-30 17:06:31 | Badalgama (Maha Oya) | 2.31 | 🟢 Normal | -0.010 |  |
| 2026-05-30 16:00:43 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-05-30 17:05:36 | Baddegama (Gin Ganga) | 2.71 | 🟢 Normal | -0.019 |  |
| 2026-05-30 17:04:20 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-05-30 17:09:25 | Panadugama (Nilwala Ganga) | 3.31 | 🟢 Normal | -0.020 |  |
| 2026-05-30 17:01:11 | Peradeniya (Mahaweli Ganga) | 1.60 | 🟢 Normal | -0.021 |  |
| 2026-05-30 17:04:57 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.028 |  |
| 2026-05-30 17:04:33 | Putupaula (Kalu Ganga) | 2.50 | 🟢 Normal | -0.029 |  |
| 2026-05-30 17:01:41 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | -0.030 |  |
| 2026-05-30 17:02:31 | Norwood (Kelani Ganga) | 0.55 | 🟢 Normal | -0.032 |  |
| 2026-05-30 17:16:00 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.037 |  |
| 2026-05-30 17:05:30 | Rathnapura (Kalu Ganga) | 2.32 | 🟢 Normal | -0.051 |  |
| 2026-05-30 17:03:13 | Hanwella (Kelani Ganga) | 2.75 | 🟢 Normal | -0.051 |  |
| 2026-05-30 17:01:14 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.075 |  |
| 2026-05-30 17:04:22 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | -0.088 |  |
| 2026-05-30 17:05:13 | Glencourse (Kelani Ganga) | 10.35 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)