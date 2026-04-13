# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--13_08:25:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **123,763 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 08:25:09 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-13 08:12:25 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.024 |  |
| 2026-04-13 08:11:49 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.056 |  |
| 2026-04-13 08:11:17 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-04-13 08:10:53 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | -0.012 |  |
| 2026-04-13 08:10:47 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.034 |  |
| 2026-04-13 08:10:45 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-13 08:10:37 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 08:09:02 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.027 |  |
| 2026-04-13 08:08:20 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | -0.009 |  |
| 2026-04-13 08:07:38 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 08:05:58 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-04-13 08:05:23 | Magura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.154 |  |
| 2026-04-13 08:05:14 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-13 08:05:11 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-04-13 08:04:43 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-04-13 08:04:14 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-13 08:04:08 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | -0.021 |  |
| 2026-04-13 08:04:07 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-13 08:04:07 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 08:03:51 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 08:03:51 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-13 08:03:44 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 08:03:19 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.070 |  |
| 2026-04-13 08:02:50 | Rathnapura (Kalu Ganga) | 3.56 | 🟢 Normal | -0.085 |  |
| 2026-04-13 08:02:30 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.221 |  |
| 2026-04-13 08:02:30 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-04-13 08:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-13 08:02:05 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 08:01:57 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 08:01:53 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 08:01:49 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-13 08:01:44 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-04-13 08:01:32 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-13 08:01:12 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 08:00:47 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-13 08:00:45 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-04-13 08:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-13 08:00:08 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.468 | 🔺 Rising |
| 2026-04-13 07:58:51 | Horowpothana (Yan Oya) | 1.49 | 🟢 Normal | 0.468 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-13 08:00:08 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.468 | 🔺 Rising |
| 2026-04-13 08:00:45 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-04-13 08:02:30 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-04-13 08:03:51 | Glencourse (Kelani Ganga) | 9.05 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-13 08:04:14 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-04-13 08:04:07 | Hanwella (Kelani Ganga) | 0.63 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-13 08:05:14 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-13 08:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-13 08:01:32 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-04-13 08:00:47 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-13 08:01:12 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 08:03:44 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-13 08:10:37 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 08:03:51 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-13 08:10:45 | Moragaswewa (Deduru Oya) | 0.16 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-13 08:00:19 | Nawalapitiya (Mahaweli Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-04-13 08:01:53 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-13 08:01:57 | Padiyathalawa (Maduru Oya) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 08:04:07 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-04-13 08:07:38 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-13 08:01:49 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-13 08:25:09 | Thanthirimale (Malwathu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-04-13 08:02:05 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-04-13 08:08:20 | Badalgama (Maha Oya) | 1.77 | 🟢 Normal | -0.009 |  |
| 2026-04-13 08:11:17 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | -0.011 |  |
| 2026-04-13 08:10:53 | Galgamuwa (Mee Oya) | 0.65 | 🟢 Normal | -0.012 |  |
| 2026-04-13 08:05:58 | Peradeniya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.020 |  |
| 2026-04-13 08:01:44 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.020 |  |
| 2026-04-13 08:04:43 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-04-13 08:05:11 | Thawalama (Gin Ganga) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-04-13 08:04:08 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | -0.021 |  |
| 2026-04-13 08:12:25 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.024 |  |
| 2026-04-13 08:09:02 | Panadugama (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.027 |  |
| 2026-04-13 08:10:47 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.034 |  |
| 2026-04-13 08:11:49 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.056 |  |
| 2026-04-13 08:03:19 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.070 |  |
| 2026-04-13 08:02:50 | Rathnapura (Kalu Ganga) | 3.56 | 🟢 Normal | -0.085 |  |
| 2026-04-13 08:05:23 | Magura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.154 |  |
| 2026-04-13 08:02:30 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | -0.221 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)