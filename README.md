# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_23:58:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **129,680 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 23:58:16 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:48:17 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.006 |  |
| 2026-04-19 23:17:12 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.110 |  |
| 2026-04-19 23:15:47 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:14:33 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:11:23 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-19 23:10:49 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:10:47 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.018 |  |
| 2026-04-19 23:08:58 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:07:18 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:06:31 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:06:22 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.191 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 23:00:50 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-04-19 23:06:22 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.191 | 🔺 Rising |
| 2026-04-19 18:00:27 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-19 23:04:16 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-19 23:01:50 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-19 23:01:03 | Horowpothana (Yan Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 23:11:23 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-19 23:58:16 | Wellawaya (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:00:51 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-19 22:02:53 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:01:37 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:04:16 | Giriulla (Maha Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:06:31 | Magura (Kalu Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:14:33 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:10:49 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:08:58 | Hanwella (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:02:02 | Ellagawa (Kalu Ganga) | 3.92 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:05:01 | Panadugama (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:01:11 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:07:18 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:02:24 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:03:42 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-19 18:02:04 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:15:47 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-19 23:48:17 | Nawalapitiya (Mahaweli Ganga) | 0.73 | 🟢 Normal | -0.006 |  |
| 2026-04-19 23:04:37 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-04-19 23:03:44 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-04-19 23:00:48 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | -0.012 |  |
| 2026-04-19 23:00:20 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.013 |  |
| 2026-04-19 21:20:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | -0.017 |  |
| 2026-04-19 23:10:47 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.018 |  |
| 2026-04-19 23:01:38 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | -0.021 |  |
| 2026-04-19 23:02:48 | Glencourse (Kelani Ganga) | 8.57 | 🟢 Normal | -0.021 |  |
| 2026-04-19 23:05:09 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.029 |  |
| 2026-04-19 22:02:45 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.050 |  |
| 2026-04-19 18:02:41 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.068 |  |
| 2026-04-19 22:06:09 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | -0.084 |  |
| 2026-04-19 23:17:12 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.110 |  |
| 2026-04-19 23:02:35 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | -1.385 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)