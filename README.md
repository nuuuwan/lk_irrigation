# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--30_04:47:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **59,401 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 04:47:14 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:36:44 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-30 04:31:55 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:31:33 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:25:55 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.028 |  |
| 2026-01-30 04:25:54 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:18:55 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:13:39 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:13:31 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:10:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:09:10 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-01-30 04:09:09 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-01-30 04:08:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-30 04:08:34 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:07:22 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:06:34 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-01-30 04:06:31 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:06:29 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 04:05:53 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:04:57 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-30 04:04:22 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-01-30 04:03:52 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:03:46 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:03:20 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:03:09 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.003 |  |
| 2026-01-30 04:03:02 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.141 |  |
| 2026-01-30 04:02:50 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:02:46 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:02:34 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:02:21 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:02:11 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:02:07 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:02:05 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:02:02 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:01:42 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:01:14 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:01:03 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 04:00:48 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:00:46 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-30 04:09:10 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | 72.000 | 🔺 Rising |
| 2026-01-30 04:06:34 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-01-30 04:08:43 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-01-30 04:36:44 | Deraniyagala (Kelani Ganga) | 0.15 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-30 04:06:29 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 04:01:03 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-29 18:02:43 | Weraganthota (Mahaweli Ganga) | -2.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-30 04:02:46 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:03:20 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:00:48 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:18:55 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:25:54 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:02:34 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-29 18:04:09 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:31:33 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-30 03:02:49 | Norwood (Kelani Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:02:50 | Hanwella (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:01:14 | Ellagawa (Kalu Ganga) | 3.79 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:47:14 | Panadugama (Nilwala Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:03:46 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:01:42 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:02:21 | Dunamale (Aththanagalu Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:02:11 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:08:34 | Badalgama (Maha Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:13:31 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:02:07 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:03:52 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-29 18:01:27 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:07:22 | Thawalama (Gin Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:31:55 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-01-30 03:05:20 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:13:39 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:10:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-30 04:03:09 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.003 |  |
| 2026-01-30 04:04:22 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-01-30 04:04:57 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-01-30 04:25:55 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | -0.028 |  |
| 2026-01-30 03:08:32 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.048 |  |
| 2026-01-30 04:03:02 | Peradeniya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.141 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)