# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--25_00:15:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **82,220 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 00:15:50 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:13:58 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-25 00:09:42 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:06:32 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:06:29 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:06:07 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-25 00:05:29 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:05:18 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-02-25 00:05:04 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.019 |  |
| 2026-02-25 00:05:03 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-25 00:04:47 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:04:35 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:03:44 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-25 00:03:39 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:03:15 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:03:12 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-25 00:03:11 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:02:52 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:02:47 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:02:47 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:02:46 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.060 |  |
| 2026-02-25 00:02:40 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-02-25 00:02:24 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.011 |  |
| 2026-02-25 00:02:24 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.049 |  |
| 2026-02-25 00:02:16 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | 0.293 | 🔺 Rising |
| 2026-02-25 00:02:16 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:01:57 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 21.600 | 🔺 Rising |
| 2026-02-25 00:01:47 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 21.600 | 🔺 Rising |
| 2026-02-25 00:01:45 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:01:42 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-02-25 00:01:24 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:01:14 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:01:11 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:01:04 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.012 |  |
| 2026-02-25 00:00:47 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-25 00:01:57 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 21.600 | 🔺 Rising |
| 2026-02-25 00:02:16 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | 0.293 | 🔺 Rising |
| 2026-02-25 00:13:58 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-02-25 00:03:12 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-25 00:05:03 | Baddegama (Gin Ganga) | 1.05 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-25 00:06:07 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-25 00:05:29 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:02:47 | Nakkala (Kumbukkan Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:00:47 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:01:42 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:02:16 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-24 18:03:16 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:01:11 | Magura (Kalu Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:06:20 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-24 23:02:44 | Norwood (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:06:32 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:15:50 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:09:42 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:02:52 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:03:11 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:04:47 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:03:39 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:02:47 | Manampitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:06:29 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:03:15 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:01:24 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-02-25 00:05:18 | Thanamalwila (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-02-25 00:02:40 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-02-25 00:01:39 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-02-25 00:03:44 | Rathnapura (Kalu Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-02-25 00:02:24 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.011 |  |
| 2026-02-25 00:01:04 | Padiyathalawa (Maduru Oya) | 0.98 | 🟢 Normal | -0.012 |  |
| 2026-02-24 23:05:23 | Dunamale (Aththanagalu Oya) | 0.35 | 🟢 Normal | -0.014 |  |
| 2026-02-25 00:05:04 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.019 |  |
| 2026-02-24 23:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.92 | 🟢 Normal | -0.027 |  |
| 2026-02-24 18:01:47 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.030 |  |
| 2026-02-24 18:06:10 | Weraganthota (Mahaweli Ganga) | -2.27 | 🟢 Normal | -0.045 |  |
| 2026-02-25 00:02:24 | Glencourse (Kelani Ganga) | 8.35 | 🟢 Normal | -0.049 |  |
| 2026-02-25 00:02:46 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.060 |  |

## River Water Level Charts by Station

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)