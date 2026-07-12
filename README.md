# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--12_07:03:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **203,992 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 07:03:02 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | -0.027 |  |
| 2026-07-12 07:02:51 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:02:50 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.012 |  |
| 2026-07-12 07:02:38 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:02:22 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-12 07:02:21 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.011 |  |
| 2026-07-12 07:02:05 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.020 |  |
| 2026-07-12 07:02:05 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:01:59 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-12 07:01:51 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:01:35 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.020 |  |
| 2026-07-12 07:01:27 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:01:24 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | -0.011 |  |
| 2026-07-12 07:01:22 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:00:46 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.003 |  |
| 2026-07-12 07:00:45 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-12 06:40:49 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.027 |  |
| 2026-07-12 06:22:12 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-12 06:18:55 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-12 06:14:24 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-12 07:02:22 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-07-12 07:01:59 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-12 06:05:28 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-12 07:00:46 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.003 |  |
| 2026-07-12 07:01:51 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:02:38 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:01:27 | Yaka Wewa (Ma Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:00:45 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-11 18:04:28 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-12 06:00:10 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:02:51 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-12 06:05:13 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-07-12 06:03:40 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-12 06:14:24 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-07-12 06:03:01 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:02:05 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-07-12 06:05:36 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-07-12 06:06:44 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-07-12 06:22:12 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-07-12 06:04:50 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-12 07:01:22 | Thanamalwila (Kirindi Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-12 06:04:36 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-07-12 06:04:18 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-07-12 06:03:08 | Rathnapura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-07-12 06:01:01 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.011 |  |
| 2026-07-12 07:01:24 | Ellagawa (Kalu Ganga) | 4.48 | 🟢 Normal | -0.011 |  |
| 2026-07-12 07:02:21 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.011 |  |
| 2026-07-12 07:02:50 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.012 |  |
| 2026-07-12 07:02:05 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.020 |  |
| 2026-07-12 07:01:35 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.020 |  |
| 2026-07-12 07:03:02 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | -0.027 |  |
| 2026-07-12 06:06:29 | Thalgahagoda (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.028 |  |
| 2026-07-12 06:05:02 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-07-12 06:02:18 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | -0.042 |  |
| 2026-07-12 06:00:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.45 | 🟢 Normal | -0.064 |  |
| 2026-07-12 06:03:33 | Glencourse (Kelani Ganga) | 9.46 | 🟢 Normal | -0.084 |  |
| 2026-07-12 06:00:35 | Putupaula (Kalu Ganga) | 0.21 | 🟢 Normal | -0.102 |  |
| 2026-07-12 06:04:18 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.108 |  |
| 2026-07-12 06:03:22 | Kithulgala (Kelani Ganga) | 1.19 | 🟢 Normal | -0.203 |  |

## River Water Level Charts by Station

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)