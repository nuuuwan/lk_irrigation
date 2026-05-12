# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_23:16:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,190 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 23:16:53 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.069 |  |
| 2026-05-12 23:14:14 | Glencourse (Kelani Ganga) | 10.59 | 🟢 Normal | 0.000 |  |
| 2026-05-12 23:10:16 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-12 23:09:06 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-12 23:07:52 | Hanwella (Kelani Ganga) | 2.05 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-12 23:06:37 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.040 |  |
| 2026-05-12 23:05:43 | Nakkala (Kumbukkan Oya) | 2.46 | 🟢 Normal | -0.778 |  |
| 2026-05-12 23:05:20 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.049 |  |
| 2026-05-12 23:05:14 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-12 23:05:01 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-12 23:04:45 | Rathnapura (Kalu Ganga) | 3.09 | 🟢 Normal | -0.107 |  |
| 2026-05-12 23:04:42 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-05-12 23:04:28 | Katharagama (Menik Ganga) | 1.62 | 🟢 Normal | -0.058 |  |
| 2026-05-12 23:04:24 | Panadugama (Nilwala Ganga) | 3.91 | 🟢 Normal | -0.078 |  |
| 2026-05-12 23:04:12 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | -0.012 |  |
| 2026-05-12 23:04:03 | Dunamale (Aththanagalu Oya) | 2.88 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-12 23:04:00 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-05-12 23:03:20 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-05-12 23:03:13 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-05-12 23:02:49 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.000 |  |
| 2026-05-12 23:02:32 | Siyambalanduwa (Heda Oya) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-05-12 23:02:20 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-05-12 23:02:16 | Thanamalwila (Kirindi Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-05-12 23:02:03 | Thaldena (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.170 |  |
| 2026-05-12 23:02:00 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-05-12 23:01:52 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-12 23:01:35 | Moragaswewa (Deduru Oya) | 1.39 | 🟢 Normal | -0.065 |  |
| 2026-05-12 23:01:27 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-12 23:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-05-12 23:01:18 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 23:01:06 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-12 23:01:01 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 23:02:00 | Ellagawa (Kalu Ganga) | 5.60 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-05-12 21:08:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.34 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-05-12 23:01:52 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-12 23:07:52 | Hanwella (Kelani Ganga) | 2.05 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-05-12 23:09:06 | Baddegama (Gin Ganga) | 1.94 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-05-12 23:04:03 | Dunamale (Aththanagalu Oya) | 2.88 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-12 22:04:38 | Putupaula (Kalu Ganga) | 0.95 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-12 23:01:27 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-05-12 23:01:06 | Peradeniya (Mahaweli Ganga) | 1.49 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-12 23:01:01 | Manampitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-12 18:00:31 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 23:04:00 | Wellawaya (Kirindi Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-05-12 23:01:18 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 23:14:14 | Glencourse (Kelani Ganga) | 10.59 | 🟢 Normal | 0.000 |  |
| 2026-05-12 23:02:49 | Badalgama (Maha Oya) | 2.71 | 🟢 Normal | 0.000 |  |
| 2026-05-12 23:10:16 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-12 23:03:20 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-05-12 23:02:32 | Siyambalanduwa (Heda Oya) | 2.69 | 🟢 Normal | -0.010 |  |
| 2026-05-12 23:05:14 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-05-12 22:01:39 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-05-12 23:02:16 | Thanamalwila (Kirindi Oya) | 1.85 | 🟢 Normal | -0.010 |  |
| 2026-05-12 23:03:13 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.010 |  |
| 2026-05-12 23:04:42 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-05-12 23:05:01 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-12 23:04:12 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | -0.012 |  |
| 2026-05-12 23:02:20 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-05-12 23:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-05-12 18:01:07 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-05-12 18:02:40 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.031 |  |
| 2026-05-12 23:06:37 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.040 |  |
| 2026-05-12 23:05:20 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | -0.049 |  |
| 2026-05-12 23:04:28 | Katharagama (Menik Ganga) | 1.62 | 🟢 Normal | -0.058 |  |
| 2026-05-12 23:01:35 | Moragaswewa (Deduru Oya) | 1.39 | 🟢 Normal | -0.065 |  |
| 2026-05-12 23:16:53 | Pitabeddara (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.069 |  |
| 2026-05-12 23:04:24 | Panadugama (Nilwala Ganga) | 3.91 | 🟢 Normal | -0.078 |  |
| 2026-05-12 21:05:06 | Magura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.085 |  |
| 2026-05-12 23:04:45 | Rathnapura (Kalu Ganga) | 3.09 | 🟢 Normal | -0.107 |  |
| 2026-05-12 23:02:03 | Thaldena (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.170 |  |
| 2026-05-12 23:05:43 | Nakkala (Kumbukkan Oya) | 2.46 | 🟢 Normal | -0.778 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)