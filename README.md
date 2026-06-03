# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--03_11:21:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **169,261 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 11:21:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-06-03 11:13:29 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:10:03 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.033 |  |
| 2026-06-03 11:08:02 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-06-03 11:07:58 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-03 11:07:52 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:07:33 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:06:33 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:06:09 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-06-03 11:05:37 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:05:20 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:05:19 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.048 |  |
| 2026-06-03 11:04:18 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.185 |  |
| 2026-06-03 11:04:17 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |
| 2026-06-03 11:03:52 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:03:26 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:03:25 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:03:16 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-06-03 11:03:06 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:02:47 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-06-03 11:02:37 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:02:29 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:02:19 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:02:11 | Glencourse (Kelani Ganga) | 9.77 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:02:07 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-06-03 11:01:54 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:01:42 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:01:42 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.029 |  |
| 2026-06-03 11:01:39 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 11:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 11:01:24 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:01:22 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-03 11:01:20 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:01:18 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:01:17 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 11:00:54 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:00:43 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 10:40:55 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-03 11:01:22 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-06-03 11:01:17 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 11:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 11:00:43 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 11:01:39 | Dunamale (Aththanagalu Oya) | 1.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-03 11:07:58 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-03 11:01:20 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:01:24 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:07:52 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:01:18 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-03 10:03:08 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:13:29 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:06:33 | Galgamuwa (Mee Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:03:25 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:02:37 | Deraniyagala (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:03:52 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:03:06 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-06-03 10:03:13 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:02:11 | Glencourse (Kelani Ganga) | 9.77 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:05:20 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:02:29 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:01:42 | Katharagama (Menik Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:05:37 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:00:54 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:07:33 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:03:26 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:02:19 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:01:54 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-03 11:06:09 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-06-03 11:02:07 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-06-03 11:21:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.89 | 🟢 Normal | -0.010 |  |
| 2026-06-03 11:08:02 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-06-03 11:03:16 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-06-03 11:04:17 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.020 |  |
| 2026-06-03 11:02:47 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-06-03 11:01:42 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.029 |  |
| 2026-06-03 11:10:03 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.033 |  |
| 2026-06-03 11:05:19 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.048 |  |
| 2026-06-03 11:04:18 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.185 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)