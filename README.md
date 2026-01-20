# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--20_14:12:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **50,810 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 14:12:24 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-20 14:10:24 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:10:08 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:08:55 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:07:44 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:07:41 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:07:13 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.901 | 🔺 Rising |
| 2026-01-20 14:07:08 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-20 14:07:05 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-01-20 14:06:11 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.048 |  |
| 2026-01-20 14:05:58 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:05:48 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-20 14:05:27 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:04:35 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:04:08 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-20 14:03:38 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:03:37 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:03:34 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-01-20 14:03:28 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-01-20 14:03:12 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.020 |  |
| 2026-01-20 14:02:45 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:02:37 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:02:35 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:02:23 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:02:22 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:02:20 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:02:20 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-01-20 14:02:10 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | -0.013 |  |
| 2026-01-20 14:01:50 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.158 |  |
| 2026-01-20 14:01:32 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-20 14:01:10 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-20 14:00:51 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:00:29 | Weraganthota (Mahaweli Ganga) | -2.39 | 🟢 Normal | -0.093 |  |
| 2026-01-20 14:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:00:18 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-20 13:58:50 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.046 |  |
| 2026-01-20 13:17:01 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-20 14:07:13 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | 0.901 | 🔺 Rising |
| 2026-01-20 14:03:34 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-01-20 14:01:32 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-01-20 14:01:10 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-20 14:04:08 | Thaldena (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-20 14:05:48 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-20 14:12:24 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-20 14:07:08 | Glencourse (Kelani Ganga) | 8.51 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-20 14:02:22 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:00:51 | Moragaswewa (Deduru Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:00:18 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:01:54 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:02:35 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:10:08 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:04:35 | Pitabeddara (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:02:20 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:07:41 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:07:44 | Panadugama (Nilwala Ganga) | 2.08 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:03:37 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:02:37 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:05:27 | Dunamale (Aththanagalu Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:05:58 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:02:45 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:02:20 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:03:38 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:08:55 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:02:23 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-01-20 14:10:24 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-20 13:06:15 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | -0.009 |  |
| 2026-01-20 14:03:28 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-01-20 14:00:18 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-20 14:02:10 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | -0.013 |  |
| 2026-01-20 14:03:12 | Hanwella (Kelani Ganga) | 0.29 | 🟢 Normal | -0.020 |  |
| 2026-01-20 14:07:05 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | -0.029 |  |
| 2026-01-20 14:02:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.30 | 🟢 Normal | -0.030 |  |
| 2026-01-20 13:58:50 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.046 |  |
| 2026-01-20 14:06:11 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.048 |  |
| 2026-01-20 14:00:29 | Weraganthota (Mahaweli Ganga) | -2.39 | 🟢 Normal | -0.093 |  |
| 2026-01-20 14:01:50 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.158 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)