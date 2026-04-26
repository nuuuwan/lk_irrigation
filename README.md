# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_21:22:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **135,880 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 21:22:22 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:08:54 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:08:05 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:07:50 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:06:56 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -18.000 |  |
| 2026-04-26 21:06:54 | Thanamalwila (Kirindi Oya) | 0.81 | 🟢 Normal | -18.000 |  |
| 2026-04-26 21:06:40 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:06:28 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-26 21:06:17 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-04-26 21:06:17 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-26 21:05:49 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-26 21:05:41 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-26 21:05:34 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-04-26 21:05:28 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:04:27 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-26 21:04:04 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:03:55 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.069 |  |
| 2026-04-26 21:03:37 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:03:19 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-04-26 21:02:48 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:02:45 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:02:41 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-26 21:02:30 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:02:23 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:02:13 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-26 21:02:09 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.112 |  |
| 2026-04-26 21:01:55 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:01:54 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-26 21:01:52 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:01:42 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:01:39 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-04-26 21:01:29 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.081 |  |
| 2026-04-26 21:01:20 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.034 |  |
| 2026-04-26 21:00:34 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:00:32 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.050 |  |
| 2026-04-26 21:00:12 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 21:03:19 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-04-26 21:04:27 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-04-26 21:05:49 | Glencourse (Kelani Ganga) | 8.86 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-26 21:02:13 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-26 21:01:54 | Pitabeddara (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-26 21:06:28 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-26 21:02:41 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-26 21:06:17 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-26 21:05:41 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-26 18:00:28 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:00:12 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:02:23 | Moragaswewa (Deduru Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:01:42 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:07:50 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:02:48 | Horowpothana (Yan Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:02:30 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:01:52 | Ellagawa (Kalu Ganga) | 4.25 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:08:54 | Panadugama (Nilwala Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:00:34 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:01:55 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:03:37 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:22:22 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:02:45 | Katharagama (Menik Ganga) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:06:40 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:08:05 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:05:28 | Rathnapura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-26 21:04:04 | Kuda Oya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-04-26 18:06:09 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | -0.009 |  |
| 2026-04-26 21:06:17 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-04-26 21:05:34 | Hanwella (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-04-26 18:03:51 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | -0.029 |  |
| 2026-04-26 21:01:39 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.031 |  |
| 2026-04-26 21:01:20 | Peradeniya (Mahaweli Ganga) | 1.33 | 🟢 Normal | -0.034 |  |
| 2026-04-26 21:00:32 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.050 |  |
| 2026-04-26 21:03:55 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.069 |  |
| 2026-04-26 21:01:29 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.081 |  |
| 2026-04-26 21:02:09 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.112 |  |
| 2026-04-26 20:08:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.78 | 🟢 Normal | -0.123 |  |
| 2026-04-26 21:06:56 | Thanamalwila (Kirindi Oya) | 0.80 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)