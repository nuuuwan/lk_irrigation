# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--19_04:45:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **76,957 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 04:45:00 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:27:36 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.027 |  |
| 2026-02-19 04:24:19 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:16:31 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-02-19 04:15:04 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.058 |  |
| 2026-02-19 04:11:33 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:08:47 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.035 |  |
| 2026-02-19 04:08:08 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-02-19 04:06:18 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:05:48 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:05:36 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-19 04:04:41 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.021 |  |
| 2026-02-19 04:04:08 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 04:03:50 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.003 |  |
| 2026-02-19 04:03:44 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-19 04:03:42 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-02-19 04:03:33 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-02-19 04:03:26 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-19 04:03:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-19 04:03:10 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:02:56 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:02:40 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:02:28 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:02:09 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:02:07 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:01:56 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:00:54 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:00:35 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.072 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-19 04:00:35 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-02-19 04:03:26 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-19 04:03:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-02-19 04:05:36 | Rathnapura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-19 04:04:08 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-19 04:00:54 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:45:00 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:02:40 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:02:56 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-18 18:04:47 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-19 00:03:53 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:02:28 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:06:18 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:01:56 | Ellagawa (Kalu Ganga) | 3.82 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:11:33 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:05:48 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:02:07 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-19 03:00:49 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-18 18:01:21 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:24:19 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:03:10 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:02:09 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-19 04:03:50 | Magura (Kalu Ganga) | 0.74 | 🟢 Normal | -0.003 |  |
| 2026-02-19 03:09:59 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.009 |  |
| 2026-02-19 04:08:08 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-02-18 18:01:50 | Weraganthota (Mahaweli Ganga) | -1.79 | 🟢 Normal | -0.010 |  |
| 2026-02-19 04:03:44 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-02-19 04:16:31 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.011 |  |
| 2026-02-19 04:03:33 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-02-19 04:03:42 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-02-19 04:04:41 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.021 |  |
| 2026-02-19 03:00:18 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | -0.021 |  |
| 2026-02-19 04:27:36 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.027 |  |
| 2026-02-19 03:02:35 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | -0.028 |  |
| 2026-02-19 04:08:47 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.035 |  |
| 2026-02-19 04:15:04 | Manampitiya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.058 |  |
| 2026-02-19 02:06:16 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | -0.060 |  |
| 2026-02-19 03:01:13 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)