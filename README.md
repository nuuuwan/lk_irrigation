# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--12_09:12:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **43,444 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 09:12:01 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.009 |  |
| 2026-01-12 09:11:03 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.016 |  |
| 2026-01-12 09:09:52 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | -0.048 |  |
| 2026-01-12 09:08:25 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:08:24 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-01-12 09:07:46 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | 1.366 | 🔺 Rising |
| 2026-01-12 09:07:35 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:07:20 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-12 09:07:07 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.042 |  |
| 2026-01-12 09:07:01 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:06:45 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:06:34 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.024 |  |
| 2026-01-12 09:06:13 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.028 |  |
| 2026-01-12 09:05:31 | Hanwella (Kelani Ganga) | 1.61 | 🟢 Normal | -0.019 |  |
| 2026-01-12 09:04:18 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:04:12 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:03:15 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-12 09:03:05 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.030 |  |
| 2026-01-12 09:03:02 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:02:48 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-12 09:02:47 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | -0.011 |  |
| 2026-01-12 09:02:42 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-01-12 09:02:28 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-12 09:02:27 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-12 09:02:26 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.040 |  |
| 2026-01-12 09:02:03 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.030 |  |
| 2026-01-12 09:02:01 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-12 09:01:46 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:01:38 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:01:31 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:01:18 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-12 09:01:11 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.033 |  |
| 2026-01-12 09:01:08 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:00:55 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.032 |  |
| 2026-01-12 09:00:51 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-12 09:00:33 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-01-12 09:00:21 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-12 09:07:46 | Glencourse (Kelani Ganga) | 9.70 | 🟢 Normal | 1.366 | 🔺 Rising |
| 2026-01-12 09:00:33 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.217 | 🔺 Rising |
| 2026-01-12 09:03:15 | Deraniyagala (Kelani Ganga) | 0.44 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-12 09:07:20 | Thawalama (Gin Ganga) | 1.26 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-12 09:02:27 | Badalgama (Maha Oya) | 2.29 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-01-12 09:02:01 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-01-12 09:00:51 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-12 09:01:08 | Moragaswewa (Deduru Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:01:31 | Yaka Wewa (Ma Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:04:12 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:07:35 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:02:26 | Pitabeddara (Nilwala Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:04:18 | Norwood (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:01:46 | Ellagawa (Kalu Ganga) | 4.16 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:08:25 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:07:01 | Padiyathalawa (Maduru Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:03:02 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:01:38 | Thanthirimale (Malwathu Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:06:45 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:01:11 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-01-12 09:12:01 | Panadugama (Nilwala Ganga) | 2.26 | 🟢 Normal | -0.009 |  |
| 2026-01-12 09:02:48 | Magura (Kalu Ganga) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-12 09:02:28 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-01-12 09:01:18 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-01-12 09:00:21 | Weraganthota (Mahaweli Ganga) | -1.52 | 🟢 Normal | -0.010 |  |
| 2026-01-12 09:08:24 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-01-12 09:02:42 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-01-12 09:02:47 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | -0.011 |  |
| 2026-01-12 09:11:03 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.016 |  |
| 2026-01-12 09:05:31 | Hanwella (Kelani Ganga) | 1.61 | 🟢 Normal | -0.019 |  |
| 2026-01-12 09:06:34 | Giriulla (Maha Oya) | 1.32 | 🟢 Normal | -0.024 |  |
| 2026-01-12 09:06:13 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.028 |  |
| 2026-01-12 09:03:05 | Putupaula (Kalu Ganga) | 0.62 | 🟢 Normal | -0.030 |  |
| 2026-01-12 09:02:03 | Wellawaya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.030 |  |
| 2026-01-12 09:00:55 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.032 |  |
| 2026-01-12 09:01:09 | Nawalapitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.033 |  |
| 2026-01-12 09:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.79 | 🟢 Normal | -0.040 |  |
| 2026-01-12 09:07:07 | Holombuwa (Kelani Ganga) | 0.72 | 🟢 Normal | -0.042 |  |
| 2026-01-12 09:09:52 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | -0.048 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)