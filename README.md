# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--03_17:11:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **35,680 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 17:11:58 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:06:44 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:06:28 | Manampitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:06:27 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-01-03 17:06:25 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:05:34 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.005 |  |
| 2026-01-03 17:05:19 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:04:57 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:04:46 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.119 |  |
| 2026-01-03 17:04:40 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:04:34 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-01-03 17:04:13 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 17:03:43 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:03:40 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:03:38 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:03:25 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:03:22 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-03 17:03:09 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-03 17:03:04 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.029 |  |
| 2026-01-03 17:03:00 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:02:51 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.021 |  |
| 2026-01-03 17:02:48 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:02:38 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:02:12 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.093 |  |
| 2026-01-03 17:02:07 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-03 17:01:44 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:01:38 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:01:26 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | -0.022 |  |
| 2026-01-03 17:01:12 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:01:11 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:00:51 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:00:50 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:00:43 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | -0.050 |  |
| 2026-01-03 17:00:35 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:00:05 | Galgamuwa (Mee Oya) | 2.52 | 🟢 Normal | -0.020 |  |
| 2026-01-03 16:53:08 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -0.012 |  |
| 2026-01-03 16:36:41 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-03 17:03:09 | Deraniyagala (Kelani Ganga) | 0.27 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-01-03 17:03:22 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-03 17:02:07 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-01-03 17:04:13 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-03 17:00:35 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:04:57 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:06:25 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:11:58 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:01:44 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:00:50 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:03:40 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-01-03 16:36:41 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:04:40 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-01-03 17:05:34 | Giriulla (Maha Oya) | 0.97 | 🟢 Normal | -0.005 |  |
| 2026-01-03 17:05:19 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:03:00 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:03:43 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:06:28 | Manampitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:02:38 | Siyambalanduwa (Heda Oya) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:01:38 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:03:25 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:00:51 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:03:38 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:02:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:06:44 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:02:48 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:01:11 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-01-03 17:01:12 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | -0.010 |  |
| 2026-01-03 16:53:08 | Horowpothana (Yan Oya) | 2.23 | 🟢 Normal | -0.012 |  |
| 2026-01-03 17:04:34 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-01-03 17:06:27 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.020 |  |
| 2026-01-03 17:00:05 | Galgamuwa (Mee Oya) | 2.52 | 🟢 Normal | -0.020 |  |
| 2026-01-03 16:08:47 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | -0.020 |  |
| 2026-01-03 17:02:51 | Thanamalwila (Kirindi Oya) | 1.05 | 🟢 Normal | -0.021 |  |
| 2026-01-03 17:01:26 | Moragaswewa (Deduru Oya) | 0.77 | 🟢 Normal | -0.022 |  |
| 2026-01-03 17:03:04 | Baddegama (Gin Ganga) | 1.10 | 🟢 Normal | -0.029 |  |
| 2026-01-03 17:00:43 | Weraganthota (Mahaweli Ganga) | -1.61 | 🟢 Normal | -0.050 |  |
| 2026-01-03 17:02:12 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.093 |  |
| 2026-01-03 17:04:46 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)