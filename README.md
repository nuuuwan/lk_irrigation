# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_12:05:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **127,497 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 12:05:34 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:04:59 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-04-17 12:04:28 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-17 12:04:15 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:04:08 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-04-17 12:04:04 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.020 |  |
| 2026-04-17 12:04:03 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:03:59 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:03:51 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-04-17 12:03:25 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:03:19 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:02:58 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.060 |  |
| 2026-04-17 12:02:54 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-17 12:02:37 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-04-17 12:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-04-17 12:02:28 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:02:14 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.021 |  |
| 2026-04-17 12:02:14 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | -0.060 |  |
| 2026-04-17 12:02:10 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.020 |  |
| 2026-04-17 12:02:10 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | -0.031 |  |
| 2026-04-17 12:02:09 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-04-17 12:01:50 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:01:30 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-17 12:01:27 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:01:19 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:01:17 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:01:16 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:01:09 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:01:04 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:00:49 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:00:47 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.020 |  |
| 2026-04-17 12:00:36 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:00:36 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.032 |  |
| 2026-04-17 12:00:29 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:17:58 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:17:06 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:14:37 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-04-17 11:12:47 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.134 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 12:02:09 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-04-17 11:12:47 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-04-17 12:04:28 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-17 12:02:54 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-17 12:01:50 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:01:09 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:01:17 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:01:27 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:01:04 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-17 11:17:58 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:03:19 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:04:03 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:03:59 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:00:29 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:03:25 | Dunamale (Aththanagalu Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:00:49 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:01:19 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:04:15 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:00:36 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:02:28 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:01:16 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:05:34 | Thalgahagoda (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-17 12:01:30 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-04-17 12:04:59 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-04-17 12:02:10 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | -0.020 |  |
| 2026-04-17 12:03:51 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-04-17 12:00:47 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | -0.020 |  |
| 2026-04-17 11:14:37 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | -0.020 |  |
| 2026-04-17 12:04:08 | Rathnapura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-04-17 12:02:37 | Giriulla (Maha Oya) | 0.96 | 🟢 Normal | -0.020 |  |
| 2026-04-17 12:04:04 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.020 |  |
| 2026-04-17 11:05:53 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-04-17 12:02:14 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | -0.021 |  |
| 2026-04-17 12:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-04-17 12:02:10 | Glencourse (Kelani Ganga) | 8.72 | 🟢 Normal | -0.031 |  |
| 2026-04-17 12:00:36 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.032 |  |
| 2026-04-17 12:02:14 | Thanamalwila (Kirindi Oya) | 0.73 | 🟢 Normal | -0.060 |  |
| 2026-04-17 12:02:58 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)