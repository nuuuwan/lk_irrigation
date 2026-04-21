# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_22:06:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,428 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 22:06:51 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-04-21 22:06:18 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-21 22:06:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.021 |  |
| 2026-04-21 22:05:32 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.093 |  |
| 2026-04-21 22:05:12 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.062 |  |
| 2026-04-21 22:05:01 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.100 |  |
| 2026-04-21 22:04:38 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-21 22:04:06 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-21 22:03:22 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 22:03:16 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.285 |  |
| 2026-04-21 22:03:10 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:02:57 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-21 22:02:50 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.050 |  |
| 2026-04-21 22:02:45 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:02:24 | Thanamalwila (Kirindi Oya) | 2.86 | 🟢 Normal | 0.523 | 🔺 Rising |
| 2026-04-21 22:01:53 | Moraketiya (Walawe Ganga) | 1.48 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2026-04-21 22:01:45 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.053 |  |
| 2026-04-21 22:01:43 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:01:28 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | -0.032 |  |
| 2026-04-21 22:01:27 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:01:27 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-21 22:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-04-21 22:01:21 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.021 |  |
| 2026-04-21 22:01:15 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:01:13 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:01:08 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-21 22:00:14 | Kuda Oya (Kirindi Oya) | 3.45 | 🟢 Normal | -0.154 |  |
| 2026-04-21 22:00:07 | Wellawaya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.110 |  |
| 2026-04-21 21:27:05 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-21 21:16:51 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 22:02:24 | Thanamalwila (Kirindi Oya) | 2.86 | 🟢 Normal | 0.523 | 🔺 Rising |
| 2026-04-21 22:01:53 | Moraketiya (Walawe Ganga) | 1.48 | 🟢 Normal | 0.349 | 🔺 Rising |
| 2026-04-21 22:01:27 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-21 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-21 22:06:18 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-21 22:02:57 | Rathnapura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-21 21:06:13 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-21 18:03:15 | Galgamuwa (Mee Oya) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-21 21:27:05 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-21 22:01:08 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-21 22:04:06 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-21 22:04:38 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-21 21:01:34 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 22:03:22 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 22:01:43 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:01:27 | Horowpothana (Yan Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:01:13 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:03:10 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:02:45 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:01:15 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:01:44 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-21 21:06:56 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:06:51 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-04-21 22:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-04-21 22:06:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.021 |  |
| 2026-04-21 22:01:21 | Magura (Kalu Ganga) | 1.35 | 🟢 Normal | -0.021 |  |
| 2026-04-21 22:01:28 | Glencourse (Kelani Ganga) | 9.02 | 🟢 Normal | -0.032 |  |
| 2026-04-21 21:10:37 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.042 |  |
| 2026-04-21 21:11:08 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | -0.045 |  |
| 2026-04-21 21:03:48 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.049 |  |
| 2026-04-21 22:02:50 | Badalgama (Maha Oya) | 2.50 | 🟢 Normal | -0.050 |  |
| 2026-04-21 22:01:45 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.053 |  |
| 2026-04-21 22:05:12 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.062 |  |
| 2026-04-21 22:05:32 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.093 |  |
| 2026-04-21 22:05:01 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | -0.100 |  |
| 2026-04-21 22:00:07 | Wellawaya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.110 |  |
| 2026-04-21 21:07:22 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | -0.125 |  |
| 2026-04-21 22:00:14 | Kuda Oya (Kirindi Oya) | 3.45 | 🟢 Normal | -0.154 |  |
| 2026-04-21 22:03:16 | Kithulgala (Kelani Ganga) | 1.28 | 🟢 Normal | -0.285 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)