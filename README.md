# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--07_21:21:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **39,411 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 21:21:16 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.043 |  |
| 2026-01-07 21:15:13 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-01-07 21:12:22 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:07:51 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:07:49 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:07:47 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-01-07 21:07:24 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.043 |  |
| 2026-01-07 21:07:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:06:47 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-07 21:06:35 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.010 |  |
| 2026-01-07 21:06:29 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-07 21:05:42 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:05:42 | Dunamale (Aththanagalu Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 21:05:18 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.050 |  |
| 2026-01-07 21:05:17 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-01-07 21:04:35 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-01-07 21:04:33 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:04:19 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.023 |  |
| 2026-01-07 21:04:01 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-01-07 21:03:37 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-07 21:03:35 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:03:27 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.011 |  |
| 2026-01-07 21:02:58 | Siyambalanduwa (Heda Oya) | 1.41 | 🟢 Normal | -0.039 |  |
| 2026-01-07 21:02:41 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-07 21:02:17 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-07 21:02:11 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:02:07 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.030 |  |
| 2026-01-07 21:01:59 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-07 21:01:52 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:01:50 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:01:37 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.059 |  |
| 2026-01-07 21:01:27 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.005 |  |
| 2026-01-07 21:01:24 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | -0.011 |  |
| 2026-01-07 21:01:14 | Manampitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.046 |  |
| 2026-01-07 21:00:55 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.064 |  |
| 2026-01-07 21:00:52 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:00:52 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-01-07 21:00:37 | Pitabeddara (Nilwala Ganga) | 1.88 | 🟢 Normal | 0.450 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-07 21:00:37 | Pitabeddara (Nilwala Ganga) | 1.88 | 🟢 Normal | 0.450 | 🔺 Rising |
| 2026-01-07 21:04:35 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-01-07 21:07:47 | Panadugama (Nilwala Ganga) | 2.66 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-01-07 21:06:47 | Rathnapura (Kalu Ganga) | 0.80 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-01-07 18:01:49 | Weraganthota (Mahaweli Ganga) | -1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 21:05:42 | Dunamale (Aththanagalu Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-07 21:05:42 | Moragaswewa (Deduru Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:01:52 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-01-07 18:01:21 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:07:49 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:04:33 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:12:22 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:00:52 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:02:11 | Katharagama (Menik Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:07:51 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:01:50 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:07:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-01-07 21:01:27 | Thaldena (Mahaweli Ganga) | 0.88 | 🟢 Normal | -0.005 |  |
| 2026-01-07 21:06:29 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-07 21:01:59 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-01-07 21:06:35 | Glencourse (Kelani Ganga) | 8.59 | 🟢 Normal | -0.010 |  |
| 2026-01-07 21:02:17 | Hanwella (Kelani Ganga) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-01-07 21:03:37 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-01-07 21:15:13 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-01-07 21:02:41 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-07 21:05:17 | Thanamalwila (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-01-07 21:03:27 | Badalgama (Maha Oya) | 2.03 | 🟢 Normal | -0.011 |  |
| 2026-01-07 21:01:24 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | -0.011 |  |
| 2026-01-07 21:00:52 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.020 |  |
| 2026-01-07 21:04:01 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.020 |  |
| 2026-01-07 18:03:25 | Thanthirimale (Malwathu Oya) | 1.77 | 🟢 Normal | -0.023 |  |
| 2026-01-07 21:04:19 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.023 |  |
| 2026-01-07 21:02:07 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.030 |  |
| 2026-01-07 21:02:58 | Siyambalanduwa (Heda Oya) | 1.41 | 🟢 Normal | -0.039 |  |
| 2026-01-07 21:21:16 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.043 |  |
| 2026-01-07 21:01:14 | Manampitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.046 |  |
| 2026-01-07 21:05:18 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.050 |  |
| 2026-01-07 21:01:37 | Thalgahagoda (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.059 |  |
| 2026-01-07 21:00:55 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)