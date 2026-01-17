# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--17_22:31:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **48,415 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 22:31:09 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.030 |  |
| 2026-01-17 22:16:32 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:15:59 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:15:16 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:14:16 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:10:00 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.017 |  |
| 2026-01-17 22:07:37 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.353 | 🔺 Rising |
| 2026-01-17 22:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-01-17 22:05:54 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-17 22:05:47 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-17 22:05:29 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:04:39 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:04:17 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:04:13 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.353 | 🔺 Rising |
| 2026-01-17 22:03:57 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:03:02 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:02:53 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:02:47 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:02:45 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.365 | 🔺 Rising |
| 2026-01-17 22:02:44 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-17 22:02:43 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:02:40 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:02:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.021 |  |
| 2026-01-17 22:02:36 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:02:32 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:02:19 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-17 22:02:16 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:02:11 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-17 22:01:59 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:01:47 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:01:42 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:01:27 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:01:14 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:01:11 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:01:09 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:00:53 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-17 22:02:45 | Peradeniya (Mahaweli Ganga) | 1.81 | 🟢 Normal | 0.365 | 🔺 Rising |
| 2026-01-17 22:07:37 | Rathnapura (Kalu Ganga) | 0.57 | 🟢 Normal | 0.353 | 🔺 Rising |
| 2026-01-17 22:05:47 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-17 22:02:11 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-17 22:02:44 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-17 22:05:54 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-17 22:01:09 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:04:17 | Nakkala (Kumbukkan Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:01:59 | Moragaswewa (Deduru Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:02:43 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:00:53 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:01:27 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-01-17 18:02:19 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:01:14 | Magura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:15:16 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:02:53 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:02:47 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:03:57 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:01:47 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:15:59 | Panadugama (Nilwala Ganga) | 2.18 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:02:32 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:01:42 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:02:36 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:03:02 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:04:39 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:02:16 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:05:29 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:16:32 | Thawalama (Gin Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:14:16 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:01:11 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:02:40 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-17 22:02:19 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-01-17 21:04:09 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-01-17 22:10:00 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.017 |  |
| 2026-01-17 22:06:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.47 | 🟢 Normal | -0.020 |  |
| 2026-01-17 18:02:02 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-01-17 22:02:40 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.021 |  |
| 2026-01-17 22:31:09 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.030 |  |
| 2026-01-17 18:01:12 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)