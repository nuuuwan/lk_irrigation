# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--18_10:06:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **128,301 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 10:06:34 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2026-04-18 10:05:56 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-04-18 10:05:14 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-18 10:05:07 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:04:35 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 1.895 | 🔺 Rising |
| 2026-04-18 10:04:28 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.048 |  |
| 2026-04-18 10:04:24 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:04:16 | Norwood (Kelani Ganga) | 0.41 | 🟢 Normal | 1.895 | 🔺 Rising |
| 2026-04-18 10:04:14 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:04:11 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:04:02 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:03:38 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-18 10:03:35 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.010 |  |
| 2026-04-18 10:03:32 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.059 |  |
| 2026-04-18 10:03:23 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:03:16 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-18 10:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | -0.070 |  |
| 2026-04-18 10:02:47 | Kithulgala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.113 |  |
| 2026-04-18 10:02:34 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-04-18 10:02:26 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:02:21 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:01:58 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.022 |  |
| 2026-04-18 10:01:51 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-18 10:01:47 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.020 |  |
| 2026-04-18 10:01:39 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:01:30 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.021 |  |
| 2026-04-18 10:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-04-18 10:01:10 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:01:09 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-18 10:01:08 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:01:00 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:00:51 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.020 |  |
| 2026-04-18 10:00:46 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:00:10 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:59:51 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:18:03 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-18 10:04:35 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 1.895 | 🔺 Rising |
| 2026-04-18 10:03:16 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-04-18 10:01:09 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-18 10:05:14 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-18 10:03:38 | Hanwella (Kelani Ganga) | 0.49 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-18 10:02:26 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:01:00 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:03:23 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:04:11 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:00:46 | Horowpothana (Yan Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:04:02 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:04:14 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:01:39 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:01:10 | Padiyathalawa (Maduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:00:10 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:01:08 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:02:21 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:04:45 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:04:58 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:59:51 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:04:24 | Peradeniya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-04-18 09:08:12 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:05:07 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-04-18 10:05:56 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | -0.009 |  |
| 2026-04-18 10:02:34 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-04-18 10:01:51 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-04-18 10:03:35 | Ellagawa (Kalu Ganga) | 4.02 | 🟢 Normal | -0.010 |  |
| 2026-04-18 10:01:15 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-04-18 10:00:51 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.020 |  |
| 2026-04-18 10:01:47 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.020 |  |
| 2026-04-18 10:01:30 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.021 |  |
| 2026-04-18 10:01:58 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.022 |  |
| 2026-04-18 09:11:15 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.027 |  |
| 2026-04-18 10:04:28 | Magura (Kalu Ganga) | 1.10 | 🟢 Normal | -0.048 |  |
| 2026-04-18 10:03:32 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | -0.059 |  |
| 2026-04-18 10:06:34 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.062 |  |
| 2026-04-18 10:02:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.69 | 🟢 Normal | -0.070 |  |
| 2026-04-18 10:02:47 | Kithulgala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.113 |  |
| 2026-04-18 09:02:03 | Putupaula (Kalu Ganga) | 0.20 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)