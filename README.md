# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_01:23:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,294 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 01:23:58 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.026 |  |
| 2026-04-15 01:16:24 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-04-15 01:14:11 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.017 |  |
| 2026-04-15 01:13:53 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-15 01:08:49 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-04-15 01:06:10 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-15 01:05:47 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-15 01:05:43 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-15 01:05:05 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-04-15 01:03:49 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.014 |  |
| 2026-04-15 01:03:43 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-15 01:03:27 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-15 01:03:16 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-15 01:02:40 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-04-15 01:02:31 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-15 01:02:20 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-04-15 01:02:18 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.028 |  |
| 2026-04-15 01:01:59 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.030 |  |
| 2026-04-15 01:01:41 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-15 01:01:39 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 01:01:27 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.043 |  |
| 2026-04-15 01:01:20 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-15 01:01:08 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 01:01:06 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.026 |  |
| 2026-04-15 01:00:36 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.025 |  |
| 2026-04-15 01:00:30 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 00:12:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-04-15 01:02:40 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-04-15 01:01:20 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-15 01:01:41 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-15 01:13:53 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-04-15 01:05:47 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-15 01:01:08 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 01:08:49 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-04-15 00:19:42 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:01:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:31:43 | Horowpothana (Yan Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:06:36 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:05:10 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-15 01:03:16 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-15 01:01:39 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 01:00:30 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-04-15 00:03:34 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-15 01:05:43 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-14 22:01:35 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-15 01:02:31 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-15 01:06:10 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-15 01:16:24 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-04-15 01:03:43 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-04-15 01:03:27 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-15 01:05:05 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.010 |  |
| 2026-04-14 22:01:47 | Kuda Oya (Kirindi Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-04-15 01:03:49 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | -0.014 |  |
| 2026-04-15 01:14:11 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.017 |  |
| 2026-04-15 00:19:27 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.018 |  |
| 2026-04-15 00:01:42 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | -0.020 |  |
| 2026-04-14 18:01:58 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | -0.021 |  |
| 2026-04-15 01:00:36 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.025 |  |
| 2026-04-15 01:23:58 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.026 |  |
| 2026-04-15 01:02:18 | Katharagama (Menik Ganga) | 0.09 | 🟢 Normal | -0.028 |  |
| 2026-04-15 01:02:20 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | -0.030 |  |
| 2026-04-15 01:01:59 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | -0.030 |  |
| 2026-04-15 01:01:27 | Peradeniya (Mahaweli Ganga) | 1.86 | 🟢 Normal | -0.043 |  |
| 2026-04-14 18:01:59 | Thanthirimale (Malwathu Oya) | 3.79 | 🟢 Normal | -0.059 |  |
| 2026-04-14 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.063 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)