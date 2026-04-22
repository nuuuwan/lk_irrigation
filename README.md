# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--22_22:25:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **132,336 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 22:25:42 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-22 22:16:05 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-22 22:14:43 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-22 22:14:30 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-04-22 22:12:31 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-22 22:09:19 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.464 | 🔺 Rising |
| 2026-04-22 22:07:17 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-22 22:07:15 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.039 |  |
| 2026-04-22 22:06:58 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-22 22:05:41 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.081 |  |
| 2026-04-22 22:05:34 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.091 |  |
| 2026-04-22 22:05:30 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-22 22:05:18 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | -0.111 |  |
| 2026-04-22 22:05:16 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.049 |  |
| 2026-04-22 22:05:10 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.046 |  |
| 2026-04-22 22:04:48 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-22 22:04:39 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-22 22:04:34 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-22 22:04:30 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-22 22:04:16 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-22 22:03:59 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-04-22 22:02:59 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-04-22 22:02:55 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-22 22:02:51 | Thanamalwila (Kirindi Oya) | 3.72 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-04-22 22:02:44 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-04-22 22:02:30 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.032 |  |
| 2026-04-22 22:02:27 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-04-22 22:02:23 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-04-22 22:02:11 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-04-22 22:01:31 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-04-22 22:01:28 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.052 |  |
| 2026-04-22 22:01:24 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | -0.010 |  |
| 2026-04-22 22:01:10 | Kuda Oya (Kirindi Oya) | 2.90 | 🟢 Normal | -0.822 |  |
| 2026-04-22 22:00:50 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-04-22 22:00:49 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-22 22:00:29 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-22 22:09:19 | Rathnapura (Kalu Ganga) | 2.01 | 🟢 Normal | 0.464 | 🔺 Rising |
| 2026-04-22 22:02:51 | Thanamalwila (Kirindi Oya) | 3.72 | 🟢 Normal | 0.317 | 🔺 Rising |
| 2026-04-22 22:02:23 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-04-22 22:04:48 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-22 22:04:34 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-22 22:12:31 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-22 22:02:55 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-04-22 22:06:58 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-04-22 18:02:14 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-22 22:05:30 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-22 22:07:17 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-22 22:14:43 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-22 22:01:31 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:01:19 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-22 22:04:16 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-04-22 22:14:30 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-04-22 22:25:42 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-22 22:00:49 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-22 22:00:29 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-22 22:04:39 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-22 22:02:59 | Badalgama (Maha Oya) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-04-22 21:19:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.85 | 🟢 Normal | -0.009 |  |
| 2026-04-22 22:04:30 | Moragaswewa (Deduru Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-04-22 22:02:11 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:02:04 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-04-22 22:01:24 | Ellagawa (Kalu Ganga) | 4.58 | 🟢 Normal | -0.010 |  |
| 2026-04-22 18:02:52 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-22 22:03:59 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-04-22 22:02:27 | Manampitiya (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.020 |  |
| 2026-04-22 22:00:50 | Wellawaya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-04-22 22:02:30 | Glencourse (Kelani Ganga) | 8.76 | 🟢 Normal | -0.032 |  |
| 2026-04-22 22:07:15 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | -0.039 |  |
| 2026-04-22 22:05:10 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.046 |  |
| 2026-04-22 22:05:16 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.049 |  |
| 2026-04-22 22:01:28 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.052 |  |
| 2026-04-22 22:05:41 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.081 |  |
| 2026-04-22 22:05:34 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.091 |  |
| 2026-04-22 22:05:18 | Nakkala (Kumbukkan Oya) | 1.46 | 🟢 Normal | -0.111 |  |
| 2026-04-22 22:01:10 | Kuda Oya (Kirindi Oya) | 2.90 | 🟢 Normal | -0.822 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)