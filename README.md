# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--10_00:17:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **147,518 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 00:17:52 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | -0.050 |  |
| 2026-05-10 00:13:49 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.017 |  |
| 2026-05-10 00:10:58 | Thanamalwila (Kirindi Oya) | 2.01 | 🟢 Normal | -0.035 |  |
| 2026-05-10 00:10:27 | Kuda Oya (Kirindi Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:09:52 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | -0.028 |  |
| 2026-05-10 00:09:29 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-05-10 00:06:53 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-05-10 00:06:48 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.058 |  |
| 2026-05-10 00:06:28 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.107 |  |
| 2026-05-10 00:06:05 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.041 |  |
| 2026-05-10 00:06:04 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-05-10 00:05:37 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.019 |  |
| 2026-05-10 00:04:49 | Katharagama (Menik Ganga) | 1.60 | 🟢 Normal | -0.011 |  |
| 2026-05-10 00:04:15 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-10 00:03:51 | Wellawaya (Kirindi Oya) | 3.08 | 🟢 Normal | -0.448 |  |
| 2026-05-10 00:03:48 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:03:44 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:03:26 | Moragaswewa (Deduru Oya) | 3.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 00:02:59 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.097 |  |
| 2026-05-10 00:02:58 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:02:43 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.107 |  |
| 2026-05-10 00:02:18 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.022 |  |
| 2026-05-10 00:02:17 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:02:15 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:02:12 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.011 |  |
| 2026-05-10 00:01:56 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-10 00:01:53 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:01:43 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:01:37 | Thaldena (Mahaweli Ganga) | 1.77 | 🟢 Normal | 0.487 | 🔺 Rising |
| 2026-05-10 00:01:30 | Nakkala (Kumbukkan Oya) | 2.64 | 🟢 Normal | 1.409 | 🔺 Rising |
| 2026-05-10 00:01:26 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-05-10 00:01:22 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:01:15 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.064 |  |
| 2026-05-10 00:00:38 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:00:08 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:00:08 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-10 00:01:30 | Nakkala (Kumbukkan Oya) | 2.64 | 🟢 Normal | 1.409 | 🔺 Rising |
| 2026-05-10 00:01:37 | Thaldena (Mahaweli Ganga) | 1.77 | 🟢 Normal | 0.487 | 🔺 Rising |
| 2026-05-09 18:02:49 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-05-10 00:04:15 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-05-10 00:01:56 | Thawalama (Gin Ganga) | 1.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-10 00:03:26 | Moragaswewa (Deduru Oya) | 3.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-10 00:01:22 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:00:08 | Horowpothana (Yan Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:01:53 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:02:15 | Panadugama (Nilwala Ganga) | 2.55 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:02:58 | Glencourse (Kelani Ganga) | 9.25 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:00:38 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:03:48 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:02:17 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:03:44 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:10:27 | Kuda Oya (Kirindi Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-05-10 00:09:29 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.009 |  |
| 2026-05-10 00:06:04 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-05-10 00:01:26 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | -0.010 |  |
| 2026-05-10 00:04:49 | Katharagama (Menik Ganga) | 1.60 | 🟢 Normal | -0.011 |  |
| 2026-05-10 00:02:12 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.011 |  |
| 2026-05-10 00:13:49 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | -0.017 |  |
| 2026-05-10 00:05:37 | Peradeniya (Mahaweli Ganga) | 1.80 | 🟢 Normal | -0.019 |  |
| 2026-05-10 00:06:53 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.020 |  |
| 2026-05-10 00:00:08 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | -0.022 |  |
| 2026-05-10 00:02:18 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.022 |  |
| 2026-05-10 00:09:52 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | -0.028 |  |
| 2026-05-10 00:10:58 | Thanamalwila (Kirindi Oya) | 2.01 | 🟢 Normal | -0.035 |  |
| 2026-05-10 00:06:05 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | -0.041 |  |
| 2026-05-10 00:17:52 | Putupaula (Kalu Ganga) | 1.08 | 🟢 Normal | -0.050 |  |
| 2026-05-09 18:00:42 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | -0.051 |  |
| 2026-05-10 00:06:48 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | -0.058 |  |
| 2026-05-09 23:08:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.04 | 🟢 Normal | -0.064 |  |
| 2026-05-10 00:01:15 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.064 |  |
| 2026-05-09 18:04:22 | Galgamuwa (Mee Oya) | 2.26 | 🟢 Normal | -0.081 |  |
| 2026-05-10 00:02:59 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.097 |  |
| 2026-05-10 00:06:28 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.107 |  |
| 2026-05-10 00:02:43 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | -0.107 |  |
| 2026-05-10 00:03:51 | Wellawaya (Kirindi Oya) | 3.08 | 🟢 Normal | -0.448 |  |

## River Water Level Charts by Station

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)