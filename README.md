# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_04:30:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **119,170 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 04:30:42 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:26:34 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:26:25 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-08 04:24:40 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:18:49 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | -0.008 |  |
| 2026-04-08 04:14:32 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:14:30 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:12:18 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-04-08 04:07:53 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -12.071 |  |
| 2026-04-08 04:06:15 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:06:12 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:06:07 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-08 04:05:17 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.029 |  |
| 2026-04-08 04:05:03 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | -12.071 |  |
| 2026-04-08 04:04:44 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:04:37 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -1.636 |  |
| 2026-04-08 04:04:15 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -1.636 |  |
| 2026-04-08 04:03:56 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:03:41 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:03:17 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-04-08 04:03:05 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:03:04 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-08 04:03:02 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-04-08 04:02:58 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:02:57 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:02:52 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:01:43 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:01:34 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | -0.010 |  |
| 2026-04-08 04:01:27 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | 0.946 | 🔺 Rising |
| 2026-04-08 04:01:18 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.051 |  |
| 2026-04-08 04:01:18 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:00:38 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:00:18 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.032 |  |
| 2026-04-08 04:00:11 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.145 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 04:01:27 | Glencourse (Kelani Ganga) | 9.36 | 🟢 Normal | 0.946 | 🔺 Rising |
| 2026-04-08 04:26:25 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-08 03:22:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-04-08 04:06:07 | Thawalama (Gin Ganga) | 0.89 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-08 03:07:04 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-08 04:03:56 | Kithulgala (Kelani Ganga) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:00:18 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:00:38 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:02:57 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:02:58 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:26:34 | Magura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:16:05 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:04:44 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:06:12 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:30:42 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-08 03:01:08 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:14:32 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:03:05 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:03:41 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:06:15 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:24:40 | Rathnapura (Kalu Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:01:43 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:02:52 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-08 04:18:49 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | -0.008 |  |
| 2026-04-08 04:12:18 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | -0.009 |  |
| 2026-04-08 02:07:29 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-08 04:03:04 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2026-04-08 04:03:02 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | -0.010 |  |
| 2026-04-08 04:01:34 | Ellagawa (Kalu Ganga) | 3.93 | 🟢 Normal | -0.010 |  |
| 2026-04-07 18:00:44 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-04-08 04:05:17 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | -0.029 |  |
| 2026-04-08 04:03:17 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.031 |  |
| 2026-04-07 18:02:51 | Galgamuwa (Mee Oya) | 0.29 | 🟢 Normal | -0.032 |  |
| 2026-04-08 04:00:16 | Nawalapitiya (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.032 |  |
| 2026-04-08 04:01:18 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.051 |  |
| 2026-04-07 18:01:46 | Weraganthota (Mahaweli Ganga) | -3.14 | 🟢 Normal | -0.060 |  |
| 2026-04-08 04:00:11 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.145 |  |
| 2026-04-08 04:04:37 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -1.636 |  |
| 2026-04-08 04:07:53 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | -12.071 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)