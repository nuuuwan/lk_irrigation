# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--22_13:13:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,001 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 13:13:14 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.005 |  |
| 2026-02-22 13:13:07 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.050 |  |
| 2026-02-22 13:10:27 | Pitabeddara (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.125 |  |
| 2026-02-22 13:09:09 | Thanamalwila (Kirindi Oya) | 1.61 | 🟢 Normal | -0.027 |  |
| 2026-02-22 13:08:38 | Magura (Kalu Ganga) | 3.11 | 🟢 Normal | -0.077 |  |
| 2026-02-22 13:08:37 | Badalgama (Maha Oya) | 3.16 | 🟢 Normal | -0.048 |  |
| 2026-02-22 13:07:37 | Putupaula (Kalu Ganga) | 1.42 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-22 13:06:57 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-02-22 13:06:57 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-02-22 13:06:17 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-02-22 13:06:13 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.095 |  |
| 2026-02-22 13:05:46 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | -0.096 |  |
| 2026-02-22 13:05:24 | Padiyathalawa (Maduru Oya) | 1.38 | 🟢 Normal | -0.018 |  |
| 2026-02-22 13:05:13 | Glencourse (Kelani Ganga) | 10.07 | 🟢 Normal | -0.129 |  |
| 2026-02-22 13:05:12 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-02-22 13:05:06 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -1.091 |  |
| 2026-02-22 13:05:01 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-22 13:04:46 | Rathnapura (Kalu Ganga) | 3.63 | 🟢 Normal | -0.141 |  |
| 2026-02-22 13:03:52 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-02-22 13:03:36 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-02-22 13:03:30 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-22 13:03:16 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-22 13:03:16 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-22 13:02:43 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | -0.120 |  |
| 2026-02-22 13:02:38 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.012 |  |
| 2026-02-22 13:02:37 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.011 |  |
| 2026-02-22 13:02:32 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | -0.213 |  |
| 2026-02-22 13:02:31 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.101 |  |
| 2026-02-22 13:02:28 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.041 |  |
| 2026-02-22 13:02:25 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-22 13:02:09 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 13:02:02 | Ellagawa (Kalu Ganga) | 4.78 | 🟢 Normal | -2.917 |  |
| 2026-02-22 13:01:55 | Manampitiya (Mahaweli Ganga) | 4.13 | 🟡 Alert | -0.118 |  |
| 2026-02-22 13:01:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.069 | 🔺 Rising |
| 2026-02-22 13:01:22 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-02-22 13:01:21 | Panadugama (Nilwala Ganga) | 4.19 | 🟢 Normal | -0.095 |  |
| 2026-02-22 13:00:39 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.031 |  |
| 2026-02-22 13:00:26 | Weraganthota (Mahaweli Ganga) | -1.27 | 🟢 Normal | -0.010 |  |
| 2026-02-22 13:00:10 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-22 13:01:42 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.069 | 🔺 Rising |
| 2026-02-22 13:01:55 | Manampitiya (Mahaweli Ganga) | 4.13 | 🟡 Alert | -0.118 |  |
| 2026-02-22 13:05:12 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-02-22 13:02:25 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-22 13:03:16 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-22 13:03:16 | Thaldena (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-22 13:07:37 | Putupaula (Kalu Ganga) | 1.42 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-22 13:02:09 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-22 13:06:57 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-02-22 13:03:30 | Siyambalanduwa (Heda Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-22 13:05:01 | Dunamale (Aththanagalu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-22 13:13:14 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.005 |  |
| 2026-02-22 13:06:57 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-02-22 13:00:26 | Weraganthota (Mahaweli Ganga) | -1.27 | 🟢 Normal | -0.010 |  |
| 2026-02-22 13:02:37 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | -0.011 |  |
| 2026-02-22 13:02:38 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | -0.012 |  |
| 2026-02-22 13:05:24 | Padiyathalawa (Maduru Oya) | 1.38 | 🟢 Normal | -0.018 |  |
| 2026-02-22 13:03:36 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-02-22 13:06:17 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.020 |  |
| 2026-02-22 13:00:10 | Nakkala (Kumbukkan Oya) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-02-22 13:01:22 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-02-22 13:03:52 | Norwood (Kelani Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-02-22 13:09:09 | Thanamalwila (Kirindi Oya) | 1.61 | 🟢 Normal | -0.027 |  |
| 2026-02-22 13:00:39 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | -0.031 |  |
| 2026-02-22 13:02:28 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.041 |  |
| 2026-02-22 13:08:37 | Badalgama (Maha Oya) | 3.16 | 🟢 Normal | -0.048 |  |
| 2026-02-22 13:13:07 | Urawa (Nilwala Ganga) | 0.60 | 🟢 Normal | -0.050 |  |
| 2026-02-22 13:08:38 | Magura (Kalu Ganga) | 3.11 | 🟢 Normal | -0.077 |  |
| 2026-02-22 13:06:13 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.095 |  |
| 2026-02-22 13:01:21 | Panadugama (Nilwala Ganga) | 4.19 | 🟢 Normal | -0.095 |  |
| 2026-02-22 13:05:46 | Giriulla (Maha Oya) | 1.70 | 🟢 Normal | -0.096 |  |
| 2026-02-22 13:02:31 | Deraniyagala (Kelani Ganga) | 0.41 | 🟢 Normal | -0.101 |  |
| 2026-02-22 13:02:43 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | -0.120 |  |
| 2026-02-22 13:10:27 | Pitabeddara (Nilwala Ganga) | 1.23 | 🟢 Normal | -0.125 |  |
| 2026-02-22 13:05:13 | Glencourse (Kelani Ganga) | 10.07 | 🟢 Normal | -0.129 |  |
| 2026-02-22 13:04:46 | Rathnapura (Kalu Ganga) | 3.63 | 🟢 Normal | -0.141 |  |
| 2026-02-22 13:02:32 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | -0.213 |  |
| 2026-02-22 13:05:06 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -1.091 |  |
| 2026-02-22 13:02:02 | Ellagawa (Kalu Ganga) | 4.78 | 🟢 Normal | -2.917 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)