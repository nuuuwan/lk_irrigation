# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_12:26:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,711 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 12:26:28 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:12:55 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 12:10:52 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:08:58 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.028 |  |
| 2026-04-15 12:08:56 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:07:55 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:06:36 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-04-15 12:06:17 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:06:14 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-04-15 12:06:05 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-15 12:05:49 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-15 12:05:45 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:05:42 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-04-15 12:05:31 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:05:07 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -90.000 |  |
| 2026-04-15 12:05:05 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | -90.000 |  |
| 2026-04-15 12:04:27 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-15 12:04:19 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-15 12:04:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.046 |  |
| 2026-04-15 12:03:46 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:03:30 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:03:30 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-15 12:03:29 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 12:02:59 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:02:19 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-04-15 12:02:13 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:02:07 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-15 12:02:03 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-15 12:02:02 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:01:56 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:01:40 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:01:39 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:01:19 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:01:18 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-04-15 12:00:43 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.131 |  |
| 2026-04-15 12:00:42 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.015 |  |
| 2026-04-15 12:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-04-15 12:00:38 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.030 |  |
| 2026-04-15 12:00:27 | Thanthirimale (Malwathu Oya) | 2.64 | 🟢 Normal | -0.030 |  |
| 2026-04-15 12:00:16 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.152 |  |
| 2026-04-15 12:00:12 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 12:05:42 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-04-15 12:06:36 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-04-15 12:04:19 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-15 12:05:49 | Pitabeddara (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-04-15 12:02:03 | Thawalama (Gin Ganga) | 1.27 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-15 12:04:27 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-15 12:03:29 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 12:12:55 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-15 12:05:31 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:01:56 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:00:12 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:01:39 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:02:13 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:08:56 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:01:40 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:05:45 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:10:52 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:26:28 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:07:55 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-04-15 11:00:48 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:03:30 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:02:59 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:02:02 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:03:46 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-15 12:01:18 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-04-15 12:03:30 | Dunamale (Aththanagalu Oya) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-04-15 12:06:05 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-04-15 12:02:07 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | -0.010 |  |
| 2026-04-15 12:02:19 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | -0.011 |  |
| 2026-04-15 12:00:42 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | -0.015 |  |
| 2026-04-15 12:00:41 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | -0.020 |  |
| 2026-04-15 12:06:14 | Magura (Kalu Ganga) | 1.24 | 🟢 Normal | -0.021 |  |
| 2026-04-15 12:08:58 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.028 |  |
| 2026-04-15 12:00:38 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.030 |  |
| 2026-04-15 12:00:27 | Thanthirimale (Malwathu Oya) | 2.64 | 🟢 Normal | -0.030 |  |
| 2026-04-15 12:04:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.64 | 🟢 Normal | -0.046 |  |
| 2026-04-15 12:00:43 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.131 |  |
| 2026-04-15 12:00:16 | Thalgahagoda (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.152 |  |
| 2026-04-15 12:05:07 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | -90.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)