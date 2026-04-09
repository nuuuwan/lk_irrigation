# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--09_11:25:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **120,331 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 11:25:06 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-04-09 11:09:22 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-09 11:09:06 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-09 11:09:03 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:07:42 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:07:03 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-04-09 11:06:44 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:05:47 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.029 |  |
| 2026-04-09 11:05:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-04-09 11:05:18 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:05:09 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-04-09 11:04:33 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:04:19 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:04:18 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:03:55 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:03:23 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:03:21 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:03:15 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.058 |  |
| 2026-04-09 11:02:57 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-09 11:02:48 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.146 |  |
| 2026-04-09 11:02:46 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.040 |  |
| 2026-04-09 11:02:29 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.021 |  |
| 2026-04-09 11:02:21 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:02:20 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:02:09 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:02:03 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:02:01 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-09 11:01:57 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-04-09 11:01:54 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:01:52 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:01:51 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-09 11:01:41 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:01:30 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:01:10 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:01:06 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:00:54 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.021 |  |
| 2026-04-09 11:00:41 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:00:10 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-09 11:01:57 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-04-09 11:02:57 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-09 11:02:01 | Putupaula (Kalu Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-09 11:09:22 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-09 11:01:06 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:00:10 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:02:03 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:01:54 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:00:41 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:02:21 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:01:52 | Pitabeddara (Nilwala Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:04:18 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:03:21 | Hanwella (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:03:23 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:01:10 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:04:33 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:04:19 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:01:41 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:09:03 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:02:20 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:05:18 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:01:30 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:06:44 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:07:42 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:03:55 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-09 11:07:03 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-04-09 11:09:06 | Magura (Kalu Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-09 11:05:09 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | -0.010 |  |
| 2026-04-09 11:01:51 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-04-09 10:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-09 11:25:06 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-04-09 11:02:29 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.021 |  |
| 2026-04-09 11:00:54 | Manampitiya (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.021 |  |
| 2026-04-09 11:05:47 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.029 |  |
| 2026-04-09 11:05:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | -0.030 |  |
| 2026-04-09 11:02:46 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.040 |  |
| 2026-04-09 10:00:37 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | -0.048 |  |
| 2026-04-09 11:03:15 | Glencourse (Kelani Ganga) | 8.64 | 🟢 Normal | -0.058 |  |
| 2026-04-09 11:02:48 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)