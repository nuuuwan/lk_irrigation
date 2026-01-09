# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--09_17:14:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **41,071 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 17:14:05 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-09 17:13:03 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 17:11:39 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:11:39 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:11:12 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:08:49 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-09 17:08:29 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:07:52 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:05:27 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:05:17 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:04:56 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.033 |  |
| 2026-01-09 17:04:56 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:04:19 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:03:59 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-09 17:03:15 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-01-09 17:03:06 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:03:02 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-09 17:02:48 | Katharagama (Menik Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-01-09 17:02:45 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:02:42 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 17:02:29 | Weraganthota (Mahaweli Ganga) | -1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:02:26 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:02:26 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-09 17:02:17 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 17:02:09 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:01:50 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:01:50 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | -0.010 |  |
| 2026-01-09 17:01:49 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:01:49 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-01-09 17:01:39 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -0.051 |  |
| 2026-01-09 17:01:37 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-01-09 17:01:35 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-09 17:01:29 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-09 17:00:57 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 17:00:39 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:00:21 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:00:13 | Manampitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.075 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-09 17:01:49 | Putupaula (Kalu Ganga) | 0.76 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-01-09 17:01:29 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-01-09 17:03:15 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-01-09 17:14:05 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-01-09 17:08:49 | Baddegama (Gin Ganga) | 0.89 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-09 17:00:57 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 17:02:42 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 17:13:03 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-09 17:02:17 | Horowpothana (Yan Oya) | 2.34 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-09 17:02:29 | Weraganthota (Mahaweli Ganga) | -1.20 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:01:50 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:00:21 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:00:21 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:02:26 | Yaka Wewa (Ma Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:04:19 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:11:12 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:02:09 | Magura (Kalu Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:02:45 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:11:39 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:07:52 | Glencourse (Kelani Ganga) | 8.55 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:03:06 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:00:39 | Dunamale (Aththanagalu Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:08:29 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:04:56 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:11:39 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:05:27 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:05:17 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:01:49 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:02:26 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-01-09 17:03:02 | Siyambalanduwa (Heda Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-09 17:01:50 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | -0.010 |  |
| 2026-01-09 17:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-01-09 17:01:37 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-01-09 17:03:59 | Thaldena (Mahaweli Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-01-09 17:01:35 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-09 17:02:48 | Katharagama (Menik Ganga) | 0.68 | 🟢 Normal | -0.020 |  |
| 2026-01-09 17:04:56 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.033 |  |
| 2026-01-09 17:01:39 | Moragaswewa (Deduru Oya) | 1.23 | 🟢 Normal | -0.051 |  |
| 2026-01-09 17:00:13 | Manampitiya (Mahaweli Ganga) | 2.50 | 🟢 Normal | -0.075 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)