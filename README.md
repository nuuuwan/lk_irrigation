# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--18_13:05:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **76,404 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 13:05:06 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 13:04:32 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-02-18 13:04:24 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:04:10 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:04:00 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-18 13:03:34 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:03:29 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:03:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-02-18 13:03:15 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-18 13:02:50 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:02:49 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-02-18 13:02:49 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:02:41 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:02:35 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.078 |  |
| 2026-02-18 13:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:02:24 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-18 13:02:15 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-02-18 13:02:13 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-18 13:02:11 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:02:10 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-02-18 13:02:00 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:01:54 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:01:31 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:01:29 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:01:17 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | -0.052 |  |
| 2026-02-18 13:01:11 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-18 13:00:46 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-18 12:59:35 | Padiyathalawa (Maduru Oya) | 1.86 | 🟢 Normal | -0.162 |  |
| 2026-02-18 12:23:03 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-18 12:16:30 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.078 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-18 13:04:32 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-02-18 12:04:52 | Manampitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.131 | 🔺 Rising |
| 2026-02-18 13:03:25 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-02-18 13:02:49 | Peradeniya (Mahaweli Ganga) | 1.28 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-02-18 13:00:46 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-18 13:02:24 | Deraniyagala (Kelani Ganga) | 0.09 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-18 13:02:13 | Nakkala (Kumbukkan Oya) | 0.90 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-18 13:04:00 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-18 13:05:06 | Pitabeddara (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 12:05:12 | Thawalama (Gin Ganga) | 1.00 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-18 13:02:41 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:02:49 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:02:11 | Moragaswewa (Deduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:04:10 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:01:29 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:02:50 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:01:54 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:02:00 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:04:24 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-18 12:02:17 | Ellagawa (Kalu Ganga) | 3.84 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:03:34 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-02-18 12:03:46 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-18 12:02:13 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-18 12:07:31 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:03:29 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:01:31 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-18 12:23:03 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-18 13:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-02-18 12:07:05 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-02-18 13:02:15 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-02-18 13:01:11 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-02-18 13:03:15 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-18 13:02:10 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | -0.011 |  |
| 2026-02-18 12:03:56 | Glencourse (Kelani Ganga) | 8.23 | 🟢 Normal | -0.019 |  |
| 2026-02-18 12:06:47 | Rathnapura (Kalu Ganga) | 0.48 | 🟢 Normal | -0.020 |  |
| 2026-02-18 11:04:16 | Thaldena (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.021 |  |
| 2026-02-18 13:01:17 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | -0.052 |  |
| 2026-02-18 13:02:35 | Baddegama (Gin Ganga) | 1.02 | 🟢 Normal | -0.078 |  |
| 2026-02-18 12:59:35 | Padiyathalawa (Maduru Oya) | 1.86 | 🟢 Normal | -0.162 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)