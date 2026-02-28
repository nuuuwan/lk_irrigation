# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--28_12:57:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **85,343 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-28 12:57:06 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:14:24 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:13:09 | Padiyathalawa (Maduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:10:48 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-02-28 12:09:51 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:09:28 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-28 12:08:29 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:08:01 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:08:00 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:06:35 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-28 12:06:26 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:05:49 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:05:38 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:05:34 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-02-28 12:05:16 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:05:10 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:04:24 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:04:12 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:04:11 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-02-28 12:03:33 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:03:15 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-02-28 12:02:59 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:02:52 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-28 12:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-02-28 12:02:37 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-02-28 12:02:21 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:02:18 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:02:14 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-02-28 12:02:11 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-02-28 12:01:58 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-28 12:01:05 | Pitabeddara (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.708 | 🔺 Rising |
| 2026-02-28 12:03:15 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-02-28 12:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.66 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-02-28 12:01:42 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-02-28 12:06:35 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-02-28 12:01:41 | Dunamale (Aththanagalu Oya) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-28 12:09:28 | Manampitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-28 12:03:33 | Weraganthota (Mahaweli Ganga) | -1.65 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:04:12 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:01:02 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:14:24 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:01:41 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:05:16 | Horowpothana (Yan Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:08:00 | Magura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:05:10 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:05:49 | Ellagawa (Kalu Ganga) | 3.97 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:09:51 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:13:09 | Padiyathalawa (Maduru Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:01:58 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:00:40 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:01:30 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:06:26 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:08:01 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:02:59 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:02:21 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:02:18 | Peradeniya (Mahaweli Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:04:24 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:05:38 | Thalgahagoda (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:57:06 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:08:29 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-28 12:10:48 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | -0.009 |  |
| 2026-02-28 12:02:52 | Nawalapitiya (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-02-28 12:01:34 | Deraniyagala (Kelani Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-02-28 12:02:14 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | -0.010 |  |
| 2026-02-28 12:02:11 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.011 |  |
| 2026-02-28 12:05:34 | Rathnapura (Kalu Ganga) | 0.61 | 🟢 Normal | -0.011 |  |
| 2026-02-28 12:02:37 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | -0.020 |  |
| 2026-02-28 12:04:11 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-02-28 12:01:20 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.021 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)