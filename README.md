# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--02_23:12:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **62,848 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 23:12:41 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.019 |  |
| 2026-02-02 23:11:02 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.018 |  |
| 2026-02-02 23:10:35 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.047 |  |
| 2026-02-02 23:10:19 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-02-02 23:08:01 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 23:06:59 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.047 |  |
| 2026-02-02 23:06:28 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | -0.022 |  |
| 2026-02-02 23:06:04 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-02-02 23:05:42 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 23:05:16 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-02 23:04:07 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-02 23:04:01 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 23:03:28 | Padiyathalawa (Maduru Oya) | 0.71 | 🟢 Normal | -0.012 |  |
| 2026-02-02 23:03:27 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-02 23:03:18 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-02 23:02:52 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-02-02 23:02:52 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-02 23:02:25 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-02 23:02:13 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-02 23:02:05 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -0.049 |  |
| 2026-02-02 23:02:00 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-02-02 23:01:30 | Peradeniya (Mahaweli Ganga) | 1.94 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-02-02 23:01:29 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-02 23:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-02 23:01:07 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 23:00:47 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-02 23:00:46 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.050 |  |
| 2026-02-02 23:00:42 | Manampitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-02-02 23:00:38 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-02 23:00:30 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-02 23:00:19 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 22:37:25 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | -0.049 |  |
| 2026-02-02 22:19:31 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.047 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 23:01:30 | Peradeniya (Mahaweli Ganga) | 1.94 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-02-02 23:02:00 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-02-02 23:10:19 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-02-02 22:05:32 | Panadugama (Nilwala Ganga) | 2.33 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-02-02 23:05:16 | Baddegama (Gin Ganga) | 1.20 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-02-02 23:03:18 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-02 23:00:19 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 23:04:01 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-02 23:01:07 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 23:05:42 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 23:00:30 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-02 23:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-02 23:02:52 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-02 23:00:47 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-02 18:09:57 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-02 23:03:27 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-02-02 23:02:25 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-02 23:08:01 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 23:04:07 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-02-02 22:06:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-02-02 23:06:04 | Badalgama (Maha Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-02-02 23:00:42 | Manampitiya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-02-02 23:00:38 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-02 23:01:29 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-02-02 22:01:25 | Yaka Wewa (Ma Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-02-02 23:02:13 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-02 22:03:25 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-02-02 22:02:19 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-02-02 23:03:28 | Padiyathalawa (Maduru Oya) | 0.71 | 🟢 Normal | -0.012 |  |
| 2026-02-02 23:11:02 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.018 |  |
| 2026-02-02 23:12:41 | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | -0.019 |  |
| 2026-02-02 23:02:52 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:03:26 | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-02 23:06:28 | Glencourse (Kelani Ganga) | 8.39 | 🟢 Normal | -0.022 |  |
| 2026-02-02 23:06:59 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.047 |  |
| 2026-02-02 23:10:35 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | -0.047 |  |
| 2026-02-02 23:02:05 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | -0.049 |  |
| 2026-02-02 23:00:46 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | -0.050 |  |
| 2026-02-02 18:01:17 | Weraganthota (Mahaweli Ganga) | -2.52 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)