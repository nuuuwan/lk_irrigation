# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--09_12:19:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **68,343 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 12:19:18 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | -0.016 |  |
| 2026-02-09 12:14:19 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-09 12:09:05 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.030 |  |
| 2026-02-09 12:07:33 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:06:49 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:06:37 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:06:13 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:06:03 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:05:47 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.031 |  |
| 2026-02-09 12:05:45 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.022 |  |
| 2026-02-09 12:05:30 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:05:16 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:05:16 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-09 12:04:52 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-09 12:04:35 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.010 |  |
| 2026-02-09 12:03:43 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.083 |  |
| 2026-02-09 12:03:35 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:03:10 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:03:05 | Putupaula (Kalu Ganga) | 0.27 | 🟢 Normal | -0.068 |  |
| 2026-02-09 12:03:00 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:03:00 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-09 12:02:51 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:02:50 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:02:48 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:02:46 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-02-09 12:02:43 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-09 12:02:29 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-02-09 12:02:18 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.030 |  |
| 2026-02-09 12:02:14 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:02:13 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:02:11 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-09 12:01:52 | Peradeniya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.075 |  |
| 2026-02-09 12:01:51 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:01:49 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:01:47 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.031 |  |
| 2026-02-09 12:01:36 | Manampitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-09 12:01:33 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:00:49 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-09 12:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-09 12:02:43 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-09 12:01:36 | Manampitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-09 12:02:11 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-09 12:05:16 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-09 12:04:52 | Moragaswewa (Deduru Oya) | 0.20 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-09 12:14:19 | Padiyathalawa (Maduru Oya) | 0.81 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-09 12:01:49 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:02:51 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:00:12 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:01:51 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:02:50 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:05:16 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:06:49 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:03:00 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:01:33 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:05:30 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:02:48 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:02:14 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:03:00 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:07:33 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:02:13 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:03:10 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:00:49 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:06:37 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:06:03 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:06:13 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-09 12:04:35 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.010 |  |
| 2026-02-09 12:19:18 | Horowpothana (Yan Oya) | 1.59 | 🟢 Normal | -0.016 |  |
| 2026-02-09 12:02:29 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.020 |  |
| 2026-02-09 12:02:46 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-02-09 12:05:45 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.022 |  |
| 2026-02-09 12:09:05 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.030 |  |
| 2026-02-09 12:02:18 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.030 |  |
| 2026-02-09 12:05:47 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | -0.031 |  |
| 2026-02-09 12:01:47 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.031 |  |
| 2026-02-09 12:03:05 | Putupaula (Kalu Ganga) | 0.27 | 🟢 Normal | -0.068 |  |
| 2026-02-09 12:01:52 | Peradeniya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.075 |  |
| 2026-02-09 12:03:43 | Glencourse (Kelani Ganga) | 8.28 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)