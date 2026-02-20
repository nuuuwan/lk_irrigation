# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--20_16:13:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,303 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 16:13:57 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-02-20 16:11:36 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:09:34 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:08:11 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-02-20 16:08:06 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-20 16:06:02 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-02-20 16:05:46 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 16:05:16 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-02-20 16:05:06 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-02-20 16:04:50 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-20 16:04:40 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-02-20 16:04:08 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-20 16:04:04 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:03:56 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:03:55 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:03:20 | Padiyathalawa (Maduru Oya) | 1.93 | 🟢 Normal | -0.124 |  |
| 2026-02-20 16:03:01 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:03:01 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-02-20 16:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-02-20 16:03:00 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:02:42 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:02:38 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:02:33 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-02-20 16:02:31 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-02-20 16:02:22 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:02:20 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:02:20 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:02:18 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.095 |  |
| 2026-02-20 16:02:06 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-20 16:01:41 | Weraganthota (Mahaweli Ganga) | -1.20 | 🟢 Normal | -0.219 |  |
| 2026-02-20 16:01:35 | Dunamale (Aththanagalu Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 16:01:25 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:01:21 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-20 16:01:00 | Manampitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-02-20 15:21:17 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-20 16:04:40 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-02-20 15:12:20 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-02-20 16:05:16 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-02-20 16:04:50 | Glencourse (Kelani Ganga) | 8.32 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-02-20 16:01:00 | Manampitiya (Mahaweli Ganga) | 2.80 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-02-20 16:08:06 | Hanwella (Kelani Ganga) | 0.40 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-20 16:01:21 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-20 16:02:06 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-20 16:04:08 | Ellagawa (Kalu Ganga) | 4.03 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-20 16:01:35 | Dunamale (Aththanagalu Oya) | 0.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 16:05:46 | Deraniyagala (Kelani Ganga) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-20 16:01:25 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:03:00 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:01:35 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:11:36 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:03:45 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:02:20 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:00:14 | Baddegama (Gin Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:03:56 | Panadugama (Nilwala Ganga) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:02:22 | Siyambalanduwa (Heda Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:03:55 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:02:42 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:04:04 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-02-20 15:21:17 | Rathnapura (Kalu Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:02:38 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:03:01 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:09:34 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:02:20 | Thanamalwila (Kirindi Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-02-20 16:13:57 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.009 |  |
| 2026-02-20 16:08:11 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-02-20 16:05:06 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.009 |  |
| 2026-02-20 16:03:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.08 | 🟢 Normal | -0.010 |  |
| 2026-02-20 16:02:33 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | -0.010 |  |
| 2026-02-20 16:06:02 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-02-20 16:02:31 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-02-20 16:03:01 | Magura (Kalu Ganga) | 1.22 | 🟢 Normal | -0.020 |  |
| 2026-02-20 16:02:18 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.095 |  |
| 2026-02-20 16:03:20 | Padiyathalawa (Maduru Oya) | 1.93 | 🟢 Normal | -0.124 |  |
| 2026-02-20 16:01:41 | Weraganthota (Mahaweli Ganga) | -1.20 | 🟢 Normal | -0.219 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)