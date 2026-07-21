# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--21_08:05:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **212,046 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-21 08:05:52 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-07-21 08:05:30 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:05:18 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | -0.049 |  |
| 2026-07-21 08:05:14 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:05:07 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-07-21 08:04:47 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:04:32 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-07-21 08:04:24 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:04:05 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:03:34 | Hanwella (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:03:28 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.064 |  |
| 2026-07-21 08:03:17 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-07-21 08:03:11 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:03:10 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:02:55 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.090 |  |
| 2026-07-21 08:02:54 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-07-21 08:02:48 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:02:48 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:02:27 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:02:17 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:02:10 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-07-21 08:01:52 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:01:50 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:01:35 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:01:19 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:01:09 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:00:44 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 08:00:17 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:00:16 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.023 |  |
| 2026-07-21 08:00:15 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-21 07:35:49 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-21 08:05:07 | Peradeniya (Mahaweli Ganga) | 1.57 | 🟢 Normal | 0.258 | 🔺 Rising |
| 2026-07-21 08:00:15 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-07-21 06:09:37 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-07-21 07:01:35 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-07-21 08:00:44 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-21 08:01:19 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:02:48 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:01:35 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:01:50 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:02:48 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:04:47 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-07-21 07:09:01 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:02:17 | Pitabeddara (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:03:34 | Hanwella (Kelani Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:04:05 | Ellagawa (Kalu Ganga) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-07-21 07:04:04 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-07-21 07:01:08 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-07-21 07:01:53 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:00:17 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:02:27 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:04:24 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:03:11 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:05:30 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:01:09 | Manampitiya (Mahaweli Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:05:14 | Thawalama (Gin Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 07:09:07 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:03:10 | Kuda Oya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-21 08:04:32 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-07-21 08:05:52 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-07-21 07:03:16 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.010 |  |
| 2026-07-21 08:02:10 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-07-21 08:02:54 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.011 |  |
| 2026-07-21 08:03:17 | Deraniyagala (Kelani Ganga) | 0.52 | 🟢 Normal | -0.020 |  |
| 2026-07-21 08:00:16 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.023 |  |
| 2026-07-21 08:05:18 | Glencourse (Kelani Ganga) | 9.11 | 🟢 Normal | -0.049 |  |
| 2026-07-21 08:03:28 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.064 |  |
| 2026-07-21 08:02:55 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.090 |  |
| 2026-07-21 07:05:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)