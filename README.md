# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--13_06:29:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,217 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 06:29:53 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.005 |  |
| 2026-01-13 06:29:35 | Thanthirimale (Malwathu Oya) | 2.50 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-13 06:25:33 | Weraganthota (Mahaweli Ganga) | -1.38 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-01-13 06:17:52 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:16:09 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:10:23 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-01-13 06:09:53 | Hanwella (Kelani Ganga) | 0.94 | 🟢 Normal | -0.028 |  |
| 2026-01-13 06:08:53 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:06:36 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:06:29 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-13 06:06:29 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:05:16 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:05:05 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.106 |  |
| 2026-01-13 06:04:48 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-01-13 06:04:34 | Horowpothana (Yan Oya) | 3.54 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-13 06:04:18 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-13 06:04:13 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.009 |  |
| 2026-01-13 06:04:10 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.025 |  |
| 2026-01-13 06:04:06 | Baddegama (Gin Ganga) | 0.76 | 🟢 Normal | -0.033 |  |
| 2026-01-13 06:04:00 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:03:19 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-13 06:03:15 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:02:51 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-01-13 06:02:49 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.099 |  |
| 2026-01-13 06:02:45 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.051 |  |
| 2026-01-13 06:02:43 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.021 |  |
| 2026-01-13 06:02:43 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-01-13 06:02:41 | Magura (Kalu Ganga) | 0.99 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-01-13 06:02:15 | Glencourse (Kelani Ganga) | 9.16 | 🟢 Normal | -0.022 |  |
| 2026-01-13 06:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.054 |  |
| 2026-01-13 06:01:46 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:01:45 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:01:40 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:01:35 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:01:27 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:01:16 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:01:09 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:00:58 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.064 |  |
| 2026-01-13 06:00:38 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-01-13 06:00:28 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-13 05:42:17 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-13 06:02:43 | Magura (Kalu Ganga) | 1.04 | 🟢 Normal | 90.000 | 🔺 Rising |
| 2026-01-13 06:03:19 | Deraniyagala (Kelani Ganga) | 0.28 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-01-13 06:10:23 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-01-13 06:29:35 | Thanthirimale (Malwathu Oya) | 2.50 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-01-13 06:04:34 | Horowpothana (Yan Oya) | 3.54 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-01-13 06:04:18 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-13 06:06:29 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-13 05:02:50 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-13 06:25:33 | Weraganthota (Mahaweli Ganga) | -1.38 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-01-13 06:01:09 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:04:00 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:00:28 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-01-13 02:03:15 | Yaka Wewa (Ma Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:01:46 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:03:15 | Ellagawa (Kalu Ganga) | 4.09 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:08:53 | Panadugama (Nilwala Ganga) | 2.23 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:01:35 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:01:16 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:06:36 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:05:16 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:17:52 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:01:40 | Rathnapura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:16:09 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:01:27 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-13 06:29:53 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | -0.005 |  |
| 2026-01-13 06:04:48 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.009 |  |
| 2026-01-13 06:04:13 | Manampitiya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.009 |  |
| 2026-01-13 06:02:51 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-01-13 06:02:43 | Badalgama (Maha Oya) | 2.27 | 🟢 Normal | -0.021 |  |
| 2026-01-13 06:00:38 | Siyambalanduwa (Heda Oya) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-01-13 06:02:15 | Glencourse (Kelani Ganga) | 9.16 | 🟢 Normal | -0.022 |  |
| 2026-01-13 06:04:10 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.025 |  |
| 2026-01-13 06:09:53 | Hanwella (Kelani Ganga) | 0.94 | 🟢 Normal | -0.028 |  |
| 2026-01-13 06:04:06 | Baddegama (Gin Ganga) | 0.76 | 🟢 Normal | -0.033 |  |
| 2026-01-13 06:02:45 | Dunamale (Aththanagalu Oya) | 1.36 | 🟢 Normal | -0.051 |  |
| 2026-01-13 06:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.054 |  |
| 2026-01-13 06:00:58 | Nakkala (Kumbukkan Oya) | 1.30 | 🟢 Normal | -0.064 |  |
| 2026-01-13 06:02:49 | Peradeniya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.099 |  |
| 2026-01-13 06:05:05 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.106 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)