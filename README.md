# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--29_01:42:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,772 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 01:42:29 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.020 |  |
| 2026-04-29 01:27:00 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-29 01:18:32 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.025 |  |
| 2026-04-29 01:10:56 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.051 |  |
| 2026-04-29 01:10:15 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-29 01:07:07 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.014 |  |
| 2026-04-29 01:06:37 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-29 01:06:16 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.009 |  |
| 2026-04-29 01:06:12 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-29 01:05:22 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-29 01:04:52 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-29 01:04:30 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-29 01:03:23 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-29 01:06:37 | Glencourse (Kelani Ganga) | 8.85 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-04-29 01:05:22 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-28 21:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.96 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-29 01:06:12 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-29 01:10:15 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-04-29 01:02:15 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 01:02:23 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-29 01:01:52 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 18:04:58 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 17:02:52 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-29 00:33:05 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-29 01:27:00 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-29 00:05:41 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-29 00:08:33 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-28 23:07:56 | Magura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-29 01:03:23 | Pitabeddara (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-29 01:00:51 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-04-29 01:01:13 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-29 01:02:37 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-29 01:04:52 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-29 00:47:38 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-29 00:04:25 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | -0.005 |  |
| 2026-04-29 01:06:16 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.009 |  |
| 2026-04-29 00:03:00 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-04-29 01:03:20 | Ellagawa (Kalu Ganga) | 4.54 | 🟢 Normal | -0.010 |  |
| 2026-04-29 01:04:30 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-28 18:04:12 | Thanthirimale (Malwathu Oya) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-04-29 00:01:51 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-04-29 01:07:07 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.014 |  |
| 2026-04-28 23:26:48 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.014 |  |
| 2026-04-29 01:42:29 | Panadugama (Nilwala Ganga) | 2.27 | 🟢 Normal | -0.020 |  |
| 2026-04-29 01:03:07 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-04-29 01:03:00 | Badalgama (Maha Oya) | 2.46 | 🟢 Normal | -0.020 |  |
| 2026-04-29 01:02:31 | Hanwella (Kelani Ganga) | 0.73 | 🟢 Normal | -0.021 |  |
| 2026-04-29 01:18:32 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | -0.025 |  |
| 2026-04-29 01:00:37 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.044 |  |
| 2026-04-29 01:10:56 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.051 |  |
| 2026-04-29 01:00:10 | Peradeniya (Mahaweli Ganga) | 1.74 | 🟢 Normal | -0.054 |  |
| 2026-04-29 01:02:14 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.268 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)