# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--18_02:45:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **48,548 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 02:45:34 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:35:28 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:28:10 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:25:49 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:22:46 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:18:21 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:15:58 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:14:00 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -6.383 |  |
| 2026-01-18 02:06:43 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:06:43 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:05:39 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-01-18 02:05:27 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:05:24 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:04:57 | Peradeniya (Mahaweli Ganga) | 2.35 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-18 02:04:39 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:04:25 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-18 02:03:58 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:03:34 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:03:19 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:03:17 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | -6.383 |  |
| 2026-01-18 02:02:46 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.096 |  |
| 2026-01-18 02:02:34 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-01-18 02:02:16 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-01-18 02:02:05 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:01:34 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | -0.012 |  |
| 2026-01-18 02:01:28 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:01:26 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.022 |  |
| 2026-01-18 02:01:25 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:01:13 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-18 02:01:08 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:01:03 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 02:00:54 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-18 02:05:39 | Glencourse (Kelani Ganga) | 8.61 | 🟢 Normal | 0.224 | 🔺 Rising |
| 2026-01-18 00:18:35 | Putupaula (Kalu Ganga) | 0.61 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-01-18 02:04:57 | Peradeniya (Mahaweli Ganga) | 2.35 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-01-18 02:00:54 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-18 01:10:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.60 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-18 02:04:25 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-01-18 02:01:03 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-18 01:07:27 | Rathnapura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-01-18 02:01:13 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-01-18 02:04:39 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:06:43 | Nakkala (Kumbukkan Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:02:05 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:18:21 | Nawalapitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:01:28 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-17 18:02:19 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-01-18 01:05:11 | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-01-18 00:50:46 | Pitabeddara (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:03:34 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:15:58 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:01:25 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:03:19 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-01-18 01:07:09 | Padiyathalawa (Maduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:25:49 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:45:34 | Dunamale (Aththanagalu Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:05:27 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:01:08 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:06:43 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:35:28 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:22:46 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:03:58 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:28:10 | Thanamalwila (Kirindi Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-01-18 02:02:16 | Kithulgala (Kelani Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-01-18 02:01:34 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | -0.012 |  |
| 2026-01-18 02:02:34 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-01-17 18:02:02 | Thanthirimale (Malwathu Oya) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-01-18 02:01:26 | Manampitiya (Mahaweli Ganga) | 1.10 | 🟢 Normal | -0.022 |  |
| 2026-01-17 18:01:12 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | -0.040 |  |
| 2026-01-18 02:02:46 | Moraketiya (Walawe Ganga) | 0.80 | 🟢 Normal | -0.096 |  |
| 2026-01-18 02:14:00 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -6.383 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)