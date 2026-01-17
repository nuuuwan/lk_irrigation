# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--18_03:03:31-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **48,563 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 03:03:31 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:03:28 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:03:18 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:02:16 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:02:04 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-18 03:01:56 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-18 03:01:49 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:01:44 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-01-18 03:01:40 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:01:39 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:01:35 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:01:19 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-01-18 03:01:08 | Peradeniya (Mahaweli Ganga) | 2.17 | 🟢 Normal | -0.192 |  |
| 2026-01-18 03:00:52 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:00:44 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:45:34 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:35:28 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:28:10 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:25:49 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:22:46 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:18:21 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:15:58 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:14:00 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-18 02:06:43 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:06:43 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 02:05:39 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-01-18 00:18:35 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-01-18 02:00:54 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-18 01:10:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-18 02:04:25 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-18 03:01:56 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-01-18 01:07:27 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-18 02:01:13 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-18 03:02:16 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:03:31 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:01:35 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:18:21 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:00:44 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:01:49 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-17 18:02:19 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-18 01:05:11 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:50:46 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:03:18 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:15:58 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:01:25 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:03:19 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-18 01:07:09 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:25:49 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:45:34 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:00:52 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:03:28 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:01:39 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:06:43 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:01:40 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:22:46 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:03:58 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:28:10 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-18 03:02:04 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-01-18 03:01:44 | Horowpothana (Yan Oya) | 1.48 | 🟢 Normal | -0.020 |  |
| 2026-01-18 03:01:19 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | -0.020 |  |
| 2026-01-17 18:02:02 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-01-17 18:01:12 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | -0.040 |  |
| 2026-01-18 02:02:46 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.096 |  |
| 2026-01-18 03:01:08 | Peradeniya (Mahaweli Ganga) | 2.17 | 🟢 Normal | -0.192 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)