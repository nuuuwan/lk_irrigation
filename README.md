# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--05_13:23:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **171,136 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 13:23:50 | Dunamale (Aththanagalu Oya) | 2.59 | 🟢 Normal | -0.007 |  |
| 2026-06-05 13:15:24 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:15:13 | Panadugama (Nilwala Ganga) | 3.02 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-06-05 13:12:14 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -12.000 |  |
| 2026-06-05 13:12:11 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -12.000 |  |
| 2026-06-05 13:10:12 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-05 13:07:43 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.018 |  |
| 2026-06-05 13:06:29 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:06:19 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.018 |  |
| 2026-06-05 13:06:19 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-05 13:06:11 | Rathnapura (Kalu Ganga) | 3.23 | 🟢 Normal | -0.063 |  |
| 2026-06-05 13:06:09 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.019 |  |
| 2026-06-05 13:05:50 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:05:25 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-05 13:04:21 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.030 |  |
| 2026-06-05 13:04:05 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.072 |  |
| 2026-06-05 13:03:59 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:03:40 | Glencourse (Kelani Ganga) | 11.46 | 🟢 Normal | -0.042 |  |
| 2026-06-05 13:03:39 | Ellagawa (Kalu Ganga) | 7.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-05 13:03:33 | Hanwella (Kelani Ganga) | 3.45 | 🟢 Normal | -0.030 |  |
| 2026-06-05 13:03:17 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-05 13:02:53 | Putupaula (Kalu Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 13:02:47 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:02:45 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-06-05 13:02:36 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:02:32 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:02:28 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:02:27 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.29 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:01:52 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.092 |  |
| 2026-06-05 13:01:48 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-05 13:01:46 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:01:26 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-06-05 13:01:12 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:01:01 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-05 13:00:57 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-06-05 13:00:45 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:00:25 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-05 13:06:19 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-06-05 13:15:13 | Panadugama (Nilwala Ganga) | 3.02 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-06-05 13:03:17 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-06-05 13:01:01 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-05 13:05:25 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-05 13:03:39 | Ellagawa (Kalu Ganga) | 7.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-05 13:01:48 | Moragaswewa (Deduru Oya) | 0.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-05 13:10:12 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-05 13:02:53 | Putupaula (Kalu Ganga) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-05 13:02:28 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:00:25 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:01:46 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:02:32 | Giriulla (Maha Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:00:45 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:02:58 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:06:29 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-06-05 12:06:06 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:03:59 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:02:36 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:02:27 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:01:12 | Thanthirimale (Malwathu Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:15:24 | Urawa (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:05:50 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:02:47 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.29 | 🟢 Normal | 0.000 |  |
| 2026-06-05 13:23:50 | Dunamale (Aththanagalu Oya) | 2.59 | 🟢 Normal | -0.007 |  |
| 2026-06-05 13:01:26 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-06-05 13:00:57 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.011 |  |
| 2026-06-05 13:07:43 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.018 |  |
| 2026-06-05 13:06:19 | Peradeniya (Mahaweli Ganga) | 2.20 | 🟢 Normal | -0.018 |  |
| 2026-06-05 13:06:09 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.019 |  |
| 2026-06-05 13:02:45 | Nawalapitiya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.020 |  |
| 2026-06-05 13:03:33 | Hanwella (Kelani Ganga) | 3.45 | 🟢 Normal | -0.030 |  |
| 2026-06-05 13:04:21 | Thawalama (Gin Ganga) | 2.07 | 🟢 Normal | -0.030 |  |
| 2026-06-05 13:03:40 | Glencourse (Kelani Ganga) | 11.46 | 🟢 Normal | -0.042 |  |
| 2026-06-05 13:06:11 | Rathnapura (Kalu Ganga) | 3.23 | 🟢 Normal | -0.063 |  |
| 2026-06-05 13:04:05 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.072 |  |
| 2026-06-05 13:01:52 | Deraniyagala (Kelani Ganga) | 1.31 | 🟢 Normal | -0.092 |  |
| 2026-06-05 13:12:14 | Magura (Kalu Ganga) | 2.29 | 🟢 Normal | -12.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)