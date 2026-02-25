# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--25_11:09:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **82,619 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 11:09:54 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-25 11:08:50 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.005 |  |
| 2026-02-25 11:07:28 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:06:50 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:06:38 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:05:31 | Dunamale (Aththanagalu Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-02-25 11:05:26 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:05:09 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.021 |  |
| 2026-02-25 11:04:52 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:04:35 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:04:11 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:04:10 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.029 |  |
| 2026-02-25 11:03:48 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 11:03:46 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.126 |  |
| 2026-02-25 11:03:39 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-25 11:03:37 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:03:16 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 11:03:12 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:02:54 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-02-25 11:02:47 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:02:41 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-02-25 11:02:34 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.346 | 🔺 Rising |
| 2026-02-25 11:02:32 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-25 11:02:08 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:02:02 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-02-25 11:02:02 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-25 11:01:59 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:01:58 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:01:56 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | -0.010 |  |
| 2026-02-25 11:01:47 | Weraganthota (Mahaweli Ganga) | 2.02 | 🟢 Normal | 4.144 | 🔺 Rising |
| 2026-02-25 11:01:34 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:01:20 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-02-25 11:00:56 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:00:51 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-25 10:46:02 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:21:58 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | -0.008 |  |
| 2026-02-25 10:18:50 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.078 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 11:01:47 | Weraganthota (Mahaweli Ganga) | 2.02 | 🟢 Normal | 4.144 | 🔺 Rising |
| 2026-02-25 11:02:34 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.346 | 🔺 Rising |
| 2026-02-25 10:18:50 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-02-25 11:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-25 11:00:51 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-25 11:03:39 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-25 11:03:48 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 11:03:16 | Deraniyagala (Kelani Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-25 11:09:54 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-25 11:07:28 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:00:56 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:01:21 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:01:59 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:03:12 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:03:37 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:04:11 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:01:34 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:02:32 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:02:47 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:04:52 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:04:35 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:03:53 | Manampitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-02-25 10:01:48 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:06:38 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:05:26 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:06:50 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:02:08 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 11:08:50 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.005 |  |
| 2026-02-25 10:21:58 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | -0.008 |  |
| 2026-02-25 11:05:31 | Dunamale (Aththanagalu Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-02-25 11:02:02 | Padiyathalawa (Maduru Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-02-25 11:02:41 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-02-25 11:02:02 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-02-25 11:02:54 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-02-25 11:01:56 | Ellagawa (Kalu Ganga) | 4.21 | 🟢 Normal | -0.010 |  |
| 2026-02-25 11:01:20 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-02-25 11:05:09 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | -0.021 |  |
| 2026-02-25 11:04:10 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.029 |  |
| 2026-02-25 11:03:46 | Putupaula (Kalu Ganga) | 0.31 | 🟢 Normal | -0.126 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)