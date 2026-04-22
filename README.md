# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_15:24:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,068 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 15:24:19 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-22 15:17:43 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-22 15:11:11 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.009 |  |
| 2026-04-22 15:10:20 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2026-04-22 15:10:16 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-04-22 15:07:31 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-22 15:07:25 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.028 |  |
| 2026-04-22 15:07:05 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-04-22 15:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.058 |  |
| 2026-04-22 15:05:37 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-22 15:05:24 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-22 15:04:36 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-22 15:04:22 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-04-22 15:04:20 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.075 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 15:10:16 | Glencourse (Kelani Ganga) | 8.79 | 🟢 Normal | 0.141 | 🔺 Rising |
| 2026-04-22 15:03:26 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-04-22 15:02:26 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-04-22 15:03:16 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-04-22 15:03:06 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-22 15:03:35 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-22 15:01:45 | Kithulgala (Kelani Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-22 15:05:24 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-04-22 15:17:43 | Horowpothana (Yan Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-22 15:03:49 | Magura (Kalu Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-04-22 15:05:37 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-04-22 15:03:49 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-22 15:00:18 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-22 15:24:19 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-22 15:00:40 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-22 15:01:35 | Thanthirimale (Malwathu Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-04-22 15:02:33 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-22 15:02:50 | Peradeniya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-22 15:04:36 | Urawa (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-22 15:07:31 | Thanamalwila (Kirindi Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-22 15:01:45 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | -0.005 |  |
| 2026-04-22 15:10:20 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.009 |  |
| 2026-04-22 15:11:11 | Kuda Oya (Kirindi Oya) | 1.65 | 🟢 Normal | -0.009 |  |
| 2026-04-22 15:03:42 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-04-22 15:00:11 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-04-22 15:01:02 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-04-22 15:04:22 | Hanwella (Kelani Ganga) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-04-22 15:02:28 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.020 |  |
| 2026-04-22 15:03:08 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | -0.021 |  |
| 2026-04-22 15:07:25 | Giriulla (Maha Oya) | 1.25 | 🟢 Normal | -0.028 |  |
| 2026-04-22 15:02:40 | Ellagawa (Kalu Ganga) | 4.78 | 🟢 Normal | -0.029 |  |
| 2026-04-22 15:03:33 | Badalgama (Maha Oya) | 2.57 | 🟢 Normal | -0.030 |  |
| 2026-04-22 15:02:06 | Wellawaya (Kirindi Oya) | 1.26 | 🟢 Normal | -0.030 |  |
| 2026-04-22 15:02:50 | Manampitiya (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.031 |  |
| 2026-04-22 15:07:05 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-04-22 15:02:23 | Moragaswewa (Deduru Oya) | 0.80 | 🟢 Normal | -0.041 |  |
| 2026-04-22 15:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | -0.058 |  |
| 2026-04-22 15:03:41 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.072 |  |
| 2026-04-22 15:04:20 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | -0.075 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)