# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_11:20:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,656 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 11:20:47 | Magura (Kalu Ganga) | 3.01 | 🟢 Normal | -0.102 |  |
| 2026-05-30 11:19:01 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:12:54 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.059 |  |
| 2026-05-30 11:11:24 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-05-30 11:10:46 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:10:31 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.081 |  |
| 2026-05-30 11:09:11 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.095 |  |
| 2026-05-30 11:09:10 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-30 11:08:13 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.015 |  |
| 2026-05-30 11:07:53 | Hanwella (Kelani Ganga) | 2.95 | 🟢 Normal | -0.048 |  |
| 2026-05-30 11:07:34 | Baddegama (Gin Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:07:17 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:07:14 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:06:57 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 11:06:19 | Panadugama (Nilwala Ganga) | 3.49 | 🟢 Normal | -0.042 |  |
| 2026-05-30 11:05:54 | Baddegama (Gin Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:05:45 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-30 11:04:25 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-05-30 11:04:17 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-05-30 11:03:52 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-05-30 11:03:42 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:03:30 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | -0.011 |  |
| 2026-05-30 11:03:27 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:03:25 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:03:21 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:03:16 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.168 |  |
| 2026-05-30 11:03:10 | Dunamale (Aththanagalu Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-05-30 11:02:38 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:02:27 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:02:07 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:01:37 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-05-30 11:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:01:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | -0.034 |  |
| 2026-05-30 11:01:25 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:01:20 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:01:00 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.020 |  |
| 2026-05-30 11:00:59 | Ellagawa (Kalu Ganga) | 7.82 | 🟢 Normal | -0.090 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 11:01:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | -0.034 |  |
| 2026-05-30 11:05:45 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-30 11:09:10 | Kithulgala (Kelani Ganga) | 1.44 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-30 09:01:23 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-30 11:06:57 | Holombuwa (Kelani Ganga) | 0.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 10:21:17 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-30 11:02:07 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:03:27 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:01:29 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:07:14 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:02:27 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:01:25 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:07:17 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:07:34 | Baddegama (Gin Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:00:12 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:03:25 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:03:21 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:02:38 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:03:42 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:01:20 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:10:46 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:19:01 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-30 11:11:24 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.009 |  |
| 2026-05-30 11:04:25 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | -0.010 |  |
| 2026-05-30 11:04:17 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-05-30 11:03:10 | Dunamale (Aththanagalu Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-05-30 11:03:52 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | -0.010 |  |
| 2026-05-30 11:01:37 | Thanamalwila (Kirindi Oya) | 0.68 | 🟢 Normal | -0.011 |  |
| 2026-05-30 11:03:30 | Glencourse (Kelani Ganga) | 10.82 | 🟢 Normal | -0.011 |  |
| 2026-05-30 11:08:13 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | -0.015 |  |
| 2026-05-30 11:01:00 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.020 |  |
| 2026-05-30 11:06:19 | Panadugama (Nilwala Ganga) | 3.49 | 🟢 Normal | -0.042 |  |
| 2026-05-30 11:07:53 | Hanwella (Kelani Ganga) | 2.95 | 🟢 Normal | -0.048 |  |
| 2026-05-30 11:12:54 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.059 |  |
| 2026-05-30 11:10:31 | Thalgahagoda (Nilwala Ganga) | 0.62 | 🟢 Normal | -0.081 |  |
| 2026-05-30 11:00:59 | Ellagawa (Kalu Ganga) | 7.82 | 🟢 Normal | -0.090 |  |
| 2026-05-30 11:09:11 | Rathnapura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.095 |  |
| 2026-05-30 11:20:47 | Magura (Kalu Ganga) | 3.01 | 🟢 Normal | -0.102 |  |
| 2026-05-30 11:03:16 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.168 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)