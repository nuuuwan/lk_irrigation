# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--17_03:00:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **127,124 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 03:00:50 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-17 03:00:47 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-17 02:51:09 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-17 02:31:15 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-17 02:16:52 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-17 02:15:05 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.026 |  |
| 2026-04-17 02:08:39 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -1.565 |  |
| 2026-04-17 02:08:22 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | -0.005 |  |
| 2026-04-17 02:08:16 | Thawalama (Gin Ganga) | 1.51 | 🟢 Normal | -1.565 |  |
| 2026-04-17 02:08:12 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-17 02:04:29 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | 1.241 | 🔺 Rising |
| 2026-04-17 01:01:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.90 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-04-17 02:16:52 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-17 03:00:50 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-17 02:04:21 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-17 02:02:52 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-17 02:04:40 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-04-17 01:00:50 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-17 02:04:36 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-17 02:51:09 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-17 02:02:47 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-17 02:03:11 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-04-17 03:00:47 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-17 02:02:01 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-17 02:31:15 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:19 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-17 02:01:59 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-17 02:04:14 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 02:02:16 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-17 02:08:12 | Moraketiya (Walawe Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-17 00:03:09 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-17 02:04:30 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-17 01:03:51 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-16 18:00:56 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-04-17 02:07:00 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-17 02:08:22 | Moragaswewa (Deduru Oya) | 0.10 | 🟢 Normal | -0.005 |  |
| 2026-04-17 02:05:10 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | -0.005 |  |
| 2026-04-17 01:12:15 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.009 |  |
| 2026-04-17 02:02:20 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-04-17 02:06:48 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-04-17 02:02:35 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-04-17 02:05:33 | Thanamalwila (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-04-17 02:02:39 | Ellagawa (Kalu Ganga) | 4.52 | 🟢 Normal | -0.020 |  |
| 2026-04-17 02:15:05 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | -0.026 |  |
| 2026-04-17 02:01:28 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | -0.030 |  |
| 2026-04-17 02:03:32 | Peradeniya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.154 |  |
| 2026-04-17 02:08:39 | Thawalama (Gin Ganga) | 1.50 | 🟢 Normal | -1.565 |  |
| 2026-04-16 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -4.696 |  |
| 2026-04-17 02:03:12 | Thaldena (Mahaweli Ganga) | 0.39 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)