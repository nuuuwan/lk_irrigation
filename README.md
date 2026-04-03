# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--03_10:05:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **114,912 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 10:05:13 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:04:54 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:04:50 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-03 10:04:39 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.030 |  |
| 2026-04-03 10:04:14 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-03 10:04:06 | Kithulgala (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:03:58 | Kithulgala (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:03:46 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:03:38 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:03:35 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-04-03 10:03:01 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | -0.105 |  |
| 2026-04-03 10:02:57 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-04-03 10:02:49 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:02:46 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:02:23 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 10:02:08 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:02:05 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:01:49 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:01:09 | Thanthirimale (Malwathu Oya) | 2.78 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-04-03 10:01:02 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 10:00:27 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-04-03 10:00:17 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-03 09:53:23 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | -0.012 |  |
| 2026-04-03 09:47:17 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-03 09:18:51 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 09:14:16 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.029 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-03 10:01:09 | Thanthirimale (Malwathu Oya) | 2.78 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-04-03 10:04:50 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-03 09:06:57 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-04-03 08:12:13 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-03 09:14:16 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-03 09:02:08 | Ellagawa (Kalu Ganga) | 3.80 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-03 10:04:14 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-03 09:02:31 | Peradeniya (Mahaweli Ganga) | 1.17 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-03 10:02:23 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 10:01:02 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-03 10:04:06 | Kithulgala (Kelani Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:03:46 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-03 09:03:56 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:02:23 | Nawalapitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:01:49 | Yaka Wewa (Ma Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-03 09:47:17 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:02:49 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-03 09:09:03 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-03 09:06:34 | Panadugama (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:03:35 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:00:17 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:05:13 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:03:38 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:02:46 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:04:54 | Badalgama (Maha Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:02:05 | Kuda Oya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:02:08 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-03 10:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-04-03 09:53:23 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | -0.012 |  |
| 2026-04-03 10:02:57 | Giriulla (Maha Oya) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-04-03 10:04:39 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.030 |  |
| 2026-04-03 10:00:27 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.030 |  |
| 2026-04-03 09:06:37 | Urawa (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.035 |  |
| 2026-04-03 09:03:14 | Rathnapura (Kalu Ganga) | 1.20 | 🟢 Normal | -0.037 |  |
| 2026-04-03 09:00:43 | Thawalama (Gin Ganga) | 1.13 | 🟢 Normal | -0.042 |  |
| 2026-04-03 09:06:44 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.054 |  |
| 2026-04-03 09:02:49 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.083 |  |
| 2026-04-03 10:03:01 | Weraganthota (Mahaweli Ganga) | -1.95 | 🟢 Normal | -0.105 |  |
| 2026-04-03 09:01:25 | Putupaula (Kalu Ganga) | 0.25 | 🟢 Normal | -0.173 |  |

## River Water Level Charts by Station

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)