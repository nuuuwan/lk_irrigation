# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--28_12:05:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **137,298 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 12:05:29 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | -0.058 |  |
| 2026-04-28 12:04:32 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:04:22 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-04-28 12:03:48 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 12:03:40 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:03:27 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.016 |  |
| 2026-04-28 12:03:27 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-28 12:03:14 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:03:09 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:03:04 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:03:03 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | -0.050 |  |
| 2026-04-28 12:02:55 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.020 |  |
| 2026-04-28 12:02:52 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:02:50 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.072 |  |
| 2026-04-28 12:02:37 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 12:02:36 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:02:35 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:02:33 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.112 |  |
| 2026-04-28 12:02:27 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:02:17 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:02:15 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:01:59 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:01:56 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-04-28 12:01:53 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-28 12:01:24 | Thanthirimale (Malwathu Oya) | 2.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-28 12:01:24 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:01:00 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-28 12:00:54 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-28 12:00:47 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-28 12:00:18 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.020 |  |
| 2026-04-28 11:58:50 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 11:46:13 | Manampitiya (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.072 |  |
| 2026-04-28 11:32:29 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-28 11:25:45 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | -0.016 |  |
| 2026-04-28 11:14:41 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-28 11:13:48 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-28 11:13:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.15 | 🟢 Normal | -0.061 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-28 11:01:51 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-04-28 12:01:00 | Putupaula (Kalu Ganga) | 0.78 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-04-28 12:00:47 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-04-28 11:06:23 | Panadugama (Nilwala Ganga) | 2.79 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-04-28 12:01:24 | Thanthirimale (Malwathu Oya) | 2.10 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-28 11:00:49 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-28 12:03:27 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-28 12:03:48 | Baddegama (Gin Ganga) | 1.81 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-28 12:02:37 | Padiyathalawa (Maduru Oya) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-28 12:02:36 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:02:17 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:03:04 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-28 11:58:50 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:02:35 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:02:27 | Ellagawa (Kalu Ganga) | 4.57 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:03:14 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:03:40 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:01:24 | Peradeniya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:04:32 | Urawa (Nilwala Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:03:09 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:02:15 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-04-28 12:04:22 | Nawalapitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-04-28 10:08:17 | Rathnapura (Kalu Ganga) | 1.32 | 🟢 Normal | -0.010 |  |
| 2026-04-28 12:01:53 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-04-28 12:01:56 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-04-28 12:00:54 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.010 |  |
| 2026-04-28 11:06:09 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.011 |  |
| 2026-04-28 11:01:27 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-04-28 12:03:27 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.016 |  |
| 2026-04-28 12:00:18 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.020 |  |
| 2026-04-28 12:02:55 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | -0.020 |  |
| 2026-04-28 12:03:03 | Hanwella (Kelani Ganga) | 1.13 | 🟢 Normal | -0.050 |  |
| 2026-04-28 11:11:14 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.050 |  |
| 2026-04-28 12:05:29 | Glencourse (Kelani Ganga) | 8.87 | 🟢 Normal | -0.058 |  |
| 2026-04-28 11:13:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.15 | 🟢 Normal | -0.061 |  |
| 2026-04-28 12:02:50 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | -0.072 |  |
| 2026-04-28 11:09:55 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.073 |  |
| 2026-04-28 11:04:41 | Magura (Kalu Ganga) | 1.37 | 🟢 Normal | -0.088 |  |
| 2026-04-28 12:02:33 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)