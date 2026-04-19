# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--19_08:19:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **129,114 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 08:19:46 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:15:12 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:09:56 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 08:09:21 | Panadugama (Nilwala Ganga) | 0.47 | 🟢 Normal | -17.689 |  |
| 2026-04-19 08:09:03 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-04-19 08:09:01 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-19 08:07:47 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-04-19 08:07:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | -0.080 |  |
| 2026-04-19 08:07:12 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-04-19 08:06:04 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.022 |  |
| 2026-04-19 08:05:35 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:05:34 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | -0.111 |  |
| 2026-04-19 08:04:52 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:04:50 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:04:32 | Panadugama (Nilwala Ganga) | 1.89 | 🟢 Normal | -17.689 |  |
| 2026-04-19 08:04:24 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-04-19 08:03:59 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:03:51 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:03:45 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:03:31 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:03:26 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 08:03:15 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:03:04 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-19 08:02:58 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:02:43 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:02:36 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:02:36 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.097 |  |
| 2026-04-19 08:02:31 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-19 08:02:19 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:02:15 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-19 08:02:01 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:01:44 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:01:31 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:01:30 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | -0.012 |  |
| 2026-04-19 08:01:30 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-19 08:01:21 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:01:16 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 08:01:13 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:00:46 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:00:42 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-19 07:38:11 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.012 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-19 08:01:30 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-19 08:02:15 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-19 08:02:31 | Hanwella (Kelani Ganga) | 0.28 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-19 08:09:03 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-04-19 07:38:11 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-19 08:09:01 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-19 08:03:26 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 08:01:16 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 08:09:56 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-19 08:03:59 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:02:36 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:19:46 | Moragaswewa (Deduru Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:00:42 | Nawalapitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:04:50 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:02:19 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:00:46 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:03:45 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:02:43 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:01:13 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:02:01 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:01:21 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:04:52 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:03:31 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:01:31 | Holombuwa (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:03:51 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:05:35 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:15:12 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:01:44 | Thanamalwila (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-19 08:03:04 | Deraniyagala (Kelani Ganga) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-04-19 08:01:30 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | -0.012 |  |
| 2026-04-19 08:07:47 | Rathnapura (Kalu Ganga) | 0.58 | 🟢 Normal | -0.020 |  |
| 2026-04-19 08:04:24 | Peradeniya (Mahaweli Ganga) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-04-19 08:06:04 | Magura (Kalu Ganga) | 1.00 | 🟢 Normal | -0.022 |  |
| 2026-04-19 08:07:12 | Thawalama (Gin Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-04-19 08:07:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | -0.080 |  |
| 2026-04-19 06:01:33 | Putupaula (Kalu Ganga) | 0.64 | 🟢 Normal | -0.086 |  |
| 2026-04-19 08:02:36 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.097 |  |
| 2026-04-19 08:05:34 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | -0.111 |  |
| 2026-04-19 08:09:21 | Panadugama (Nilwala Ganga) | 0.47 | 🟢 Normal | -17.689 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)