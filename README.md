# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--08_06:32:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **119,244 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 06:32:52 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.001 |  |
| 2026-04-08 06:09:23 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:08:08 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:07:21 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.136 |  |
| 2026-04-08 06:07:17 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:07:12 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:06:54 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:06:27 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | -0.013 |  |
| 2026-04-08 06:06:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.007 |  |
| 2026-04-08 06:06:09 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.005 |  |
| 2026-04-08 06:05:36 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:05:22 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:05:19 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.067 |  |
| 2026-04-08 06:04:44 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:04:27 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | -0.003 |  |
| 2026-04-08 06:04:17 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:04:16 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:03:56 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.011 |  |
| 2026-04-08 06:03:55 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:03:52 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:03:42 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-08 06:03:37 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:03:21 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-04-08 06:03:20 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-08 06:03:13 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:02:39 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-08 06:02:36 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-08 06:02:28 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-08 06:02:24 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-08 06:02:22 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:02:08 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:02:07 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:02:04 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-04-08 06:01:28 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:01:15 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-08 06:01:06 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.798 |  |
| 2026-04-08 06:00:48 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -1.895 |  |
| 2026-04-08 06:00:34 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-08 06:00:30 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:00:29 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -1.895 |  |
| 2026-04-08 05:56:34 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-08 05:46:43 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-08 06:03:42 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-08 06:02:24 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-08 06:02:36 | Weraganthota (Mahaweli Ganga) | -2.63 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-08 06:00:34 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-08 06:01:15 | Rathnapura (Kalu Ganga) | 0.45 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-04-08 06:02:39 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-08 06:02:04 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-04-08 06:03:52 | Wellawaya (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:04:44 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:04:17 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:04:16 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:02:22 | Magura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:02:08 | Pitabeddara (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:07:12 | Hanwella (Kelani Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:03:37 | Deraniyagala (Kelani Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:09:23 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:03:13 | Panadugama (Nilwala Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:07:17 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:03:55 | Dunamale (Aththanagalu Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:05:22 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:05:36 | Thawalama (Gin Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:08:08 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:01:28 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-08 06:32:52 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.001 |  |
| 2026-04-08 06:04:27 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | -0.003 |  |
| 2026-04-08 06:06:09 | Moraketiya (Walawe Ganga) | 0.91 | 🟢 Normal | -0.005 |  |
| 2026-04-08 06:06:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.50 | 🟢 Normal | -0.007 |  |
| 2026-04-08 02:07:29 | Urawa (Nilwala Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-04-08 06:03:20 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-08 06:02:28 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-04-07 18:00:44 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-04-08 06:03:56 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | -0.011 |  |
| 2026-04-08 06:06:27 | Ellagawa (Kalu Ganga) | 3.91 | 🟢 Normal | -0.013 |  |
| 2026-04-08 06:03:21 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-04-08 06:05:19 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.067 |  |
| 2026-04-08 06:07:21 | Putupaula (Kalu Ganga) | 0.66 | 🟢 Normal | -0.136 |  |
| 2026-04-08 06:01:06 | Glencourse (Kelani Ganga) | 8.80 | 🟢 Normal | -0.798 |  |
| 2026-04-08 06:00:48 | Manampitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | -1.895 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)