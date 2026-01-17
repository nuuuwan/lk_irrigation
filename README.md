# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--17_23:17:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **48,443 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 23:17:01 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.008 |  |
| 2026-01-17 23:16:27 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:15:21 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-17 23:14:49 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.027 |  |
| 2026-01-17 23:07:38 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:07:14 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-01-17 23:05:16 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.012 |  |
| 2026-01-17 23:05:15 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:04:45 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-01-17 23:04:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-01-17 23:04:01 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-17 23:03:57 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-01-17 23:03:46 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:03:33 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:03:20 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-17 23:03:18 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-01-17 23:02:37 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:02:34 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-17 23:02:28 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:02:12 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:01:57 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:01:55 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:01:47 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-17 23:01:35 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.023 |  |
| 2026-01-17 23:01:34 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-01-17 23:01:33 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 23:01:10 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:00:06 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:31:09 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.027 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 23:01:34 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.194 | 🔺 Rising |
| 2026-01-17 23:03:57 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-01-17 22:05:47 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-17 23:04:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-01-17 23:01:47 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-17 23:15:21 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-17 23:04:01 | Rathnapura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-17 23:02:34 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-17 23:01:33 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-17 23:01:57 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:01:10 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:03:46 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:16:27 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:01:27 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-17 18:02:19 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:15:16 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:02:37 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:05:15 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:02:32 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:00:06 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:02:28 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:03:33 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:02:12 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:07:38 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:16:32 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:14:16 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:01:11 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:01:55 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 23:17:01 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.008 |  |
| 2026-01-17 23:07:14 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.009 |  |
| 2026-01-17 23:03:20 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-01-17 23:04:45 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-01-17 23:03:18 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | -0.010 |  |
| 2026-01-17 21:04:09 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-01-17 23:05:16 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.012 |  |
| 2026-01-17 18:02:02 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-01-17 23:01:35 | Manampitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | -0.023 |  |
| 2026-01-17 23:14:49 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.027 |  |
| 2026-01-17 18:01:12 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)