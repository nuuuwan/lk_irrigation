# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--15_16:17:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **125,872 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 16:17:51 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.008 |  |
| 2026-04-15 16:14:58 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:14:17 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-04-15 16:11:15 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.009 |  |
| 2026-04-15 16:09:58 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-04-15 16:08:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:08:13 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:06:55 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.119 |  |
| 2026-04-15 16:06:31 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.009 |  |
| 2026-04-15 16:06:16 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:05:45 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-15 16:05:44 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.115 |  |
| 2026-04-15 16:05:35 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.114 |  |
| 2026-04-15 16:04:34 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:04:28 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-04-15 16:04:24 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-15 16:04:03 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:04:02 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:03:43 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-04-15 16:03:43 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | -0.039 |  |
| 2026-04-15 16:03:35 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:03:33 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:03:16 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:03:15 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-04-15 16:03:02 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:02:54 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.031 |  |
| 2026-04-15 16:02:32 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:02:31 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-15 16:02:30 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-15 16:02:05 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:01:59 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:01:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:01:14 | Thanthirimale (Malwathu Oya) | 2.48 | 🟢 Normal | -0.040 |  |
| 2026-04-15 16:01:11 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-15 16:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-04-15 16:01:07 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-04-15 16:00:54 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-04-15 16:00:40 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-15 16:00:08 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-15 16:09:58 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-04-15 16:00:40 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-15 16:06:16 | Kithulgala (Kelani Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:00:08 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:01:41 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:04:34 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:03:02 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:04:03 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:03:33 | Ellagawa (Kalu Ganga) | 4.26 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:14:58 | Panadugama (Nilwala Ganga) | 2.13 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:03:16 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:02:32 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:01:59 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:03:35 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:02:05 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:04:02 | Thawalama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:08:13 | Peradeniya (Mahaweli Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:08:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-04-15 16:17:51 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | -0.008 |  |
| 2026-04-15 16:11:15 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.009 |  |
| 2026-04-15 16:14:17 | Magura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.009 |  |
| 2026-04-15 16:06:31 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | -0.009 |  |
| 2026-04-15 16:04:24 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-04-15 16:02:31 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-04-15 16:05:45 | Holombuwa (Kelani Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-04-15 16:02:30 | Wellawaya (Kirindi Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-04-15 16:00:54 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-04-15 16:01:10 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-04-15 16:03:15 | Rathnapura (Kalu Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-04-15 16:01:11 | Moragaswewa (Deduru Oya) | 0.32 | 🟢 Normal | -0.020 |  |
| 2026-04-15 16:01:07 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-04-15 16:03:43 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | -0.020 |  |
| 2026-04-15 16:04:28 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.030 |  |
| 2026-04-15 16:02:54 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.031 |  |
| 2026-04-15 16:03:43 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | -0.039 |  |
| 2026-04-15 16:01:14 | Thanthirimale (Malwathu Oya) | 2.48 | 🟢 Normal | -0.040 |  |
| 2026-04-15 16:05:35 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.114 |  |
| 2026-04-15 16:05:44 | Thanamalwila (Kirindi Oya) | 0.95 | 🟢 Normal | -0.115 |  |
| 2026-04-15 16:06:55 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.119 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)