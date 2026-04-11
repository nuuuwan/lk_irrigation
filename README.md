# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--11_15:11:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **122,259 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 15:11:24 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:08:20 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-04-11 15:08:19 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-11 15:06:43 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.028 |  |
| 2026-04-11 15:06:29 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:06:06 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.018 |  |
| 2026-04-11 15:05:55 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-11 15:05:47 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:05:33 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:05:23 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-11 15:04:28 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:04:21 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.030 |  |
| 2026-04-11 15:04:20 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:04:18 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:04:00 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.053 |  |
| 2026-04-11 15:03:59 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.051 |  |
| 2026-04-11 15:03:48 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:03:38 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:03:37 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-04-11 15:03:20 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-04-11 15:03:18 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-11 15:03:11 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:02:55 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:02:48 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.051 |  |
| 2026-04-11 15:02:38 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-11 15:02:35 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-11 15:02:27 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-04-11 15:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-04-11 15:01:45 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.091 |  |
| 2026-04-11 15:01:27 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:01:23 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:01:14 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:01:13 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:01:12 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.059 |  |
| 2026-04-11 15:01:11 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:01:01 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.118 |  |
| 2026-04-11 15:00:47 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:00:18 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.021 |  |
| 2026-04-11 15:00:02 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.033 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-11 15:08:19 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-04-11 15:00:02 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-04-11 15:02:38 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-11 15:05:23 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-11 15:05:55 | Nawalapitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-11 15:01:11 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:05:33 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:04:18 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:03:38 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:00:47 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:06:29 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:04:20 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:03:48 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:01:23 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:02:55 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:04:28 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:05:47 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:01:13 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:01:27 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:11:24 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:03:11 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:01:14 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-11 15:08:20 | Thanamalwila (Kirindi Oya) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-04-11 15:03:20 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-04-11 15:02:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-04-11 15:03:18 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-04-11 15:02:35 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-11 15:03:37 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | -0.010 |  |
| 2026-04-11 15:02:27 | Peradeniya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.011 |  |
| 2026-04-11 15:06:06 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.018 |  |
| 2026-04-11 15:00:18 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.021 |  |
| 2026-04-11 15:06:43 | Manampitiya (Mahaweli Ganga) | 0.13 | 🟢 Normal | -0.028 |  |
| 2026-04-11 15:04:21 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.030 |  |
| 2026-04-11 15:02:48 | Glencourse (Kelani Ganga) | 8.36 | 🟢 Normal | -0.051 |  |
| 2026-04-11 15:03:59 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | -0.051 |  |
| 2026-04-11 15:04:00 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | -0.053 |  |
| 2026-04-11 15:01:12 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.059 |  |
| 2026-04-11 15:01:45 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.091 |  |
| 2026-04-11 15:01:01 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | -0.118 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

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

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)