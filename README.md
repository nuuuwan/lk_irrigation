# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_00:08:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,122 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 00:08:21 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:08:18 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:08:03 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:07:09 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.068 |  |
| 2026-01-12 00:06:59 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-12 00:06:47 | Magura (Kalu Ganga) | 0.11 | 🟢 Normal | -0.959 |  |
| 2026-01-12 00:06:40 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:06:33 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | 0.502 | 🔺 Rising |
| 2026-01-12 00:06:18 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:05:58 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:05:51 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.111 |  |
| 2026-01-12 00:05:28 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:04:53 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.005 |  |
| 2026-01-12 00:04:50 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.058 |  |
| 2026-01-12 00:04:19 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-01-12 00:04:16 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:04:00 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-12 00:03:28 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.066 |  |
| 2026-01-12 00:03:22 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-12 00:03:08 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:02:48 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:02:46 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 00:02:38 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:02:33 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.021 |  |
| 2026-01-12 00:02:21 | Siyambalanduwa (Heda Oya) | 1.25 | 🟢 Normal | -0.049 |  |
| 2026-01-12 00:02:20 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:02:07 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 00:01:53 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:01:44 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:01:41 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:01:39 | Manampitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-12 00:01:14 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:01:12 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 00:00:42 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:00:08 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-01-11 23:45:21 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.066 |  |
| 2026-01-11 23:16:52 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:16:29 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:14:07 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:13:58 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.068 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 00:06:33 | Glencourse (Kelani Ganga) | 9.61 | 🟢 Normal | 0.502 | 🔺 Rising |
| 2026-01-12 00:03:22 | Dunamale (Aththanagalu Oya) | 0.88 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-01-11 18:00:33 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-12 00:04:00 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-12 00:06:59 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-11 22:03:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.46 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 00:01:39 | Manampitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-01-12 00:02:46 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 00:02:07 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 00:01:12 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 00:02:20 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:01:30 | Weraganthota (Mahaweli Ganga) | -1.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:08:21 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:02:38 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:01:44 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:00:42 | Yaka Wewa (Ma Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-11 18:02:19 | Galgamuwa (Mee Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:08:18 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:03:25 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:01:53 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-11 23:03:29 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:06:40 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:06:18 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:02:48 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:05:28 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:01:41 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:04:16 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:03:08 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:05:58 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-12 00:04:53 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | -0.005 |  |
| 2026-01-12 00:04:19 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.020 |  |
| 2026-01-12 00:00:08 | Horowpothana (Yan Oya) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-01-12 00:02:33 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.021 |  |
| 2026-01-12 00:02:21 | Siyambalanduwa (Heda Oya) | 1.25 | 🟢 Normal | -0.049 |  |
| 2026-01-12 00:04:50 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.058 |  |
| 2026-01-12 00:03:28 | Rathnapura (Kalu Ganga) | 0.71 | 🟢 Normal | -0.066 |  |
| 2026-01-12 00:07:09 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | -0.068 |  |
| 2026-01-12 00:05:51 | Putupaula (Kalu Ganga) | 0.32 | 🟢 Normal | -0.111 |  |
| 2026-01-12 00:06:47 | Magura (Kalu Ganga) | 0.11 | 🟢 Normal | -0.959 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)