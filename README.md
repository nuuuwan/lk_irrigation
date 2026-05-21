# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--21_14:47:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **157,923 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 14:47:54 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:13:39 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:10:38 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.027 |  |
| 2026-05-21 14:10:02 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:09:54 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-05-21 14:09:53 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:09:10 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-21 14:06:59 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-05-21 14:06:48 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-05-21 14:06:42 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:06:15 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:05:52 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-21 14:05:15 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:05:13 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-21 14:04:51 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:04:44 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-05-21 14:04:28 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-05-21 14:03:50 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:03:34 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-05-21 14:03:34 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.030 |  |
| 2026-05-21 14:03:24 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.040 |  |
| 2026-05-21 14:03:19 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:03:19 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:02:49 | Glencourse (Kelani Ganga) | 9.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-21 14:02:47 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:02:47 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-21 14:02:45 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-05-21 14:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.040 |  |
| 2026-05-21 14:02:30 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-21 14:09:54 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-05-21 14:02:47 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-21 14:05:52 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-21 14:09:10 | Rathnapura (Kalu Ganga) | 1.59 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-21 14:02:49 | Glencourse (Kelani Ganga) | 9.79 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-21 14:02:11 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-21 14:02:08 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:00:14 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:03:19 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:03:19 | Nawalapitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:09:53 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:01:01 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:03:50 | Galgamuwa (Mee Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:02:30 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:02:47 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:02:08 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:47:54 | Panadugama (Nilwala Ganga) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:01:52 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:05:15 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:02:12 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:13:39 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:06:15 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:10:02 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:01:46 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:06:42 | Thawalama (Gin Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:04:51 | Thanamalwila (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-05-21 14:06:48 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-05-21 14:06:59 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-05-21 14:04:44 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-05-21 14:03:34 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-05-21 14:05:13 | Peradeniya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-21 14:00:19 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.010 |  |
| 2026-05-21 14:02:45 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-05-21 14:04:28 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-05-21 14:01:18 | Thanthirimale (Malwathu Oya) | 1.75 | 🟢 Normal | -0.020 |  |
| 2026-05-21 14:10:38 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.027 |  |
| 2026-05-21 14:03:34 | Ellagawa (Kalu Ganga) | 5.52 | 🟢 Normal | -0.030 |  |
| 2026-05-21 14:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.04 | 🟢 Normal | -0.040 |  |
| 2026-05-21 14:03:24 | Hanwella (Kelani Ganga) | 1.77 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)