# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--31_23:32:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,029 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 23:32:21 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:16:24 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:12:21 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.880 | 🔺 Rising |
| 2026-01-31 23:10:34 | Manampitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.186 |  |
| 2026-01-31 23:09:40 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 23:07:51 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:06:02 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-31 23:05:32 | Holombuwa (Kelani Ganga) | 0.37 | 🟢 Normal | 0.880 | 🔺 Rising |
| 2026-01-31 23:04:57 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 12.436 | 🔺 Rising |
| 2026-01-31 23:04:37 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:04:36 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-31 23:04:02 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 12.436 | 🔺 Rising |
| 2026-01-31 23:03:45 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-01-31 23:03:43 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.040 |  |
| 2026-01-31 23:03:38 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:03:28 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-01-31 23:03:27 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:03:13 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:02:36 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.022 |  |
| 2026-01-31 23:02:26 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-01-31 23:02:22 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-31 23:02:20 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:02:11 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-31 23:02:06 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:02:04 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:01:32 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:01:08 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-31 23:01:05 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-01-31 23:01:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-01-31 23:00:52 | Manampitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.186 |  |
| 2026-01-31 23:00:28 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:00:22 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 22:47:18 | Manampitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.186 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-31 23:04:57 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 12.436 | 🔺 Rising |
| 2026-01-31 23:12:21 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.880 | 🔺 Rising |
| 2026-01-31 23:01:05 | Peradeniya (Mahaweli Ganga) | 1.91 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-01-31 22:26:01 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-01-31 23:04:36 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-01-31 23:01:08 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-01-31 23:02:22 | Pitabeddara (Nilwala Ganga) | 0.41 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-31 23:01:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-01-31 22:09:31 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-01-31 23:06:02 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-01-31 23:00:22 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 23:09:40 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-31 22:11:39 | Panadugama (Nilwala Ganga) | 2.06 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-31 22:14:33 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-01-31 23:00:28 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:16:24 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:03:27 | Moragaswewa (Deduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-01-31 22:00:54 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-31 21:01:40 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:03:38 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:08:19 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:07:51 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:02:04 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:32:21 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | 0.000 |  |
| 2026-01-31 22:02:37 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:02:20 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:03:13 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:01:52 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:01:32 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:02:06 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-31 23:03:45 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-01-31 23:03:28 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | -0.010 |  |
| 2026-01-31 23:02:26 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-01-31 23:02:11 | Padiyathalawa (Maduru Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-01-31 22:00:43 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-01-31 23:02:36 | Hanwella (Kelani Ganga) | 0.31 | 🟢 Normal | -0.022 |  |
| 2026-01-31 23:03:43 | Thalgahagoda (Nilwala Ganga) | 0.31 | 🟢 Normal | -0.040 |  |
| 2026-01-31 18:00:08 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | -0.051 |  |
| 2026-01-31 23:10:34 | Manampitiya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.186 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)