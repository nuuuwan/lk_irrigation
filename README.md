# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_23:40:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,493 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 23:40:19 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-30 23:29:58 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | -0.007 |  |
| 2026-04-30 23:10:59 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | -0.009 |  |
| 2026-04-30 23:10:25 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:10:23 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-04-30 23:10:07 | Rathnapura (Kalu Ganga) | 2.73 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-30 23:08:20 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.039 |  |
| 2026-04-30 23:08:18 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:06:38 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:05:43 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:04:43 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-04-30 23:04:30 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-30 23:04:20 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-04-30 23:03:38 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.029 |  |
| 2026-04-30 23:03:37 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:03:26 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:03:18 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:02:51 | Yaka Wewa (Ma Oya) | 1.51 | 🟢 Normal | -0.247 |  |
| 2026-04-30 23:02:26 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-04-30 23:02:18 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.014 |  |
| 2026-04-30 23:02:18 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:02:12 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-04-30 23:02:11 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-04-30 23:01:40 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-04-30 23:01:27 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:01:27 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:01:25 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-30 23:01:20 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:01:10 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-30 23:00:36 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 23:10:07 | Rathnapura (Kalu Ganga) | 2.73 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-04-30 23:01:40 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-04-30 23:01:10 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-30 23:01:25 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-04-30 22:01:09 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-04-30 22:01:11 | Glencourse (Kelani Ganga) | 8.75 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-04-30 23:04:30 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-30 23:40:19 | Kithulgala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-04-30 23:01:20 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:08:18 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:03:18 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:01:27 | Ellagawa (Kalu Ganga) | 4.35 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:01:27 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:02:18 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:03:26 | Dunamale (Aththanagalu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:03:37 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:05:43 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:10:25 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:02:32 | Thanthirimale (Malwathu Oya) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-04-30 22:19:49 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:06:38 | Kuda Oya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-30 23:29:58 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | -0.007 |  |
| 2026-04-30 23:10:59 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | -0.009 |  |
| 2026-04-30 22:13:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | -0.009 |  |
| 2026-04-30 22:06:38 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-04-30 23:04:43 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-04-30 22:04:21 | Nawalapitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:02:01 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.010 |  |
| 2026-04-30 23:02:12 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:03:14 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-30 23:02:26 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-04-30 23:04:20 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-04-30 23:02:18 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | -0.014 |  |
| 2026-04-30 23:10:23 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-04-30 23:02:11 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-04-30 23:03:38 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.029 |  |
| 2026-04-30 23:00:36 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.032 |  |
| 2026-04-30 23:08:20 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.039 |  |
| 2026-04-30 23:02:51 | Yaka Wewa (Ma Oya) | 1.51 | 🟢 Normal | -0.247 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)