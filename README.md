# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_17:04:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,745 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 17:04:53 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-12 17:04:52 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.013 |  |
| 2026-01-12 17:03:41 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 17:03:19 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-12 17:03:19 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-12 17:03:13 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 17:03:02 | Hanwella (Kelani Ganga) | 1.06 | 🟢 Normal | -0.060 |  |
| 2026-01-12 17:02:58 | Yaka Wewa (Ma Oya) | 2.88 | 🟢 Normal | -0.438 |  |
| 2026-01-12 17:02:53 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.024 |  |
| 2026-01-12 17:02:52 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | 0.000 |  |
| 2026-01-12 17:02:16 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | -0.010 |  |
| 2026-01-12 17:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.030 |  |
| 2026-01-12 17:01:59 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 17:01:54 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-01-12 17:01:54 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-01-12 17:01:52 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-01-12 17:01:48 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-01-12 17:01:44 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.081 |  |
| 2026-01-12 17:01:14 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-12 17:01:05 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-12 17:00:32 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-12 17:00:21 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 16:58:33 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:23:16 | Horowpothana (Yan Oya) | 2.78 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-12 16:22:37 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:18:19 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.013 |  |
| 2026-01-12 16:16:22 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:16:15 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:14:29 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:13:53 | Baddegama (Gin Ganga) | 0.94 | 🟢 Normal | -0.024 |  |
| 2026-01-12 16:12:53 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-01-12 16:09:34 | Yaka Wewa (Ma Oya) | 3.27 | 🟢 Normal | -0.438 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 17:01:48 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.260 | 🔺 Rising |
| 2026-01-12 16:03:45 | Dunamale (Aththanagalu Oya) | 0.83 | 🟢 Normal | 0.180 | 🔺 Rising |
| 2026-01-12 17:01:52 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-01-12 16:23:16 | Horowpothana (Yan Oya) | 2.78 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-01-12 17:01:05 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-12 16:03:01 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-12 17:00:21 | Weraganthota (Mahaweli Ganga) | -1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-12 17:03:19 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:01:18 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 17:01:59 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 17:00:32 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-12 17:03:41 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:00:18 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-12 17:02:52 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | 0.000 |  |
| 2026-01-12 17:04:53 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-12 17:03:19 | Siyambalanduwa (Heda Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:02:45 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:03:33 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:00:27 | Manampitiya (Mahaweli Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:06:47 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-12 17:03:13 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:16:22 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:58:33 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 17:01:14 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:05:50 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-01-12 16:12:53 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-01-12 17:02:16 | Ellagawa (Kalu Ganga) | 4.12 | 🟢 Normal | -0.010 |  |
| 2026-01-12 16:03:06 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | -0.012 |  |
| 2026-01-12 17:04:52 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | -0.013 |  |
| 2026-01-12 17:01:54 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-01-12 17:02:53 | Baddegama (Gin Ganga) | 0.92 | 🟢 Normal | -0.024 |  |
| 2026-01-12 16:06:30 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.029 |  |
| 2026-01-12 17:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.73 | 🟢 Normal | -0.030 |  |
| 2026-01-12 17:01:54 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.030 |  |
| 2026-01-12 16:03:11 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.039 |  |
| 2026-01-12 17:03:02 | Hanwella (Kelani Ganga) | 1.06 | 🟢 Normal | -0.060 |  |
| 2026-01-12 17:01:44 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | -0.081 |  |
| 2026-01-12 16:07:28 | Peradeniya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -0.134 |  |
| 2026-01-12 17:02:58 | Yaka Wewa (Ma Oya) | 2.88 | 🟢 Normal | -0.438 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)