# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--07_00:05:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **118,142 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 00:05:37 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-07 00:05:24 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -36.000 |  |
| 2026-04-07 00:05:23 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-07 00:05:22 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | -36.000 |  |
| 2026-04-07 00:05:20 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-07 00:05:20 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 00:05:20 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-07 00:04:48 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-07 00:03:59 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-07 00:03:54 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-07 00:03:18 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-07 00:03:04 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-07 00:02:47 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-07 00:02:41 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-07 00:02:26 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-07 00:02:15 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-07 00:02:06 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-07 00:02:00 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-04-07 00:01:39 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-07 00:01:35 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 00:01:29 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-07 00:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-07 00:01:00 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-06 23:54:59 | Dunamale (Aththanagalu Oya) | 0.41 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-06 23:51:02 | Wellawaya (Kirindi Oya) | 0.82 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-06 23:35:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-07 00:02:00 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.130 | 🔺 Rising |
| 2026-04-07 00:05:20 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-07 00:05:23 | Wellawaya (Kirindi Oya) | 0.83 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-04-07 00:01:00 | Glencourse (Kelani Ganga) | 8.66 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-07 00:02:41 | Giriulla (Maha Oya) | 1.09 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-07 00:03:54 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-07 00:02:15 | Hanwella (Kelani Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-06 23:04:17 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-07 00:03:59 | Ellagawa (Kalu Ganga) | 4.17 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-07 00:05:37 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-07 00:01:35 | Kuda Oya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 00:05:20 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-07 00:05:20 | Thanamalwila (Kirindi Oya) | 0.35 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-07 00:02:26 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-07 00:02:47 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-07 00:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-06 23:01:39 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-07 00:02:06 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:00:26 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-06 23:10:22 | Magura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 23:03:17 | Pitabeddara (Nilwala Ganga) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-06 23:07:15 | Panadugama (Nilwala Ganga) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-04-07 00:01:29 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-06 23:02:35 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-04-07 00:01:39 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-07 00:04:48 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 23:06:16 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-07 00:03:18 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-07 00:03:04 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-06 23:35:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-06 18:01:18 | Thanthirimale (Malwathu Oya) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-04-06 23:02:42 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.011 |  |
| 2026-04-06 23:11:12 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | -0.027 |  |
| 2026-04-06 23:05:51 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.031 |  |
| 2026-04-06 23:04:51 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.048 |  |
| 2026-04-06 18:01:26 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.079 |  |
| 2026-04-06 23:09:09 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | -0.082 |  |
| 2026-04-06 23:11:19 | Putupaula (Kalu Ganga) | 0.23 | 🟢 Normal | -0.133 |  |
| 2026-04-07 00:05:24 | Rathnapura (Kalu Ganga) | 0.51 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)