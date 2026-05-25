# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--25_15:10:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **161,353 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 15:10:51 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-05-25 15:07:02 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.009 |  |
| 2026-05-25 15:06:07 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.044 |  |
| 2026-05-25 15:05:52 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:05:19 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-25 15:05:03 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:04:52 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:04:40 | Glencourse (Kelani Ganga) | 11.69 | 🟢 Normal | -0.107 |  |
| 2026-05-25 15:04:33 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:04:24 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:04:21 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-25 15:04:02 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-05-25 15:03:45 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.041 |  |
| 2026-05-25 15:03:41 | Putupaula (Kalu Ganga) | 2.86 | 🟢 Normal | -0.051 |  |
| 2026-05-25 15:03:30 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-25 15:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.27 | 🟡 Alert | -0.049 |  |
| 2026-05-25 15:03:27 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-25 15:03:17 | Hanwella (Kelani Ganga) | 4.60 | 🟢 Normal | -0.092 |  |
| 2026-05-25 15:03:17 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:03:04 | Deraniyagala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 15:03:02 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:02:45 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.020 |  |
| 2026-05-25 15:02:41 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-05-25 15:02:29 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:02:27 | Galgamuwa (Mee Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:02:27 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-25 15:02:27 | Ellagawa (Kalu Ganga) | 8.95 | 🟢 Normal | -0.020 |  |
| 2026-05-25 15:02:20 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.065 |  |
| 2026-05-25 15:02:04 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-05-25 15:02:03 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:01:59 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-05-25 15:01:56 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:01:54 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.032 |  |
| 2026-05-25 15:01:50 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:01:46 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-25 15:01:32 | Rathnapura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.124 |  |
| 2026-05-25 15:01:25 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:01:23 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:00:38 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:00:15 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | -0.168 |  |
| 2026-05-25 14:56:41 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | -0.168 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-25 15:03:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.27 | 🟡 Alert | -0.049 |  |
| 2026-05-25 15:10:51 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-05-25 15:05:19 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-25 15:03:27 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-25 15:02:27 | Badalgama (Maha Oya) | 2.74 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-25 15:01:46 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-25 15:04:21 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-25 15:03:30 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-25 15:03:04 | Deraniyagala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-25 15:01:23 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:04:33 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:01:25 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:00:38 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:02:27 | Galgamuwa (Mee Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:02:03 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:04:52 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:05:52 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:01:50 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:03:17 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:02:29 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:05:03 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:01:56 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:03:02 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-25 15:07:02 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | -0.009 |  |
| 2026-05-25 15:02:04 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-05-25 15:01:59 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.020 |  |
| 2026-05-25 15:02:41 | Moragaswewa (Deduru Oya) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-05-25 15:02:27 | Ellagawa (Kalu Ganga) | 8.95 | 🟢 Normal | -0.020 |  |
| 2026-05-25 15:02:45 | Manampitiya (Mahaweli Ganga) | 0.01 | 🟢 Normal | -0.020 |  |
| 2026-05-25 15:04:02 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-05-25 15:01:54 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.032 |  |
| 2026-05-25 15:03:45 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | -0.041 |  |
| 2026-05-25 15:06:07 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.044 |  |
| 2026-05-25 15:03:41 | Putupaula (Kalu Ganga) | 2.86 | 🟢 Normal | -0.051 |  |
| 2026-05-25 15:02:20 | Peradeniya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.065 |  |
| 2026-05-25 15:03:17 | Hanwella (Kelani Ganga) | 4.60 | 🟢 Normal | -0.092 |  |
| 2026-05-25 15:04:40 | Glencourse (Kelani Ganga) | 11.69 | 🟢 Normal | -0.107 |  |
| 2026-05-25 15:01:32 | Rathnapura (Kalu Ganga) | 3.80 | 🟢 Normal | -0.124 |  |
| 2026-05-25 15:00:15 | Thanthirimale (Malwathu Oya) | 1.35 | 🟢 Normal | -0.168 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)