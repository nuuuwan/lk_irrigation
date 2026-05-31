# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--31_16:05:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **166,737 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 16:05:48 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-31 16:05:07 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-05-31 16:04:05 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:03:58 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:03:44 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:03:20 | Hanwella (Kelani Ganga) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-05-31 16:03:16 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:03:10 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:03:08 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:03:02 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 16:02:59 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-31 16:02:40 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:02:21 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:02:20 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-05-31 16:02:19 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-05-31 16:02:12 | Glencourse (Kelani Ganga) | 10.07 | 🟢 Normal | -0.081 |  |
| 2026-05-31 16:01:58 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | -0.012 |  |
| 2026-05-31 16:01:47 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:01:29 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-05-31 16:01:16 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:01:11 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-31 16:01:09 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | -0.072 |  |
| 2026-05-31 16:01:06 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:00:30 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:00:14 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-31 16:05:07 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-05-31 16:01:11 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-05-31 15:03:38 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-31 15:08:03 | Magura (Kalu Ganga) | 2.25 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-31 16:03:02 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-31 16:01:16 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:02:40 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:02:38 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:01:49 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:01:06 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:02:21 | Galgamuwa (Mee Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:01:47 | Pitabeddara (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:03:10 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:00:12 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:03:44 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:04:05 | Katharagama (Menik Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:03:58 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:04:37 | Holombuwa (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:03:08 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:00:30 | Thanthirimale (Malwathu Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:13:07 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-31 16:03:16 | Thalgahagoda (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-31 15:09:54 | Panadugama (Nilwala Ganga) | 2.81 | 🟢 Normal | -0.009 |  |
| 2026-05-31 16:00:14 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | -0.010 |  |
| 2026-05-31 16:05:48 | Thanamalwila (Kirindi Oya) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-05-31 15:02:52 | Giriulla (Maha Oya) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-05-31 16:02:59 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-05-31 16:03:20 | Hanwella (Kelani Ganga) | 2.25 | 🟢 Normal | -0.010 |  |
| 2026-05-31 16:01:29 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-05-31 16:01:58 | Moragaswewa (Deduru Oya) | 0.28 | 🟢 Normal | -0.012 |  |
| 2026-05-31 16:02:19 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-05-31 16:02:20 | Deraniyagala (Kelani Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-05-31 15:03:47 | Peradeniya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.021 |  |
| 2026-05-31 15:00:08 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | -0.028 |  |
| 2026-05-31 15:07:02 | Rathnapura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.028 |  |
| 2026-05-31 15:03:23 | Ellagawa (Kalu Ganga) | 5.91 | 🟢 Normal | -0.031 |  |
| 2026-05-31 16:01:09 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | -0.072 |  |
| 2026-05-31 16:02:12 | Glencourse (Kelani Ganga) | 10.07 | 🟢 Normal | -0.081 |  |
| 2026-05-31 15:09:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.65 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)