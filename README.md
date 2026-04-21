# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_23:04:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **131,457 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 23:04:15 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-21 23:04:03 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.029 |  |
| 2026-04-21 23:03:56 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.079 |  |
| 2026-04-21 23:03:33 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-21 23:02:53 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-21 23:02:39 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | -0.086 |  |
| 2026-04-21 23:02:26 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 23:02:25 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | -0.040 |  |
| 2026-04-21 23:02:25 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.132 |  |
| 2026-04-21 23:02:14 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-21 23:02:13 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-04-21 23:02:12 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-21 23:01:54 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-21 23:01:51 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-21 23:01:50 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 23:01:40 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | -0.080 |  |
| 2026-04-21 23:01:22 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.012 |  |
| 2026-04-21 23:01:20 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -2.043 |  |
| 2026-04-21 23:01:11 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 23:00:30 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:25:59 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:17:53 | Moraketiya (Walawe Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:13:50 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 22:02:24 | Thanamalwila (Kirindi Oya) | 2.86 | 🟢 Normal | 0.523 | 🔺 Rising |
| 2026-04-21 23:02:13 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-04-21 22:01:27 | Peradeniya (Mahaweli Ganga) | 2.04 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-21 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-21 23:02:14 | Thawalama (Gin Ganga) | 1.70 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-21 22:06:18 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-21 18:03:15 | Galgamuwa (Mee Oya) | 1.08 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-21 22:11:01 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-21 23:01:50 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 23:01:11 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 23:02:12 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:01:43 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-21 23:03:33 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-21 23:02:26 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-21 23:04:15 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:17:53 | Moraketiya (Walawe Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-04-21 23:01:54 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-21 23:02:53 | Dunamale (Aththanagalu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-21 23:00:30 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:01:15 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-21 23:01:51 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-04-21 18:01:44 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:13:50 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:25:59 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-21 22:06:51 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-04-21 23:01:22 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.012 |  |
| 2026-04-21 22:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-04-21 22:06:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | -0.021 |  |
| 2026-04-21 23:04:03 | Magura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.029 |  |
| 2026-04-21 23:02:25 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | -0.040 |  |
| 2026-04-21 22:09:31 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.041 |  |
| 2026-04-21 22:01:45 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.053 |  |
| 2026-04-21 22:05:12 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | -0.062 |  |
| 2026-04-21 23:03:56 | Ellagawa (Kalu Ganga) | 5.65 | 🟢 Normal | -0.079 |  |
| 2026-04-21 23:01:40 | Glencourse (Kelani Ganga) | 8.94 | 🟢 Normal | -0.080 |  |
| 2026-04-21 23:02:39 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | -0.086 |  |
| 2026-04-21 22:00:07 | Wellawaya (Kirindi Oya) | 1.69 | 🟢 Normal | -0.110 |  |
| 2026-04-21 23:02:25 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.132 |  |
| 2026-04-21 23:01:20 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -2.043 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)