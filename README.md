# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--06_02:14:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **198,435 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 02:14:01 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -1.800 |  |
| 2026-07-06 02:13:41 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -1.800 |  |
| 2026-07-06 02:13:25 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -1.800 |  |
| 2026-07-06 02:13:21 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:11:20 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:10:59 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.018 |  |
| 2026-07-06 02:10:52 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | -0.028 |  |
| 2026-07-06 02:09:25 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:08:46 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:08:41 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.028 |  |
| 2026-07-06 02:08:35 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-07-06 02:07:55 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:07:38 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:07:27 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:06:50 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.028 |  |
| 2026-07-06 02:06:04 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.012 |  |
| 2026-07-06 02:05:56 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.010 |  |
| 2026-07-06 02:05:47 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -1.333 |  |
| 2026-07-06 02:05:45 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.322 |  |
| 2026-07-06 02:05:20 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | -1.333 |  |
| 2026-07-06 02:04:28 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:04:12 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:04:11 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:03:59 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:03:07 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:02:37 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:02:26 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:02:15 | Thalgahagoda (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.062 |  |
| 2026-07-06 02:02:13 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-07-06 02:02:12 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | -0.020 |  |
| 2026-07-06 02:02:05 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.020 |  |
| 2026-07-06 02:01:54 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-07-06 02:01:45 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:01:30 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:01:28 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:00:57 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:00:41 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-06 00:16:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.161 | 🔺 Rising |
| 2026-07-06 02:08:35 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-07-06 01:05:13 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-06 00:00:14 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:01:28 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:03:59 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:03:07 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:00:41 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:05:41 | Galgamuwa (Mee Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:07:27 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:02:37 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:11:20 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:02:54 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:01:45 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:07:55 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:02:26 | Dunamale (Aththanagalu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:08:39 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:08:46 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:04:12 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-05 18:03:25 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:04:28 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:13:21 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-07-06 01:13:10 | Thanamalwila (Kirindi Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-06 02:01:54 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-07-05 18:00:08 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-07-06 02:05:56 | Glencourse (Kelani Ganga) | 10.24 | 🟢 Normal | -0.010 |  |
| 2026-07-06 02:06:04 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.012 |  |
| 2026-07-06 02:10:59 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.018 |  |
| 2026-07-06 02:02:13 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.020 |  |
| 2026-07-06 02:02:12 | Ellagawa (Kalu Ganga) | 5.06 | 🟢 Normal | -0.020 |  |
| 2026-07-06 02:02:05 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.020 |  |
| 2026-07-06 02:06:50 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | -0.028 |  |
| 2026-07-06 02:10:52 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | -0.028 |  |
| 2026-07-06 02:08:41 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.028 |  |
| 2026-07-06 02:02:15 | Thalgahagoda (Nilwala Ganga) | 0.04 | 🟢 Normal | -0.062 |  |
| 2026-07-06 02:05:45 | Peradeniya (Mahaweli Ganga) | 2.36 | 🟢 Normal | -0.322 |  |
| 2026-07-06 01:07:41 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | -0.667 |  |
| 2026-07-06 02:05:47 | Nawalapitiya (Mahaweli Ganga) | 1.42 | 🟢 Normal | -1.333 |  |
| 2026-07-06 02:14:01 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -1.800 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)