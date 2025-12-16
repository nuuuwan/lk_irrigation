# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--16_23:07:04-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **19,876 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 23:07:04 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.009 |  |
| 2025-12-16 23:05:26 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.012 |  |
| 2025-12-16 23:05:15 | Yaka Wewa (Ma Oya) | 1.39 | 🟢 Normal | -0.020 |  |
| 2025-12-16 23:04:52 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-16 23:04:47 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 23:04:36 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-16 23:04:20 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.029 |  |
| 2025-12-16 23:04:04 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 23:03:54 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-16 23:03:48 | Hanwella (Kelani Ganga) | 1.11 | 🟢 Normal | -0.022 |  |
| 2025-12-16 23:03:41 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-16 23:03:38 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-16 23:03:33 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-16 23:03:25 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-16 23:03:04 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-16 23:02:48 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-16 23:02:38 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | -0.063 |  |
| 2025-12-16 23:02:37 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-16 23:02:35 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 23:02:12 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.010 |  |
| 2025-12-16 23:02:11 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-16 23:02:10 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-16 23:02:09 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 23:02:02 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-16 23:01:38 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-16 23:01:32 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 23:01:17 | Ellagawa (Kalu Ganga) | 4.77 | 🟢 Normal | -0.010 |  |
| 2025-12-16 23:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-16 23:00:27 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:28:56 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.007 |  |
| 2025-12-16 22:23:42 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:14:39 | Rathnapura (Kalu Ganga) | 1.28 | 🟢 Normal | -0.012 |  |
| 2025-12-16 22:12:18 | Glencourse (Kelani Ganga) | 9.20 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-16 22:10:18 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:09:53 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.013 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-16 22:00:43 | Horowpothana (Yan Oya) | 6.04 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2025-12-16 23:03:41 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2025-12-16 23:01:38 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2025-12-16 23:03:33 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2025-12-16 23:02:48 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2025-12-16 21:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.10 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2025-12-16 23:04:52 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-16 23:02:11 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2025-12-16 22:07:49 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 23:01:32 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 23:02:35 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 23:04:04 | Thaldena (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-16 23:02:02 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2025-12-16 23:03:38 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2025-12-16 23:02:10 | Giriulla (Maha Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2025-12-16 18:04:31 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2025-12-16 23:03:04 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-16 23:03:25 | Padiyathalawa (Maduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2025-12-16 23:04:47 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-16 23:02:37 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2025-12-16 23:04:36 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2025-12-16 23:00:27 | Kuda Oya (Kirindi Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-16 23:02:09 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2025-12-16 22:28:56 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.007 |  |
| 2025-12-16 23:07:04 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.009 |  |
| 2025-12-16 23:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2025-12-16 23:01:17 | Ellagawa (Kalu Ganga) | 4.77 | 🟢 Normal | -0.010 |  |
| 2025-12-16 22:05:17 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.010 |  |
| 2025-12-16 23:03:54 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | -0.010 |  |
| 2025-12-16 23:02:12 | Peradeniya (Mahaweli Ganga) | 2.76 | 🟢 Normal | -0.010 |  |
| 2025-12-16 23:05:26 | Rathnapura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.012 |  |
| 2025-12-16 22:09:53 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | -0.013 |  |
| 2025-12-16 23:05:15 | Yaka Wewa (Ma Oya) | 1.39 | 🟢 Normal | -0.020 |  |
| 2025-12-16 23:03:48 | Hanwella (Kelani Ganga) | 1.11 | 🟢 Normal | -0.022 |  |
| 2025-12-16 22:03:58 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.025 |  |
| 2025-12-16 23:04:20 | Manampitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.029 |  |
| 2025-12-16 23:02:38 | Katharagama (Menik Ganga) | 0.24 | 🟢 Normal | -0.063 |  |
| 2025-12-16 18:03:31 | Thanthirimale (Malwathu Oya) | 3.20 | 🟢 Normal | -0.101 |  |
| 2025-12-16 18:05:13 | Weraganthota (Mahaweli Ganga) | -1.30 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)